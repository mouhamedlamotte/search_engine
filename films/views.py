from django.shortcuts import render
from .serializers import FilmSerializer
from .documents import FilmDocument
from .models import Film
from elasticsearch_dsl.query import MultiMatch

from rest_framework import generics


class ListFilmsView(generics.ListAPIView):
    serializer_class = FilmSerializer
    queryset = Film.objects.all()
    
    
class SeachFilmView(generics.ListAPIView):
    serializer_class = FilmSerializer
    def get_queryset(self):
        q = self.request.query_params.get('q')
        if q:
            query = MultiMatch(query=q, fields=['original_title', 'title', 'overview'] , fuzziness='AUTO')
            return FilmDocument.search().query(query).to_queryset()
        return Film.objects.none()
    

