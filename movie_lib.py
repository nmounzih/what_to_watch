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
        for rate in rating_dict.values():
            for single_rating in rate:
                if self.id == single_rating.movie_id:
                    temp_rate_list.append(int(single_rating.number))
        return round(sum(temp_rate_list) / len(temp_rate_list), 1) # maybe do more formatting later

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
            return [v.number for key, value in rating_dict_user.items() for v in value if self.id == key]
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


def main():
    """make list of movie instances to be analyzed"""
    movies_list = []
    genre_list = []
    with open("u.item", encoding="latin_1") as f:
        reader = csv.DictReader(f, delimiter='|', fieldnames=["movie_id", "movie_title_and_year", "release_date", "imdb_url"])
        for row in reader:
            genre_list.append(row[None])
            del row[None]# this is a hack to deal with problem
            movies_list.append(Movie(**row))
        movies_dict = {movies.id: movies for movies in movies_list}

    """make list of users to be analyzed"""
    user_list = []
    with open("u.user", encoding="latin_1") as f:
        reader = csv.DictReader(f, delimiter='|', fieldnames=["user_id", "user_age", "gender", "job", "zip_code"])
        for row in reader:
            user_list.append(User(**row))
        user_dict = {users.id: users for users in user_list}

    """make list of ratings to be analyzed"""
    rating_list = []
    with open("u.data", encoding='latin_1') as f:
        reader = csv.DictReader(f, delimiter='\t', fieldnames=['user', 'movie_id', 'score', 'timestamp'])
        for row in reader:
            rating_list.append(Rating(**row))
        rating_dict_movie_id = {}
        rating_dict_user = {}
        for data in rating_list:
            rating_dict_movie_list.setdefault(data.movie_id, []).append(data)
            rating_dict_user.setdefault(data.user, []).append(data)



if __name__ == "__main__":
    main()
