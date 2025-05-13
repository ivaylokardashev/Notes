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

✅ Основни функции
🔐 Login/Register с JWT

🚫 Защитени маршрути

🔁 Refresh на токена автоматично

🌍 Axios interceptor с Authorization

🧠 Глобален AuthContext със isAuthorized състояние

🧹 Logout с изчистване на токени