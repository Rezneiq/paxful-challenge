from django.urls import path
from statistic.views import StatisticApiView


urlpatterns = [
    path('statistics/', StatisticApiView.as_view())
]