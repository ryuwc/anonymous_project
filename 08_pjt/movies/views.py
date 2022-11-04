from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe

from movies.models import Movie, Genre


# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    genres = get_list_or_404(Genre)
    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request, genre_pk):
    movies = get_list_or_404(Movie)
    genres = get_list_or_404(Genre)
    cur_genre = get_object_or_404(Genre, pk=genre_pk)
    genre_movies = []
    for movie in movies:
        for genre in movie.genres.all():
            if genre.pk == genre_pk:
                genre_movies.append(movie)
    genre_movies.sort(key=lambda x: x.vote_average, reverse=True)
    context = {
        'genre': cur_genre,
        'movies': genre_movies[:9],
        'genres': genres,
    }
    return render(request, 'movies/recommended.html', context)