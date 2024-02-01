import argparse

from tech_blog_trend_notifier.api import APIClient
from tech_blog_trend_notifier.mail import MailClient


def main(args: argparse.Namespace) -> None:
    api = APIClient()
    mail = MailClient(args.config)
    articles = api.get_articles()
    mail.send(articles)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Send tech blog articles to your email"
    )
    parser.add_argument(
        "--config", type=str, default="config.yaml", help="config file path"
    )
    args = parser.parse_args()
    main(args)
