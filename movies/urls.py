from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.MoviesListView.as_view(), name='MovieList'),
    path('new', views.MovieCreateView.as_view(), name='MovieCreate'),
]