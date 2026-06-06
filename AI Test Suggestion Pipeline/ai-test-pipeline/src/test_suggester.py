import json
import subprocess
from typing import List, Dict

class TestSuggester:
    """Generates test suggestions using AI based on code analysis."""
    
    def __init__(self, model_name: str = "codellama:7b"):
        """
        Initialize the test suggester.
        
        Args:
            model_name: Name of the Ollama model to use
        """
        self.model_name = model_name
    
    def generate_prompt(self, function_data: Dict) -> str:
        """
        Create a prompt for the AI model based on function data.
        
        Args:
            function_data: Dictionary containing function metadata
            
        Returns:
            Formatted prompt string
        """
        # TODO: Build a structured prompt that includes:
        # - Function name and signature
        # - Complexity metrics
        # - Request for test cases covering edge cases
        # TODO: Format as clear instructions for the AI
        pass
    
    def call_ollama(self, prompt: str) -> str:
        """
        Call Ollama API to generate test suggestions.
        
        Args:
            prompt: The prompt to send to the model
            
        Returns:
            AI-generated response
        """
        # TODO: Use subprocess to call ollama CLI
        # TODO: Format command: ollama run <model> "<prompt>"
        # TODO: Capture and return output
        pass
    
    def parse_suggestions(self, ai_response: str) -> List[Dict]:
        """
        Parse AI response into structured test suggestions.
        
        Args:
            ai_response: Raw response from AI model
            
        Returns:
            List of test case suggestions
        """
        # TODO: Extract test case descriptions
        # TODO: Identify test inputs and expected outputs
        # TODO: Categorize by test type (happy path, edge case, error)
        pass
    
    def suggest_tests(self, function_data: Dict) -> Dict:
        """
        Generate complete test suggestions for a function.
        
        Args:
            function_data: Function metadata from analyzer
            
        Returns:
            Dictionary with test suggestions and rationale
        """
        # TODO: Generate prompt
        # TODO: Call AI model
        # TODO: Parse response
        # TODO: Return structured suggestions
        pass
