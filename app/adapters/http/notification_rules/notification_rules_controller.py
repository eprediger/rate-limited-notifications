from fastapi import APIRouter, status

from app.adapters.persistence.notification_rules.model import notification_rules
from app.domain.notification_rule import NotificationRule

router = APIRouter(
    prefix="/notification-rules",
    tags=["Notification Rules"]
)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_notification(rule: NotificationRule):
    notification_rules.append(rule)
    return rule


@router.get("")
def get_notifications():
    return notification_rules
