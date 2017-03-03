from movie_lib import *

# recommends movies to a user based on average ranking
# movies must have more than 1 ranking
# we will recommend the top five movies
# use load_data from movie_lib to get needed collection

def main():
    all_movies_avg = []
    ratings_dict = load_data(3)
    movie_dict = load_data(1)
    avg_ratings_dict = {}
    top_five_movies = []
    for id_num, list_of_ratings in ratings_dict.items():
        if len(list_of_ratings) >= 3:
            for this_rating in list_of_ratings:
                avg_ratings_dict.setdefault(int(id_num), []).append(int(this_rating.number))
            for movie in movie_dict.values():
                print("\n\n\n trying to get avg ratings")
                print(movie, type(movie))
                all_movies_avg.append(id_num, movie[0].get_rating_average(avg_ratings_dict))


main()
