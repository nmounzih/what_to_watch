from movie_lib import *
import os

def clear():
    os.system("clear")

def main_menu_go():
    back_to_main = input("\nHit enter to return to the main menu. ").lower
    clear()
    main()

def main():
    # movies, users, ratings by movie, rating by user
    all_data = (load_data(0), load_data(1), load_data(2)
, load_data(3))
    # build collections to be refined
    movie_dict = all_data[0]
    user_dict = all_data[1]
    ratings_dict_by_movie = all_data[2]
    user_rating_dict = all_data[3]
    """dict of movies by their avg rating"""
    avg_ratings_dict = build_avg_rating_dicts(ratings_dict_by_movie)
    """all movie avgs list of tuples"""
    movies_avg_list = build_all_movie_avg_list(avg_ratings_dict)

    # """list of all movies a user hasn't seen"""
    # rec_unseen_movie_to_user(movies_avg_list, user_rating_dict, "84")
    #
    # """top n recommended movies for user 84"""

    # get_top_movies(rec_unseen_movie_to_user(movies_avg_list, user_rating_dict, "84"), 15)
    #
    # print("most similar user to 84 is: ")
    # print(find_most_similar_user(user_rating_dict, user_dict, "84"))
    #
    # most_sim_user = find_most_similar_user(user_rating_dict, user_dict, "84")
    #
    # """compare two most similar user movie lists"""
    # print(compare_movie_lists(get_rated_movie_list_for_user(user_rating_dict,"84"),
    # get_rated_movie_list_for_user(user_rating_dict, most_sim_user)))
    #
    # similar_movies_tup_list = (compare_movie_lists(get_rated_movie_list_for_user(user_rating_dict,"84"),
    # get_rated_movie_list_for_user(user_rating_dict, most_sim_user)))
    #
    # """sort and recommend movies"""
    # print(sort_and_recommend(similar_movies_tup_list))
    """Interface code"""

    print("\nWelcome! What do you want to watch?")
    print("Here are the current most popular movies:\n\n")
    print("Top Movies\n")

    top_movie_ids = []
    top_movies = []
    count = 1
    for movie_tup in get_top_movies(movies_avg_list, 10):
        top_movie_ids.append(movie_tup[1])
    for id in top_movie_ids:
        try:
            if id not in top_movies:
                top_movies.append(movie_dict[str(id)][0].title_and_year)
        except KeyError:
            continue
    for film in top_movies:
        print(count, film)
        count += 1

    print("\n[1] for list of popular movies you haven't seen\n[2] for list of recommendations personalized for you.\nType [q] to quit. ")
    user_input = str(input("Enter: "))

    unseen_movie_ids = []
    top_unseen_movies = []
    unseen_count = 1
    if user_input == '1':
        clear()
        user_id = str(input("Please enter your user id: "))
        clear()
        print("Checkout these popular movies!\n")
        for movie_tup in get_top_movies(rec_unseen_movie_to_user(movies_avg_list, user_rating_dict, user_id), 10):
            unseen_movie_ids.append(movie_tup[1])
        for id in unseen_movie_ids:
            try:
                if id not in top_unseen_movies:
                    top_unseen_movies.append(movie_dict[str(id)][0].title_and_year)
            except KeyError:
                continue
        for film in top_unseen_movies:
            print(unseen_count, film)
            unseen_count += 1
        main_menu_go()

    elif user_input == '2':
        clear()
        user_id = str(input("Please enter your user id: "))
        clear()
        user_2 = find_most_similar_user(user_rating_dict, user_dict, user_id)
        user1_list = []
        user2_list = []
        for key in user_rating_dict:
            if user_id == key:
                user1_list.append(user_rating_dict[key])
            elif user_2 == key:
                user2_list.append(user_rating_dict[key])
        rec_set = compare_movie_lists(user1_list, user2_list)
        rating_choice = int(input("What is the lowest rating you want to see? "))
        rec_tupe_list = sort_and_recommend(rec_set, desired_rating_cutoff=rating_choice)
        rec_movies_id = []
        rec_movies = []
        rec_count = 1
        for rec_tupe in rec_tupe_list:
            rec_movies_id.append(rec_tupe[0])
        for id in rec_movies_id:
            try:
                if id not in rec_movies:
                    rec_movies.append(movie_dict[id][0].title_and_year)
            except KeyError:
                continue
        for film in rec_movies:
            print(rec_count, film)
            rec_count += 1
        main_menu_go()

    elif user_input == 'q'.lower():
        clear()
        exit()
main()
