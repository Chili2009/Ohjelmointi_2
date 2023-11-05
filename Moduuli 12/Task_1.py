import requests


def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        joke_text = joke_data["value"]
        return joke_text
    else:
        return "Unable to fetch Chuck Norris joke."


if __name__ == "__main__":
    joke = get_random_chuck_norris_joke()
    print("Chuck Norris Joke:")
    print(joke)
