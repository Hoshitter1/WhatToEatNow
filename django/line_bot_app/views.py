import os
from typing import List, Type, Optional

from django.http import HttpResponseForbidden, HttpResponse
from rest_framework.views import APIView

from linebot import WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models.events import Event

from .manager_bases import SpecificManagerBase
from .actions.general_action_manager import GeneralActionManager
from .actions.base import ActionBase


class LineCallBack(APIView):
    channel_secret = os.environ["YOUR_CHANNEL_SECRET"]

    def post(self, request):
        """
        """
        signature = request.META.get('HTTP_X_LINE_SIGNATURE', False)
        if not signature:
            # TODO: Add a error log
            print('signature was not found')
            return HttpResponseForbidden()

        body = request.body.decode('utf-8')
        try:
            events: List[Type[Event]] = WebhookParser(self.__class__.channel_secret).parse(body, signature)
        except InvalidSignatureError:
            # TODO: Add a error log
            print(self.__class__.channel_secret)
            print('Invalid signature error')
            return HttpResponseForbidden()

        self.__execute_action(events)
        return HttpResponse('OK', status=200)

    @staticmethod
    def __execute_action(events: List[Type[Event]]) -> None:
        """
        # TODO: Use async or celory to handle action from here
        Args:
            events (List[Type[Event]]):

        """
        for event in events:
            # TODO: Leave these until some other actions are integrated apart from Message.
            # Probably new class has to be created so action manager and specific action manager are put together
            event_type: str = event.type
            specific_action_manager: Optional[Type[SpecificManagerBase]] = GeneralActionManager.get_manager(event_type)
            if specific_action_manager is None:
                continue

            action: Optional[ActionBase] = specific_action_manager.get_action(event)
            if action is None:
                continue
            action.execute()
