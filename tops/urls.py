from django.urls import path
from .views import Top10PollutedCitiesView, Top10CleanestCitiesView

urlpatterns = [
    path('top10pollutedcities/', Top10PollutedCitiesView.as_view(), name='top-10-polluted-cities'),
    path('top10cleanestcities/', Top10CleanestCitiesView.as_view(), name='top-10-cleanest-cities'),
]