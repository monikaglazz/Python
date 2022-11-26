
import requests
import json

# set an api key
headers = {'x-api-key': '259b32fd-2b04-4228-8ab6-4530f4fcaa68'}


# function to get content with json
def get_content_json(request):
    try:
        content = request.json()
    except json.decoder.JSONDecodeError:
        print("Wrong format")
    else:
        return content


# function to get favorites cats
def get_favorites_cats(user_id):
    param = {"sub_id": user_id}
    r = requests.get("https://api.thecatapi.com/v1/favourites",
                     headers=headers, params=param)
    return get_content_json(r)


# function to get random cats images
def get_random_cat():
    r = requests.get(
        "https://api.thecatapi.com/v1/images/search", headers=headers)
    return get_content_json(r)[0]


# function to add favorites cats to user account
def add_cat_to_favorites(user_id, cat_id):
    param = {"sub_id": user_id,
             "image_id": cat_id}
    r = requests.post("https://api.thecatapi.com/v1/favourites/",
                      json=param, headers=headers)
    return get_content_json(r)


# function to remove favorite cat from user account
def remove_favorite_cat(cat_id):
    r = requests.delete(
        'https://api.thecatapi.com/v1/favourites/' + str(cat_id), headers=headers)
    return get_content_json(r)


# Here getting username and password
# check correction of data
# log in correctly
# get from database userId and user Name

name = "Monica"
user_id = "dr56h"

print("Hello", name + "!", "Nice to see you again!")
while True:
    what_to_do = input(
        "Tell me what to do: \n1 - Show favorites cats \n2 - Add new cat \n3 - log out\n")

    # show favorites cats
    if what_to_do == "1":
        favorite_cats = get_favorites_cats(user_id)
        if len(favorite_cats) == 0:
            print("You don't have favorites cats")
        else:
            print("Your favorites cats: ")
            for cat in favorite_cats:
                print("Cat id: ", cat["id"], "URL: ", cat["image"]["url"])
            remove = input(
                "Do you want do remove any cat from the favorites? Y/N \n")
            if remove.upper() == "Y":
                cat_id = int(input("Give the cat ID you want to remove: "))
                remove_favorite_cat(cat_id)
                print("Cat was removed successfully :( You are a terrible human!")
            elif remove.upper() == "N":
                print("Yey! The cats love you!")
            else:
                print("You have to chose Y - yes or N - no")
    # add new cat
    elif what_to_do == "2":
        randomCat = get_random_cat()
        print("You drawn this cat: ", randomCat["url"])
        decision = input("Do you want to add it to your favorites? Y/N \n")
        if decision.upper() == "Y":
            add_cat_to_favorites(user_id, randomCat["id"])
            print("Cat was added successfully!")
        elif decision.upper() == "N":
            print("That's sad :(")
        else:
            print("You have to chose Y - yes or N - no")
    # log out
    elif what_to_do == "3":
        print("See ya!")
        break
