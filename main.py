from tech_blog_trend_notifier.api import APIClient
from tech_blog_trend_notifier.mail import MailClient


def main():
    api = APIClient()
    articles = api.get_articles()
    mail = MailClient()


if __name__ == "__main__":
    main()
