"""Configuration loader with environment variable support."""

import os
import yaml
from pathlib import Path
from typing import Dict, Any


class Config:
    """Pipeline configuration with env var substitution."""
    
    def __init__(self, config_path: str = None):
        self.config_path = config_path or self._find_config()
        self.data = self._load()
    
    def _find_config(self) -> str:
        """Find config file in order of preference."""
        candidates = [
            "pipeline/config.local.yaml",
            "pipeline/config.yaml",
        ]
        for candidate in candidates:
            if Path(candidate).exists():
                return candidate
        return candidates[-1]
    
    def _load(self) -> Dict[str, Any]:
        """Load YAML with environment variable substitution."""
        if not Path(self.config_path).exists():
            raise FileNotFoundError(f"Config not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            content = f.read()
        
        # Substitute environment variables: ${VAR} or $VAR
        content = os.path.expandvars(content)
        
        return yaml.safe_load(content)
    
    def get(self, key: str, default=None):
        """Get nested config value via dot notation."""
        keys = key.split('.')
        value = self.data
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    @property
    def llm_provider(self) -> str:
        return self.get('llm.provider', 'google')
    
    @property
    def llm_config(self) -> Dict[str, Any]:
        provider = self.llm_provider
        return self.get(f'llm.{provider}', {})
    
    @property
    def image_provider(self) -> str:
        return self.get('image_gen.provider', 'google')
    
    @property
    def platforms(self) -> Dict[str, Any]:
        return self.get('platforms', {})
