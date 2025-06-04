💸 SmartBudget – Personal Finance Tracker
SmartBudget is a full-stack web application built using Vue 3 (frontend) and Django REST Framework (backend) that helps users track expenses, predict future spending, and analyze budgeting patterns with the help of Machine Learning. This system is designed to make financial planning smart, personalized, and easy to use.

🧠 Features
🔐 Secure User Authentication (JWT-based)

💰 Expense Tracking: Categorize expenses like rent, groceries, transport, etc.

📊 Analytics Dashboard: Visual insights on monthly spending

🤖 ML-Based Predictions: Forecast upcoming monthly expenses

📤 Real-Time API Integration

🌐 CORS-enabled for frontend-backend communication

🛡️ User registration with email, mobile number, and gender

🗂️ Tech Stack
Layer	Technology
Frontend	Vue 3 + Vite
Backend	Django + DRF
Auth	JWT (SimpleJWT)
ML Model	Python (scikit-learn/pandas)
Database	SQLite / PostgreSQL
Deployment	Docker / Localhost

🚀 Getting Started
📦 Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/smartbudget.git
cd smartbudget
🖥 Backend Setup (Django)
bash
Copy
Edit
cd smartbudget-backend
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🌐 Frontend Setup (Vue 3 + Vite)
bash
Copy
Edit
cd smartbudget-frontend
npm install
npm run dev
Ensure the backend runs on http://localhost:8000 and frontend on http://localhost:5173.

🔑 Authentication Flow
Register via /api/register/

Obtain tokens from /api/token/

Use access token in frontend via Authorization: Bearer <token>

⚙️ Commands You Might Use
Purpose	Command
Start Django backend	python manage.py runserver
Run Vue frontend	npm run dev
Install Vue packages	npm install
Migrate DB models	python manage.py migrate
Create superuser	python manage.py createsuperuser

🧠 ML Model (Brief)
Model: Linear Regression / Decision Tree

Data: Expense category vs. Amount

Trained on 2-year synthetic JSON data

Prediction shown on the dashboard

🔍 Insights & Suggestions
Make sure CORS is configured properly (django-cors-headers)

Frontend should call login API using Content-Type: application/json

JWT tokens should be stored securely (e.g., localStorage)

Use .env for sensitive credentials

Add pagination and filtering in the API for large datasets