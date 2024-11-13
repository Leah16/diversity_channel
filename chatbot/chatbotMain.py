import streamlit as st
import requests
import json
import ollama
from typing import List, Dict

def chatbotMain():
    
    # 初始化会话状态
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 定义系统提示词和角色提示词
    SYSTEM_PROMPT = """I want you to act as a patient and guiding mentor who helps users through their questions. You must only respond in English. Your responses should be conversational and flow naturally like human typing, avoiding markdown formatting or numbered/bulleted lists. Write in a continuous, paragraph-style format as if you're having a natural conversation. Important: Only answer questions related to Japan and Japanese life. For any other topics, politely decline to answer and remind the user that you can only help with Japan-related questions."""
    
    CHARACTER_PROMPT = """You are Sakura Tanaka, a 21-year-old Japanese university student studying International Relations at Waseda University in Tokyo. You've lived in Tokyo your whole life but have also traveled extensively throughout Japan. You're friendly, enthusiastic, and always eager to help others understand Japanese culture, lifestyle, and customs. You have extensive knowledge about:
    - Daily life in Japan (transportation, shopping, housing)
    - Japanese education system and student life
    - Japanese customs, traditions, and etiquette
    - Popular culture, entertainment, and trends
    - Local food and dining customs
    - Tourist spots and travel tips
    You speak English fluently but occasionally use simple Japanese expressions naturally in your conversation. You're cheerful and helpful, but also respectful and polite in a way that reflects Japanese cultural values."""
    
    # 定义与Ollama通信的函数
    def query_ollama(prompt: str, model: str = "llama2"):
        try:
            full_prompt = f"{SYSTEM_PROMPT}\n\n{CHARACTER_PROMPT}\n\nUser: {prompt}\nAssistant:"
            
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": model,
                    "prompt": full_prompt,
                    "stream": True
                },
                stream=True
            )
            response.raise_for_status()
            
            # 逐字符产生响应
            for chunk in response.iter_lines():
                if chunk:
                    json_response = json.loads(chunk.decode('utf-8'))
                    if 'response' in json_response:
                        yield json_response['response']
                        
        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with Ollama: {str(e)}")
            yield ""

    # 模型选择
    available_models = [model["name"] for model in ollama.list()["models"]]
    selected_model = st.selectbox("Select a model", available_models)
    
    # 显示聊天历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 用户输入
    if prompt := st.chat_input("Your question"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # 逐字符显示响应
            for response_chunk in query_ollama(prompt, selected_model):
                full_response += response_chunk
                # 使用st.write而不是markdown可能会有更好的实时性能
                message_placeholder.write(full_response + "▌")
                
            message_placeholder.write(full_response)
            
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # 添加清除聊天历史的按钮
    if st.button("Clear chat history"):
        st.session_state.messages = []
        st.experimental_rerun()
    

if __name__ == "__main__":
    chatbotMain()