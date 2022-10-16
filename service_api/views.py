from ast import keyword
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponsePermanentRedirect

from django.forms import ValidationError
from django.forms.models import model_to_dict
from django.contrib import messages

import requests
from django.urls import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _  # noqa: F401

from rest_framework import generics, status, views, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.viewsets import GenericViewSet, ModelViewSet, ViewSet
from rest_framework import status

from rest_framework.settings import api_settings

from nunki_demo import settings

import tweepy

import time
import pandas as pd 
from bs4 import BeautifulSoup


# Config
api_key = "CxCkNuSCmuelWNslaQhm9G7bq"
api_key_secret = "gJMNhCM6GoBAeK086LELVSunbdfSo1a02yeR0ehmAKtA8pkUZT"
access_token = "1365307419291746313-i2bEAmjz6NPErFs3cVhyE1LG0KF7SO"
access_token_secret = "KUCoEdshHZ7VUqKrY7S7FVUrFmjOPaD6uznOoHjzXQhMo"

# Authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Create your views here.

class CustomRedirect(HttpResponsePermanentRedirect):
    allowed_schemes = settings.REDIRECT_ALLOWED_SCHEMES

    
class TwitterApiViewset(ViewSet):
    
    # ************************************* Part One of Assignment ******************************         
    
    q = openapi.Parameter('q', in_=openapi.IN_QUERY, 
                          description='keyword is the text to search on twitter', type=openapi.TYPE_STRING)
                        
    media = openapi.Parameter('media', in_=openapi.IN_QUERY,
                              description='boolean parameter to show or not media ', type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(
        manual_parameters=[q, media])
    
    # first part of first task
    # search endpoint definition to get tweets from a query
    def search(self, request, *args, **kwargs):
        # requesting parameter passed in endpoint call 
        q = request.query_params.get('q', None)
        media = request.query_params.get('media', None)
        
        # declaring empry list that will collect tweets if there is any
        tweet_list = []
        
        # Number of tweets to retrieve
        limit = 5
        # limit = 20

        try:
            # first case scenario only the query has been filled 
            # and / or the media boollean attribute is set at true 
            if q:
                # using tweepy package with methode cursor to get tweets
                tweets = tweepy.Cursor(api.search_tweets, q=q, include_entities=True, tweet_mode='extended').items(limit)
                                
                # for tweet in tweets:
                    # tweet_list.append(tweet)
                    # tweet_list.append([tweet.id, tweet.user.screen_name, tweet.full_text])
                    
                # filling the list with the retrieved tweets 
                tweet_list.extend(iter(tweets))
             
            # second case scenario the query and the media boollean attribute have been filled 
            # and the media boollean attribute is set at false 
            if q and media and media.lower() == 'false':
                # using tweepy package with methode cursor to get tweets
                tweets = tweepy.Cursor(api.search_tweets, q=q, include_entities=False, tweet_mode='extended').items(limit)
                                
                # for tweet in tweets:    
                    # tweet_list.append(tweet)
                    # tweet_list.append([tweet.id, tweet.user.screen_name, tweet.full_text])
                    
                # filling the list with the retrieved tweets 
                tweet_list.extend(iter(tweets))
                    
            return HttpResponse(
                # json.dumps(tweet_list),
                tweet_list,
                status=status.HTTP_200_OK,
            )
            
        except Exception as e:
            return Response(
                f'Error found => [ERR]: {e}',
                status=status.HTTP_400_BAD_REQUEST,
            )
            
    # Second part of first task 
    # Users endpoint definition to get a twitter user info from user id
    def users(self, request, user_id, *args, **kwargs):
        user = {}
        
        try:
            if user_id:
                # using get_user with id 
                user = api.get_user(user_id=user_id)

            return HttpResponse(
                # json.dumps(model_to_dict(user)),
                user,
                status=status.HTTP_200_OK,
            )
            
        except Exception as e:
            return Response(
                f'Error found => [ERR]: {e}',
                status=status.HTTP_400_BAD_REQUEST,
            )
       
    
    # *****************************************************************************         
    # ************************************* Part Two of Assignment ******************************         
    keyword = openapi.Parameter('keyword', in_=openapi.IN_QUERY,
    description='keyword is the text to search on the website', type=openapi.TYPE_STRING)

    @swagger_auto_schema(
        manual_parameters=[keyword])
       
    # ads endpoint definition to scrap ads from a website 
    def ads(self, request, *args, **kwargs):
        keyword = request.query_params.get('keyword', None)
        ads = []
        
        try:
        
            # https://ci.coinafrique.com/search?category=&keyword=montres
            # https://ci.coinafrique.com/search?keyword=montres&page=2
            
            # base URL for the CoinAfrique website
            base_url = "https://ci.coinafrique.com"

            # URL for the first page
            # page_1_url = base_url + '/search?category=&keyword='+keyword if keyword else base_url
            page_1_url = f'{base_url}/search?category=&keyword=' + keyword if keyword else base_url

            # use requests library to get the response
            response = requests.get(page_1_url)

            # use BS to parse the text of the HTML response
            soup = BeautifulSoup(response.text, "lxml")

            # find all of the relevant ads
            # div class="advertissement-section" found after inspecting the website 
            ads = soup.find_all("div", attrs={"class": "advertissement-section"})
            
            print(ads)
            
            return HttpResponse(
                # json.dumps(ads),
                ads,
                status=status.HTTP_200_OK,
            )
            
        except Exception as e:
            return Response(
                f'Error found => [ERR]: {e}',
                status=status.HTTP_400_BAD_REQUEST,
            )



