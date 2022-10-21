from dataclasses import field
from rest_framework import serializers
from .models import Actor, Review, Movie

class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'

class ActorMovieTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)


class ActorSerializer(serializers.ModelSerializer):
    movies = ActorMovieTitleSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = '__all__'
    
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieActorNameSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Actor
        fields = ('name',)
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class MovieSerializer(serializers.ModelSerializer):
    actors = MovieActorNameSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    movie = ActorMovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
        