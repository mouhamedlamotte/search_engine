from django.urls import path
from .views import ListFilmsView, SeachFilmView


urlpatterns = [
    path('', ListFilmsView.as_view(), name='list-film'),
    path('search/', SeachFilmView.as_view(), name='search-film'),
]
