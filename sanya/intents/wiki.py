from bs4 import BeautifulSoup
import requests


__all__ = ("Wikipedia")



class Wikipedia:
    def search(self, page: str):
        response = requests.get(
            url=f"https://en.wikipedia.org/wiki/{page}",
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id="firstHeading")
        return title.string