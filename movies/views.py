from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView


# Create your views here.
from movies.models import Movie


class MoviesListView(ListView):
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'genre', 'rating', 'director']