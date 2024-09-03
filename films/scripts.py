import requests
from .models import filmGenre, Film


def get_data():
    add_genres()
    base_url = 'https://api.themoviedb.org/3/movie/popular?api_key=1b262a3dd722d08f625a785220526fcd&language=fr-FR&page=1'
    pages = 100
    for i in range(pages):
        url = f'{base_url}&page={i+1}'
        print()
        print()
        print('page ======>' + str(i+1))
        print()
        print()
        data = requests.get(url).json()
        for film in data['results']:
            print()
            print()
            try :
                film_obj = Film.objects.create(
                    adult=film['adult'],
                    original_language=film['original_language'],
                    original_title=film['original_title'],
                    overview=film['overview'],
                    popularity=film['popularity'],
                    poster_path='https://image.tmdb.org/t/p/w500'+film['poster_path'],
                    release_date=film['release_date'],
                    title=film['title'],
                    vote_average=film['vote_average'],
                    vote_count=film['vote_count'],
                )
                film_obj.genre_ids.set(film['genre_ids'])
                print('film ======>' + str(film['title']))
                print()
                print()
                print(film)
            except Exception as e:
                print('error')
                print('')
                print('')
                print(e)
                print('')
                print('')
    return "done"


def add_genres():
    genres = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=1b262a3dd722d08f625a785220526fcd&language=fr-FR').json()
    for genre in genres['genres']:
        filmGenre.objects.create(name=genre['name'], id=genre['id'])


    