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
test_user2 = User(**{"user_id":6, "user_age":15, "gender":"F", "job":"Student", "zip_code":94502})
test_user3 = User(**{"user_id":5, "user_age":25, "gender":"M", "job":"Scientist", "zip_code":93117})

movie_dict = {test_movie.id: test_movie, test_movie2.id: test_movie2}

ratings_list = [test_ratings1, test_ratings2, test_ratings3, test_ratings4, test_ratings5, test_ratings6]
ratings_dict = {}

user_dict = {test_user, test_user2, test_user3}
rating_dict_by_user = {'4': [('242', '3'), ('393', '4'), ('381', '4')], '6': [('242', '3'), ('393', '4'), ('25', '1')], '5': [('175', '5')]}

user1_list = [('742', '3'), ('121', '4'), ('1033', '4')]
user2_list = [('200', '5'), ('36', '2')]

for rating in ratings_list:
    ratings_dict.setdefault(rating.movie_id, []).append(rating)

for rating in ratings_list:
    rating_dict_by_user.setdefault(rating.user, []).append(rating)

avg_ratings_dict = build_avg_rating_dicts(ratings_dict)
avg_list = build_all_movie_avg_list(avg_ratings_dict)

def test_get_rating_average(): # make instance for some movie, get average
    assert test_movie.get_rating_average(ratings_dict) == 3.417

def test_get_all_movie_rating(): # make instance for some movie get all ratings
    assert test_movie.get_all_movie_rating(ratings_dict) == [4, 2, 3]

def test_get_movie_name_in_list(): #    make instance for movie and get its name
    assert test_movie.get_movie_name(123, movie_dict) == "Jurrassic Park (1993)"


def test_get_movie_name_not_in_list(): # makes instance for movie that isn't in the list
    assert test_movie3.get_movie_name(789, movie_dict) == "Sorry your selection is not in our data set"

def test_get_all_ratings_from_user(): # tests getting all user ratings via the user id
    assert test_user.get_all_ratings_for_user(rating_dict_by_user) == [4, 5]


"""new tests"""

# def test_load_data_valid_input():
#     """test that load data returns expected collection type with valid input"""
#     """Valid input is an int between 0 and 3"""
#     """0 for movies, 1 for users, 2 for ratings by movie id, and 3 for ratings by user id"""
#     assert type(load_data(1)) is 'dict'

@raises(InvalidInputException)
def test_load_data_invalid_input():
    """tests load data raises InvalidInputException to the user for an invalid entry"""
    load_data(4)

def test_build_avg_rating_dicts():
    assert build_avg_rating_dicts(ratings_dict) == {123: [4, 2, 3], 456: [2, 5, 4]}

def test_build_all_movie_avg_list():
    assert build_all_movie_avg_list(avg_ratings_dict) == [(3.0, 123), (3.6667, 456)]

def test_get_top_movies():
    assert get_top_movies(avg_list, 1) == [(3.6667, 456)]

# user 4 is our test dummy
#def test_get_rated_movie_list_for_user():
#    assert get_rated_movie_list_for_user(rating_dict_by_user, 4) == [4 4 123 986324687, 4 5 456 986324687]

#def test_rec_unseen_movie_to_user():
#    assert rec_unseen_movie_to_user(avg_list, rating_dict_by_user, 4)

#def test_sort_and_recommend():


def test_compare_movie_lists():
    assert compare_movie_lists(user1_list, user2_list) == {'2', '3', '121', '36', '5', '200', '742', '4', '1033'}

#def test_find_most_similar_user():
#    assert find_most_similar_user(rating_dict_by_user, user_dict, '4') == 6
