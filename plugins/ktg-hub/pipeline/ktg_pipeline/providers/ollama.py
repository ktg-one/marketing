"""Ollama local LLM provider."""

import requests
from typing import Iterator, Dict, Any
from .base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    """Provider for local Ollama instances."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.base_url = config.get('base_url', 'http://localhost:11434')
        self.model = config.get('model', 'llama3')
        self.temperature = config.get('temperature', 0.7)
        self.max_tokens = config.get('max_tokens', 2000)
    
    def generate(self, prompt: str, system: str = None) -> str:
        """Generate text using Ollama API."""
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.max_tokens
            }
        }
        
        if system:
            payload["system"] = system
        
        try:
            response = requests.post(url, json=payload, timeout=300)
            response.raise_for_status()
            return response.json().get('response', '')
        except requests.exceptions.ConnectionError:
            raise ConnectionError(
                f"Cannot connect to Ollama at {self.base_url}. "
                "Is Ollama running? Try: ollama serve"
            )
        except Exception as e:
            raise RuntimeError(f"Ollama generation failed: {e}")
    
    def stream(self, prompt: str, system: str = None) -> Iterator[str]:
        """Stream text generation."""
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": True,
            "options": {
                "temperature": self.temperature,
                "num_predict": self.max_tokens
            }
        }
        
        if system:
            payload["system"] = system
        
        response = requests.post(url, json=payload, stream=True, timeout=300)
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                import json
                data = json.loads(line)
                if 'response' in data:
                    yield data['response']
    
    def list_models(self) -> list:
        """List available Ollama models."""
        url = f"{self.base_url}/api/tags"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return [m['name'] for m in response.json().get('models', [])]
        except:
            return []
