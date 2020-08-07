import requests
from bs4 import BeautifulSoup
limit = 0
try:
    while(True):
        url = "https://myanimelist.net/topanime.php?limit="
        url = url+str(limit)
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'lxml')
        animes = soup.find_all('tr', {'class': 'ranking-list'})
        for anime in animes:
            rank = anime.find("td", {"valign": "top"})
            name = anime.find(
                "a", {"class": "hoverinfo_trigger fl-l fs14 fw-b"})
            details = anime.find("div", {"class": "information di-ib mt4"})
            score = anime.find(
                "div", {"class": "js-top-ranking-score-col di-ib al"})

            anime_details = list(details)

            anime_category = (anime_details[0]).strip()
            anime_year = (anime_details[2]).strip()
            anime_members = (anime_details[4]).strip()
            anime_score = score.span.text
            anime_name = name.string
            anime_rank = anime.td.span.text

            print(anime_rank, anime_name, anime_score,
                  anime_members, anime_year, anime_category)
        limit = limit+50
except Exception as e:
    print(e)