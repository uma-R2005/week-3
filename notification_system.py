class EmailNotificationMixin:
    def send_email(self, message):
        print(f"Sending email: {message}")

class SMSNotificationMixin:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

class NotificationSystem(EmailNotificationMixin, SMSNotificationMixin):
    def notify(self, method, message):
        if method == "email":
            self.send_email(message)
        elif method == "sms":
            self.send_sms(message)
        else:
            print("Unknown notification method")

# Usage:
notif = NotificationSystem()
method = input("Notification method (email/sms): ").strip().lower()
msg = input("Message to send: ")
notif.notify(method, msg)
