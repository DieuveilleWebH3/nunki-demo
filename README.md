# INTRODUCTION #


This document provides the instructions for using / interacting with the Nunki Api Demo Application developed by ***Dieuveille BOUSSA ELLENGA***. 


<br>
<br>

## Part I

Retrieve content from twitter api, by building a wrapper api around it.

**Language:** **Python**
**Framework:** **Django**
**Package:** **Tweepy**

<br>

### Task : Build an API that has two endpoints

 - GET /search?q=<keyword>&media=<boolean> => it searches content related to the keyword on twitter,  the media params decide whether the tweets should have media content attached to it or not.

<br>

 - GET /users/<user_id> => it gets the content related to the user on twitter


<br>
<br>

## Part II

Add a new endpoint to your api that retrieve contents from classified ads websites

**Package:** **BeautifulSoup**

<br>

### Task : Build a scrapper that retrieves contents from a classified ads search

 - You should build a scraper that scrapes all classified ads posted on the following website: https://ci.coinafrique.com/
 
 <br>

 - The endpoint should take a keyword as an input that will search on this web-site to only get classified ads related to that content.


<br>
<br>


# Prerequisite Or Dependencies

## Docker and Docker-Compose


<br>
<br>



# COMMANDS 

## Clone the git repo

```
git clone https://github.com/DieuveilleWebH3/nunki-demo.git  
```

## Open the main directory / root folder 

```
cd nunki-demo
```

## Start the project with 

```
docker-compose up
```

## Visit  http://127.0.0.1:8089/

