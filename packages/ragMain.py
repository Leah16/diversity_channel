from langchain_ollama import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List, Dict
import os
import requests

class RAGModule:
    def __init__(self, model_name: str = "llama2"):
        self.model_name = model_name
        self.embeddings = OllamaEmbeddings(model=model_name)
        self.vector_store = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    
    @staticmethod
    def get_available_models() -> List[str]:
        """获取Ollama本地可用的模型列表"""
        try:
            response = requests.get('http://localhost:11434/api/tags')
            if response.status_code == 200:
                models = response.json()
                # 提取模型名称列表
                return [model['name'] for model in models['models']]
            return ["llama2"]  # 如果API调用失败，返回默认模型
        except Exception as e:
            print(f"Error fetching models: {e}")
            return ["llama2"]  # 发生错误时返回默认模型
    
    def update_embedding_model(self, new_model_name: str) -> None:
        """更新嵌入式模型"""
        self.model_name = new_model_name
        self.embeddings = OllamaEmbeddings(model=new_model_name)
        # 如果已有向量存储，需要重新处理
        if hasattr(self, '_last_documents_dir') and self._last_documents_dir:
            self.load_documents(self._last_documents_dir)
    
    def load_documents(self, documents_dir: str) -> None:
        """加载文档并创建向量存储"""
        self._last_documents_dir = documents_dir  # 保存最后使用的文档目录
        texts = []
        for filename in os.listdir(documents_dir):
            if filename.endswith('.txt'):
                with open(os.path.join(documents_dir, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    chunks = self.text_splitter.split_text(content)
                    texts.extend(chunks)
        
        self.vector_store = FAISS.from_texts(texts, self.embeddings)
    
    def get_relevant_context(self, query: str, k: int = 3) -> str:
        """检索相关上下文"""
        if not self.vector_store:
            return ""
        
        docs = self.vector_store.similarity_search(query, k=k)
        return "\n\n".join([doc.page_content for doc in docs]) 