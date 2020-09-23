from main import app
import tmdb_client
from unittest.mock import Mock
import pytest
import requests
from functools import partial

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None


def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr('tmdb_client.requests.get', requests_mock)


   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
   mock_single_movie = ['Movie 1']

   request_mock = Mock()
   response = request_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr('tmdb_client.requests.get', request_mock)

   movie = tmdb_client.get_single_movie(1)
   assert movie == mock_single_movie

def test_get_movie_images(monkeypatch):
   mock_movie_image = {'img1':'someurl'}
   request_mock = Mock()
   response = request_mock.return_value
   response.json.return_value = mock_movie_image
   monkeypatch.setattr('tmdb_client.requests.get', request_mock)

   image = tmdb_client.get_movie_images(1)
   assert image == mock_movie_image

def test_get_single_movie_cast():
   mock_movie_cast = ['cast1', 'cast2']
   cast = tmdb_client.get_single_movie_cast(100)
   assert type(cast) == type(mock_movie_cast)


@pytest.mark.parametrize("test_input,expected",
                         [('now_playing', 200),
                          ('popular', 200),
                          ('top_rated', 200),
                          ('upcoming', 200)])

def test_homepage(monkeypatch, test_input, expected):
   mock_result = ['Movie_1', 'Movie2', 'Movie3', 'Movie4', 'Movie5', 'Movie6', 'Movie7', 'Movie8', 'Movie9'] #{'results': [],'cast': []}
   api_mock = Mock()
   response = api_mock.return_value
   response.json.return_value = mock_result
   monkeypatch.setattr(requests, "get", api_mock)

   with app.test_client() as client:
      r = client.get('/', query_string={'list_type': f'{test_input}'})
      assert r.status_code == 200
      api_mock.assert_called_once_with(test_input)

 # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr('tmdb_client.requests.get', requests_mock)


   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list