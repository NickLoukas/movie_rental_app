from rest_framework import viewsets, filters
from movies.models import Movie, Order
from .serializers import MovieListSerializer, UserSerializer, OrderSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    filterset_fields = ['title', 'genre']
    search_fields = ['title', 'genre']



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
