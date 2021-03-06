from typing import List

from linebot.models import TextSendMessage

from user_detail.models import UserDetail
from .message_action_manager import MessageActionManager
from .base import MessageBase


# TODO: Use regex later
@MessageActionManager.register(['好き', 'すき'])
class LikeRecipe(MessageBase):

    def execute(self) -> None:
        """Update what the speaker dislike.
        TODO: This function should probably be closed once webapp is open
        Examples of text
            'りんご すき'
            'たまご 好き'

        """
        #TODO: NLP
        if '好き' in self.text:
            update_item = self.text.strip('好き')
        if 'すき' in self.text:
            update_item = self.text.strip('すき')
        user = {'line_message_uid': self.speaker}
        update = {'update_field': 'like_recipe', 'update_item': update_item}

        try:
            UserDetail.objects.update_preferences(user, **update)
        except Exception:
            # TODO wrap exception
            msg = TextSendMessage(text=f'なんか入力がおかしいよ！')
            self.LINE_BOT_API.push_message(self.reply_to, messages=msg)
            raise Exception('Some shit happened')

        msg = TextSendMessage(text=f'{update_item}が好きなんだね！覚えたよ！')
        self.LINE_BOT_API.reply_message(self.reply_token, msg)
