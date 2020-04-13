# def send_account_linking_url(self, event) -> None:
#     try:
#         result = self.line_bot_api.issue_link_token(self.line_message_uid)
#     except Exception as e:
#         raise Exception('client error xxx')  # TODO: create wrapper
#     token = result.link_token
#     account_link_url = f'http://localhost/login?linkToken={token}'
#     msg = TextSendMessage(text=account_link_url)
#     line_bot_api.reply_message(event.reply_token, msg)
