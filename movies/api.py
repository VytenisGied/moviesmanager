from movies.models import Movie
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = MovieSerializer

    def get_queryset(self):
        return self.request.user.movies.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)