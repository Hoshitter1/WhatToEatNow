from linebot.models import TextSendMessage

# This way works but I do know want relatively
from user_detail.models import UserDetail
# This code works
# from .message_action_manager import MessageActionManager
# from .base import MessageBase
# from ...clients.rakuten_recipe import rakuten

# ideally I want to import like this
from line_bot_app.clients import Rakuten
from .message_action_manager import MessageActionManager
from .base import MessageBase


@MessageActionManager.register(['test', 'テスト'])
class Test(MessageBase):

    def execute(self) -> None:
        """Test gives you instructions of coding in action
        """
        # Get user detail
        obj = UserDetail.objects.all().filter(line_message_uid=self.speaker).first()
        if obj is None:
            obj = UserDetail.objects.create_new_account(line_message_uid=self.speaker)
        like_ingredients_raw: str = obj.like_ingredients  # None?
        if len(like_ingredients_raw) == 0:
            like_ingredients = []
        else:
            like_ingredients: list = like_ingredients_raw[1:-1].split(',')

        # Send message
        msg = TextSendMessage(text='I LOVE ZILYA')
        self.LINE_BOT_API.push_message(self.reply_to, messages=msg)

        # Reply
        result = Rakuten.request()
        suggest_link = result.results[0].recipe_url
        # suggest_link = result.list[0].
        account_link_url = (
            f'speaker:{self.speaker}'
            f'reply_to:{self.reply_to}'
            f'これ食え{suggest_link}'
        )
        msg = TextSendMessage(text=account_link_url)
        self.LINE_BOT_API.reply_message(self.reply_token, msg)
