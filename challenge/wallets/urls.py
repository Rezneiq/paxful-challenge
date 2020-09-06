from django.urls import path
from wallets import views


urlpatterns = [
    path('wallets/', views.WalletsApiView.as_view()),
    path('wallets/<str:address>', views.WalletApiView.as_view()),
    path('wallets/<str:address>/transactions', views.WalletTransactionsApiView.as_view()),
]