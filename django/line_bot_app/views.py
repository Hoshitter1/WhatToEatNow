import os
from dataclasses import dataclass

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationMessage, AccountLinkEvent
)

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse

from user_detail.models import UserDetail

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


def _tmp_food_search_func(like_ingredients, num_of_trial=5):
    for i in range(num_of_trial):
        ingredients = 'kinoko'
        if ingredients in like_ingredients:
            break
    return 'url'


class LineBotBase:

    @csrf_exempt
    def callback(self):
        """
        Webhook request always comes here first
        so handler will be enabled.
        """
        # This needs to be updated
        signature = self.META['HTTP_X_LINE_SIGNATURE']
        body = self.body.decode('utf-8')
        try:
            handler.handle(body, signature)
        except InvalidSignatureError:
            HttpResponseForbidden()
        return HttpResponse('OK', status=200)

    @handler.add(AccountLinkEvent)
    def auth_notification(self, event):
        nonce = event.link.nonce
        # TODO: Search account uid from the nonce, and link msg_user_id to profile_uid
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="認証できたで！！！！！"
                                 f"your nonce is {nonce}"
                                 f"your id is {event.source.user_id}")
        )


@dataclass
class LineBot(LineBotBase):
    line_message_uid = None
    message_from_user = None

    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(self, event) -> None:
        self.message_from_user = event.message.text
        test_terms = ("テスト")
        linking_terms = ("連携", 'れんけい')
        all_terms = (
            *test_terms,
            *linking_terms,
        )

        # If message does not include any terms specified, do nothing.
        if self.message_from_user not in all_terms:
            return

        self.line_message_uid = event.source.user_id
        if self.message_from_user in test_terms:
            try:
                self.test(event)
            except Exception as e:
                raise Exception('Error xxxx')

        if self.message_from_user in linking_terms:
            try:
                self.send_account_linking_url(event)
            except Exception as e:
                raise Exception('Error xxxx')

    def test(self, event) -> None:
        obj = UserDetail.objects.all().filter(line_message_uid=self.line_message_uid).first()
        if obj is None:
            obj = UserDetail.objects.create_new_account(line_message_uid=self.line_message_uid)
        like_ingredients_raw: str = obj.like_ingredients  # None?
        if len(like_ingredients_raw) == 0:
            like_ingredients = []
        else:
            like_ingredients: list = like_ingredients_raw[1:-1].split(',')
        suggest_link = _tmp_food_search_func(like_ingredients)
        msg = TextSendMessage(text=suggest_link)
        line_bot_api.push_message(self.line_message_uid, messages=self.message_from_user)
        account_link_url = f'{self.line_message_uid}\n This is test{suggest_link}'
        msg = TextSendMessage(text=account_link_url)
        line_bot_api.reply_message(event.reply_token, msg)

    def send_account_linking_url(self, event) -> None:
        try:
            result = line_bot_api.issue_link_token(self.line_message_uid)
        except Exception as e:
            raise Exception('client error xxx')  # TODO: create wrapper
        token = result.link_token
        account_link_url = f'http://localhost/login?linkToken={token}'
        msg = TextSendMessage(text=account_link_url)
        line_bot_api.reply_message(event.reply_token, msg)
