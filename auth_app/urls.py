from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserDetailAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('user/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]
