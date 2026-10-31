from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, abort
from werkzeug.utils import secure_filename
from pathlib import Path
from datetime import datetime
import json
import os

BASE_DIR = Path(__file__).resolve().parent
PRIVATE_DIR = BASE_DIR / "data" / "private_uploads"
DATA_DIR = BASE_DIR / "data"
RESUME_DIR = PRIVATE_DIR / "resume"
ACADEMIC_DIR = PRIVATE_DIR / "academic"
for folder in (RESUME_DIR, ACADEMIC_DIR, DATA_DIR):
    folder.mkdir(parents=True, exist_ok=True)

app = Flask(__name__)
app.secret_key = os.environ.get("PORTFOLIO_SECRET_KEY", "local-demo-secret-change-before-deployment")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB per upload
ADMIN_PASSWORD = os.environ.get("PORTFOLIO_ADMIN_PASSWORD", "admin123")

PROFILE = {
    "name": "Adarsh Raj",
    "initials": "AR",
    "role": "MCA Student · Aspiring Software Developer",
    "tagline": "I turn ideas into useful, thoughtful digital experiences.",
    "location": "India",
    "email": "adarsh@example.com",  # Replace with your real email before publishing.
    "about": "I am an MCA student building a strong foundation in programming, web development, databases and problem-solving. I enjoy learning by building practical projects, documenting what I learn and improving each version through feedback.",
    "availability": "Open to internships and entry-level opportunities",
}

SKILLS = [
    {"name": "Python", "level": "Learning & building", "icon": "Py"},
    {"name": "Flask", "level": "Web applications", "icon": "Fl"},
    {"name": "HTML & CSS", "level": "Responsive UI", "icon": "</>"},
    {"name": "Java", "level": "Core programming", "icon": "Ja"},
    {"name": "SQL / DBMS", "level": "Data fundamentals", "icon": "DB"},
    {"name": "C / C++", "level": "Problem-solving", "icon": "C+"},
]

PROJECTS = [
    {"number": "01", "name": "Personal Portfolio Website", "type": "Web development", "description": "A responsive portfolio built with Flask, Jinja templates, HTML and CSS, with a private area for managing documents.", "tags": ["Python", "Flask", "HTML/CSS"]},
    {"number": "02", "name": "Yoga & Therapy Center Management System", "type": "MCA mini project", "description": "A small-scale system concept for presenting classes, therapy services, member registration and booking workflows.", "tags": ["Web app", "Database design", "UI"]},
    {"number": "03", "name": "Practice Question Generator", "type": "Generative AI concept", "description": "A learning-focused concept for generating practice questions and short assessments from course material using prompt-based AI.", "tags": ["AI", "Prompting", "Education"]},
]

EXPERIENCE = [
    {"period": "Present", "title": "MCA Student", "organization": "University Institute of Computing · Chandigarh University", "description": "Developing practical skills through coursework, programming exercises and small application projects."},
    {"period": "Project-based", "title": "Independent Project Builder", "organization": "Academic and personal practice", "description": "Practising how to plan, build, test and explain beginner-friendly software projects."},
]

BLOGS = [
    {"category": "Learning notes", "read": "4 min read", "title": "What I learned while building my first Flask website", "summary": "A beginner-friendly look at routes, templates, static files and how the pieces of a small web app connect.", "date": "Learning journal"},
    {"category": "Programming", "read": "5 min read", "title": "Why small projects make programming easier to understand", "summary": "How breaking a large idea into small functions and features makes debugging and explaining code less intimidating.", "date": "Learning journal"},
    {"category": "Career growth", "read": "3 min read", "title": "Building a portfolio while studying MCA", "summary": "A practical approach to documenting projects, writing clear summaries and showing progress honestly.", "date": "Learning journal"},
]

ALLOWED_RESUME = {"pdf", "doc", "docx"}
ALLOWED_ACADEMIC = {"pdf", "doc", "docx", "txt", "png", "jpg", "jpeg", "xlsx", "pptx"}


def read_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def write_json(path, value):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(value, file, indent=2, ensure_ascii=False)


def resume_metadata():
    return read_json(DATA_DIR / "resume.json", None)


def allowed_file(filename, allowed):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed


@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE, skills=SKILLS, projects=PROJECTS,
                           experience=EXPERIENCE, blogs=BLOGS, resume=resume_metadata())


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    if not name or not email or not message or "@" not in email:
        flash("Please complete every field with a valid email address.", "error")
    else:
        messages = read_json(DATA_DIR / "messages.json", [])
        messages.append({"name": name, "email": email, "message": message,
                         "created_at": datetime.now().isoformat(timespec="minutes")})
        write_json(DATA_DIR / "messages.json", messages)
        flash("Thanks! Your message was saved on this computer.", "success")
    return redirect(url_for("home", _anchor="contact"))


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST" and request.form.get("action") == "login":
        if request.form.get("password", "") == ADMIN_PASSWORD:
            session["portfolio_admin"] = True
            flash("You are signed in. Manage your documents below.", "success")
        else:
            flash("That password did not match. Please try again.", "error")
        return redirect(url_for("admin"))

    if not session.get("portfolio_admin"):
        return render_template("admin.html", logged_in=False, profile=PROFILE)
    return render_template("admin.html", logged_in=True, profile=PROFILE,
                           resume=resume_metadata(), documents=read_json(DATA_DIR / "academic_documents.json", []),
                           messages=read_json(DATA_DIR / "messages.json", []))


@app.route("/admin/logout", methods=["POST"])
def admin_logout():
    session.pop("portfolio_admin", None)
    flash("You have signed out of the document manager.", "success")
    return redirect(url_for("admin"))


@app.route("/admin/resume", methods=["POST"])
def upload_resume():
    if not session.get("portfolio_admin"):
        abort(403)
    file = request.files.get("resume")
    if not file or not file.filename:
        flash("Choose a resume file first.", "error")
    elif not allowed_file(file.filename, ALLOWED_RESUME):
        flash("Resume must be a PDF, DOC or DOCX file.", "error")
    else:
        original = secure_filename(file.filename)
        suffix = Path(original).suffix.lower()
        stored_name = "resume" + suffix
        for old in RESUME_DIR.glob("resume.*"):
            old.unlink(missing_ok=True)
        file.save(RESUME_DIR / stored_name)
        write_json(DATA_DIR / "resume.json", {"filename": original, "stored_name": stored_name,
                    "uploaded_at": datetime.now().strftime("%d %b %Y, %H:%M")})
        flash("Resume uploaded. The Resume section on your portfolio is now updated.", "success")
    return redirect(url_for("admin"))


@app.route("/resume/download")
def download_resume():
    info = resume_metadata()
    if not info:
        abort(404)
    return send_from_directory(RESUME_DIR, info["stored_name"], as_attachment=True, download_name=info["filename"])


@app.route("/admin/academic", methods=["POST"])
def upload_academic():
    if not session.get("portfolio_admin"):
        abort(403)
    file = request.files.get("document")
    title = request.form.get("title", "").strip()
    category = request.form.get("category", "Academic document").strip() or "Academic document"
    if not file or not file.filename or not title:
        flash("Add a document title and choose a file.", "error")
    elif not allowed_file(file.filename, ALLOWED_ACADEMIC):
        flash("Unsupported file type. Use PDF, DOC/DOCX, TXT, PNG/JPG, XLSX or PPTX.", "error")
    else:
        original = secure_filename(file.filename)
        stamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
        stored = f"{stamp}_{original}"
        file.save(ACADEMIC_DIR / stored)
        docs = read_json(DATA_DIR / "academic_documents.json", [])
        docs.insert(0, {"id": stamp, "title": title, "category": category, "filename": original,
                        "stored_name": stored, "uploaded_at": datetime.now().strftime("%d %b %Y, %H:%M")})
        write_json(DATA_DIR / "academic_documents.json", docs)
        flash("Academic document uploaded and saved privately on this computer.", "success")
    return redirect(url_for("admin"))


@app.route("/admin/academic/<doc_id>/download")
def download_academic(doc_id):
    if not session.get("portfolio_admin"):
        abort(403)
    docs = read_json(DATA_DIR / "academic_documents.json", [])
    document = next((item for item in docs if item["id"] == doc_id), None)
    if not document:
        abort(404)
    return send_from_directory(ACADEMIC_DIR, document["stored_name"], as_attachment=True, download_name=document["filename"])


@app.errorhandler(413)
def too_large(_error):
    flash("That file is too large. Please choose a file smaller than 10 MB.", "error")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    # Local development only. Use a production server before public deployment.
    app.run(debug=False)
