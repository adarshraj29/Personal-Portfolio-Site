<div align="center">

# ✨ Adarsh Raj — Personal Portfolio & Showcase

> **A modern, responsive, card-based MCA portfolio & personal showcase built with Python, Flask, Jinja2, and Vanilla Web Technologies — featuring an integrated private administration portal.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-black?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

[View Demo](#-quick-start) • [Features](#-features) • [Project Structure](#-project-structure) • [Setup & Installation](#-setup--installation) • [Admin Dashboard](#-admin-dashboard--file-manager) • [Customization](#-customization-guide)

---

</div>

## 📌 Overview

This repository contains a full-featured, sleek personal portfolio website designed for **Adarsh Raj**, an MCA student and aspiring software developer. 

Unlike static portfolio templates, this web application is powered by **Flask** and features both:
1. **A public-facing portfolio** designed with editorial typography, interactive cards, smooth navigation, and a direct contact form.
2. **A private administrative workspace (`/admin`)** allowing the portfolio owner to securely sign in, upload and replace their public resume, store private academic credentials (certificates, marksheets, project reports), and review contact form submissions locally.

---

## 🚀 Features

### 🌟 Public Portfolio
- **Hero Section**: Eyebrow status indicator (`Open to internships`), dynamic greeting, action buttons, and animated code card mockup.
- **About Me**: Narrative background, quick summary statistics, and personal philosophy.
- **Interactive Toolkit / Skills**: Card grid showcasing programming languages, web technologies, and database proficiencies.
- **Academic & Project Journey**: Clean vertical timeline tracking educational milestones and self-directed project development.
- **Selected Works**: Showcase cards highlighting projects, concepts, categories, and technology stacks.
- **Resume Section**: Real-time status badge showing uploaded resume details with a direct one-click download button.
- **Notes & Ideas (Blog Cards)**: Editorial reading journal for developer notes, tech tutorials, and insights.
- **Contact Form**: Interactive form allowing visitors to leave a message. Validated on the server side and stored safely in local storage.
- **Responsive Layout**: Designed mobile-first with adaptive layouts, custom navigation drawer, and cross-browser support.

### 🛡️ Private Admin Workspace (`/admin`)
- **Password-Protected Authentication**: Secure session-based manager dashboard protected by a configurable admin password.
- **Resume Management**: Upload or replace your public resume (`.pdf`, `.doc`, `.docx`) up to 10 MB.
- **Private Academic Vault**: Securely upload certificates, transcripts, and marksheets (`.pdf`, `.docx`, `.xlsx`, `.pptx`, `.png`, `.jpg`).
- **Protected Downloads**: Academic files cannot be accessed or downloaded by the public without an active manager login session.
- **Local Message Log**: View visitor inquiries and messages sent via the contact form in real-time.
- **File Validation & Safety**: Uses Werkzeug's `secure_filename`, strictly enforced extension whitelisting, and size restrictions.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3.8+, Flask 3.x | Routing, template rendering, file handling, session management |
| **Templating** | Jinja2 | Dynamic HTML rendering, flash notifications, component loops |
| **Frontend** | HTML5, Modern CSS3 | Custom typography (`Manrope`, `DM Mono`), flexbox & CSS grid, animations |
| **Client Script** | Vanilla JavaScript | Mobile hamburger drawer toggle, interactive accessibility states |
| **Data Storage** | Local JSON & Secure Storage | Lightweight, portable metadata storage (`data/` directory) |
| **Security** | Werkzeug Utilities | Safe filenames, file size enforcement, session hashing |

---

## 📂 Project Structure

```text
Personal-Portfolio-Site/
│
├── .gitignore                   # Files and directories ignored by Git (venv, uploads, secrets)
├── .env.example                 # Template for environment variables
├── requirements.txt             # Project dependencies (Flask)
├── README.md                    # Project documentation
├── app.py                       # Main Flask application with routes and controllers
│
├── data/                        # Persistent local data directory
│   ├── messages.json            # Contact messages store (JSON)
│   └── private_uploads/         # Uploaded documents
│       ├── academic/            # Private academic files (restricted to admin)
│       └── resume/              # Public resume file
│
├── static/                      # Static assets
│   ├── css/
│   │   └── style.css            # Custom responsive styles and color system
│   └── js/
│       └── main.js              # Navigation toggling and client UI behaviors
│
└── templates/                   # Jinja2 HTML templates
    ├── index.html               # Main public portfolio page
    └── admin.html               # Private portfolio manager dashboard
```

---

## ⚡ Setup & Installation

Follow these steps to run the portfolio on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/adarshraj29/Personal-Portfolio-Site.git
cd Personal-Portfolio-Site
```

### 2. Create and Activate a Virtual Environment

**On Windows (Command Prompt / PowerShell):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

Create a `.env` file or export environment variables:

```bash
# Windows (cmd):
set PORTFOLIO_SECRET_KEY=your-secure-random-key
set PORTFOLIO_ADMIN_PASSWORD=your-custom-admin-password

# Windows (PowerShell):
$env:PORTFOLIO_SECRET_KEY="your-secure-random-key"
$env:PORTFOLIO_ADMIN_PASSWORD="your-custom-admin-password"

# macOS / Linux:
export PORTFOLIO_SECRET_KEY="your-secure-random-key"
export PORTFOLIO_ADMIN_PASSWORD="your-custom-admin-password"
```

> **Note:** If no environment variables are set, default fallback values are provided for local development.

### 5. Start the Application
```bash
python app.py
```

### 6. Access the Website
Open your browser and navigate to:
- **Public Portfolio:** [http://127.0.0.1:5000](http://127.0.0.1:5000)
- **Admin Manager:** [http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin)

---

## 🔐 Admin Dashboard & File Manager

To manage your resume and documents:

1. Click **Manage portfolio ↗** in the top navigation or go directly to `http://127.0.0.1:5000/admin`.
2. Enter the admin password:
   - **Default local password:** `admin123` *(change this via `PORTFOLIO_ADMIN_PASSWORD` in production)*.
3. Once logged in, you can:
   - 📄 **Upload / Replace Resume**: Instantly updates the download link on the public homepage.
   - 🎓 **Upload Academic Documents**: Store marksheets, degree certificates, and letters of recommendation.
   - 📬 **View Inbound Inquiries**: Review visitor messages submitted via the contact form.
   - 🚪 **Sign Out**: Clears your session securely.

---

## 🎨 Customization Guide

You can easily customize all details directly in [app.py](file:///d:/personal%20portfolio%20site/app.py):

### Updating Your Profile
Edit the `PROFILE` dictionary in `app.py`:
```python
PROFILE = {
    "name": "Your Name",
    "initials": "YN",
    "role": "MCA Student · Aspiring Software Engineer",
    "tagline": "Crafting clean and impactful digital products.",
    "location": "India",
    "email": "your.email@example.com",
    "about": "Your bio and journey description here...",
    "availability": "Open to internships & new opportunities",
}
```

### Updating Skills & Projects
Edit `SKILLS`, `PROJECTS`, `EXPERIENCE`, and `BLOGS` in `app.py`:
```python
SKILLS = [
    {"name": "Python", "level": "Web & Scripting", "icon": "Py"},
    {"name": "Flask", "level": "Backend APIs", "icon": "Fl"},
    ...
]
```

### Styling & Theme
Customize colors, fonts, and spacing in [static/css/style.css](file:///d:/personal%20portfolio%20site/static/css/style.css).

---

## 🌐 Deployment

The application is structured to deploy smoothly on modern hosting providers:

### Deploy to Render / Railway / PythonAnywhere
1. Create a `Procfile` (if deploying to Heroku or Render):
   ```text
   web: gunicorn app:app
   ```
2. Add `gunicorn` to your dependencies if required:
   ```bash
   pip install gunicorn
   pip freeze > requirements.txt
   ```
3. Set your production environment variables in your cloud provider's dashboard:
   - `PORTFOLIO_SECRET_KEY`: Long random string.
   - `PORTFOLIO_ADMIN_PASSWORD`: Strong password.
   - `PYTHON_VERSION`: e.g., `3.10.x` or `3.11.x`.

---

## 🔒 Security Best Practices

- **Change Demo Credentials**: Always set a strong, unique `PORTFOLIO_ADMIN_PASSWORD` and `PORTFOLIO_SECRET_KEY` before public hosting.
- **Protect Uploaded Data**: The `data/private_uploads/` folder is excluded by default in `.gitignore` to prevent committing personal transcripts or documents to public repositories.
- **Production Server**: For live deployments, run behind a production WSGI server (such as Gunicorn or uWSGI) with HTTPS enabled.

---

## 👨‍💻 Author

**Adarsh Raj**  
- 🎓 MCA Student · Aspiring Software Developer  
- 🐙 GitHub: [@adarshraj29](https://github.com/adarshraj29)  
- ✉️ Email: [rajadarsh232@gmail.com](mailto:rajadarsh232@gmail.com)

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

<div align="center">
  <sub>Built with ❤️ by Adarsh Raj</sub>
</div>
