from django.shortcuts import render, get_object_or_404
from main.models import Movie
from django.views.generic.base import View

class MovieCatalogView(View):
    def get(self, request):
        return render(request, "cinema/catalog.html")

class MovieDetailView(View):
    def get(self, request, movie_slug):
        movie = get_object_or_404(Movie, slug=movie_slug)
        context = {
            "movie": movie,
        }
        return render(request, "cinema/movie.html", context)
