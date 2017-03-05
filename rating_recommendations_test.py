from nose.tools import raises
from rating_recommendations import *


test_list = [(1.0, 303), (5.0, 404), (4.7, 99), (3.4, 176), (3.0, 10), (4.5, 310), (5.0, 76), (2.5, 16), (1.5, 47), (3.567, 30), (5.0, 7), (4.2, 52), (3.78, 26), (2.8, 75), (1.0, 99), (1.2, 101), (1.0, 45), (1.0, 82), (1.3, 66), (1.4, 202)]
test_user_rate_dict = {}

def test_get_top_10():
    assert get_top_10(test_list) == [(5.0, 404), (5.0, 76), (5.0, 7), (4.7, 99), (4.5, 310), (4.2, 52), (3.78, 26), (3.567, 30), (3.4, 176), (3.0, 10)]


def test_rec_unseen_movie_to_user():
    assert rec_unseen_movie_to_user(test_list, test_user_rate_dict, "")
