import torch
import soundfile as sf
import ChatTTS
import os
import numpy as np

class TTSEngine:

    """初始化"""
    def __init__(self):
        # 初始化TTS引擎
        self.chat = ChatTTS.Chat()
        self.chat.load(compile=False)
        # 创建临时音频文件夹
        os.makedirs("temp_audio", exist_ok=True)
        # 固定的音频文件路径
        self.audio_file = "temp_audio/last_response.wav"

    """
    生成语音
    Args:
        text (str): 要生成的文本
    Returns:
        str: 生成的音频文件路径
    """
    def generate_speech(self, text: str) -> str:
        # 加载音色权重
        rand_spk = torch.load("arts/ttsSeed.pt", weights_only=True)

        # 配置参数
        params_infer_code = self.chat.InferCodeParams(
            spk_emb = rand_spk, # add sampled speaker 
            temperature = .1,   # using custom temperature
            top_P = 0.7,        # top P decode
            top_K = 20,         # top K decode
        )

        # 配置说话风格
        params_refine_text = self.chat.RefineTextParams(
            prompt='[oral_0][laugh_0][break_6]',
        )
         # 生成语音
        wavs = self.chat.infer(
            [text], 
            params_infer_code = params_infer_code, 
            params_refine_text = params_refine_text
        )
        
        # 使用for循环保存音频
        for i in range(len(wavs)):
            # 使用 torchaudio 保存音频，指定后端
            import torchaudio
            torchaudio.save(
                self.audio_file,
                torch.tensor(wavs[i]).unsqueeze(0),  # 添加通道维度
                sample_rate=24000,
                backend="soundfile"  # 显式指定后端
            )
        
        return self.audio_file
    """
    检查是否可以使用TTS功能
    Returns:
        bool: 是否可以使用TTS功能
    """
    @staticmethod
    def is_available() -> bool:
        return torch.cuda.is_available()