from api import APIClient


def main():
    api = APIClient()
    articles = api.get_articles()


if __name__ == "__main__":
    main()
