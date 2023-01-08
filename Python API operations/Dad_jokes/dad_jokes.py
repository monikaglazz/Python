# Program to get random dad joke from https://icanhazdadjoke.com

import requests
from random import choice

# get topic from user
topic = input("Give the topic of jokes you want to search: ")

# get response
r_json = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()

# assign list of jokes
list_with_jokes = r_json["results"]

# assign number of jokes
number_of_jokes = r_json["total_jokes"]

if number_of_jokes > 1:
    print(
        f"\nI've found {number_of_jokes} jokes about {topic}. One of them:\n",
        choice(list_with_jokes)['joke']
    )
elif number_of_jokes == 1:
    print(
        f"I've found one joke about {topic}. Here it is:\n",
        list_with_jokes[0]['joke']
    )
else:
    print(f"I don't have any jokes about {topic}! Please try again.")
