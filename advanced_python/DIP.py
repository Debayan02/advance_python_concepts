#Dependency Inversion Principle

class EmailService:
    def send_email(self, message, receiver):
        print(f"Sending email: {message} to {receiver}")

class SmsService:
    def send_sms(self, message, receiver):
        print(f"Sending SMS: {message} to {receiver} ")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        elif method == "sms":
            self.sms_service.send_sms()

notification1=NotificationService()
print(notification1.send_notification("Hello","Debayan","email"))
