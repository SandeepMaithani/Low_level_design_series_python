from observer_pattern.observer.notification_alert_observer import NotificationAlertObserver


class EmailAlertObserverImpl(NotificationAlertObserver):

    def __init__(self, email_id, observable_instance) -> None:
        self.email_id = email_id
        self.observable_instance = observable_instance

    
    def update(self):
        alert_body = "New socks available, this is email notification powered by observer pattern"
        self.send_alert_via_email(message=alert_body)

    def send_alert_via_email(self, message):
        print(f"alert: '{message}' send via email to : '{self.email_id}'.")