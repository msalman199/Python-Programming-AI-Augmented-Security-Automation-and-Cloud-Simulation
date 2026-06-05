from flask import Flask, jsonify, request
from flask_httpauth import HTTPTokenAuth
import json

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# Mock data
users = [
    {"id": 1, "name": "Alice Johnson", "role": "DevOps Engineer"},
    {"id": 2, "name": "Bob Smith", "role": "SRE"},
    {"id": 3, "name": "Carol White", "role": "Platform Engineer"}
]

# Valid token for authentication
VALID_TOKEN = "dev-token-12345"

@auth.verify_token
def verify_token(token):
    return token == VALID_TOKEN

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "service": "User API"})

@app.route('/api/users', methods=['GET'])
@auth.login_required
def get_users():
    return jsonify({"users": users, "count": len(users)})

@app.route('/api/users/<int:user_id>', methods=['GET'])
@auth.login_required
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

def health_check(self):
    try:
        response = self.session.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        click.echo("Error: Cannot connect to API server", err=True)
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {str(e)}", err=True)
        sys.exit(1)
@cli.command()
def health():
    """Check API server health"""
    client = APIClient(API_BASE_URL)
    result = client.health_check()
    click.echo(f"Status: {result.get('status')}")
    click.echo(f"Service: {result.get('service')}")

