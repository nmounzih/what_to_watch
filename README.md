# what_to_watch

Pair programmed a movie recommendation app that operates like Netflix. We took 100,000 movie ratings accumulated in data files on https://grouplens.org/datasets/movielens/. These files contained data on users, ratings, and movies. This program ranks top movies, top movies seen by a user, and recommends movies that a user has not seen. Movie recommendations are based on finding the euclidean distance between users and recommending movies that similar users rated well. This program is operated from the CLI.

 ## Getting Started

 1. movie_lib.py
   - Defines classes for Movie, Rating, User objects,
   - load_data(n) buils desired data, n must be 0 <= n >= 3
     a. 0 is movie data, 1 is user data, 2 is ratings by movie id and 3 is ratings by user id
   - Run with command line from its directory, "python3 movie_lib.py"

 2. movie_lib_test.py
   - Run via command line from its directory, "nosetests movie_lib_test.py"

 3. choose_your_movie.py
   - The interface for choosing what you'd like to watch.
   - Run via command line from its directory, "python3 choose_your_movie.py"

 4. u.user, u.item, u.data,
  - Data files needed to load the info to be processed

 ### Prerequisites

 Python3

 ## Running the tests

 Tests are run on "nosetest movie_lib_test.py"

 ## Deployment

 Add additional notes about how to deploy this on a live system

 ## Built With

 * Python3

 ## Authors

 - Will Warren
 - Nadia Mounzih
