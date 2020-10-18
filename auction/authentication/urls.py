from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user_details),
    path('get_user_data/', views.get_user_data),
]