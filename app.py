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
    home_content = """
    <div class="card">
        <h1 style="color:#ffcc00;">Multi-Cloud DevOps Training</h1>
        <h2 style="color:#f87171;">By Veera Sir – Naresh IT</h2>

        <p>
            Welcome to the <b>industry-oriented Multi-Cloud DevOps Training</b> designed by
            <b>Veera Sir</b> at <b>Naresh IT</b>.
        </p>

        <p>
            Hands-on implementation, real production scenarios,
            and end-to-end CI/CD pipelines.
        </p>
    </div>

    <div class="card" style="background:#1a1a2e; color:#ffcc66; padding:20px; line-height:1.8; border-radius:12px; box-shadow: 0 4px 12px rgba(0,0,0,0.5);">
    <h2 style="color:#ffaa00; font-size:28px; margin-bottom:15px;">Real-Time DevOps Projects By veera Sir NareshIt</h2>
    <ul style="list-style-type: square; padding-left: 20px; font-size:16px;">
        <li>Multi-Tier Full-Stack Node.js Application Deployed on AWS Using 20+ Services with High Availability, Scalability, Networking, Security, and Monitoring</li>
        <li>Cloud Deployment of a Scalable, Resilient Full-Stack Python Application on AWS EC2 with Disaster Recovery Strategy</li>
        <li>Cloud-Native Deployment of a Full-Stack Java Spring Boot Application on Azure with High Availability and Disaster Recovery Strategy</li>
        <li>Cloud-Native Deployment of a Full-Stack Node.js Application on GCP with High Availability, Scalability, Networking, Security</li>
        <li>Automated Database Migration from EC2-Hosted MySQL to Amazon RDS Using AWS Database Migration Service (DMS) with Minimal Downtime and High Availability</li>
        <li>End-to-End Application Migration from On-Premises Infrastructure to AWS Cloud with High Availability, Scalability, and Security Best Practices</li>
        <li>Optimized Static Web Hosting Architecture on AWS S3 with CDN and Custom Domain</li>
        <li>Implementing Automated Backup Strategies in AWS Cloud Using Serverless Lambda Functions</li>
        <li>End-to-End CDN Optimization: Configuring CloudFront for Low Latency and Automating Cache Invalidation Using Lambda</li>
        <li>Cloud-Native Full-Stack Application Deployment on AWS ECS Fargate with CI/CD, Auto Scaling, and Secure Networking</li>
        <li>Unified Infrastructure Monitoring with Prometheus and Grafana: Centralized Dashboard for Multi-Server Observability</li>
        <li>Centralized Logging with Amazon CloudWatch and Cost-Optimized Log Archival to S3 Using AWS Lambda serverless</li>
        <li>End-to-End Automation of Multi-Tier AWS, Azure and GCP Cloud Infrastructure Using Terraform with Complete Networking, Security, and Deployment Layers</li>
        <li>End-to-End Automation of Java Maven Application Deployment on Apache Tomcat Using CI/CD Practices</li>
        <li>End-to-End Cloud-Native CI/CD Pipeline for Node.js Microservices with Jenkins and Kubernetes</li>
        <li>End-to-End DevOps Automation for Node.js Microservices with GitLab CI/CD and Kubernetes (EKS)</li>
        <li>End-to-End CI/CD Pipeline for Java Applications Using Azure DevOps, Docker, and Kubernetes AKS</li>
        <li>End-to-End CI/CD Pipeline (GitLab CI/CD) for Java Applications Using Azure DevOps, Docker, and Kubernetes GKE</li>
        <li>Full-Stack Microservices Application (Python, Java, Node.js) Deployment on AWS Using CI/CD, GitOps, Helm, and Centralized Monitoring with Prometheus, Grafana, and the EFK Stack</li>
        <li>End-to-End Production-Grade EKS Cluster Deployment on AWS, Azure, and GCP Using Terraform with High Availability, Scalability, and Secure Networking</li>
        <li>Fully Managed Serverless Full-Stack Deployment Using AWS Services (Lambda, API Gateway, DynamoDB)</li>
        <li>End-to-End Patch Management and Monitoring Configuration Using Ansible</li>
        <li>Containerized Full-Stack Application Deployment Using Docker & Docker Compose</li>
        <li>Centralized Application Log Monitoring and Visualization on Amazon EKS Using the ELK Stack (Elasticsearch, Logstash, Kibana) for Enhanced Observability</li>
        <li>Scalable Multi-Application Deployment on EC2 Using ALB Path-Based Routing</li>
        <li>Enterprise Identity and Access Management Using AWS SSO</li>
        <li>End-to-End CI/CD for Microservices on Amazon EKS Using Argo CD and GitHub Actions</li>
        <li>End-to-End Kubernetes Application Deployment Using Ingress Controllers for High Availability, Load Balancing, and Traffic Management</li>
    </ul>
</div>


    <div class="card">
        <h2 style="color:#00e5ff;">Why Multi-Cloud DevOps?</h2>
        <ul>
            <li>Multiple cloud providers</li>
            <li>High availability & vendor independence</li>
            <li>Better cost optimization</li>
            <li>Enterprise disaster recovery</li>
            <li>Higher salaries</li>
        </ul>
    </div>

    <div class="card">
        <h2 style="color:#00ff99;">What You Will Learn</h2>
        <ul>
            <li>AWS, Azure & GCP</li>
            <li>Linux & Shell scripting</li>
            <li>CI/CD pipelines</li>
            <li>Docker & Kubernetes</li>
            <li>Terraform & Ansible</li>
            <li>GitOps & Automation</li>
        </ul>
    </div>


    <div class="card">
        <h2 style="color:#ff6699;">Why Naresh IT & Veera Sir?</h2>
        <ul>
            <li>12+ years excellence</li>
            <li>Real-time trainer</li>
            <li>Interview focused</li>
            <li>Mock interviews</li>
        </ul>
    </div>
    """

    # Pass the home_content to get_layout
    return get_layout("Home", home_content)


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
