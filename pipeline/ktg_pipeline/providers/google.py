"""Google AI Studio provider."""

import requests
from typing import Iterator, Dict, Any
from .base import BaseLLMProvider, BaseImageProvider


class GoogleProvider(BaseLLMProvider, BaseImageProvider):
    """Provider for Google AI Studio API."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config.get('api_key')
        if not self.api_key:
            raise ValueError("Google API key required. Set GOOGLE_API_KEY env var.")
        
        self.model = config.get('model', 'gemini-2.0-flash-exp')
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 2000)
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
    
    def generate(self, prompt: str, system: str = None) -> str:
        """Generate text using Google AI Studio API."""
        url = f"{self.base_url}/models/{self.model}:generateContent"
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": self.temperature,
                "maxOutputTokens": self.max_tokens
            }
        }
        
        if system:
            payload["systemInstruction"] = {"parts": [{"text": system}]}
        
        params = {"key": self.api_key}
        
        try:
            response = requests.post(url, json=payload, params=params, timeout=120)
            response.raise_for_status()
            data = response.json()
            
            if 'candidates' in data and len(data['candidates']) > 0:
                parts = data['candidates'][0].get('content', {}).get('parts', [])
                return ''.join(p.get('text', '') for p in parts)
            return ""
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                raise RuntimeError("Google API rate limit exceeded. Wait a moment.")
            raise RuntimeError(f"Google API error: {e}")
        except Exception as e:
            raise RuntimeError(f"Google generation failed: {e}")
    
    def stream(self, prompt: str, system: str = None) -> Iterator[str]:
        """Stream not implemented for Google (non-streaming API simpler)."""
        yield self.generate(prompt, system)
    
    def generate(self, prompt: str, width: int = 1024, height: int = 1024) -> str:
        """Generate image using Google AI Studio (if model supports it)."""
        # Image generation via Gemini requires specific model
        # This is a placeholder - actual implementation depends on API
        raise NotImplementedError("Image generation via Google API not yet implemented")
