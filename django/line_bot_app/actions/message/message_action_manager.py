from typing import Dict, List

from linebot.models import MessageEvent
from linebot.models.events import Event

# TODO Fix the relative import
from ...manager_bases import SpecificManagerBase
from ..general_action_manager import GeneralActionManager


@GeneralActionManager.register('message')
class MessageActionManager(SpecificManagerBase):
    TRIGGER_AND_ACTION: Dict[List[str], Event] = {}

    @classmethod
    def register(cls, trigger: List[str]):
        """Collect all specific action managers

        Returns:

        """

        def decorator(cls_):
            cls.TRIGGER_AND_ACTION[cls_] = trigger
            return cls_

        return decorator

    @classmethod
    def get_action(cls, event: MessageEvent):
        """TODO
        """
        action = None
        if hasattr(event.message, 'text'):
            action = cls.text_action(event)
        return action

    @classmethod
    def text_action(cls, event: MessageEvent):
        action = None
        msg_from_user = event.message.text

        triggers: List[str]
        for action_, triggers in cls.TRIGGER_AND_ACTION.items():
            for trigger in triggers:
                if trigger in msg_from_user:
                    return action_(event)
        return action
