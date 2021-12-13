from . import views
from django.urls import path

app_name='games'
urlpatterns = [
    path('', views.GamesView.as_view(), name='index')
]