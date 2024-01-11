# REST API Movie recommendation project- OMDB and TasteDive APIs
## Overview
This project is part of the professional certification – ‘Python 3 specialization’ that I took from University of Michigan.
This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).
TasteDive was used to get related movies for a whole list of titles. I have combined the resulting lists of related movies, and sorted them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)
## Data Used
The documentation for the TasteDive API is at https://tastedive.com/read/api.
The documentation for the OMDB API is at https://www.omdbapi.com/
Note : To avoid problems with rate limits and site accessibility, a cache file with results for all the queries you need to make to both OMDB and TasteDive was given in the course. So, I've used requests_with_caching.get() rather than requests.get()

### Functions to deal with TasteDive API data
Function ‘get_movies_from_tastedive’ - It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.
Function ‘extract_movie_titles’ - extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive
Function ‘get_related_titles’ - takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
### Functions to deal with OMDB API data
Function ‘get_movie_data’ - It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.
Function ‘get_movie_rating’ - It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
Function ‘get_sorted_recommendations’ - It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

