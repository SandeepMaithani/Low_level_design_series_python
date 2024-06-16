from observer_pattern.observer.notification_alert_observer import NotificationAlertObserver


class MobileAlertObserverImpl(NotificationAlertObserver):

    def __init__(self, user_name, observable_instance) -> None:
        self.user_name = user_name
        self.observable_instance = observable_instance
    

    def update(self):
        alert_body = "New socks available. this is mobile push notification powered by observer pattern"
        self.send_alert_via_mobile(message=alert_body)
    
    def send_alert_via_mobile(self, message):
        print(f"alert: '{message}' send via mobile push to : '{self.user_name}'.")