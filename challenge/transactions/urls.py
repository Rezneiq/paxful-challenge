from django.urls import path
from transactions.views import TransactionsApiView
urlpatterns = [
    path('transactions/', TransactionsApiView.as_view())
]