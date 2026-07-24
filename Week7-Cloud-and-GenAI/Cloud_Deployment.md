# Week 7 - Cloud Deployment

## Overview

Cloud Deployment is the process of hosting applications and services on cloud platforms instead of traditional on-premises infrastructure. It enables organizations to build, deploy, scale, and manage applications efficiently using cloud resources.

---

# 1. Cloud Computing Fundamentals

## What is Cloud Computing?

Cloud Computing is the delivery of computing services such as servers, storage, databases, networking, software, analytics, and artificial intelligence over the Internet.

### Benefits

- Cost Efficiency
- Scalability
- High Availability
- Reliability
- Global Accessibility
- Automatic Updates
- Disaster Recovery

### Service Models

### Infrastructure as a Service (IaaS)

Provides virtualized computing resources over the internet.

Examples:
- Amazon EC2
- Azure Virtual Machines
- Google Compute Engine

### Platform as a Service (PaaS)

Provides a complete development and deployment environment.

Examples:
- Azure App Service
- Google App Engine
- AWS Elastic Beanstalk

### Software as a Service (SaaS)

Provides software applications over the internet.

Examples:
- Microsoft 365
- Gmail
- Salesforce

---

# 2. Amazon Web Services (AWS)

AWS is Amazon's cloud computing platform offering more than 200 cloud services.

### Popular AWS Services

- EC2
- S3
- Lambda
- RDS
- IAM
- CloudWatch

### Advantages

- Highly Scalable
- Secure
- Pay-as-you-go Pricing
- Global Infrastructure

---

# 3. Microsoft Azure

Microsoft Azure is a cloud platform that supports building, deploying, and managing applications.

### Azure Services

- Azure Virtual Machines
- Azure Storage
- Azure SQL Database
- Azure Functions
- Azure App Service
- Azure DevOps

### Benefits

- Excellent Microsoft Integration
- Enterprise Ready
- Hybrid Cloud Support
- Strong Security

---

# 4. Google Cloud Platform (GCP)

Google Cloud Platform provides cloud computing services using Google's infrastructure.

### GCP Services

- Compute Engine
- Cloud Storage
- Cloud Run
- Kubernetes Engine
- BigQuery
- Cloud Functions

### Advantages

- High Performance
- AI and Machine Learning Support
- Global Network
- Flexible Pricing

---

# 5. Docker

## What is Docker?

Docker is a containerization platform used to package applications along with their dependencies.

### Features

- Lightweight
- Portable
- Fast Deployment
- Environment Consistency
- Easy Scaling

### Docker Components

- Docker Engine
- Docker Image
- Docker Container
- Docker Hub
- Dockerfile

### Basic Docker Commands

```bash
docker --version
docker images
docker ps
docker pull nginx
docker run nginx
docker stop <container_id>
docker rm <container_id>
```

---

# 6. Kubernetes

## What is Kubernetes?

Kubernetes is an open-source container orchestration platform used to deploy, scale, and manage containerized applications.

### Key Components

- Cluster
- Node
- Pod
- Deployment
- Service
- Namespace

### Features

- Auto Scaling
- Load Balancing
- Self Healing
- Rolling Updates
- Service Discovery

---

# 7. Continuous Integration and Continuous Deployment (CI/CD)

## Continuous Integration (CI)

Developers frequently merge code into a shared repository where automated builds and tests are executed.

### Benefits

- Early Bug Detection
- Faster Development
- Better Code Quality

---

## Continuous Deployment (CD)

Automatically deploys verified code changes to production environments.

### Benefits

- Faster Releases
- Reduced Manual Errors
- Continuous Delivery

---

# 8. GitHub Actions

GitHub Actions is GitHub's automation platform used for building, testing, and deploying applications.

### Features

- Workflow Automation
- Event Triggers
- Matrix Builds
- Marketplace Actions
- CI/CD Integration

### Workflow File Location

```
.github/workflows/
```

Example:

```yaml
name: Build Project

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Display Message
        run: echo "Hello World"
```

---

# 9. Azure Pipelines

Azure Pipelines is Microsoft's cloud-based CI/CD service available through Azure DevOps.

### Features

- Build Automation
- Continuous Integration
- Continuous Deployment
- Cross Platform Support
- YAML Pipelines

### Pipeline Stages

- Source
- Build
- Test
- Release
- Deploy

Example YAML

```yaml
trigger:
- main

pool:
  vmImage: ubuntu-latest

steps:
- script: echo "Building Project"
```

---

# 10. Cloud Security

Cloud security protects cloud-based systems, applications, and data.

### Security Best Practices

- Multi-Factor Authentication
- Identity and Access Management
- Data Encryption
- Backup and Recovery
- Secure APIs
- Network Security

---

# Learning Outcomes

After completing this module, you will be able to:

- Understand Cloud Computing concepts.
- Explain IaaS, PaaS, and SaaS.
- Identify AWS, Azure, and GCP services.
- Understand Docker and containerization.
- Explain Kubernetes architecture.
- Understand CI/CD pipelines.
- Create basic GitHub Actions workflows.
- Understand Azure Pipelines.
- Apply cloud security best practices.

---

# Summary

Cloud Deployment enables organizations to build scalable, secure, and highly available applications. Modern cloud platforms combined with Docker, Kubernetes, GitHub Actions, and Azure Pipelines simplify software deployment while improving reliability and development speed.