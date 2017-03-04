from movie_lib import *

# recommends movies to a user based on average ranking
# movies must have more than 1 ranking
# we will recommend the top five movies
# use load_data from movie_lib to get needed collection

def main():
    # movies, users, ratings by movie, rating by user
    all_data = (load_data(1), load_data(2), load_data(3)
, load_data(4))
    movie_dict = all_data[0]
    user_dict = all_data[1]
    ratings_dict_by_movie = all_data[2]
    user_rating_dict = all_data[3]
    avg_ratings_dict = {}
    top_five_movies = []
    movies_avg_list = []

    """builds average rating dictionaries"""
    for id_num, list_of_ratings in ratings_dict_by_movie.items():
        if len(list_of_ratings) >= 2:
            for this_rating in list_of_ratings:
                avg_ratings_dict.setdefault(int(id_num), []).append(int(this_rating.number))

    """makes the list of movie averages"""
    for movie_id in avg_ratings_dict.keys():
        movie_avg = sum(avg_ratings_dict[movie_id])/len(avg_ratings_dict[movie_id])
        movies_avg_list.append((round(movie_avg, 4), (int(movie_id))))
    get_top_10(movies_avg_list)

    print(get_euclidean_distance(user_rating_dict["20"], user_rating_dict["25"]))

def get_top_10(avg_list):
    """gets top 10 movies from any list"""
    top_10_movies = []
    for id_avg_tup in avg_list:
        top_10_movies.append(max(avg_list))
        avg_list.remove(max(avg_list))
        top_10_movies = top_10_movies[:10]
    return top_10_movies

def rec_unseen_movie_to_user(avg_list, rate_dict_user, user_id):
    """recommends movies a user hasn't seen"""
    recommended_movies = []
    user_movie_list = [rate_dict_user[user_id] for rating in rate_dict_user]
    for average in avg_list:
        if not average[1] in user_movie_list:
            recommended_movies.append(average)

    return get_top_10(recommended_movies)

def get_euclidean_distance(user1_list, user2_list):
    """taking two lists of movies a user has seen, we find the distance between them, the distance being how similar they are on a scale from 0 to 1. 1 means 100 percent identical"""

    if len(user1_list) is 0:
        return 0

    sorted_user1_list = sorted(user1_list)
    sorted_user2_list = sorted(user2_list)

    differences = [int(user1_tup[0]) - int(user2_tup[0]) for user1_tup, user2_tup in zip(sorted_user1_list, sorted_user2_list)]

    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + (sum_of_squares**(0.5)))

def compare_users(user1_id, user2_id, user_dict):
    pass


main()
