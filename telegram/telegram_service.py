import os

import telegram


class TelegramServices:
    def __init__(self):
        self.bot = telegram.Bot(token=os.environ['telegram_token'])

    def send_message_with_post(self, link, title) -> None:
        self.bot.sendMessage(
            chat_id='@coingeckonewstetbot',
            text=f'{link} \n <b>{title}</b>',
            parse_mode=telegram.ParseMode.HTML)
