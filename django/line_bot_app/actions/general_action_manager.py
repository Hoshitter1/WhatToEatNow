from typing import Optional, Type

from line_bot_app.manager_bases import GeneralManagerBase, SpecificManagerBase


class GeneralActionManager(GeneralManagerBase):

    EVENT_AND_ACTION = {}

    @classmethod
    def register(cls, event_type: str):
        """Collect all specific action managers

        Returns:

        """
        def decorator(cls_):
            cls.EVENT_AND_ACTION[event_type] = cls_
            return cls_
        return decorator

    @classmethod
    def get_manager(cls, event_type: str) -> Optional[Type[SpecificManagerBase]]:
        """Collect specific actions
        e.g WhatToCookDinner

        Returns:
            specific_action_manager:
        """
        specific_action_manager = cls.EVENT_AND_ACTION.get(event_type, None)
        return specific_action_manager
