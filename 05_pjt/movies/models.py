from logging import PlaceHolder
from random import choices
from django.db import models


choice = (
    ('코미디', '코미디'),
    ('로맨스', '로맨스'),
    ('SF', 'SF'),
    ('액션', '액션')
)
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

