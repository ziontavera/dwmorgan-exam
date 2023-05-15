from django.urls import path
from covid_tracker_app.api.views import CovidTrackerView

urlpatterns = [
    path("confirmed/", CovidTrackerView.as_view(), name="confirmed_cases"),
]
