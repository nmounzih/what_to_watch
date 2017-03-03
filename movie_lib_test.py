from nose.tools import raises
from movie_lib import *
# test suite for week 2 project

test_movie = Movie(**{"movie_id": 123, "movie_title_and_year":"Jurrassic Park (1993)", "release_date":"June 11, 1993", "imdb_url":"https://www.imdb.com/title/tt0107290/"})
test_movie2 = Movie(**{"id":456, "title_and_year":"Saving Private Ryan (1998)", "release_date":"July 24, 1998", "imdb_url":"https://www.imdb.com/title/tt0107290/"})
test_movie3 = Movie(**{"id":789, "title_and_year":"Pirates of the Carribean (2001)", "release_date":"June 5, 2001", "imdb_url":"https://www.imdb.com/title/tt0107290/"})
test_ratings1 = Rating(**{"user":4, "movie_id":123, "score":4, "timestamp":986324687})
test_ratings2 = Rating(**{"user":6, "movie_id":123, "score":2, "timestamp":886322387})
test_ratings3 = Rating(**{"user":5, "movie_id":123, "score":3, "timestamp":896324687})
test_ratings4 = Rating(**{"user":6, "movie_id":456, "score":2, "timestamp":896385687})
test_ratings5 = Rating(**{"user":4, "movie_id":456, "score":5, "timestamp":986324687})
test_ratings6 = Rating(**{"user":5, "movie_id":456, "score":4.5, "timestamp":896324687})
test_user = User(**{"user_id":4, "user_age":30, "gender":"M", "job":"Pro Wrestler", "zip_code":27707})

movie_dict = {test_movie.id: test_movie, test_movie2.id: test_movie2}

ratings_list = [test_ratings1, test_ratings2, test_ratings3, test_ratings4, test_ratings5, test_ratings6]
ratings_dict = {}
rating_dict_by_user = {}

for rating in ratings_list:
    ratings_dict.setdefault(rating.movie_id, []).append(rating)

for rating in ratings_list:
    rating_dict_by_user.setdefault(rating.user, []).append(rating)

def test_get_rating_average(): # make instance for some movie, get average
    assert test_movie.get_rating_average(ratings_dict) == 3

def test_get_all_movie_rating(): # make instance for some movie get all ratings
    assert test_movie.get_all_movie_rating(ratings_dict) == [4, 2, 3]

def test_get_movie_name_in_list(): #    make instance for movie and get its name
    assert test_movie.get_movie_name(123, movie_dict) == "Jurrassic Park (1993)"


def test_get_movie_name_not_in_list(): # makes instance for movie that isn't in the list
    assert test_movie3.get_movie_name(789, movie_dict) == "Sorry your selection is not in our data set"

def test_get_all_ratings_from_user(): # tests getting all user ratings via the user id
    print(test_user.get_all_ratings_for_user(rating_dict_by_user))
    assert test_user.get_all_ratings_for_user(rating_dict_by_user) == [4, 5]
