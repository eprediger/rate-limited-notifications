from app.domain.notification import NotificationCreate


class Gateway:
    def send(self, notification: NotificationCreate):
        print(f"sending message '{notification.message}' to user '{notification.user_id}'")


def get_gateway():
    yield Gateway()
