from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponsePermanentRedirect

from django.forms import ValidationError
from django.forms.models import model_to_dict
from django.contrib import messages

from datetime import datetime, timedelta, timezone

from django.views import View 

import jwt
import json
from json import dumps, loads, JSONEncoder, JSONDecoder
import random
import csv
import xlrd
import openpyxl

import requests
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
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
    
    q = openapi.Parameter('q', in_=openapi.IN_QUERY,
            description='keyword is the text to search on twitter', type=openapi.TYPE_STRING)
                        
    media = openapi.Parameter('media', in_=openapi.IN_QUERY,
        description='media ', type=openapi.TYPE_BOOLEAN)

    @swagger_auto_schema(
        manual_parameters=[q, media])
    
    # def search(self, request, keyword, boolean, *args, **kwargs):
    def search(self, request, *args, **kwargs):
        q = request.query_params.get('q', None)
        media = request.query_params.get('media', None)
        tweet_list = []
        
        limit = 1
        # limit = 20

        try:
            # if q and media and media.lower() == 'true':
            if q :
                tweets = tweepy.Cursor(api.search_tweets, q=q, include_entities=True, tweet_mode='extended').items(limit)
                
                # print(tweets)
                
                for tweet in tweets:
                    print(tweet)
                    print("\n")
                    
                    tweet_list.append(tweet)
                    # tweet_list.append([tweet.id, tweet.user.screen_name, tweet.full_text])
                    
            if q and media and media.lower() == 'false':
                tweets = tweepy.Cursor(api.search_tweets, q=q, include_entities=False, tweet_mode='extended').items(limit)
                
                # print(tweets)
                
                for tweet in tweets:
                    print(tweet)
                    print("\n")
                    
                    tweet_list.append(tweet)
                    # tweet_list.append([tweet.id, tweet.user.screen_name, tweet.full_text])
                    
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

            


