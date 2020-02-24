import os

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden, HttpResponse

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, LocationMessage, AccountLinkEvent
)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    """
    Webhook request always comes here first
    so handler will be enabled.
    """
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()
    return HttpResponse('OK', status=200)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    test_terms = ["テスト"]
    is_interact_mode = False
    for term in test_terms:
        if term in event.message.text:
            is_interact_mode = True

    if is_interact_mode:
        # Get linkToken for user to link their line account with webapp
        uid = event.source.user_id
        account_link_url = f'{uid}\n This is test'
        msg = TextSendMessage(text=account_link_url)
        line_bot_api.reply_message(event.reply_token, msg)
        # msg = TextSendMessage(text=f'{profile.display_name}')
        # line_bot_api.push_message(send_to, messages=msg)


@handler.add(AccountLinkEvent)
def auth_notification(event):
    nonce = event.link.nonce
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="認証できたで！！！！！"
                             f"your nonce is {nonce}"
                             f"your id is {event.source.user_id}")
    )


@handler.add(MessageEvent, message=TextMessage)
def send_account_linking_url(event):
    linking_terms = ["連携", 'れんけい']
    is_interact_mode = False
    if event.message.text in linking_terms:
        is_interact_mode = True

    if is_interact_mode:
        # Get linkToken for user to link their line account with webapp
        uid = event.source.user_id
        result = line_bot_api.issue_link_token(uid)
        token = result.link_token
        account_link_url = f'http://localhost/login?linkToken={token}'
        msg = TextSendMessage(text=account_link_url)
        line_bot_api.reply_message(event.reply_token, msg)
