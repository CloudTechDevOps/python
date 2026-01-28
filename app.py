# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "<h1>Welcome to Jenkins Tutorials</h1>"

# # ❌ DO NOT use app.run() in Azure


import os
from flask import Flask

app = Flask(__name__)

# ---------- Common HTML Style ----------
STYLE = """
<style>
body {
    margin: 0;
    font-family: Arial, Helvetica, sans-serif;
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.navbar {
    background-color: #111;
    padding: 15px;
    text-align: center;
}
.navbar a {
    color: #00e5ff;
    margin: 0 15px;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
}
.navbar a:hover {
    color: #ffcc00;
}
.container {
    padding: 40px;
}
.card {
    background-color: rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
}
h1, h2 {
    color: #ffcc00;
}
ul {
    line-height: 1.8;
}
.footer {
    text-align: center;
    padding: 15px;
    background-color: #111;
    font-size: 14px;
    color: #ccc;
}
</style>
"""

# ---------- Home Page ----------
@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>Multicloud DevOps</title>
        {STYLE}
    </head>
    <body>

    <div class="navbar">
        <a href="/">Home</a>
        <a href="/syllabus">Syllabus</a>
    </div>

    <div class="container">
        <div class="card">
            <h1>Multicloud DevOps with Veera Sir</h1>
            <h2>Naresh IT</h2>
            <p>
                Become an <b>Industry-Ready DevOps Engineer</b> with hands-on
                experience across <b>AWS, Azure, and GCP</b>.
            </p>
        </div>

        <div class="card">
            <h2>Why This Course?</h2>
            <ul>
                <li>Real-time DevOps projects</li>
                <li>CI/CD with Jenkins & GitHub Actions</li>
                <li>Docker & Kubernetes (EKS, AKS, GKE)</li>
                <li>Terraform for Multicloud</li>
                <li>Monitoring, Security & Best Practices</li>
            </ul>
        </div>

        <div class="card">
            <h2>Cloud Detected</h2>
            <p>
                Running on: <b>{os.getenv("CLOUD_PROVIDER", "Multicloud Environment")}</b>
            </p>
        </div>
    </div>

    <div class="footer">
        © 2026 Naresh IT | Multicloud DevOps Program
    </div>

    </body>
    </html>
    """

# ---------- Syllabus Page ----------
@app.route("/syllabus")
def syllabus():
    return f"""
    <html>
    <head>
        <title>DevOps Syllabus</title>
        {STYLE}
    </head>
    <body>

    <div class="navbar">
        <a href="/">Home</a>
        <a href="/syllabus">Syllabus</a>
    </div>

    <div class="container">

        <div class="card">
            <h1>Multicloud DevOps Syllabus</h1>
        </div>

        <div class="card">
            <h2>Core DevOps</h2>
            <ul>
                <li>Linux & Shell Scripting</li>
                <li>Git & GitHub</li>
                <li>Jenkins CI/CD Pipelines</li>
                <li>Docker & Containerization</li>
            </ul>
        </div>

        <div class="card">
            <h2>Kubernetes & Cloud</h2>
            <ul>
                <li>Kubernetes Architecture</li>
                <li>AWS (EC2, VPC, EKS, IAM)</li>
                <li>Azure (VMs, App Service, AKS)</li>
                <li>GCP (Compute Engine, GKE)</li>
            </ul>
        </div>

        <div class="card">
            <h2>Advanced DevOps</h2>
            <ul>
                <li>Terraform (IaC)</li>
                <li>Monitoring – Prometheus & Grafana</li>
                <li>DevSecOps – Trivy, SonarQube</li>
                <li>Real-Time Multicloud Projects</li>
            </ul>
        </div>

    </div>

    <div class="footer">
        Designed for DevOps Engineers | Veera Sir – Naresh IT
    </div>

    </body>
    </html>
    """

# ❌ No app.run() — gunicorn will handle it
