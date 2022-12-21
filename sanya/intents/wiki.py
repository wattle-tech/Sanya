from bs4 import BeautifulSoup
import requests


__all__ = ("Wikipedia")



class Wikipedia:

    @property
    def title(self, page: str) -> str:
        response = requests.get(
            url=f"https://en.wikipedia.org/wiki/{page}",
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find(id="firstHeading")
        return title.string

    @property
    def shorten_description(self, page: str) -> str:
        response = requests.get(
            url=f"https://en.wikipedia.org/wiki/{page}",
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        shd = soup.find(_class="shortdescription nomobile noexcerpt noprint searchaux")
        return shd.string

    @property
    def description(self, page: str) -> str:
        response = requests.get(
            url=f"https://en.wikipedia.org/wiki/{page}",
        )
        soup = BeautifulSoup(response.content, 'html.parser')

        d = soup.find(_class="")
        return d .string

    
    