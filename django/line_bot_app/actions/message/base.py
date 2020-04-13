from ..base import ActionBase
from linebot.models import MessageEvent


class MessageBase(ActionBase):

    def __init__(self, event: MessageEvent):
        # breakpoint()
        if hasattr(event.source, 'group_id'):
            self.reply_to = event.source.group_id
        elif hasattr(event.source, 'room_id'):
            self.reply_to = event.source.room_id
        elif hasattr(event.source, 'user_id'):
            self.reply_to = event.source.user_id
        self.speaker = event.source.user_id
        self.reply_token = event.reply_token
        self.text = event.message.text
