from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import requests as http_requests

load_dotenv()

app = Flask(__name__)
CORS(app)

# Supabase configuration
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://rxztomvvwytetepornaq.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ4enRvbXZ2d3l0ZXRlcG9ybmFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NDA5NDYsImV4cCI6MjA4NzUxNjk0Nn0.FwDpjsfOSCV05maEhuEU7PSAJn09VW9z3L87x2vAeIE")

# GitHub configuration
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME", "H1karuuu")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route("/")
def home():
    return jsonify({"message": "Jayzee Portfolio API is running!", "status": "ok"})


@app.route("/api/repos", methods=["GET"])
def get_repos():
    """GET - Fetch public GitHub repositories for the user."""
    try:
        url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
        params = {
            "sort": "updated",
            "direction": "desc",
            "per_page": 20,
            "type": "owner"
        }
        headers = {"Accept": "application/vnd.github.v3+json"}
        resp = http_requests.get(url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        repos = resp.json()

        # Return only relevant fields
        result = []
        for repo in repos:
            if not repo.get("fork", False):
                result.append({
                    "id": repo["id"],
                    "name": repo["name"],
                    "description": repo.get("description"),
                    "html_url": repo["html_url"],
                    "language": repo.get("language"),
                    "stargazers_count": repo.get("stargazers_count", 0),
                    "forks_count": repo.get("forks_count", 0),
                    "updated_at": repo.get("updated_at"),
                    "topics": repo.get("topics", [])
                })

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/messages", methods=["GET"])
def get_messages():
    """GET - Retrieve all guestbook messages, newest first."""
    try:
        response = supabase.table("messages").select("*").order("created_at", desc=True).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/messages", methods=["POST"])
def create_message():
    """POST - Insert a new guestbook message."""
    try:
        data = request.get_json()

        # Validate required fields
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        message = data.get("message", "").strip()

        if not name or not email or not message:
            return jsonify({"error": "Name, email, and message are required."}), 400

        # Insert into Supabase
        response = supabase.table("messages").insert({
            "name": name,
            "email": email,
            "message": message
        }).execute()

        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
