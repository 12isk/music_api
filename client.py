import requests


def get_artist():
    name = input("What is the name of the artist you want to find?: ")
    try:
        response = requests.get(f"http://127.0.0.1:8000/artists/name/{name}")
        return response.json()
    except:
        print("An error Occured. Artist was not found.")


def get_albums():
    id = int(input("Enter the id of the artist whose albums you want to display: "))

    try:
        response = requests.get(f"http://127.0.0.1:8000/artists/{id}/albums")
        # returning json as we do not want an object thrown at us
        return response.json()
    except:
        print("An error Occured. Artist was not found.")


def get_tracks():
    album_id = int(
        input("What is the id of the album whose tracks you want to display?: ")
    )
    try:
        response = requests.get(f"http://127.0.0.1:8000/albums/{album_id}")
        return response.json()
    except:
        print("An error Occured. Artist was not found.")


def main():
    choice = input(
        "What do you want, user?\n"
        + "Tap '1' to look for an Artist by *name*; \n "
        + "Tap '2' to look for the albums of an artist.\n"
        + "Tap '3' to look for the songs in an album.\n"
        "Tap'q' to quit"
    )

    match (choice):
        case "1":
            get_artist()

        case "2":
            get_albums()
        case "3":
            get_tracks()
        case "q":
            quit()
