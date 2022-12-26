from db.database import DatabaseServices
import boto3
from parser.parse_service import WebSiteParser

from telegram.telegram_service import TelegramServices


if __name__ == '__main__':
    parser_service = WebSiteParser()
    database_service = DatabaseServices(session=boto3.resource('dynamodb', region_name='us-west-2'))
    tg_service = TelegramServices()

    all_news = parser_service.parse_news_from_site()
    for news in all_news:
        if database_service.check_if_news_is_processed(news[1]):
            tg_service.send_message_with_post(link=news[1], title=news[0])
            database_service.add_news_to_table(news)
        else:
            print(f'${news} already processed')
