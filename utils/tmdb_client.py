import requests
import random
import my_token
from http import HTTPStatus

def get_movies_list(list_type='popular'):
    available_lists = ['now_playing', 'popular', 'top_rated', 'upcoming']
    if list_type not in available_lists:
        list_type = 'popular'
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    api_token = my_token.get_my_token()
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = my_token.get_my_token()
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = my_token.get_my_token()
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    api_token = my_token.get_my_token()
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    api_token = my_token.get_my_token()
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(list_type, how_many):
    data = get_movies_list(list_type)
    return data["results"][:how_many]


def get_random_movies(list_type, how_many):
    data = get_movies_list(list_type)
    return random.sample(data["results"], how_many)
