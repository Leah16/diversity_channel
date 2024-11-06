import streamlit as st
import requests
import json
import ollama
from typing import List, Dict

def chatbotMain():
    
    # 初始化会话状态
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 定义与Ollama通信的函数
    def query_ollama(prompt: str, model: str = "llama2") -> str:
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=60
            )
            response.raise_for_status()
            return response.json().get("response", "")
        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with Ollama: {str(e)}")
            return ""

    # 模型选择
    available_models = [model["name"] for model in ollama.list()["models"]]
    selected_model = st.selectbox("Select a model", available_models)
    
    # 显示聊天历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 用户输入
    if prompt := st.chat_input("Your question"):
        # 添加用户消息到历史
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # 显示助手正在输入的状态
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")
            
            # 调用Ollama API
            response = query_ollama(prompt, selected_model)
            
            # 更新消息
            message_placeholder.markdown(response)
            
        # 添加助手回复到历史
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    # 添加清除聊天历史的按钮
    if st.button("Clear chat history"):
        st.session_state.messages = []
        st.experimental_rerun()
    

if __name__ == "__main__":
    chatbotMain()