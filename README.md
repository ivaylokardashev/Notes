# 🛡️ React + Django JWT Authentication App

Това е пълнофункционално уеб приложение, използващо:

- ✅ **React** (Frontend)
- 🔐 **Django REST Framework** (Backend)
- 🔑 **JWT Authentication** (с access и refresh tokens)
- 🔄 **Автоматично презареждане на токени**
- 🔒 **Protected Routes**
- 🌐 **Axios** с `Authorization` header
- 🔁 **Auth Context** за глобално управление на потребителската сесия

---

🔐 Как работи автентикацията
Потребителят се логва → получава access и refresh токени

access токенът се пази в localStorage и се изпраща автоматично чрез Axios

Ако токенът изтече, ProtectedRoute използва refresh токена, за да получи нов

AuthContext следи дали потребителят е логнат и предоставя това състояние глобално

---

🆔Sample Test Data
username: admin
password: admin

---

📃How to run backend and frontend
To run your site (both backend and frontend), follow these steps:

**Backend (Django REST API):**
1. Open a terminal and navigate to the `backend` directory:
   ```
   cd backend
   ```
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Apply database migrations:
   ```
   python manage.py migrate
   ```
4. Start the Django development server:
   ```
   python manage.py runserver
   ```
   This will start the backend at [http://127.0.0.1:8000](http://127.0.0.1:8000).

**Frontend (React + Vite):**
1. Open a new terminal and navigate to the `frontend` directory:
   ```
   cd frontend
   ```
2. Install Node.js dependencies:
   ```
   npm install
   ```
3. Start the Vite development server:
   ```
   npm run dev
   ```
   This will start the frontend, usually at [http://localhost:5173](http://localhost:5173) (the terminal will show the exact URL).

**Notes:**
- The frontend is configured to use the backend at `http://127.0.0.1:8000` via the `VITE_API_URL` variable in `frontend/.env`.
- Make sure both servers are running at the same time (use two terminals).
- You can now access the app in your browser at the frontend URL.

If you want me to run these commands for you, please toggle to Act mode.

---

✅ Основни функции
🔐 Login/Register с JWT

🚫 Защитени маршрути

🔁 Refresh на токена автоматично

🌍 Axios interceptor с Authorization

🧠 Глобален AuthContext със isAuthorized състояние

🧹 Logout с изчистване на токени

---