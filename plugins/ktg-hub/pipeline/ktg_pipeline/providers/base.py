"""Base provider interface."""

from abc import ABC, abstractmethod
from typing import Iterator, Dict, Any


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    def generate(self, prompt: str, system: str = None) -> str:
        """Generate text from prompt."""
        pass
    
    @abstractmethod
    def stream(self, prompt: str, system: str = None) -> Iterator[str]:
        """Stream text generation."""
        pass


class BaseImageProvider(ABC):
    """Abstract base class for image providers."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    @abstractmethod
    def generate_image(self, prompt: str, width: int = 1024, height: int = 1024) -> str:
        """Generate image from prompt, return path to saved image."""
        pass
