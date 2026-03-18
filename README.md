# 💰 FinTrack API — Personal Finance Management System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions)
![JWT](https://img.shields.io/badge/Auth-JWT_Secured-orange?style=for-the-badge)
![Cloud](https://img.shields.io/badge/Cloud-Render_Deployed-46E3B7?style=for-the-badge)

> A production-grade, secure REST API for personal finance tracking — built with software engineering best practices including JWT authentication, containerization, automated CI/CD pipelines, and cloud deployment.

---

## 🎯 Project Overview

FinTrack is a **secure, scalable, and resilient** backend system that allows users to manage their personal finances — tracking income, expenses, and generating financial summaries. This project was built following industry-standard software development practices including secure coding, application resiliency, agile development workflows, and automated deployment pipelines.

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python, Flask | Core API development |
| **Database** | SQLite + SQLAlchemy ORM | Relational data modeling |
| **Authentication** | Flask-JWT-Extended | Secure token-based auth |
| **Containerization** | Docker | Environment consistency |
| **CI/CD** | GitHub Actions | Automated build & test pipeline |
| **Cloud Deployment** | Render | Live cloud hosting |
| **Testing** | Pytest | Automated test execution |
| **Version Control** | Git + GitHub | Source control & collaboration |

---

## 🏗️ System Architecture

```
Client Request
      │
      ▼
┌─────────────────┐
│   JWT Auth Layer │  ◄── Secure token validation on every request
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Flask Routes   │  ◄── RESTful API endpoints
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  SQLAlchemy ORM  │  ◄── Abstracted relational database access
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   SQLite DB      │  ◄── Persistent relational data storage
└─────────────────┘
```

---

## 🔐 Security Implementation

This project follows **secure coding practices** aligned with industry standards:

- **JWT Authentication** — All sensitive endpoints protected with JSON Web Tokens
- **Token Expiry** — Tokens expire automatically to prevent unauthorized reuse
- **Input Validation** — Request payloads validated before database operations
- **Environment Isolation** — Sensitive configs excluded via `.gitignore`
- **Error Handling** — Structured error responses prevent internal data leakage

---

## 📡 API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|:---:|-------------|
| `POST` | `/login` | ❌ | Authenticate user and receive JWT token |
| `POST` | `/transactions` | ✅ | Add a new income or expense transaction |
| `GET` | `/transactions/<user>` | ✅ | Retrieve all transactions for a user |
| `GET` | `/summary/<user>` | ✅ | Get financial summary — income, expense, balance |

---

## 🚀 CI/CD Pipeline

Every `git push` automatically triggers the following pipeline via **GitHub Actions**:

```
Push to GitHub
      │
      ▼
┌──────────────────────┐
│  1. Checkout Code     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  2. Setup Python 3.10 │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  3. Install Deps      │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  4. Run Pytest        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  5. Build Docker Image│
└──────────────────────┘
```

This ensures **every commit is automatically validated** — a core Agile DevOps practice.

---

## 🐳 Run with Docker

```bash
# Build the image
docker build -t fintrack-api .

# Run the container
docker run -p 5000:5000 fintrack-api
```

---

## 💻 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/SoumyasreeMitra/fintrack-api.git
cd fintrack-api

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python app.py

# Server runs at http://localhost:5000
```

---

## 🧪 Sample API Usage

**Step 1 — Login to get token:**
```bash
POST /login
{
  "username": "soumya"
}
# Returns: { "token": "eyJ..." }
```

**Step 2 — Add a transaction (with token):**
```bash
POST /transactions
Headers: Authorization: Bearer <token>
{
  "user": "soumya",
  "category": "Salary",
  "amount": 50000,
  "type": "income",
  "date": "2025-01-01"
}
```

**Step 3 — Get financial summary:**
```bash
GET /summary/soumya
Headers: Authorization: Bearer <token>

# Returns:
{
  "income": 50000,
  "expense": 12000,
  "balance": 38000
}
```

---

## 📁 Project Structure

```
fintrack-api/
├── app.py                  # Application entry point, config
├── models.py               # SQLAlchemy database models
├── routes.py               # API route definitions
├── requirements.txt        # Project dependencies
├── Dockerfile              # Container configuration
├── test_app.py             # Automated test suite
├── .gitignore              # Excludes sensitive/unnecessary files
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI/CD pipeline
```

---

## 🌱 Software Engineering Practices Demonstrated

| Practice | Implementation |
|---|---|
| **Secure Coding** | JWT auth, input validation, error handling |
| **Agile / CI/CD** | Automated GitHub Actions pipeline on every push |
| **Application Resiliency** | Structured error handlers (404, 500) |
| **Containerization** | Dockerized for consistent environments |
| **Cloud Deployment** | Live deployment on Render cloud platform |
| **Relational Database** | SQLAlchemy ORM with SQLite |
| **RESTful Architecture** | Stateless API with standard HTTP methods |
| **Version Control** | Feature-driven commits with descriptive messages |

---

## 🔮 Future Enhancements

- [ ] Migrate to PostgreSQL for production-grade relational storage
- [ ] Add Redis caching for high-frequency summary queries
- [ ] Implement role-based access control (RBAC)
- [ ] Deploy on AWS EC2 with RDS backend
- [ ] Add Swagger/OpenAPI documentation

---

## 👩‍💻 Author

**Soumyasree Mitra**
- GitHub: [@SoumyasreeMitra](https://github.com/SoumyasreeMitra)
- LinkedIn: [linkedin.com/in/soumyasree-mitra](#)

---

> *Built with a focus on security, scalability, and clean software engineering — reflecting real-world development standards.*
