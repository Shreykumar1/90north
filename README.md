# 90North Technical Assessment

## Overview
This repository contains a full-stack web application featuring a real-time chat system, responsive frontend design, and AWS serverless components. The project demonstrates proficiency in Django, WebSocket implementation, frontend development, and AWS services.

## Project Components

### 1. Frontend
- Responsive layout with fixed navigation
- Three-panel design (collapsible left menu, main content, right panel)
- Adaptive scaling based on viewport width:
  - 992px-1600px: 90% scale
  - 700px-767px: 80% scale
  - 600px-700px: 75% scale
  - ≤600px: 50% scale

### 2. Django Chat Application
A real-time chat system with the following features:
- User authentication (signup/login)
- Real-time messaging using WebSocket
- Persistent message history
- User list with chat initiation
- Responsive chat interface

### 3. AWS Components
- Lambda function for number addition
- Lambda function for S3 file storage (documents/PDFs)

## Getting Started

### Prerequisites
- Python 3.8+
- pip package manager
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/90north.git
cd 90north
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Reset the database:
```bash
python manage.py migrate --noinput
python manage.py flush
```

2. Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## Live Demo
- Frontend & Django Application: [PythonAnywhere Link]
- API Documentation: [API Docs Link]

## Project Structure
```
90north/
├── frontend/      # Frontend assets and components
├── chat/          # Django chat application
├── aws/          # AWS Lambda functions
```
