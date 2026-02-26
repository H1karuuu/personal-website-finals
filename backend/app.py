from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import time
import requests as http_requests

load_dotenv()

app = Flask(__name__)

# Allow all origins – this is a public portfolio API
CORS(app)

# Supabase configuration
SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://rxztomvvwytetepornaq.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ4enRvbXZ2d3l0ZXRlcG9ybmFxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5NDA5NDYsImV4cCI6MjA4NzUxNjk0Nn0.FwDpjsfOSCV05maEhuEU7PSAJn09VW9z3L87x2vAeIE")
SUPABASE_REST_URL = f"{SUPABASE_URL}/rest/v1"

# GitHub configuration
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME", "H1karuuu")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Simple in-memory cache for GitHub repos (avoid rate limits)
_repos_cache = {"data": None, "expires": 0}

def supabase_headers(prefer=None):
    """Build headers for Supabase REST API calls."""
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
    }
    if prefer:
        headers["Prefer"] = prefer
    return headers


@app.route("/")
def home():
    return jsonify({"message": "Jayzee Portfolio API is running!", "status": "ok"})


@app.after_request
def add_cors_headers(response):
    """Ensure CORS headers are always present on every response."""
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/api/repos", methods=["GET"])
def get_repos():
    """GET - Fetch public GitHub repositories (cached for 10 minutes)."""
    global _repos_cache
    try:
        # Return cached data if still fresh
        now = time.time()
        if _repos_cache["data"] is not None and now < _repos_cache["expires"]:
            return jsonify(_repos_cache["data"]), 200

        url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
        params = {
            "sort": "updated",
            "direction": "desc",
            "per_page": 20,
            "type": "owner"
        }
        headers = {"Accept": "application/vnd.github.v3+json"}
        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"

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

        # Cache for 10 minutes
        _repos_cache = {"data": result, "expires": now + 600}
        return jsonify(result), 200
    except Exception as e:
        # If cache exists but expired, still return stale data with a warning
        if _repos_cache["data"] is not None:
            return jsonify(_repos_cache["data"]), 200
        return jsonify({"error": str(e)}), 500


@app.route("/api/messages", methods=["GET"])
def get_messages():
    """GET - Retrieve all guestbook messages, newest first."""
    try:
        url = f"{SUPABASE_REST_URL}/messages?select=*&order=created_at.desc"
        resp = http_requests.get(url, headers=supabase_headers(), timeout=10)
        resp.raise_for_status()
        return jsonify(resp.json()), 200
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

        # Insert into Supabase via REST API
        url = f"{SUPABASE_REST_URL}/messages"
        payload = {"name": name, "email": email, "message": message}
        resp = http_requests.post(
            url,
            json=payload,
            headers=supabase_headers(prefer="return=representation"),
            timeout=10
        )
        resp.raise_for_status()

        return jsonify(resp.json()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
