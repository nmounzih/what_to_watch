import csv

# week 2 weekend hw will and nadia
# building a movie recommendation engine from movie rating info


class Movie:
    def __init__(self, **kwargs):
        self.id = kwargs.get('movie_id')
        self.title_and_year = kwargs.get('movie_title_and_year')
        self.release_date= kwargs.get('release_date')
        self.url = kwargs.get('imdb_url')

    def __repr__(self):
        return "{} {} {} {}".format(self.id, self.title_and_year, self.release_date, self.url)

    def get_rating_average(self, rating_dict):
        temp_rate_list = []
        for rate_list in rating_dict.values():
            for single_rating in rate_list:
                #if self.id == single_rating.movie_id:  # change to work with uesr organized rating_dict
                temp_rate_list.append(single_rating.number)
        return round(sum(temp_rate_list) / len(temp_rate_list), 3) # maybe do more formatting later

    def get_all_movie_rating(self, rating_dict):
        temp_rate_list = []
        for rate in rating_dict.values():
            for single_rating in rate:
                if self.id == single_rating.movie_id:
                    temp_rate_list.append(int(single_rating.number))
        return temp_rate_list

    def get_movie_name(self, id_num, movies_dict):
        try:
            return movies_dict[id_num].title_and_year
        except KeyError:
            return "Sorry your selection is not in our data set"



    # do other stuff later maybe!!

class User:
    def __init__(self, **kwargs):
        self.id = kwargs.get("user_id")
        self.age = kwargs.get("user_age")
        self.gender = kwargs.get("gender")
        self.job = kwargs.get("job")
        self.zip_code = kwargs.get("zip_code")


    def __repr__(self):
        return "{} {} {} {} {}".format(self.id, self.age, self.gender, self.job, self.zip_code)

    def get_all_ratings_for_user(self, rating_dict_user):
        try:
            return [v.number for key, value in rating_dict_user.items() for v in value if self.id == key and isinstance(v, Rating)]
            return [v[1] for key, value in rating_dict_user.items() for v in value if self.id == key]
        except KeyError:
            return "Sorry your selection is not in our data set"

class Rating:
    def __init__(self, **kwargs):
        self.number = kwargs.get('score')
        self.user = kwargs.get('user')
        self.movie_id = kwargs.get('movie_id')
        self.timestamp = kwargs.get('timestamp')

    def __repr__(self):
        return "{} {} {} {}".format(self.user, self.number, self.movie_id, self.timestamp)

class InvalidInputException(ValueError):
    pass

# 1 will return the movie_dict, 2 the user_dict, 3 the ratings_dict_movie_id and 4 the ratings_dict_user
def load_data(return_value_int):
    if return_value_int == 0:
        """make list of movie instances to be analyzed"""
        movies_list = []
        genre_list = []
        movie_dict = {}
        with open("u.item", encoding="latin_1") as f:
            reader = csv.DictReader(f, delimiter='|', fieldnames=["movie_id", "movie_title_and_year", "release_date", "imdb_url"])
            for row in reader:
                genre_list.append(row[None])
                del row[None]# this is a hack to deal with problem
                movies_list.append(Movie(**row))
            for movie in movies_list:
                movie_dict.setdefault(movie.id, []).append(movie)
        return movie_dict

    elif return_value_int == 1:
        """make list of users to be analyzed"""
        user_list = []
        users_dict = {}
        with open("u.user", encoding="latin_1") as f:
            reader = csv.DictReader(f, delimiter='|', fieldnames=["user_id", "user_age", "gender", "job", "zip_code"])
            for row in reader:
                user_list.append(User(**row))
            for user in user_list:
                users_dict.setdefault(user.id, []).append(user)
        return users_dict

    elif return_value_int == 2 or return_value_int == 3:
        """make list of ratings to be analyzed"""
        rating_list = []
        with open("u.data", encoding='latin_1') as f:
            reader = csv.DictReader(f, delimiter='\t', fieldnames=['user', 'movie_id', 'score', 'timestamp'])
            for row in reader:
                rating_list.append(Rating(**row))
        rating_dict_movie_id = {}
        rating_dict_user = {}
        for rating in rating_list:
            rating_dict_movie_id.setdefault(rating.movie_id, []).append(rating)
            rating_dict_user.setdefault(rating.user, []).append((rating.movie_id, rating.number))
        if return_value_int == 2:
            return rating_dict_movie_id
        elif return_value_int == 3:
            return rating_dict_user
    else:
        raise InvalidInputException


# helper functions

def build_avg_rating_dicts(ratings_dict_movie_id):
    """builds average rating dictionaries"""
    avg_ratings_dict = {}
    for id_num, list_of_ratings in ratings_dict_movie_id.items():
        if len(list_of_ratings) >= 2:
            for this_rating in list_of_ratings:
                avg_ratings_dict.setdefault(id_num, []).append(int(this_rating.number))
    return avg_ratings_dict

def build_all_movie_avg_list(avg_ratings_d):
    """makes the list of movie averages"""
    movies_avg_list = []
    sum_ratings = 0
    for movie_id, rating_list in avg_ratings_d.items():
        for rating in rating_list:
            sum_ratings += rating
        movie_avg = sum_ratings / len(rating_list)
        movies_avg_list.append((round(movie_avg, 4), (int(movie_id))))
        sum_ratings = 0
    return movies_avg_list

def get_top_movies(avg_list, num_movies):
    """gets top N movies from any list, as long as the movie as at least n ratings"""
    top_movies = []
    if num_movies > len(avg_list):
        return "You requested a number of movies longer than the list. Please enter a smaller number of movies to see"
    for movie_avg_tup in avg_list:
        top_movies.append(max(avg_list))
        avg_list.remove(max(avg_list))
    top_movies = top_movies[:num_movies]
    return top_movies

def get_rated_movie_list_for_user(rate_dict_user, user_id):
    return rate_dict_user[user_id]

def rec_unseen_movie_to_user(avg_list, rate_dict_user, user_id):
    """recommends movies a user hasn't seen"""
    recommended_movies = []
    user_movie_list = rate_dict_user[user_id]
    zip_zap = zip(avg_list, user_movie_list)
    for zap in zip_zap:
        if zap[0][1] != zap[1].movie_id:
            recommended_movies.append(zap[1])
    return recommended_movies

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

def find_most_similar_user(all_users_rating_dict, all_user_inst_dict, base_user_id_num):
    """finds most similar user"""
    most_sim_user = ""
    last_comp_score = 0
    for user in all_users_rating_dict:
        if int(user) <= 100 and user != base_user_id_num:  # only for test file
            new_comp_score = get_euclidean_distance(all_user_inst_dict[base_user_id_num][0].get_all_ratings_for_user(all_users_rating_dict),
            all_user_inst_dict[user][0].get_all_ratings_for_user(all_users_rating_dict))
            if new_comp_score > last_comp_score:
                most_sim_user = user
                last_comp_score = new_comp_score
        return most_sim_user

def compare_movie_lists(user1_list, user2_list):
    user1 = set()
    user2 = set()
    for movie_tupes_list in user1_list:
        for single_tupe in movie_tupes_list:
            user1.add(single_tupe)
    for movie_tupes_list in user2_list:
        for single_tupe in movie_tupes_list:
            user2.add(single_tupe)
    return user1 ^ user2

def sort_and_recommend(movie_rec_set, desired_rating_cutoff=0):
    recommended_movies = [movie for movie in movie_rec_set if int(movie[1]) >= desired_rating_cutoff]
    return sorted(recommended_movies)
