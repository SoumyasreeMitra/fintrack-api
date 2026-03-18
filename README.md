💰 FinTrack API — Personal Finance Management System

A production-grade, secure REST API for personal finance tracking — built with software engineering best practices including JWT authentication, containerization, automated CI/CD pipelines, and cloud deployment.

⚙️ Tech Stack
LayerTechnologyPurposeBackendPython, FlaskCore API developmentDatabaseSQLite + SQLAlchemy ORMRelational data modelingAuthenticationFlask-JWT-ExtendedSecure token-based authContainerizationDockerEnvironment consistencyCI/CDGitHub ActionsAutomated build & test pipelineCloud DeploymentRenderLive cloud hostingTestingPytestAutomated test executionVersion ControlGit + GitHubSource control & collaboration

🏗️ System Architecture
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

🔐 Security Implementation
This project follows secure coding practices aligned with industry standards:

JWT Authentication — All sensitive endpoints protected with JSON Web Tokens
Token Expiry — Tokens expire automatically to prevent unauthorized reuse
Input Validation — Request payloads validated before database operations
Environment Isolation — Sensitive configs excluded via .gitignore
Error Handling — Structured error responses prevent internal data leakage


📡 API Endpoints
MethodEndpointAuth RequiredDescriptionPOST/login❌Authenticate user and receive JWT tokenPOST/transactions✅Add a new income or expense transactionGET/transactions/<user>✅Retrieve all transactions for a userGET/summary/<user>✅Get financial summary — income, expense, balance

🚀 CI/CD Pipeline
Every git push automatically triggers the following pipeline via GitHub Actions:
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
This ensures every commit is automatically validated — a core Agile DevOps practice.

🐳 Run with Docker
bash# Build the image
docker build -t fintrack-api .

# Run the container
docker run -p 5000:5000 fintrack-api

💻 Run Locally
bash# 1. Clone the repository
git clone https://github.com/YOURUSERNAME/fintrack-api.git
cd fintrack-api

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python app.py

# Server runs at http://localhost:5000

🧪 Sample API Usage
Step 1 — Login to get token:
bashPOST /login
{
  "username": "soumya"
}
# Returns: { "token": "eyJ..." }
Step 2 — Add a transaction (with token):
bashPOST /transactions
Headers: Authorization: Bearer <token>
{
  "user": "soumya",
  "category": "Salary",
  "amount": 50000,
  "type": "income",
  "date": "2025-01-01"
}
Step 3 — Get financial summary:
bashGET /summary/soumya
Headers: Authorization: Bearer <token>

# Returns:
{
  "income": 50000,
  "expense": 12000,
  "balance": 38000
}

📁 Project Structure
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

🌱 Software Engineering Practices Demonstrated
PracticeImplementationSecure CodingJWT auth, input validation, error handlingAgile / CI/CDAutomated GitHub Actions pipeline on every pushApplication ResiliencyStructured error handlers (404, 500)ContainerizationDockerized for consistent environmentsCloud DeploymentLive deployment on Render cloud platformRelational DatabaseSQLAlchemy ORM with SQLiteRESTful ArchitectureStateless API with standard HTTP methodsVersion ControlFeature-driven commits with descriptive messages

🔮 Future Enhancements

 Migrate to PostgreSQL for production-grade relational storage
 Add Redis caching for high-frequency summary queries
 Implement role-based access control (RBAC)
 Deploy on AWS EC2 with RDS backend
 Add Swagger/OpenAPI documentation


👩‍💻 Author
Soumyasree Mitra

GitHub: @SoumyasreeMitra
LinkedIn: linkedin.com/in/soumyasreemitra