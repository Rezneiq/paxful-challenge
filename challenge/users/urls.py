from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UsersRegistrationApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view())
]