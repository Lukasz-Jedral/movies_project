import requests
import random
import my_token


def call_tmbd_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    api_token = my_token.get_my_token()
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type='popular'):
    available_lists = ['now_playing', 'popular', 'top_rated', 'upcoming']
    if list_type not in available_lists:
        list_type = 'popular'
    return call_tmbd_api(f'movie/{list_type}')


def get_single_movie(movie_id):
    return call_tmbd_api(f'movie/{movie_id}')


def get_single_movie_cast(movie_id):
    response = call_tmbd_api(f'movie/{movie_id}/credits')
    return response["cast"]


def get_movie_images(movie_id):
    return call_tmbd_api(f'movie/{movie_id}/images')


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(list_type, how_many):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_random_movies(list_type, how_many):
    data = get_movies_list(list_type)
    return random.sample(data["results"], how_many)
