from django.urls import path
import users.views

urlpatterns = [
    path('login/', users.views.LoginUser.as_view(), name='user_login'),
    path('register/', users.views.RegisterUser.as_view(), name='user_register'),
]