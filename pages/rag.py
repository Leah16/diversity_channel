import streamlit as st
import os
from packages.ragMain import RAGModule
from packages.etlPythonSidebar import ETLsidebar
#side bar
ETLsidebar()

def knowledge_base_page():
    st.title("Knowledge Base Management")
    
    # 初始化RAG模块
    if "rag_module" not in st.session_state:
        st.session_state.rag_module = RAGModule()
    
    # 添加模型选择
    st.header("Embedding Model Settings")
    col1, col2 = st.columns([3, 1])  # 创建两列布局
    
    # 从Ollama获取可用模型列表
    available_models = RAGModule.get_available_models()
    
    with col1:
        if not available_models:
            st.error("No models found in Ollama. Please install at least one model.")
            selected_model = None
        else:
            # 确保当前模型在列表中
            current_model = st.session_state.rag_module.model_name
            if current_model not in available_models:
                available_models.append(current_model)
            
            selected_model = st.selectbox(
                "Select Embedding Model",
                available_models,
                index=available_models.index(current_model)
            )
    
    # 如果有可用模型且模型发生变化，更新嵌入模型
    if selected_model and selected_model != st.session_state.rag_module.model_name:
        with st.spinner("Updating embedding model..."):
            st.session_state.rag_module.update_embedding_model(selected_model)
            st.success(f"Embedding model updated to {selected_model}")
    
    st.divider()  # 添加分隔线
    
    # 文档上传部分
    st.header("Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload knowledge base documents",
        accept_multiple_files=True,
        type=['txt']
    )
    
    if uploaded_files:
        # 创建临时目录存储上传的文件
        temp_dir = "temp_docs"
        os.makedirs(temp_dir, exist_ok=True)
        
        # 保存上传的文件
        for file in uploaded_files:
            with open(os.path.join(temp_dir, file.name), 'wb') as f:
                f.write(file.getbuffer())
        
        if st.button("Process Documents"):
            with st.spinner("Processing documents..."):
                # 加载文档到RAG模块
                st.session_state.rag_module.load_documents(temp_dir)
                st.success("Documents processed and loaded successfully!")
    
    # 显示当前加载的文档状态
    st.header("Current Status")
    if st.session_state.rag_module.vector_store:
        st.success("Vector store is initialized and ready to use")
    else:
        st.warning("No documents have been processed yet")

if __name__ == "__main__":
    knowledge_base_page() 