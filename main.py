from tech_blog_trend_notifier.api import APIClient
from tech_blog_trend_notifier.mail import MailClient


def main() -> None:
    api = APIClient()
    mail = MailClient()
    articles = api.get_articles()
    mail.send(articles)


if __name__ == "__main__":
    main()
