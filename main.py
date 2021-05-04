from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

# <h3 class="jsx-4245974604">100) Stand By Me</h3>
soup = BeautifulSoup(empire_web_page, "html.parser")
movie_names = soup.find_all(name="h3",class_ = "jsx-4245974604")

movie_title = [movie.getText() for movie in movie_names]
movies = movie_title[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")