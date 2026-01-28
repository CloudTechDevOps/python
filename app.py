from flask import Flask
import os

app = Flask(__name__)

# Enhanced CSS with vibrant block colors
STYLE = """
<style>
    body {
        margin: 0;
        font-family: 'Consolas', 'Segoe UI', monospace;
        background: #0f172a;
        color: #ffffff;
        line-height: 1.6;
    }
    .navbar {
        background: #1e293b;
        padding: 15px;
        text-align: center;
        position: sticky;
        top: 0;
        z-index: 1000;
        border-bottom: 2px solid #334155;
    }
    .navbar a {
        color: #00e5ff;
        margin: 0 20px;
        text-decoration: none;
        font-size: 18px;
        font-weight: bold;
    }
    .navbar a:hover { color: #ffcc00; }
    
    .container { padding: 30px; max-width: 1100px; margin: auto; }
    
    .card {
        background: rgba(30, 41, 59, 0.7);
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.4);
        margin-bottom: 20px;
    }

    /* Color Coded Sections */
    .block-header { border-left: 8px solid #ffcc00; background: #2d3748; padding: 15px; margin-top: 20px; }
    .block-cloud { border-left: 8px solid #00e5ff; background: #1a365d; padding: 15px; margin-bottom: 10px; }
    .block-devops { border-left: 8px solid #a78bfa; background: #2e1065; padding: 15px; margin-bottom: 10px; }
    .block-automation { border-left: 8px solid #4ade80; background: #064e3b; padding: 15px; margin-bottom: 10px; }
    .block-security { border-left: 8px solid #f87171; background: #450a0a; padding: 15px; margin-bottom: 10px; }

    pre {
        white-space: pre-wrap;
        word-wrap: break-word;
        font-size: 15px;
        color: #e2e8f0;
        margin: 0;
    }
    h1, h2 { margin-top: 0; }
    .footer {
        margin-top: 30px;
        background: #0b0f19;
        text-align: center;
        padding: 20px;
        font-size: 14px;
        color: #94a3b8;
    }
</style>
"""

def get_layout(title, content):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        {STYLE}
    </head>
    <body>

        <div class="navbar">
            <a href="/">Home</a>
            <a href="/syllabus">syllabus</a>
        </div>

        <div class="container">

            <div class="card">
                <h1 style="color:#ffcc00;">Multi-Cloud DevOps Training</h1>
                <h2>By Veera Sir – Naresh IT</h2>

                <p>
                    Welcome to the <b>industry-oriented Multi-Cloud DevOps program</b> designed by
                    <b>Veera Sir</b> at <b>Naresh IT</b>.  
                    This course is structured to help learners become
                    <b>job-ready DevOps Engineers</b> with real-time exposure to
                    <b>AWS, Azure, and GCP</b>.
                </p>

                <p>
                    The training focuses on <b>hands-on implementation</b>,
                    <b>real production scenarios</b>, and
                    <b>end-to-end CI/CD pipelines</b>
                    used by modern enterprises.
                </p>
            </div>

            <div class="card">
                <h2 style="color:#00e5ff;">Why Multi-Cloud DevOps?</h2>
                <ul>
                    <li>Most enterprises use <b>multiple cloud providers</b></li>
                    <li>High availability & vendor independence</li>
                    <li>Better cost optimization strategies</li>
                    <li>Enterprise-grade disaster recovery</li>
                    <li>Cloud-agnostic DevOps skills = <b>higher salaries</b></li>
                </ul>
            </div>

            <div class="card">
                <h2 style="color:#00ff99;">What You Will Learn</h2>
                <ul>
                    <li>AWS, Azure & GCP core cloud services</li>
                    <li>Linux & Shell scripting from scratch</li>
                    <li>CI/CD with Jenkins, Azure DevOps & GitLab</li>
                    <li>Docker & Kubernetes (EKS, AKS)</li>
                    <li>Infrastructure as Code using Terraform & Ansible</li>
                    <li>Monitoring with Grafana & Prometheus</li>
                    <li>GitOps with Argo CD</li>
                    <li>Automation using Python & Boto3</li>
                </ul>
            </div>

            <div class="card">
                <h2 style="color:#ffaa00;">Real-Time DevOps Project</h2>
                <p>
                    Learners will work on a <b>real-time enterprise DevOps project</b>
                    covering:
                </p>
                <ul>
                    <li>Multi-cloud infrastructure setup</li>
                    <li>CI/CD pipeline design</li>
                    <li>Dockerized applications</li>
                    <li>Kubernetes deployment</li>
                    <li>Monitoring & alerting</li>
                    <li>Production-grade security practices</li>
                </ul>
            </div>

            <div class="card">
                <h2 style="color:#ff6699;">Why Naresh IT & Veera Sir?</h2>
                <ul>
                    <li>20+ years of training excellence</li>
                    <li>Trainer with <b>real production experience</b></li>
                    <li>Interview-focused training</li>
                    <li>Resume & mock interview support</li>
                    <li>Trusted by thousands of DevOps professionals</li>
                </ul>
            </div>

            <!-- Dynamic page content -->
            {content}

        </div>

        <div class="footer">
            © 2026 Veera Sir – Naresh IT <br>
            Multi-Cloud DevOps | AWS | Azure | GCP | Kubernetes | Terraform
        </div>

    </body>
    </html>
    """

@app.route("/")
def home():
    content = """
    <div class="card">
        <h1 style="color:#ffcc00;">Multi-Cloud DevOps Training</h1>
        <h2>By Veera Sir – Naresh IT</h2>
        <p>Welcome to the industry-oriented Multi-Cloud DevOps program...</p>
    </div>

    <div class="card">
        <h2 style="color:#00e5ff;">Why Multi-Cloud DevOps?</h2>
        <ul>
            <li>Multiple cloud providers</li>
            <li>High availability</li>
            <li>Vendor independence</li>
        </ul>
    </div>
    """
    return get_layout("Home", content)

@app.route("/syllabus")
def syllabus():
    content = f"""
    <h1 style="color:#ffcc00; text-align:center;">Complete Course Syllabus</h1>
    
    <div class="block-header">
        <h2 style="color:#ffcc00;">Modules Overview (1-35)</h2>
        <pre>
● Module 01:  Aws,Azure And Gcp Cloud Overview  
● Module 02:  Linux Introduction  
● Module 03:  AWS Elastic Compute Cloud (ec2)  
● Module 04:  Azure Virtual Machine (VM) 
● Module 05:  GCP Compute Engine 
● Module 06:  AWS Virtual Private Cloud (VPC)  
● Module 07:  Azure Virtual Network (VNET)  
● Module 08:  GCP Cloud Virtual Network 
● Module 09:  AWS S3 Storage Service 
● Module 10:  Azure Blob Storage  
● Module 11:  GCP Cloud Storage  
● Module 12:  Identity and Access Management 
● Module 13: Amazon Relational Database and DynamoDB  
● Module 14: Security Services 
● Module 15: Serverless service lambda 
● Module 16: Amazon Route 53 
● Module 17: Overview Of Devops 
● Module 18: Shell scripting  
● Module 19: Web App Servers Configurations 
● Module 20: Version Control with Git 
● Module 21: Build tool Maven 
● Module 22: SonarQube Overview 
● Module 23: Continuous Integration – Jenkins 
● Module 24: Azure CICD 
● Module 25: Git Lab CICD 
● Module 26: Docker 
● Module 27: Orchestration using Kubernetes 
● Module 28: Azure Kubernetes Service (AKS) 
● Module 29: Overview of Argo CD   
● Module 30: Continuous Monitoring with Grafana 
● Module 31: Ansible 
● Module 32: Terraform 
● Module 33: Python Boto3 
● Module 34: Project to cover all Tools 
● Module 35: Resume Preparation
        </pre>
    </div>

    <div class="block-cloud">
        <h2 style="color:#00e5ff;">Section 1: Cloud Foundational Concepts</h2>
        <pre>
1. Introduction to Cloud Computing 
• What is Cloud Computing? 
• Evolution and importance of cloud technology 
• Key players in the market: AWS, Azure, GCP 

2. Why Cloud Computing? 
• Traditional infrastructure vs. cloud infrastructure 
• Benefits of moving to the cloud for businesses 
• Use cases across industries: startups, enterprises, etc. 

3. Benefits of Cloud Computing 
• Cost Efficiency, Scalability, Elasticity, Flexibility
• Disaster Recovery and Business Continuity 
• Global Accessibility and High Availability 
• Automated Infrastructure Management (AI/ML) 

4. Types of Cloud Computing 
• Public Cloud (AWS, Azure, GCP) 
• Private Cloud & Hybrid Cloud
• Community Cloud

5. Cloud Service Models 
• SaaS: Software as a Service (Gmail, Salesforce) 
• PaaS: Platform as a Service (Beanstalk, App Service) 
• IaaS: Infrastructure as a Service (EC2, VM, GCE) 

6. Scaling & Issues
• Horizontal vs Vertical Scaling 
• Vendor Lock-In, Downtime, Data Privacy
• Cloud Costing Models: Pay-as-you-go vs Reserved
        </pre>
    </div>

    <div class="block-automation">
        <h2 style="color:#4ade80;">Section 2: Virtualization & Linux</h2>
        <pre>
2. Virtualization 
• Virtualization and cloud computing    
• Types of virtualization & Hypervisor Concepts 
• Vendors & Benefits

3. Linux           
• Important Linux commands & filesystem
• File permissions & Process management 
• User account & Software management  
• Networking in Linux 
        </pre>
    </div>

    <div class="block-cloud">
        <h2 style="color:#00e5ff;">Section 3: Multi-Cloud Compute & Networking</h2>
        <pre>
AWS EC2, Azure VM, GCP Compute Engine 
• Instance launch (Windows & Linux) 
• Key pair management & Security groups / NSG / Firewall 
• Storage, snapshots, User data, and metadata 
• Load balancers & Auto scaling (Fixed/Dynamic)
• AWS CLI and IAM roles 

Networking (AWS VPC, Azure VNET, GCP Network) 
• IP addressing & CIDR 
• Subnets & Route tables 
• Internet Gateway & Network ACLs 

Storage Services 
• S3, Blob Storage, Cloud Storage 
• Versioning & Lifecycle management 
• Static website hosting & Cross-region replication 
        </pre>
    </div>

    <div class="block-security">
        <h2 style="color:#f87171;">Section 4: Security, Databases & Serverless</h2>
        <pre>
IAM & Security
• Root vs IAM, MFA, Password policies 
• Roles, Groups, and Custom policies 
• Secrets Manager, KMS, ACM, WAF, Shield, CloudTrail 

Databases 
• RDS (MySQL, MSSQL, Aurora) 
• Multi-AZ & Read Replicas 
• DynamoDB & Migration service 

AWS Lambda 
• Boto3 automation & Environment configuration 
• Layers & Limitations 

Route 53 
• DNS Records & Routing policies (Failover, Latency, Geo)
        </pre>
    </div>

    <div class="block-devops">
        <h2 style="color:#a78bfa;">Section 5: DevOps Tools & CI/CD</h2>
        <pre>
DevOps Overview 
• DevOps pipeline & ecosystem 

Shell Scripting 
• Variables, Operators, Conditions, Loops, Functions 

Web Servers 
• Apache & Tomcat configuration and deployment 

CI/CD Tools
• Git: Branching, Merging, Rebase, Remote Repos
• Maven: POM, Lifecycle, Dependencies
• SonarQube: Code scan & Maven integration
• Jenkins: Master-slave, Plugins, Jobs
• Azure CICD & Git Lab CICD
        </pre>
    </div>

    <div class="block-devops">
        <h2 style="color:#a78bfa;">Section 6: Containers & Orchestration</h2>
        <pre>
Docker 
• Images, Containers, Dockerfile 
• Docker Compose & Docker Swarm 

Kubernetes 
• Architecture, Deployments, Services 
• Helm Charts & RBAC 
• AKS / EKS integration 
• EFK Stack (Logs)
• Argo CD (GitOps & Continuous Delivery) 
• Grafana & Prometheus (Monitoring)
        </pre>
    </div>

    <div class="block-automation">
        <h2 style="color:#4ade80;">Section 7: Infrastructure as Code & Final</h2>
        <pre>
Ansible 
• Inventory, Playbooks, Roles, Modules 

Terraform 
• Providers, Resources, State, Modules 
• AWS labs & Best practices 

Python Boto3 
• AWS automation with Python 

Final Project 
• End-to-end DevOps project 
• Resume preparation & Mock interviews 
        </pre>
    </div>
    """
    return get_layout("Complete Course Syllabus", content)

if __name__ == "__main__":
    app.run(debug=True)
