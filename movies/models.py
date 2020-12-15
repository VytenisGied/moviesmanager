from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    poster = models.CharField(max_length=500,)
    movie_id = models.CharField(max_length=50,)
    owner = models.ForeignKey(User, related_name="movies", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)