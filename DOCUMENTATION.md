# Personal Portfolio Website — Project Documentation

---

**Project Title:** Personal Portfolio Website with Guestbook  
**Developer:** John Christian "Jayzee" Lopez  
**Course:** Bachelor of Science in Information Technology  
**Subject:** Web Programming  
**Date:** February 2026  
**Repository:** https://github.com/H1karuuu/personal-website-finals

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Objectives](#2-objectives)
3. [Technologies Used](#3-technologies-used)
4. [System Architecture](#4-system-architecture)
5. [Project Structure](#5-project-structure)
6. [Frontend Implementation](#6-frontend-implementation)
7. [Backend Implementation (Flask REST API)](#7-backend-implementation-flask-rest-api)
8. [Database Design (Supabase)](#8-database-design-supabase)
9. [API Endpoints](#9-api-endpoints)
10. [Responsive Design](#10-responsive-design)
11. [Deployment](#11-deployment)
12. [Features Summary](#12-features-summary)
13. [Screenshots / Page Sections](#13-screenshots--page-sections)
14. [How to Run Locally](#14-how-to-run-locally)
15. [Environment Variables](#15-environment-variables)
16. [Resources and Credits](#16-resources-and-credits)
17. [Conclusion](#17-conclusion)

---

## 1. Project Overview

This project is a personal portfolio website built as a single-page application (SPA) using **Vue.js 3** for the frontend and a **Flask REST API** for the backend. The website showcases the developer's profile, education history, skills, goals, GitHub projects, and contact information. It also includes an interactive **guestbook** feature that allows visitors to leave messages, which are stored in a **Supabase** (PostgreSQL) database via the Flask API.

The frontend is hosted on **Vercel** and the backend is hosted on **Render.com**, demonstrating a full-stack deployment workflow suitable for modern web applications.

---

## 2. Objectives

- Build a fully functional personal portfolio website using **Vue.js** as the frontend framework.
- Implement a **Flask REST API** backend with both **GET** and **POST** HTTP methods.
- Connect the backend to a **Supabase PostgreSQL database** for persistent data storage.
- Deploy the frontend to **Vercel** and the backend to **Render.com**.
- Make the website fully **responsive** for both mobile and desktop devices.
- Integrate the **GitHub API** to dynamically showcase the developer's repositories.
- Implement an interactive **guestbook** (message board) where visitors can submit and view messages.

---

## 3. Technologies Used

### Frontend
| Technology | Version | Purpose |
|---|---|---|
| Vue.js | 3.5.13 | JavaScript framework for building the SPA |
| Vite | 6.2.0 | Build tool and development server |
| @vitejs/plugin-vue | 5.2.3 | Vue 3 support for Vite |
| HTML5 / CSS3 | — | Page structure and styling |
| JavaScript (ES6+) | — | Client-side logic and API calls |

### Backend
| Technology | Version | Purpose |
|---|---|---|
| Python | 3.x | Backend programming language |
| Flask | 3.1.0 | Lightweight web framework for the REST API |
| Flask-CORS | 5.0.1 | Cross-Origin Resource Sharing support |
| Supabase (Python SDK) | 2.13.0 | Client for Supabase PostgreSQL database |
| Gunicorn | 23.0.0 | Production WSGI HTTP server |
| Requests | 2.32.3 | HTTP library for GitHub API calls |
| python-dotenv | 1.1.0 | Environment variable management |

### Database & Hosting
| Service | Purpose |
|---|---|
| Supabase | PostgreSQL database for storing guestbook messages |
| Vercel | Frontend hosting and deployment |
| Render.com | Backend API hosting and deployment |
| GitHub API | Dynamic fetching of public repositories |

---

## 4. System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER (Browser)                           │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              Vue.js 3 Frontend (Vercel)                   │  │
│  │  ┌─────────┐  ┌──────────┐  ┌───────────┐  ┌─────────┐  │  │
│  │  │  Hero   │  │  About   │  │  Skills   │  │  Goals  │  │  │
│  │  └─────────┘  └──────────┘  └───────────┘  └─────────┘  │  │
│  │  ┌─────────┐  ┌──────────┐  ┌───────────┐  ┌─────────┐  │  │
│  │  │ History │  │ Projects │  │  Contact  │  │Guestbook│  │  │
│  │  └─────────┘  └──────────┘  └───────────┘  └─────────┘  │  │
│  └───────────────────────┬───────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────┘
                           │ HTTP Requests (fetch)
                           │ GET /api/messages
                           │ POST /api/messages
                           │ GET /api/repos
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                 Flask REST API (Render.com)                      │
│                                                                  │
│  ┌────────────┐   ┌───────────────┐   ┌───────────────────────┐ │
│  │  app.py    │   │  Flask-CORS   │   │  Gunicorn (WSGI)     │ │
│  │  Routes:   │   │  (Cross-Origin│   │  (Production Server) │ │
│  │  /api/msgs │   │   Support)    │   │                       │ │
│  │  /api/repos│   └───────────────┘   └───────────────────────┘ │
│  └─────┬──────┘                                                  │
│        │                                                         │
└────────┼─────────────────────────────────────────────────────────┘
         │                          │
         │ Supabase SDK             │ HTTP GET
         ▼                          ▼
┌─────────────────┐   ┌──────────────────────┐
│   Supabase      │   │   GitHub REST API    │
│   (PostgreSQL)  │   │   /users/{user}/repos│
│                 │   │                      │
│  messages table │   │  Public Repositories │
└─────────────────┘   └──────────────────────┘
```

### Data Flow

1. **Page Load:** The Vue.js frontend loads in the browser and calls `GET /api/messages` and `GET /api/repos` from the Flask backend.
2. **Fetching Repos:** The Flask backend forwards the request to the GitHub API, filters results, and returns them to the frontend.
3. **Fetching Messages:** The Flask backend queries the Supabase `messages` table and returns all guestbook entries sorted by newest first.
4. **Submitting a Message:** The visitor fills out the guestbook form. The frontend sends a `POST /api/messages` request with JSON data. Flask validates the input and inserts the record into Supabase.

---

## 5. Project Structure

```
personal-website-finals/
│
├── README.md                          # Project README
├── DOCUMENTATION.md                   # This documentation file
│
├── frontend/                          # Vue.js Frontend Application
│   ├── index.html                     # HTML entry point
│   ├── package.json                   # Node.js dependencies & scripts
│   ├── package-lock.json              # Dependency lock file
│   ├── vite.config.js                 # Vite build configuration
│   ├── .env                           # Environment variables (API URL)
│   ├── .env.example                   # Environment template
│   └── src/
│       ├── main.js                    # Vue app initialization
│       ├── App.vue                    # Root Vue component
│       ├── components/
│       │   └── PersonalProfile.vue    # Main portfolio component (594 lines)
│       └── assets/
│           ├── styles.css             # Global stylesheet (1160 lines)
│           └── Photo/
│               ├── Profile.png        # Developer profile photo
│               └── header.gif         # Animated hero banner image
│
└── backend/                           # Flask REST API Backend
    ├── app.py                         # Flask application & API routes
    ├── requirements.txt               # Python dependencies
    ├── .env                           # Environment variables (Supabase keys)
    └── .env.example                   # Environment template
```

---

## 6. Frontend Implementation

### 6.1 Vue.js Component Architecture

The frontend is a single-page application built with **Vue.js 3** using the **Options API**. The main component is `PersonalProfile.vue`, which contains the entire portfolio layout, data, and logic.

**Component:** `PersonalProfile.vue`  
**Lines of Code:** 594  
**Sections:**
- Template (HTML structure with Vue directives)
- Script (data, methods, lifecycle hooks)

### 6.2 Page Sections

The portfolio website is divided into the following sections, each accessible via the navigation bar:

| Section | Navigation ID | Description |
|---|---|---|
| **Hero** | `#home` | Full-width banner with animated GIF background, profile photo with glow effect, name, and call-to-action buttons |
| **About Me** | `#about` | Introduction paragraphs with stats cards (Graduate Year, Course, Scholarship) |
| **Personal History** | `#history` | Timeline layout showing education, current studies, and IT experience |
| **Skills & Interests** | `#skills` | Three-column grid with Technical Skills, Gaming & Strategy, and Personal Interests |
| **Goals & Achievements** | `#goals` | Six goal cards with icons (Cybersecurity Firm, Financial Freedom, Family, etc.) |
| **My Projects** | `#projects` | Dynamic GitHub repository cards fetched from the API |
| **Get In Touch** | `#contact` | Contact information (Email, Phone, Location) |
| **Leave a Message** | `#guestbook` | Guestbook form (POST) and message list (GET) |
| **Resources & Credits** | `#resources` | Attribution for fonts, images, and tools used |
| **Footer** | — | Social media links (Facebook, Instagram, GitHub, LinkedIn) with SVG icons |

### 6.3 Key Frontend Features

**Reactive Navigation Bar:**
- Fixed position at the top of the page
- Hamburger menu toggle for mobile devices
- Smooth scroll to sections using anchor links
- Backdrop blur effect with neon-red accent border

**Hero Section:**
- Animated GIF (`header.gif`) as full-width background
- Dark overlay gradient for text readability
- Profile image with CSS glow animation
- Scroll indicator animation at the bottom

**GitHub Repositories Grid:**
- Fetched dynamically from the Flask API at page load
- Each repo displayed as an interactive card with:
  - Repository name and description
  - Programming language with color-coded dot
  - Star count and fork count with SVG icons
  - "Last updated" relative time (e.g., "3 days ago")
- Cards link directly to the GitHub repository page

**Guestbook (Message Board):**
- **Form Fields:** Name, Email, Message (all required)
- **Validation:** Client-side (HTML `required`) and server-side (Flask)
- **Submit Flow:** Sends POST request → Shows success/error feedback → Refreshes message list
- **Message Display:** Cards with author name, date, and message body
- Loading states and empty-state messages

**Social Media Footer:**
- SVG icons for Facebook, Instagram, GitHub, and LinkedIn
- Links open in new tabs with `rel="noopener"` for security
- Hover effects with neon-red glow

### 6.4 API Integration (Frontend)

The frontend communicates with the Flask backend using the JavaScript `fetch()` API:

```javascript
// API base URL from environment variable
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api'

// GET - Fetch all guestbook messages
async fetchMessages() {
  const res = await fetch(`${API_URL}/messages`)
  const data = await res.json()
  this.messages = data
}

// GET - Fetch GitHub repositories
async fetchRepos() {
  const res = await fetch(`${API_URL}/repos`)
  const data = await res.json()
  this.repos = data
}

// POST - Submit a new guestbook message
async handleSubmit() {
  const res = await fetch(`${API_URL}/messages`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      name: this.form.name,
      email: this.form.email,
      message: this.form.message
    })
  })
}
```

---

## 7. Backend Implementation (Flask REST API)

### 7.1 Application Setup

The backend is built with **Flask**, a lightweight Python web framework. It serves as a REST API that handles:
1. Guestbook message storage and retrieval (via Supabase)
2. GitHub repository fetching (via GitHub REST API)

**File:** `backend/app.py`

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import requests as http_requests

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configuration from environment variables
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "")
GITHUB_USERNAME = os.environ.get("GITHUB_USERNAME", "H1karuuu")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
```

### 7.2 CORS Configuration

**Flask-CORS** is used to allow cross-origin requests from the Vercel-hosted frontend to the Render-hosted backend. Without CORS, the browser would block requests between different domains.

```python
CORS(app)  # Allows all origins (suitable for development/demo)
```

### 7.3 Route Handlers

The API has **three main routes** plus a health check endpoint:

| Route | Method | Description |
|---|---|---|
| `/` | GET | Health check — returns API status |
| `/api/repos` | GET | Fetches public GitHub repositories |
| `/api/messages` | GET | Retrieves all guestbook messages |
| `/api/messages` | POST | Creates a new guestbook message |

---

## 8. Database Design (Supabase)

### 8.1 About Supabase

Supabase is an open-source Firebase alternative that provides a PostgreSQL database, authentication, and REST APIs. In this project, Supabase is used to store guestbook messages.

### 8.2 Table Schema

**Table Name:** `messages`

| Column | Type | Constraints | Description |
|---|---|---|---|
| `id` | `bigint` | Primary Key, Auto-increment | Unique message identifier |
| `name` | `text` | NOT NULL | Name of the visitor |
| `email` | `text` | NOT NULL | Email of the visitor |
| `message` | `text` | NOT NULL | The guestbook message content |
| `created_at` | `timestamptz` | DEFAULT `now()` | Timestamp when the message was created |

### 8.3 SQL Schema

```sql
CREATE TABLE messages (
    id         BIGINT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name       TEXT NOT NULL,
    email      TEXT NOT NULL,
    message    TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;

-- Policy: Allow anyone to read messages
CREATE POLICY "Allow public read" ON messages
    FOR SELECT USING (true);

-- Policy: Allow anyone to insert messages
CREATE POLICY "Allow public insert" ON messages
    FOR INSERT WITH CHECK (true);
```

### 8.4 Row Level Security (RLS)

Supabase uses Row Level Security to control data access. Two policies are applied:
- **Allow public read:** Anyone can retrieve messages (for displaying in the guestbook).
- **Allow public insert:** Anyone can submit a new message (via the guestbook form).

---

## 9. API Endpoints

### 9.1 Health Check

**Endpoint:** `GET /`

**Response:**
```json
{
  "message": "Jayzee Portfolio API is running!",
  "status": "ok"
}
```

### 9.2 Get GitHub Repositories

**Endpoint:** `GET /api/repos`  
**Method:** GET  
**Description:** Fetches the developer's public GitHub repositories, excluding forks, sorted by most recently updated.

**Process:**
1. Flask sends a GET request to `https://api.github.com/users/H1karuuu/repos`
2. Filters out forked repositories
3. Returns only relevant fields

**Success Response (200):**
```json
[
  {
    "id": 123456789,
    "name": "personal-website-finals",
    "description": "Personal portfolio website with Vue.js and Flask",
    "html_url": "https://github.com/H1karuuu/personal-website-finals",
    "language": "Vue",
    "stargazers_count": 0,
    "forks_count": 0,
    "updated_at": "2026-02-24T12:00:00Z",
    "topics": []
  }
]
```

**Error Response (500):**
```json
{
  "error": "Error message description"
}
```

### 9.3 Get Guestbook Messages

**Endpoint:** `GET /api/messages`  
**Method:** GET  
**Description:** Retrieves all guestbook messages from the Supabase database, ordered by newest first.

**Success Response (200):**
```json
[
  {
    "id": 1,
    "name": "Visitor Name",
    "email": "visitor@example.com",
    "message": "Great portfolio!",
    "created_at": "2026-02-24T10:30:00+00:00"
  }
]
```

### 9.4 Create Guestbook Message

**Endpoint:** `POST /api/messages`  
**Method:** POST  
**Content-Type:** `application/json`  
**Description:** Creates a new guestbook message entry in the Supabase database.

**Request Body:**
```json
{
  "name": "Visitor Name",
  "email": "visitor@example.com",
  "message": "This is my message"
}
```

**Validation Rules:**
- All three fields (`name`, `email`, `message`) are required
- Fields are trimmed of leading/trailing whitespace
- Empty fields after trimming return a 400 error

**Success Response (201):**
```json
[
  {
    "id": 2,
    "name": "Visitor Name",
    "email": "visitor@example.com",
    "message": "This is my message",
    "created_at": "2026-02-24T12:00:00+00:00"
  }
]
```

**Validation Error Response (400):**
```json
{
  "error": "Name, email, and message are required."
}
```

---

## 10. Responsive Design

The website is fully responsive and optimized for three screen sizes using CSS media queries.

### 10.1 Breakpoints

| Breakpoint | Target Devices | Key Changes |
|---|---|---|
| > 968px | Desktop / Laptop | Full multi-column layouts, hover effects |
| 641px – 968px | Tablet | Two-column grids collapse, reduced padding |
| ≤ 640px | Mobile | Single column, hamburger menu, stacked cards |

### 10.2 Mobile Adaptations

- **Navigation:** Hamburger menu replaces horizontal nav links
- **Hero Section:** Reduced font sizes, smaller profile image
- **About Grid:** Switches from 2-column to single column
- **Skills Grid:** Switches from 3-column to single column
- **Goals Grid:** Switches from 3-column to 2-column, then single column
- **Repos Grid:** Switches from 2-column to single column
- **Guestbook:** Form and messages stack vertically
- **Footer:** Social icons remain horizontally centered

### 10.3 CSS Architecture

**File:** `frontend/src/assets/styles.css` (1,160 lines)

Key CSS features used:
- **CSS Custom Properties (Variables):** For consistent theming (neon-red color palette)
- **CSS Grid:** For multi-column layouts (about, skills, goals, repos, resources)
- **Flexbox:** For alignment and spacing within components
- **Backdrop Filter:** For frosted glass effect on the navbar
- **CSS Animations:** Scroll indicator bounce, profile image glow pulse
- **CSS Transitions:** Hover effects on cards, buttons, and links
- **Media Queries:** Responsive breakpoints at 968px and 640px

### 10.4 Design Theme

The website uses a **neon-red cyberpunk** aesthetic:

| Variable | Value | Usage |
|---|---|---|
| `--neon-red` | `#ff0055` | Primary accent color |
| `--neon-red-bright` | `#ff1744` | Hover states |
| `--neon-red-dark` | `#cc0033` | Gradient endpoints |
| `--dark-bg` | `#000000` | Page background |
| `--dark-section` | `#0a0a0a` | Alternating section background |
| `--card-bg` | `#111111` | Card backgrounds |
| `--text-primary` | `#ffffff` | Main text color |
| `--text-secondary` | `#b0b0b0` | Subdued text color |

**Fonts:**
- **Orbitron** — Used for headings (futuristic/tech feel)
- **Rajdhani** — Used for body text (clean, modern)

---

## 11. Deployment

### 11.1 Frontend Deployment (Vercel)

| Setting | Value |
|---|---|
| Platform | Vercel (vercel.com) |
| Repository | GitHub: H1karuuu/personal-website-finals |
| Root Directory | `frontend` |
| Framework Preset | Vite |
| Build Command | `npm run build` |
| Output Directory | `dist` |
| Environment Variable | `VITE_API_URL` = Render backend URL + `/api` |

**Steps:**
1. Push code to GitHub repository
2. Import the repository on Vercel
3. Set the root directory to `frontend`
4. Add the `VITE_API_URL` environment variable
5. Deploy — Vercel automatically builds with Vite

### 11.2 Backend Deployment (Render.com)

| Setting | Value |
|---|---|
| Platform | Render (render.com) |
| Service Type | Web Service |
| Repository | GitHub: H1karuuu/personal-website-finals |
| Root Directory | `backend` |
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app --bind 0.0.0.0:$PORT` |
| Environment Variables | `SUPABASE_URL`, `SUPABASE_KEY`, `GITHUB_USERNAME` |

**Steps:**
1. Create a new Web Service on Render
2. Connect the GitHub repository
3. Set root directory to `backend`
4. Configure the build and start commands
5. Add environment variables for Supabase and GitHub
6. Deploy

### 11.3 Database Setup (Supabase)

1. Create a new project on supabase.com
2. Navigate to the SQL Editor
3. Run the SQL schema from Section 8.3 to create the `messages` table
4. Copy the **Project URL** and **anon (public) API key** from Project Settings → API
5. Set these values as environment variables in Render

---

## 12. Features Summary

| # | Feature | Implementation | HTTP Method |
|---|---|---|---|
| 1 | Personal portfolio with multiple sections | Vue.js SPA | — |
| 2 | Responsive design (mobile & desktop) | CSS media queries | — |
| 3 | Dynamic GitHub repository showcase | Flask API + GitHub API | GET |
| 4 | Guestbook - view messages | Flask API + Supabase | GET |
| 5 | Guestbook - submit messages | Flask API + Supabase | POST |
| 6 | Animated hero banner | CSS + GIF image | — |
| 7 | Social media footer links | SVG icons + external links | — |
| 8 | Navigation with smooth scrolling | Vue.js + CSS | — |
| 9 | Mobile hamburger menu | Vue.js reactive state | — |
| 10 | Form validation | Client-side + Server-side | — |
| 11 | Loading states & error handling | Vue.js reactive data | — |
| 12 | REST API Backend | Flask on Render.com | GET, POST |
| 13 | PostgreSQL Database | Supabase | — |
| 14 | Cross-Origin Support | Flask-CORS | — |

---

## 13. Screenshots / Page Sections

*(Insert screenshots of the following sections when preparing the Word document)*

1. **Hero Section** — Full-width banner with profile photo, name, and CTA buttons
2. **About Me** — Bio paragraphs with stats cards
3. **Personal History** — Timeline layout with education and experience
4. **Skills & Interests** — Three-column skill categories with icons
5. **Goals & Achievements** — Six goal cards in a responsive grid
6. **My Projects** — GitHub repository cards with language, stars, and forks
7. **Get In Touch** — Contact information display
8. **Leave a Message (Guestbook)** — Form and message list side by side
9. **Footer** — Social media SVG icons with neon glow
10. **Mobile View** — Hamburger menu, stacked single-column layout
11. **Render Dashboard** — Backend API running on Render.com
12. **Supabase Dashboard** — Messages table with stored entries

---

## 14. How to Run Locally

### 14.1 Prerequisites

- **Node.js** (v18 or higher) and **npm**
- **Python** (v3.9 or higher) and **pip**
- A **Supabase** project with the `messages` table created

### 14.2 Backend Setup

```bash
# Navigate to the backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Create a .env file with your credentials
# SUPABASE_URL=https://your-project.supabase.co
# SUPABASE_KEY=your-anon-key
# GITHUB_USERNAME=H1karuuu

# Start the Flask development server
python app.py
```

The API will be available at `http://localhost:5000`.

### 14.3 Frontend Setup

```bash
# Navigate to the frontend directory
cd frontend

# Install Node.js dependencies
npm install

# Create a .env file
# VITE_API_URL=http://localhost:5000/api

# Start the Vite development server
npm run dev
```

The frontend will be available at `http://localhost:5173`.

### 14.4 Build for Production

```bash
cd frontend
npm run build
```

The production-ready files will be generated in the `frontend/dist/` directory.

---

## 15. Environment Variables

### Frontend (`frontend/.env`)

| Variable | Description | Example |
|---|---|---|
| `VITE_API_URL` | Base URL of the Flask API | `https://your-app.onrender.com/api` |

### Backend (`backend/.env`)

| Variable | Description | Example |
|---|---|---|
| `SUPABASE_URL` | Supabase project URL | `https://xxxxx.supabase.co` |
| `SUPABASE_KEY` | Supabase anon (public) API key | `eyJhbGciOiJIUzI1NiIs...` |
| `GITHUB_USERNAME` | GitHub username for repos fetch | `H1karuuu` |

---

## 16. Resources and Credits

### Fonts
- **Orbitron** — Google Fonts (https://fonts.google.com/specimen/Orbitron)
- **Rajdhani** — Google Fonts (https://fonts.google.com/specimen/Rajdhani)

### Images
- Profile Photo: Personal image owned by the developer
- Header Banner: Original animated GIF owned by the developer

### Frameworks & Libraries
- **Vue.js 3** — https://vuejs.org/
- **Vite** — https://vitejs.dev/
- **Flask** — https://flask.palletsprojects.com/
- **Supabase** — https://supabase.com/
- **GitHub REST API** — https://docs.github.com/en/rest

### Hosting
- **Vercel** — https://vercel.com/ (Frontend)
- **Render** — https://render.com/ (Backend)

### AI Assistance
- Development tools were used to assist in planning and refining code structure
- Guided assistance supported layout, styling, and responsive design decisions
- Final implementation, customization, and content by the developer

---

## 17. Conclusion

This personal portfolio website demonstrates a complete full-stack web development workflow. The project fulfills the following course requirements:

- **Vue.js frontend** — The entire website is built as a Vue.js 3 single-page application with reactive data binding, component architecture, and modern JavaScript.
- **Flask REST API backend** — A Python-based API hosted on Render.com serves data to the frontend through well-defined endpoints.
- **GET and POST methods** — The guestbook feature implements both GET (retrieve messages) and POST (submit messages) HTTP methods. The GitHub repos feature uses an additional GET endpoint.
- **Supabase database** — All guestbook messages are persisted in a PostgreSQL database hosted on Supabase with proper Row Level Security policies.
- **Responsive design** — The website is fully responsive across desktop, tablet, and mobile devices using CSS media queries, Grid, and Flexbox.

The project showcases practical skills in frontend development, API design, database integration, deployment, and responsive web design — core competencies for modern web programming.

---

*End of Documentation*
