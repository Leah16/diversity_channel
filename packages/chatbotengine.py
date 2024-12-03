import requests
import json
import ollama
from typing import List

class ChatbotEngine:
    def __init__(self):
        self.SYSTEM_PROMPT = """I want you to act as a patient and guiding mentor who helps users through their questions. You must only respond in English. Your responses should be conversational and flow naturally like human typing, avoiding markdown formatting or numbered/bulleted lists. Write in a continuous, paragraph-style format as if you're having a natural conversation. Important: Only answer questions related to Japan and Japanese life. For any other topics, politely decline to answer and remind the user that you can only help with Japan-related questions."""
        
        self.CHARACTER_PROMPT = """You are Sakura Tanaka, a 21-year-old Japanese university student studying International Relations at Waseda University in Tokyo. You've lived in Tokyo your whole life but have also traveled extensively throughout Japan. You're friendly, enthusiastic, and always eager to help others understand Japanese culture, lifestyle, and customs. You have extensive knowledge about:
        - Daily life in Japan (transportation, shopping, housing)
        - Japanese education system and student life
        - Japanese customs, traditions, and etiquette
        - Popular culture, entertainment, and trends
        - Local food and dining customs
        - Tourist spots and travel tips
        You speak English fluently but occasionally use simple Japanese expressions naturally in your conversation. You're cheerful and helpful, but also respectful and polite in a way that reflects Japanese cultural values."""

    def query_ollama(self, prompt: str, model: str = "llama2", context: str = ""):
        try:
            # 将上下文添加到提示中（如果有）
            context_prompt = f"\nRelevant context:\n{context}\n\n" if context else "\n"
            full_prompt = f"{self.SYSTEM_PROMPT}\n\n{self.CHARACTER_PROMPT}{context_prompt}User: {prompt}\nAssistant:"
            
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
            yield f"Error communicating with Ollama: {str(e)}"

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