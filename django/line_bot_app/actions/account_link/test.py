# @handler.add(AccountLinkEvent)
# def auth_notification(self, event):
#     nonce = event.link.nonce
#     # TODO: Search account uid from the nonce, and link msg_user_id to profile_uid
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text="認証できたで！！！！！"
#                              f"your nonce is {nonce}"
#                              f"your id is {event.source.user_id}")
#     )
