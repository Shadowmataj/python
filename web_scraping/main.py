from bs4 import BeautifulSoup
import requests
#
# with open("website.html") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# response =  requests.get("https://news.ycombinator.com/news")
# content = response.text
#
# soup = BeautifulSoup(content, "html.parser")
#
# scores_list = soup.find_all(class_="score")
# scores_dict = {}
#
# for score in scores_list:
#     scores_dict[score.get("id").split("_")[1]] = int(score.text.split(" ")[0])
#
# higher_points = max(scores_dict, key=scores_dict.get)
# print(higher_points)
# higher = soup.find(id=higher_points)
#
# print(higher.select(".titleline a")[0].get("href"))


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

movies_site_response = requests.get(url=URL)

soup = BeautifulSoup(movies_site_response.text, "html.parser")
titles = soup.find_all(name="h3", class_="title")
titles_text = [title.text for title in titles]
titles_text[41] = titles_text[41].replace("â", "-")

with open("movies.txt", "w") as file:
    for title in titles_text[::-1]:
        file.write(f"{title}\n")
