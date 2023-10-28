from fastapi import HTTPException
import pprint
import requests
import urllib

BASE = "http://127.0.0.1:8000"


def get_artist():
    name = input("What is the name of the artist you want to find?: ")
    escaped = urllib.parse.quote(name, safe="")
    try:
        response = requests.get(f"{BASE}/artists/name/{escaped}")
        return response.json()
    except HTTPException:
        print("An error Occured. Artist was not found.")


def get_albums_by_id():
    id = int(input("Enter the id of the artist whose albums you want to display: "))

    try:
        response = requests.get(f"{BASE}/artists/{id}/albums")
        # returning json as we do not want an object thrown at us
        return response.json()
    except HTTPException:
        print("An error Occured. Artist was not found.")


def get_tracks():
    album_id = int(
        input("What is the id of the album whose tracks you want to display?: ")
    )
    try:
        response = requests.get(f"{BASE}/albums/{album_id}")
        return response.json()
    except HTTPException:
        print("An error Occured. Artist was not found.")


def get_genre():
    genre_id = int(input("What is the id of the genre you want to display?: "))
    try:
        response = requests.get(f"{BASE}/genres/{genre_id}")
        return response.json()
    except HTTPException:
        print("An error Occured. Genre was not found.")


def add_genre():
    genre_name = input("What is the name of the genre you want to create?: ")
    # creating a dictionnary that would store our query data
    data = {"title": genre_name}
    try:
        response = requests.post(f"{BASE}/genres/", params=data)
        return response.json()
    except HTTPException:
        print("An error Occured. Unable to create Genre.")


def main():
    choice = input(
        "What do you want, user?\n"
        + "Tap '1' to look for an Artist by *name*, \n "
        + "Tap '2' to look for the albums of an artist,\n"
        + "Tap '3' to look for the songs in an album,\n"
        + "Tap '4' to display songs of the genre you chose,\n"
        + "Tap '5' to add a genre,\n"
        "Tap 'q' to quit.\n" + "Enter your choice: "
    )
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=True)
    print("\n")
    match (choice):
        case "1":
            pp.pprint(get_artist())
        case "2":
            pp.pprint(get_albums_by_id())
        case "3":
            pp.pprint(get_tracks())
        case "4":
            pp.pprint(get_genre())
        case "5":
            pp.pprint(add_genre())
        case "q":
            quit()


main()
