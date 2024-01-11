import requests_with_caching
import json

def get_movies_from_tastedive(movie_or_artist_name):
    param={'q':movie_or_artist_name,'type':'movies','limit':5}
    base='https://tastedive.com/api/similar'
    resp=requests_with_caching.get(base,params=param)
    return resp.json()
    
def extract_movie_titles(resp_tastedive):
    result=resp_tastedive['Similar']['Results']
    return [i['Name'] for i in result]
    
def get_related_titles(movie_titles):
    related_movie_list=[get_movies_from_tastedive(i) for i in movie_titles]
    lst_of_lst=[extract_movie_titles(i) for i in related_movie_list]
    a=[]
    for item in lst_of_lst:
        a=a+item
    return(list(set(a)))

def get_movie_data(movie):
    param={'t':movie,'r':'json'}
    base="http://www.omdbapi.com/"
    resp=requests_with_caching.get(base,params=param)
    return resp.json()

def get_movie_rating(omdb_result):
    ratings=omdb_result['Ratings']
    for i in ratings:
        if i['Source']=="Rotten Tomatoes":
            return int(i['Value'][:-1])
    return 0

def get_sorted_recommendations(movie_list):
    related_movie_list=get_related_titles(movie_list)
    #print(related_movie_list)
    movie_rating={}
    for item in related_movie_list:
        movie_rating[item]=get_movie_rating(get_movie_data(item))
    movie_rating=sorted(movie_rating.items(),reverse=True,key=lambda x:(x[1],x[0]))
    return [j[0] for j in movie_rating]
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))

