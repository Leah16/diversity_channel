import streamlit as st  # 导入Streamlit库用于创建Web界面
from typing import List, Dict  # 导入类型提示
from packages.chatbotEngine import ChatbotEngine  # 导入自定义的聊天引擎模块
from packages.ttsEngine import TTSEngine  # 导入TTS引擎
import os

def functionButton():
    # 功能按钮格式
    col1, col2, col3, col4 = st.columns(4)  

     # 录音按钮 (始终可用)
    with col1:
        st.button("🎤")
        
    # 清除历史按钮
    with col2:
        if len(st.session_state.messages) > 0:
            if st.button("🗑️"):
                st.session_state.messages = []
                st.rerun()

    # 翻译按钮
    with col3:
        last_message = st.session_state.messages[-1] if st.session_state.messages else None
        if last_message and last_message["role"] == "assistant":
            st.button("🌐")
    
    # 音频按钮和播放器
    with col4:
        last_message = st.session_state.messages[-1] if st.session_state.messages else None
        
        if ("last_audio" in st.session_state and 
            os.path.exists(st.session_state.last_audio) and 
            st.session_state.messages and 
            st.session_state.messages[-1]["content"] == st.session_state.last_audio_text):
            # 显示音频播放器
            st.audio(st.session_state.last_audio)
        elif last_message and last_message["role"] == "assistant":
            # 显示音频生成按钮
            if st.button("🔊"):
                try:
                    audio_file = st.session_state.tts_engine.generate_speech(last_message["content"])
                    st.session_state.last_audio = audio_file
                    st.session_state.last_audio_text = last_message["content"]
                    st.rerun()
                except Exception as e:
                    st.error(f"Failed to generate audio: {str(e)}")

def chatbotMain():
    # 初始化TTS引擎
    if "tts_engine" not in st.session_state:
        st.session_state.tts_engine = TTSEngine()
    
    # 如果聊天引擎不存在，创建一个新的实例
    if "chat_engine" not in st.session_state:
        st.session_state.chat_engine = ChatbotEngine()
    
    # 初始化消息历史列表
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # 创建模型选择下拉框
    available_models = ChatbotEngine.get_available_models()
    selected_model = st.selectbox("Select a model", available_models)
    
    # 遍历并显示所有历史消息
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 创建用户输入框并处理输入
    if prompt := st.chat_input("Your question"):
        
        # 如果有新对话，清除之前的音频
        if "last_audio" in st.session_state:
            del st.session_state.last_audio
        
        # 初始化RAG上下文
        context = ""
        if "rag_module" in st.session_state and st.session_state.rag_module.vector_store:
            context = st.session_state.rag_module.get_context(prompt)
            
        # 将用户输入添加到消息历史
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
            
        # 处理助手响应
        with st.chat_message("assistant"):
            message_placeholder = st.empty()  # 创建占位符用于流式显示
            full_response = ""  # 存储完整响应
            
            # 流式接收并显示AI响应
            for response_chunk in st.session_state.chat_engine.query_ollama(
                prompt, 
                selected_model,
                context=context if "rag_module" in st.session_state and st.session_state.rag_module.vector_store else ""
            ):
                full_response += response_chunk
                message_placeholder.write(full_response + "▌")  # 显示打字效果
            
            message_placeholder.write(full_response)  # 显示最终完整响应
            
            # 将助手响应添加到消息历史
            st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # 功能按钮
    functionButton()
    

if __name__ == "__main__":
    chatbotMain()  # 程序入口点