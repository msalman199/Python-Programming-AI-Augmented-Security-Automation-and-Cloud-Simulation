#!/usr/bin/env python3
import click
import requests
from tabulate import tabulate
import json
import sys

# Configuration
API_BASE_URL = "http://127.0.0.1:5000/api"
TOKEN_FILE = "~/.user_cli_token"

class APIClient:
    """Client for interacting with the User API"""
    
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token
        self.session = requests.Session()
        if self.token:
            self.session.headers.update({
                'Authorization': f'Bearer {self.token}'
            })
    
    def health_check(self):
        """
        Check API health status
        
        Returns:
            dict: Health status response
        """
        # TODO: Implement GET request to /health endpoint
        # TODO: Handle connection errors
        # TODO: Return JSON response
        pass
    
    def get_users(self):
        """
        Retrieve all users from the API
        
        Returns:
            list: List of user dictionaries
        """
        # TODO: Implement authenticated GET request to /users endpoint
        # TODO: Handle authentication errors (401)
        # TODO: Parse and return user list from response
        pass
    
    def get_user_by_id(self, user_id):
        """
        Retrieve a specific user by ID
        
        Args:
            user_id: Integer user ID
            
        Returns:
            dict: User information or None if not found
        """
        # TODO: Implement authenticated GET request to /users/{user_id}
        # TODO: Handle 404 errors appropriately
        # TODO: Return user data or None
        pass

@click.group()
def cli():
    """User Management CLI - Interact with User API"""
    pass

@cli.command()
def health():
    """Check API server health"""
    # TODO: Create APIClient instance
    # TODO: Call health_check method
    # TODO: Display results in user-friendly format
    pass

@cli.command()
@click.option('--token', required=True, help='API authentication token')
def list_users(token):
    """List all users"""
    # TODO: Create authenticated APIClient instance
    # TODO: Fetch users using get_users method
    # TODO: Format output using tabulate library
    # TODO: Handle errors gracefully
    pass

@cli.command()
@click.argument('user_id', type=int)
@click.option('--token', required=True, help='API authentication token')
def get_user(user_id, token):
    """Get user details by ID"""
    # TODO: Create authenticated APIClient instance
    # TODO: Fetch specific user
    # TODO: Display user information
    # TODO: Handle user not found scenario
    pass

if __name__ == '__main__':
    cli()
