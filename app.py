from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to Jenkins Tutorials</h1>"

# ❌ DO NOT use app.run() in Azure
