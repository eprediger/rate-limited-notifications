class NotificationNotFoundError(Exception):
    def __init__(self, notification_type: str):
        self.code = "NOTIFICATION_NOT_FOUND_ERROR"
        self.message = f"Notification '{notification_type}' not found"
        super().__init__(self.code, self.message)
