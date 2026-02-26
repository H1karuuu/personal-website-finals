<template>
  <div class="portfolio" :class="{ 'light-mode': isLightMode }">
    <!-- Navigation -->
    <nav class="navbar">
      <div class="nav-container">
        <div class="logo">JAYZEE</div>
        <button class="menu-toggle" :class="{ active: isMenuOpen }" @click="toggleMenu" aria-label="Toggle menu">
          <span></span>
          <span></span>
          <span></span>
        </button>
        <ul class="nav-menu" :class="{ active: isMenuOpen }">
          <li v-for="item in navItems" :key="item.id">
            <a :href="`#${item.id}`" class="nav-link" @click="closeMenu">{{ item.name }}</a>
          </li>
          <li>
            <button class="theme-toggle" @click="toggleTheme" :aria-label="isLightMode ? 'Switch to dark mode' : 'Switch to light mode'">
              <svg v-if="isLightMode" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
              <svg v-else xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
            </button>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Hero Section with Banner -->
    <section id="home" class="hero-section">
      <div class="hero-banner">
        <img :src="bannerImage" alt="Cover Banner" class="banner-image">
        <div class="banner-overlay"></div>
      </div>
      <div class="hero-content">
        <div class="profile-image-container">
          <img :src="profileImage" alt="Profile Picture" class="profile-image">
          <div class="image-glow"></div>
        </div>
        <h1 class="hero-title">{{ hero.title }}</h1>
        <p class="hero-subtitle">{{ hero.subtitle }}</p>
        <p class="hero-description">{{ hero.description }}</p>
        <div class="cta-buttons">
          <a href="#about" class="btn btn-primary">Explore My Work</a>
          <a href="#contact" class="btn btn-secondary">Get In Touch</a>
        </div>
      </div>
      <div class="scroll-indicator">
        <span></span>
      </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
      <div class="container">
        <h2 class="section-title">About Me</h2>
        <div class="section-content">
          <div class="about-grid">
            <div class="about-text">
              <p v-for="(paragraph, index) in about.paragraphs" :key="index">
                {{ paragraph }}
              </p>
            </div>
            <div class="about-stats">
              <div v-for="stat in about.stats" :key="stat.label" class="stat-card">
                <div class="stat-number">{{ stat.number }}</div>
                <div class="stat-label">{{ stat.label }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- History Section -->
    <section id="history" class="section section-dark">
      <div class="container">
        <h2 class="section-title">Personal History</h2>
        <div class="section-content">
          <div class="timeline">
            <div v-for="item in timeline" :key="item.title" class="timeline-item">
              <div class="timeline-marker"></div>
              <div class="timeline-content">
                <h3>{{ item.title }}</h3>
                <h4>{{ item.subtitle }}</h4>
                <p>{{ item.description }}</p>
                <p v-if="item.detail" class="timeline-detail">{{ item.detail }}</p>
                <ul v-if="item.list" class="timeline-list">
                  <li v-for="listItem in item.list" :key="listItem">{{ listItem }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section">
      <div class="container">
        <h2 class="section-title">Skills & Interests</h2>
        <div class="section-content">
          <div class="skills-grid">
            <div v-for="category in skills" :key="category.title" class="skill-category">
              <div class="skill-icon" v-html="category.icon"></div>
              <h3>{{ category.title }}</h3>
              <ul class="skill-list">
                <li v-for="skill in category.items" :key="skill">{{ skill }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Goals Section -->
    <section id="goals" class="section section-dark">
      <div class="container">
        <h2 class="section-title">Goals & Achievements</h2>
        <div class="section-content">
          <div class="goals-container">
            <div v-for="goal in goals" :key="goal.title" class="goal-card">
              <div class="goal-icon" v-html="goal.icon"></div>
              <h3>{{ goal.title }}</h3>
              <p>{{ goal.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- GitHub Projects Section -->
    <section id="projects" class="section">
      <div class="container">
        <h2 class="section-title">My Projects</h2>
        <p class="section-subtitle">Showcasing my GitHub repositories</p>
        <div class="section-content">
          <p v-if="isLoadingRepos" class="loading-text" style="text-align:center;">Loading repositories...</p>
          <p v-else-if="repos.length === 0" class="no-messages" style="text-align:center;">No repositories found.</p>
          <div v-else class="repos-grid">
            <a
              v-for="repo in repos"
              :key="repo.id"
              :href="repo.html_url"
              target="_blank"
              rel="noopener"
              class="repo-card"
            >
              <div class="repo-header">
                <svg class="repo-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 16 16" fill="currentColor"><path d="M2 2.5A2.5 2.5 0 014.5 0h8.75a.75.75 0 01.75.75v12.5a.75.75 0 01-.75.75h-2.5a.75.75 0 110-1.5h1.75v-2h-8a1 1 0 00-.714 1.7.75.75 0 01-1.072 1.05A2.495 2.495 0 012 11.5v-9zm10.5-1V9h-8c-.356 0-.694.074-1 .208V2.5a1 1 0 011-1h8zM5 12.25v3.25a.25.25 0 00.4.2l1.45-1.087a.25.25 0 01.3 0L8.6 15.7a.25.25 0 00.4-.2v-3.25a.25.25 0 00-.25-.25h-3.5a.25.25 0 00-.25.25z"/></svg>
                <h3>{{ repo.name }}</h3>
              </div>
              <p class="repo-description">{{ repo.description || 'No description provided' }}</p>
              <div class="repo-meta">
                <span v-if="repo.language" class="repo-language">
                  <span class="language-dot" :style="{ background: getLanguageColor(repo.language) }"></span>
                  {{ repo.language }}
                </span>
                <span class="repo-stars">
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/></svg>
                  {{ repo.stargazers_count }}
                </span>
                <span class="repo-forks">
                  <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 16 16" fill="currentColor"><path d="M5 3.25a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm0 2.122a2.25 2.25 0 10-1.5 0v.878A2.25 2.25 0 005.75 8.5h1.5v2.128a2.251 2.251 0 101.5 0V8.5h1.5a2.25 2.25 0 002.25-2.25v-.878a2.25 2.25 0 10-1.5 0v.878a.75.75 0 01-.75.75h-4.5A.75.75 0 015 6.25v-.878zm3.75 7.378a.75.75 0 11-1.5 0 .75.75 0 011.5 0zm3-8.75a.75.75 0 100-1.5.75.75 0 000 1.5z"/></svg>
                  {{ repo.forks_count }}
                </span>
              </div>
              <div class="repo-updated">Updated {{ formatRepoDate(repo.updated_at) }}</div>
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
      <div class="container">
        <h2 class="section-title">Get In Touch</h2>
        <div class="section-content">
          <div class="contact-container">
            <div class="contact-info">
              <h3>Let's Connect</h3>
              <p>{{ contact.intro }}</p>
              <div class="contact-methods">
                <div v-for="method in contact.methods" :key="method.title" class="contact-method">
                  <div class="contact-icon" v-html="method.icon"></div>
                  <div class="contact-details">
                    <h4>{{ method.title }}</h4>
                    <p>{{ method.value }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Guestbook / Messages Section -->
    <section id="guestbook" class="section section-dark">
      <div class="container">
        <h2 class="section-title">Leave a Message</h2>
        <div class="section-content">
          <div class="guestbook-container">
            <!-- Message Form -->
            <div class="guestbook-form">
              <form @submit.prevent="handleSubmit">
                <div class="form-group">
                  <input
                    v-model="form.name"
                    type="text"
                    placeholder="Your Name"
                    required
                  >
                </div>
                <div class="form-group">
                  <input
                    v-model="form.email"
                    type="email"
                    placeholder="Your Email"
                    required
                  >
                </div>
                <div class="form-group">
                  <textarea
                    v-model="form.message"
                    rows="5"
                    placeholder="Your Message"
                    required
                  ></textarea>
                </div>
                <button type="submit" class="btn btn-primary" :disabled="isSubmitting">
                  {{ isSubmitting ? 'Sending...' : 'Send Message' }}
                </button>
                <p v-if="submitStatus" class="submit-status" :class="submitStatusClass">
                  {{ submitStatus }}
                </p>
              </form>
            </div>

            <!-- Messages List -->
            <div class="guestbook-messages">
              <h3 class="messages-title">Recent Messages</h3>
              <p v-if="isLoadingMessages" class="loading-text">Loading messages...</p>
              <p v-else-if="messages.length === 0" class="no-messages">No messages yet. Be the first to leave one!</p>
              <div v-else class="messages-list">
                <div v-for="msg in messages" :key="msg.id" class="message-card">
                  <div class="message-header">
                    <span class="message-author">{{ msg.name }}</span>
                    <span class="message-date">{{ formatDate(msg.created_at) }}</span>
                  </div>
                  <p class="message-body">{{ msg.message }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Resources Section -->
    <section id="resources" class="section">
      <div class="container">
        <h2 class="section-title">Resources & Credits</h2>
        <div class="section-content">
          <div class="resources-grid">
            <div v-for="category in resources" :key="category.title" class="resource-category">
              <h3>{{ category.title }}</h3>
              <ul>
                <li v-for="item in category.items" :key="item.text">
                  <a v-if="item.link" :href="item.link" target="_blank" rel="noopener">
                    {{ item.text }}
                  </a>
                  <span v-else>{{ item.text }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-socials">
            <a href="https://www.facebook.com/Jayzee018" target="_blank" rel="noopener" aria-label="Facebook" class="social-link">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </a>
            <a href="https://www.instagram.com/_jayzee18/" target="_blank" rel="noopener" aria-label="Instagram" class="social-link">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
            </a>
            <a href="https://github.com/H1karuuu" target="_blank" rel="noopener" aria-label="GitHub" class="social-link">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            </a>
            <a href="https://www.linkedin.com/in/john-christian-lopez-7b9507322/" target="_blank" rel="noopener" aria-label="LinkedIn" class="social-link">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
          </div>
          <p>&copy; 2025 Jayzee. All rights reserved.</p>
          <p>Built with passion for technology and innovation</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
import profileImage from '@/assets/Photo/Profile.png'
import bannerImage from '@/assets/Photo/header.gif'

const API_URL = import.meta.env.VITE_API_URL || 'https://jayzee-portfolio-api.onrender.com/api'

export default {
  name: 'PersonalProfile',
  data() {
    return {
      isMenuOpen: false,
      isLightMode: false,
      profileImage,
      bannerImage,
      isSubmitting: false,
      isLoadingMessages: false,
      isLoadingRepos: false,
      submitStatus: '',
      submitStatusClass: '',
      messages: [],
      repos: [],
      navItems: [
        { id: 'home', name: 'Home' },
        { id: 'about', name: 'About' },
        { id: 'history', name: 'History' },
        { id: 'skills', name: 'Skills' },
        { id: 'goals', name: 'Goals' },
        { id: 'projects', name: 'Projects' },
        { id: 'contact', name: 'Contact' },
        { id: 'guestbook', name: 'Guestbook' }
      ],
      hero: {
        title: 'Welcome to My Portfolio',
        subtitle: "I'm Jayzee",
        description: 'IT Student | Technology Enthusiast | Future Cybersecurity Specialist'
      },
      about: {
        paragraphs: [
          'I am someone who is deeply interested in technology, especially in how new innovations shape the future. I enjoy understanding how things work, from machine parts to computer systems, and I\'m constantly learning new skills that will help me grow in the IT field.',
          'My passion lies in cybersecurity and building innovative solutions. I believe in the power of technology to transform lives and create opportunities. With a strong foundation in IT and a drive to excel, I\'m working towards establishing my own firm specializing in cybersecurity.'
        ],
        stats: [
          { number: '2024', label: 'Graduate Year' },
          { number: 'BSIT', label: 'Current Course' },
          { number: '50%', label: 'Scholarship' }
        ]
      },
      timeline: [
        {
          title: 'Education',
          subtitle: 'National University MOA Campus',
          description: 'Graduated from Senior High School in Pasay City',
          detail: 'Awarded NU SHS Discount 2024 – 50% Tuition Scholarship (excluding miscellaneous fees)'
        },
        {
          title: 'Current Studies',
          subtitle: 'Bachelor of Science in Information Technology',
          description: 'Pursuing my passion for technology and cybersecurity',
          detail: 'Focusing on front-end and back-end development, computer systems, and security'
        },
        {
          title: 'IT Experience',
          subtitle: 'Practical Skills Development',
          description: 'Built hands-on experience through personal projects and gaming',
          list: [
            'Building and troubleshooting CPUs and desktop computers',
            'Basic front-end and back-end development',
            'Esports gaming on mobile and PC platforms'
          ]
        }
      ],
      skills: [
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>',
          title: 'Technical Skills',
          items: [
            'Computer Hardware Assembly & Troubleshooting',
            'Front-end Development (HTML, CSS, JavaScript)',
            'Back-end Development Basics',
            'Desktop Computer Systems',
            'Problem Solving & Critical Thinking'
          ]
        },
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="3" x2="6" y2="15"></line><circle cx="18" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><path d="M18 9a9 9 0 0 1-9 9"></path></svg>',
          title: 'Gaming & Strategy',
          items: [
            'Esports Gaming (Mobile & PC)',
            'Chess & Strategy Games',
            'Team Coordination',
            'Quick Decision Making'
          ]
        },
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="16"></line><line x1="8" y1="12" x2="16" y2="12"></line></svg>',
          title: 'Personal Interests',
          items: [
            'Understanding Machine Parts',
            'Technology Innovation',
            'Music (Various Genres)',
            'Walking & Physical Activity',
            'Continuous Learning'
          ]
        }
      ],
      goals: [
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>',
          title: 'Cybersecurity Firm',
          description: 'Start an IT firm specializing in cybersecurity solutions and protecting digital assets'
        },
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>',
          title: 'Financial Freedom',
          description: 'Achieve sustainable financial independence where resources enable dreams and opportunities'
        },
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>',
          title: 'Family & Community',
          description: 'Provide for the people I cherish and create positive impact in my community'
        },
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>',
          title: 'Industry Recognition',
          description: 'Become a notable figure in the IT industry through innovation and excellence'
        },
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polyline></svg>',
          title: 'Business Growth',
          description: 'Build and grow a successful company that creates value and employment opportunities'
        },
        {
          icon: '<svg xmlns="http://www.w3.org/2000/svg" width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>',
          title: 'Scholarship Achievement',
          description: 'Received NU SHS 50% Tuition Scholarship for academic excellence'
        }
      ],
      contact: {
        intro: "I'm always open to discussing new opportunities, collaborations, or just having a conversation about technology and innovation.",
        methods: [
          { icon: '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>', title: 'Email', value: 'jzlopez@student.apc.edu.ph' },
          { icon: '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>', title: 'Phone', value: '+63 945 334 4925' },
          { icon: '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>', title: 'Location', value: 'Pasay City, Philippines' }
        ]
      },
      resources: [
        {
          title: 'Fonts',
          items: [
            { text: 'Orbitron - Google Fonts', link: 'https://fonts.google.com/specimen/Orbitron' },
            { text: 'Rajdhani - Google Fonts', link: 'https://fonts.google.com/specimen/Rajdhani' }
          ]
        },
        {
          title: 'Images',
          items: [
            { text: 'Profile Photo: Personal image owned by the developer' },
            { text: 'All images used are original and for educational purposes' }
          ]
        },
        {
          title: 'Development',
          items: [
            { text: 'Vue.js 3 + Vite' },
            { text: 'Flask REST API Backend' },
            { text: 'Supabase (PostgreSQL)' },
            { text: 'Hosted on Vercel (Frontend) & Render (Backend)' }
          ]
        },
        {
          title: 'AI Assistance',
          items: [
            { text: 'Development tools were used to assist in planning and refining code structure' },
            { text: 'Guided assistance supported layout, styling, and responsive design decisions' },
            { text: 'Final implementation, customization, and content by Jayzee' }
          ]
        }
      ],
      form: {
        name: '',
        email: '',
        message: ''
      }
    }
  },
  mounted() {
    this.fetchMessages()
    this.fetchRepos()
    // Load saved theme preference
    const savedTheme = localStorage.getItem('theme')
    if (savedTheme === 'light') {
      this.isLightMode = true
    }
  },
  methods: {
    toggleTheme() {
      this.isLightMode = !this.isLightMode
      localStorage.setItem('theme', this.isLightMode ? 'light' : 'dark')
    },
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen
    },
    closeMenu() {
      this.isMenuOpen = false
    },
    formatDate(dateStr) {
      const date = new Date(dateStr)
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
    },
    async fetchMessages() {
      this.isLoadingMessages = true
      try {
        const res = await fetch(`${API_URL}/messages`)
        if (!res.ok) throw new Error('Failed to fetch messages')
        const data = await res.json()
        this.messages = data
      } catch (err) {
        console.error('Error fetching messages:', err)
      } finally {
        this.isLoadingMessages = false
      }
    },
    async fetchRepos() {
      this.isLoadingRepos = true
      try {
        const res = await fetch(`${API_URL}/repos`)
        if (!res.ok) throw new Error('Failed to fetch repos')
        const data = await res.json()
        this.repos = data
      } catch (err) {
        console.error('Error fetching repos:', err)
      } finally {
        this.isLoadingRepos = false
      }
    },
    formatRepoDate(dateStr) {
      const date = new Date(dateStr)
      const now = new Date()
      const diffMs = now - date
      const diffDays = Math.floor(diffMs / (1000 * 60 * 60 * 24))
      if (diffDays === 0) return 'today'
      if (diffDays === 1) return 'yesterday'
      if (diffDays < 30) return `${diffDays} days ago`
      if (diffDays < 365) return `${Math.floor(diffDays / 30)} months ago`
      return `${Math.floor(diffDays / 365)} years ago`
    },
    getLanguageColor(language) {
      const colors = {
        JavaScript: '#f1e05a',
        TypeScript: '#3178c6',
        Python: '#3572A5',
        HTML: '#e34c26',
        CSS: '#563d7c',
        Vue: '#41b883',
        Java: '#b07219',
        'C++': '#f34b7d',
        C: '#555555',
        PHP: '#4F5D95',
        Ruby: '#701516',
        Go: '#00ADD8',
        Rust: '#dea584',
        Shell: '#89e051',
        Dart: '#00B4AB',
        Kotlin: '#A97BFF',
        Swift: '#F05138'
      }
      return colors[language] || '#8b949e'
    },
    async handleSubmit() {
      this.isSubmitting = true
      this.submitStatus = ''
      try {
        const res = await fetch(`${API_URL}/messages`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name: this.form.name,
            email: this.form.email,
            message: this.form.message
          })
        })
        if (!res.ok) throw new Error('Failed to send message')
        this.submitStatus = 'Thank you for your message! 🎉'
        this.submitStatusClass = 'success'
        this.form = { name: '', email: '', message: '' }
        this.fetchMessages()
      } catch (err) {
        console.error('Error submitting message:', err)
        this.submitStatus = 'Failed to send message. Please try again.'
        this.submitStatusClass = 'error'
      } finally {
        this.isSubmitting = false
        setTimeout(() => { this.submitStatus = '' }, 5000)
      }
    }
  }
}
</script>
