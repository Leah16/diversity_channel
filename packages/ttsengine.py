import torch
import soundfile as sf
import ChatTTS
import os
import numpy as np

class TTSEngine:
    def __init__(self):
        """初始化TTS引擎"""
        self.chat = ChatTTS.Chat()
        self.chat.load(compile=False)
        # 创建临时音频文件夹
        os.makedirs("temp_audio", exist_ok=True)
        # 固定的音频文件路径
        self.audio_file = "temp_audio/last_response.wav"
    
    def generate_speech(self, text: str) -> str:
        """
        将文本转换为语音
        
        Args:
            text: 需要转换的文本
        
        Returns:
            str: 音频文件路径
        """
        # 生成语音
        wavs = self.chat.infer([text])
        
        # 使用for循环保存音频
        for i in range(len(wavs)):
            # 使用soundfile保存音频
            sf.write(self.audio_file, wavs[i], 24000)
        
        return self.audio_file
    
    @staticmethod
    def is_available() -> bool:
        """检查是否可以使用TTS功能"""
        return torch.cuda.is_available()