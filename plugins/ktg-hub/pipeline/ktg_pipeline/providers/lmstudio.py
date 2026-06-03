"""LM Studio provider (OpenAI-compatible local API)."""

import requests
from typing import Iterator, Dict, Any
from .base import BaseLLMProvider


class LMStudioProvider(BaseLLMProvider):
    """Provider for LM Studio local server."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.base_url = config.get('base_url', 'http://localhost:1234/v1')
        self.model = config.get('model', 'local-model')
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 2000)
    
    def generate(self, prompt: str, system: str = None) -> str:
        """Generate using OpenAI-compatible API."""
        url = f"{self.base_url}/chat/completions"
        
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "stream": False
        }
        
        try:
            response = requests.post(url, json=payload, timeout=300)
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                f"Cannot connect to LM Studio at {self.base_url}. "
                "Is LM Studio running with server enabled?"
            )
        except Exception as e:
            raise RuntimeError(f"LM Studio generation failed: {e}")
    
    def stream(self, prompt: str, system: str = None) -> Iterator[str]:
        """Stream generation."""
        # For simplicity, just return full response
        yield self.generate(prompt, system)
