import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

from omegaconf import OmegaConf


class MailClient:
    def __init__(self, config_filepath: str) -> None:
        config = OmegaConf.load(config_filepath)
        self.to_address = config.to_address
        self.from_address = config.from_address
        self.password = config.password

        self.smtpobj = smtplib.SMTP("smtp.gmail.com", 587)
        self.smtpobj.starttls()
        self.smtpobj.login(self.from_address, self.password)

    def send(self, articles: dict[str, list[dict]]) -> None:
        body_text = self._create_body(articles)
        msg = MIMEText(body_text, "html", "utf-8")
        msg["From"] = self.from_address
        msg["To"] = self.to_address
        now = formatdate()
        msg["Date"] = now
        msg["Subject"] = "-".join(now.split()[1:4][::-1])

        self.smtpobj.send_message(msg)
        self.smtpobj.close()

    def _create_body(
        self, articles: dict[str, list[dict]], articles_per_site: int = 5
    ) -> str:
        body = "<h1>Today's Trend Tech Blob</h1>\n"
        for site, articles in articles.items():
            body += f"<h2>{site}</h2>\n"
            for article in articles[:articles_per_site]:
                body += f"<h3><a href={article['url']}>{article['title']}</a></h3>\n"
                body += f"<p>Published at: {article['published_at']}</p>\n"
                body += f"<p>Liked count: {article['liked_count']}</p>\n"
                body += f"<p>Categories: {', '.join(article['categories'])}</p>\n"
                body += "<br>\n"
        return body
