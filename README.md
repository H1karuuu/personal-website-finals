# Jayzee Portfolio — Personal Profile Website

A personal portfolio website built with **Vue.js 3** (frontend) and a **Flask REST API** (backend), connected to a **Supabase** PostgreSQL database. Features a guestbook with message posting, GitHub repos showcase, and a fully responsive neon-red cyberpunk design.

---

## Live Links

| Service  | URL |
| -------- | --- |
| Frontend | _(Deploy to Vercel — see instructions below)_ |
| Backend  | _(Deploy to Render — see instructions below)_ |

---

## Tech Stack

| Layer    | Technology |
| -------- | ---------- |
| Frontend | Vue.js 3, Vite, CSS3 |
| Backend  | Python, Flask, Flask-CORS, Gunicorn |
| Database | Supabase (PostgreSQL) |
| Hosting  | Vercel (frontend), Render (backend) |

---

## Project Structure

```
personal-website-finals/
├── frontend/                  # Vue.js 3 + Vite frontend
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   │   ├── Photo/
│   │   │   │   ├── Profile.jpg       # Profile photo
│   │   │   │   └── Banner.jpg        # Hero banner/cover image
│   │   │   └── styles.css            # Global styles
│   │   ├── components/
│   │   │   └── PersonalProfile.vue   # Main portfolio component
│   │   ├── App.vue
│   │   └── main.js
│   ├── .env                           # VITE_API_URL
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── backend/                   # Flask REST API
│   ├── app.py                 # Flask app with routes
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # SUPABASE_URL, SUPABASE_KEY
│   └── .gitignore
└── README.md
```

---

## Features

- **Personal Profile** — Hero section with cover banner (Facebook-style), animated profile picture, about me, education timeline, skills grid
- **GitHub Repos Showcase** — Dynamically fetches and displays public GitHub repositories via the REST API (`GET /api/repos`)
- **Guestbook** — Visitors can leave messages (name, email, message) which are stored in Supabase and displayed in real-time
  - `POST /api/messages` — Submit a new message
  - `GET /api/messages` — Retrieve all messages (newest first)
- **Goals & Achievements** — Cards displaying personal/professional goals
- **Contact Info** — Email, phone, location details
- **Social Media Links** — Facebook, Instagram, GitHub, LinkedIn in footer
- **Responsive Design** — Fully responsive for desktop, tablet, and mobile
- **Neon Cyberpunk Theme** — Dark background with red neon accents, glow effects, and smooth animations

---

## REST API Endpoints

| Method | Endpoint         | Description                          |
| ------ | ---------------- | ------------------------------------ |
| GET    | `/`              | Health check                         |
| GET    | `/api/messages`  | Retrieve all guestbook messages      |
| POST   | `/api/messages`  | Create a new guestbook message       |
| GET    | `/api/repos`     | Fetch GitHub repositories            |

### POST `/api/messages` — Request Body

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Great portfolio!"
}
```

---

## Supabase Setup

### 1. Create the `messages` table

Go to your Supabase dashboard → **SQL Editor** → Run this:

```sql
CREATE TABLE messages (
  id BIGSERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT NOT NULL,
  message TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Enable Row Level Security
ALTER TABLE messages ENABLE ROW LEVEL SECURITY;

-- Allow anyone to read messages
CREATE POLICY "Allow public read" ON messages
  FOR SELECT USING (true);

-- Allow anyone to insert messages
CREATE POLICY "Allow public insert" ON messages
  FOR INSERT WITH CHECK (true);
```

### 2. Get your Supabase credentials

- Go to **Project Settings** → **API**
- Copy the **Project URL** and **anon/public key**

---

## Local Development

### Frontend

```bash
cd frontend
npm install
```

Create `frontend/.env`:
```
VITE_API_URL=http://localhost:5000/api
```

```bash
npm run dev
```

The frontend runs at `http://localhost:5173`.

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

Create `backend/.env`:
```
SUPABASE_URL=https://rxztomvvwytetepornaq.supabase.co
SUPABASE_KEY=your_supabase_anon_key
GITHUB_USERNAME=H1karuuu
```

```bash
python app.py
```

The API runs at `http://localhost:5000`.

---

## Deployment

### Frontend → Vercel

1. Push the repo to GitHub
2. Go to [vercel.com](https://vercel.com) → **New Project** → Import your GitHub repo
3. Set the **Root Directory** to `frontend`
4. Framework Preset: **Vite**
5. Add Environment Variable:
   - `VITE_API_URL` = `https://your-render-backend-url.onrender.com/api`
6. Click **Deploy**

### Backend → Render (Step-by-Step)

#### Step 1: Create a Render Account
1. Go to [render.com](https://render.com) and sign up (GitHub sign-in recommended)

#### Step 2: Create a New Web Service
1. From the Render dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository (`H1karuuu/personal-website-finals`)

#### Step 3: Configure the Service
Fill in these settings:

| Setting | Value |
| ------- | ----- |
| **Name** | `jayzee-portfolio-api` |
| **Region** | Singapore (or nearest) |
| **Root Directory** | `backend` |
| **Runtime** | Python |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app --bind 0.0.0.0:$PORT` |
| **Instance Type** | Free |

#### Step 4: Add Environment Variables
Click **"Environment"** section and add:

| Key | Value |
| --- | ----- |
| `SUPABASE_URL` | `https://rxztomvvwytetepornaq.supabase.co` |
| `SUPABASE_KEY` | `your_supabase_anon_public_key` |
| `GITHUB_USERNAME` | `H1karuuu` |
| `PYTHON_VERSION` | `3.11.0` |

#### Step 5: Deploy
1. Click **"Create Web Service"**
2. Render will automatically build and deploy your Flask API
3. Once deployed, you'll get a URL like: `https://jayzee-portfolio-api.onrender.com`
4. Test it: visit `https://jayzee-portfolio-api.onrender.com/` — you should see:
   ```json
   {"message": "Jayzee Portfolio API is running!", "status": "ok"}
   ```

#### Step 6: Update Frontend
1. Go back to Vercel → Your project → **Settings** → **Environment Variables**
2. Update `VITE_API_URL` to `https://jayzee-portfolio-api.onrender.com/api`
3. Redeploy the frontend

---

## Adding Your Photos

Place your images in `frontend/src/assets/Photo/`:

- `Profile.jpg` — Your profile picture (the one in the white shirt)
- `Banner.jpg` — The pixel art Japanese scene (used as hero cover/banner)

The code imports these automatically. If your images have different extensions (`.png`, `.webp`), update the imports in `PersonalProfile.vue`:

```js
import profileImage from '@/assets/Photo/Profile.png'
import bannerImage from '@/assets/Photo/Banner.png'
```

---

## Resources & Credits

- **Fonts**: [Orbitron](https://fonts.google.com/specimen/Orbitron), [Rajdhani](https://fonts.google.com/specimen/Rajdhani) — Google Fonts
- **Icons**: Inline SVGs (GitHub, Facebook, Instagram, LinkedIn)
- **Framework**: Vue.js 3, Vite
- **Backend**: Flask, Gunicorn
- **Database**: Supabase (PostgreSQL)
- **AI Assistance**: Used for code structure planning and optimization
- **Final implementation and content**: Jayzee

---

## License

This project is for educational purposes. © 2025 Jayzee. All rights reserved.