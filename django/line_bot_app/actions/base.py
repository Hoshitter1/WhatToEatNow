import os

from linebot import LineBotApi


class ActionBase:
    LINE_BOT_API = LineBotApi(os.environ["YOUR_CHANNEL_ACCESS_TOKEN"])

    def execute(self):
        raise NotImplementedError('execute function has to be defined')
