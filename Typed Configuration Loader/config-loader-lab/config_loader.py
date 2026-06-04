from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, validator
import yaml
import json
import os


class DatabaseConfig(BaseModel):
    """Database connection configuration"""
    host: str = Field(default="localhost")
    port: int = Field(default=5432, ge=1, le=65535)
    username: str
    password: str
    database: str
    max_connections: int = Field(default=10, ge=1, le=100)
    
    @validator('host')
    def validate_host(cls, v):
        """
        TODO: Implement host validation
        - Check if host is not empty
        - Validate format (basic check for localhost or IP pattern)
        """
        pass


class CacheConfig(BaseModel):
    """Cache configuration"""
    enabled: bool = Field(default=True)
    ttl_seconds: int = Field(default=300, ge=0)
    max_size_mb: int = Field(default=100, ge=1)
    
    # TODO: Add validator for max_size_mb to ensure it doesn't exceed 1024


class LoggingConfig(BaseModel):
    """Logging configuration"""
    level: str = Field(default="INFO")
    format: str = Field(default="json")
    output_path: Optional[str] = Field(default="/var/log/app.log")
    
    @validator('level')
    def validate_log_level(cls, v):
        """
        TODO: Validate log level
        - Accept only: DEBUG, INFO, WARNING, ERROR, CRITICAL
        - Convert to uppercase
        - Raise ValueError if invalid
        """
        pass


class AppConfig(BaseModel):
    """Main application configuration"""
    app_name: str
    environment: str = Field(default="development")
    debug: bool = Field(default=False)
    database: DatabaseConfig
    cache: CacheConfig = Field(default_factory=CacheConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    
    @validator('environment')
    def validate_environment(cls, v):
        """
        TODO: Validate environment
        - Accept only: development, staging, production
        - Raise ValueError if invalid
        """
        pass


class ConfigLoader:
    """Configuration loader with type validation"""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config: Optional[AppConfig] = None
    
    def load(self) -> AppConfig:
        """
        Load and validate configuration from file
        
        TODO: Implement the following:
        1. Check if config file exists
        2. Determine file type (JSON or YAML) from extension
        3. Read and parse the file
        4. Validate using AppConfig model
        5. Handle errors appropriately
        
        Returns:
            AppConfig: Validated configuration object
        
        Raises:
            FileNotFoundError: If config file doesn't exist
            ValueError: If config is invalid
        """
        pass
    
    def _load_json(self, file_path: str) -> Dict[str, Any]:
        """
        TODO: Load JSON configuration file
        - Open and read file
        - Parse JSON
        - Return dictionary
        """
        pass
    
    def _load_yaml(self, file_path: str) -> Dict[str, Any]:
        """
        TODO: Load YAML configuration file
        - Open and read file
        - Parse YAML
        - Return dictionary
        """
        pass
    
    def validate_config(self, config_dict: Dict[str, Any]) -> AppConfig:
        """
        TODO: Validate configuration dictionary
        - Create AppConfig instance from dictionary
        - Handle validation errors with clear messages
        - Return validated config
        """
        pass
    
    def get_config(self) -> AppConfig:
        """Return loaded configuration"""
        if self.config is None:
            raise RuntimeError("Configuration not loaded. Call load() first.")
        return self.config
    
    def reload(self) -> AppConfig:
        """
        TODO: Reload configuration from file
        - Call load() again
        - Update self.config
        - Return new config
        """
        pass
