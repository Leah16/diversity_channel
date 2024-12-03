import streamlit as st  # 导入Streamlit库用于创建Web界面
from typing import List, Dict  # 导入类型提示
from packages.chatbotengine import ChatbotEngine  # 导入自定义的聊天引擎模块
from packages.ttsengine import TTSEngine  # 导入TTS引擎
import os

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
    
    # 创建一个行来放置按钮和音频播放器
    col1, col2, col3 = st.columns(3)
    
    # 清除历史按钮
    with col1:
        if st.button("Clear chat history"):
            st.session_state.messages = []  # 清空消息历史
            st.rerun()  # 重新加载页面
    
    # 音频生成按钮
    with col2:
        # 只有在有消息历史且最后一条是助手消息时才启用按钮
        last_message = st.session_state.messages[-1] if st.session_state.messages else None
        can_play = last_message and last_message["role"] == "assistant"
        
        # 生成音频按钮
        if st.button("🔊 Generate audio", disabled=not can_play):
            try:
                audio_file = st.session_state.tts_engine.generate_speech(last_message["content"])
                st.session_state.last_audio = audio_file
                st.session_state.last_audio_text = last_message["content"]  # 保存对应的文本
                st.rerun()
            except Exception as e:
                st.error(f"Failed to generate audio: {str(e)}")
    
    # 音频播放器
    with col3:
        if ("last_audio" in st.session_state and 
            os.path.exists(st.session_state.last_audio) and 
            st.session_state.messages and 
            st.session_state.messages[-1]["content"] == st.session_state.last_audio_text):
            st.audio(st.session_state.last_audio)
    

if __name__ == "__main__":
    chatbotMain()  # 程序入口点