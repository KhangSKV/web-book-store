from django.urls import path
from .views import UserDetailView, UserListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user-detail')
]