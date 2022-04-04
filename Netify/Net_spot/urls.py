from django.urls import path
from .views import Home,Movie_Home
from . import views

app_name='Net_spot'
urlpatterns = [
    path('',Home.as_view()),
    path('',Movie_Home.as_view())
]
