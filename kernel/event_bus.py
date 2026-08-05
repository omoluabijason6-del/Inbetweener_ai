from collections import defaultdict


class EventBus:
    """
    Simple publish / subscribe event system.
    """

    def __init__(self):
        self.listeners = defaultdict(list)

    def subscribe(self, event_name, callback):
        """
        Register a listener.
        """

        self.listeners[event_name].append(callback)

    def publish(self, event_name, data=None):
        """
        Notify all listeners.
        """

        print(f"[Event] {event_name}")

        for callback in self.listeners[event_name]:
            callback(data)