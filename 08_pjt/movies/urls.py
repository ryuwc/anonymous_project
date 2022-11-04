from django.urls import path
from movies import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/<int:genre_pk>/', views.recommended, name='recommended'),
]
