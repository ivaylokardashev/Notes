
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
# Prebuild views for creating JWT (access + refresh) token and preview for refreshing token
# Helps after creating user to assign token to them
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Links root to views
# When go to specific root we call specific view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls")),
]