from django import forms
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView


# Create your views here.
from movies.models import Movie


class MoviesListView(ListView):
    model = Movie


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'genre', 'rating', 'director')
        widgets = {'title': forms.TextInput(attrs={'class': 'titleform'}),
                   'genre': forms.TextInput(attrs={'class': 'genreform'}),
                   'rating': forms.TextInput(attrs={'class': 'ratingform'}),
                   'director': forms.TextInput(attrs={'class': 'directorform'})
                   }


class MovieCreateView(CreateView):
    model = Movie
    # fields = ['title', 'genre', 'rating', 'director']
    form_class = QuestionForm
