from django.urls import path
from cinema import views as cinema_views

app_name = "cinema"

urlpatterns = [
    path("", cinema_views.MovieCatalogView.as_view(), name="catalog"),
    path("movie/<slug:movie_slug>/", cinema_views.MovieDetailView.as_view(), name="movie"),
]
