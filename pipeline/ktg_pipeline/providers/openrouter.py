"""OpenRouter provider (unified API for many models)."""

import requests
from typing import Iterator, Dict, Any
from .base import BaseLLMProvider


class OpenRouterProvider(BaseLLMProvider):
    """Provider for OpenRouter API."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config.get('api_key')
        if not self.api_key:
            raise ValueError("OpenRouter API key required. Set OPENROUTER_API_KEY env var.")
        
        self.model = config.get('model', 'qwen/qwen-2.5-72b-instruct')
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 2000)
        self.base_url = "https://openrouter.ai/api/v1"
    
    def generate(self, prompt: str, system: str = None) -> str:
        """Generate using OpenRouter API."""
        url = f"{self.base_url}/chat/completions"
        
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://ktg.one",  # Required by OpenRouter
            "X-Title": "KTG Content Pipeline"
        }
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise RuntimeError("OpenRouter API key invalid")
            elif e.response.status_code == 429:
                raise RuntimeError("OpenRouter rate limit exceeded")
            raise RuntimeError(f"OpenRouter API error: {e}")
        except Exception as e:
            raise RuntimeError(f"OpenRouter generation failed: {e}")
    
    def stream(self, prompt: str, system: str = None) -> Iterator[str]:
        """Stream generation."""
        yield self.generate(prompt, system)
