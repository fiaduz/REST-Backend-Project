from django.urls import path
from .views import RegisterView, UserView, LogoutView, TodoListCreate, TodoDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/", UserView.as_view(), name="user"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("todos/", TodoListCreate.as_view(), name="todo-list"),
    path("todos/<int:pk>/", TodoDetail.as_view(), name="todo-detail"),
]
