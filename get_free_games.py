import requests
from bs4 import BeautifulSoup

def fetch_free_games():
    url = "https://steamdb.info/upcoming/free/"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    free_games = []
    rows = soup.select("table.table-products tbody tr")

    for row in rows:
        if "Free promotion" in row.text:
            app_id = row["data-appid"]
            free_games.append(app_id)

    return free_games
