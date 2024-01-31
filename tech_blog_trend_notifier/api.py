import os

import requests
from bs4 import BeautifulSoup


class APIClient:
    def __init__(self) -> None:
        self.qiita_url = "https://qiita.com/"
        self.zenn_url = "https://zenn.dev/api/articles?article_type=tech"

    def get_articles(self):
        qiita_articles = self.__get_qiita_articles()
        zenn_articles = self._get_zenn_articles()
        return qiita_articles + zenn_articles

    def __get_qiita_articles(self):
        response = requests.get(self.qiita_url).text
        soup = BeautifulSoup(response, "html.parser")
        articles = soup.find_all("article")

        result = []
        for article in articles:
            title = article.find("h2").text
            url = article.find("a").get("href")
            published_at = article.find("header").find("time").text
            footer = article.find("footer")
            liked_count = int(footer.find("span", {"class": "style-176d67y"}).text)
            categories = [category.text for category in footer.find_all("li")]
            result.append(
                {
                    "title": title,
                    "url": url,
                    "published_at": published_at,
                    "liked_count": liked_count,
                    "categories": categories,
                }
            )
        return result

    def _get_zenn_articles(self):
        articles = requests.get(self.zenn_url).json()["articles"]
        result = []
        for article in articles:
            result.append(
                {
                    "title": article["title"],
                    "url": os.path.join("https://zenn.dev/", article["path"]),
                    "published_at": article["published_at"].split("T")[0],
                    "liked_count": article["liked_count"],
                    "categories": [],
                }
            )
        return result
