from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Movie

# Create your views here.
def movies(request):
    movies = Movie.objects.all()
    return render(request, "movies.html", {"movies":movies})



