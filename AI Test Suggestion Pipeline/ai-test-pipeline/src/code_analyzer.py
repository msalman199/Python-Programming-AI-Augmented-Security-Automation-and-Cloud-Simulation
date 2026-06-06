import ast
import os
from typing import List, Dict
from git import Repo

class CodeAnalyzer:
    """Analyzes code changes and extracts relevant information for test suggestions."""
    
    def __init__(self, repo_path: str):
        """
        Initialize the code analyzer.
        
        Args:
            repo_path: Path to the git repository
        """
        self.repo_path = repo_path
        self.repo = None
        # TODO: Initialize git repository object
    
    def get_changed_files(self, commit_range: str = "HEAD~1..HEAD") -> List[str]:
        """
        Get list of changed Python files in the commit range.
        
        Args:
            commit_range: Git commit range to analyze
            
        Returns:
            List of changed Python file paths
        """
        # TODO: Use git diff to get changed files
        # TODO: Filter only .py files
        # TODO: Return list of file paths
        pass
    
    def extract_functions(self, file_path: str) -> List[Dict]:
        """
        Extract function definitions from a Python file.
        
        Args:
            file_path: Path to Python file
            
        Returns:
            List of dictionaries containing function metadata
        """
        # TODO: Read file content
        # TODO: Parse with ast module
        # TODO: Extract function names, parameters, and docstrings
        # TODO: Return structured data
        pass
    
    def analyze_complexity(self, function_node: ast.FunctionDef) -> Dict:
        """
        Analyze function complexity metrics.
        
        Args:
            function_node: AST node of the function
            
        Returns:
            Dictionary with complexity metrics
        """
        # TODO: Count branches (if/else statements)
        # TODO: Count loops
        # TODO: Calculate cyclomatic complexity estimate
        pass
