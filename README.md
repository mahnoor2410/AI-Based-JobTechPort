# JobTechPort 💼

**JobTechPort** is an AI-augmented Django-based job portal that streamlines the hiring process with intelligent resume ranking, user-friendly interfaces, and email-based notification systems. Designed for both applicants and administrators, it enables resume uploads, tracks application statuses, and provides smart AI analysis powered by NLP techniques. The platform ensures security through Django’s built-in authentication, while staff can easily manage job listings and user applications from a custom admin dashboard.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

The recruitment process is often inefficient, time-consuming, and biased. **JobTechPort** tackles these challenges with a modern AI-enhanced hiring portal that allows applicants to apply with resumes while enabling recruiters to assess candidate suitability using intelligent resume ranking.

With role-based access (admin vs. user), automated email alerts, and resume parsing, JobTechPort transforms manual filtering into a seamless, data-driven workflow. Its modular Django architecture ensures security, scalability, and maintainability.

---

## Features

- **User Authentication**: Secure registration, login/logout, and session management using Django’s auth system.
- **AI-Powered Resume Ranking**: Automatically scores resumes against job descriptions using NLP techniques (via `ai.py`).
- **Job Listings**: Browse open positions, view detailed job descriptions, and apply online.
- **Resume Upload**: Supports PDF uploads and parses them to extract text for ranking.
- **Admin Dashboard**: Staff-only view to manage applications, update statuses (Accepted/Rejected), and trigger AI reprocessing.
- **Application Status Tracking**: Users can view the status of their applications in a dedicated dashboard.
- **Email Notifications**: Sends confirmation and decision emails to applicants based on status updates.
- **Job Management**: Admins can create, edit, and delete job postings through intuitive interfaces.
- **Processing Status Control**: Admins can manually toggle AI processing states for applications.

---

## Tech Stack

- **Backend**: Python, Django, Django ORM, Django Admin
- **Frontend**: Django Templates (HTML/CSS), Bootstrap
- **AI/NLP**: PDF Resume Text Extraction, Custom Resume-Job Matching Algorithm
- **Database**: SQLite (development) / PostgreSQL (production)
- **Utilities**: `os`, `re`, `PyPDF2` or `pdfminer`, `smtplib`, `send_mail` (via Django)
- **Email Backend**: Django email system configured via SMTP

---

## System Architecture

- **Authentication**: Django's built-in auth system handles secure login, registration, and permission checks.
- **AI Ranking Pipeline**:
  1. User uploads resume (PDF).
  2. AI module (`ai.py`) extracts text from PDF.
  3. Resume is compared to job description using a similarity algorithm.
  4. Score is stored in the database for admin review.
- **Admin Panel**:
  - Admin/staff users access all applications, update statuses, and trigger email notifications.
  - Update AI processing flags if needed.
- **Job Management**:
  - CRUD operations for job postings by staff users.
- **User Dashboard**:
  - Applicants view their job applications and current statuses.

---

## Getting Started

### Prerequisites

- Python 3.8+
- Django 4.x
- Git
- Virtualenv (recommended)
- SMTP credentials for email (Gmail or custom SMTP)

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/JobTechPort.git
    cd JobTechPort
    ```

2. **Create and Activate Virtual Environment**

    ```bash
    python -m venv venv
    source venv/Scripts/activate  # Windows
    # source venv/bin/activate   # macOS/Linux
    ```

3. **Install Requirements**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py migrate
    ```

5. **Create Superuser (Admin)**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run Development Server**

    ```bash
    python manage.py runserver
    ```

---

## Usage

- Visit `http://127.0.0.1:8000/`
- Register as a user and explore job listings.
- Upload resume to apply for a job.
- Log in as an admin to manage jobs and applications.
- Admin can update statuses and send emails with one click.

---

## Screenshots

![Image](https://github.com/user-attachments/assets/04970cac-4373-4374-b5a8-8e46e68f2db1)

![Image](https://github.com/user-attachments/assets/e40b42b0-5241-4879-8221-b60b7bb0fd95)

![Image](https://github.com/user-attachments/assets/2cde3a14-1013-410e-8253-504ef7cbb4d9)

![Image](https://github.com/user-attachments/assets/b96eedfc-4b70-4222-9993-bec321ed5b64)

![Image](https://github.com/user-attachments/assets/65b25a9f-b10b-4c64-848b-4c240480cd88)

---

## Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them.
4. Push to your branch: `git push origin feature/new-feature`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Authors

- Mahnoor Shahid  

---
