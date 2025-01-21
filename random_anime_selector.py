import requests
from bs4 import BeautifulSoup
import random


def fetch_anime_titles_from_wikipedia():
    urls = [
        "https://en.wikipedia.org/wiki/Category:Crunchyroll_anime",
        "https://en.wikipedia.org/w/index.php?title=Category:Crunchyroll_anime&pagefrom=Dances+with+the+Dragons%0ADances+with+the+Dragons#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Crunchyroll_anime&pagefrom=I+Can%27t+Understand+What+My+Husband+Is+Saying#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Crunchyroll_anime&pagefrom=Muteking%2C+The+Dashing+Warrior#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Crunchyroll_anime&pagefrom=Shikimori%27s+Not+Just+a+Cutie#mw-pages",
        "https://en.wikipedia.org/w/index.php?title=Category:Crunchyroll_anime&pagefrom=Yuzuki+Family%27s+Four+Sons%2C+The%0AThe+Yuzuki+Family%27s+Four+Sons#mw-pages",
    ]

    anime_titles = []
    
    for url in urls:
        try:
            # Fetch the webpage content
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad status codes

            # Parse the HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract anime titles from the category pages
            # Titles are within <div class="mw-category-group"> under <a> tags
            links = soup.select(".mw-category-group a")
            anime_titles.extend([link.text.strip() for link in links])

        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch {url}: {e}")
            continue
        

    return anime_titles

def main():
    # Fetch anime titles from Wikipedia
    anime_titles = fetch_anime_titles_from_wikipedia()

    if anime_titles:
        print(f"Fetched {len(anime_titles)} anime titles!")
        while True:
            # Select a random anime title
            random_anime = random.choice(anime_titles)
            print(f"Random Anime Selected: {random_anime}")

            # Ask the user if they want another random title
            user_input = input("Generate another random anime? (yes/no): ").strip().lower()
            if user_input not in ("yes", "y"):
                print("Goodbye!")
                break
    else:
        print("No anime titles found! Please check the URLs or network connection.")


main()
    

