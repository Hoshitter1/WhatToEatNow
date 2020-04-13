class SpecificManagerBase:
    """defines the behavior of specific manager classes

    """

    @classmethod
    def register(cls, event_type):
        raise NotImplementedError('')

    @classmethod
    def get_action(cls, msg_event):
        raise NotImplementedError('')


class GeneralManagerBase:
    """defines the behavior of general manager classes

    """

    @classmethod
    def register(cls, event_type):
        raise NotImplementedError('')

    @classmethod
    def get_manager(cls, msg_event):
        raise NotImplementedError('')
