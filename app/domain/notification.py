from datetime import datetime

from pydantic import BaseModel


class NotificationBase(BaseModel):
    type: str
    user_id: str


class NotificationCreate(NotificationBase):
    message: str


class Notification(NotificationBase):
    id: int
    sent_at: datetime

    class Config:
        orm_mode = True
