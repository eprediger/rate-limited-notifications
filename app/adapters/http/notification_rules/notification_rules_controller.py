from fastapi import APIRouter, status, Depends
from typing import List
from sqlalchemy.orm import Session

from app.domain.notification_rule import NotificationRuleBase, NotificationRule
from app.adapters.persistence.notification_rules import repository
from app.adapters.persistence.database import get_db

router = APIRouter(
    prefix="/notification-rules",
    tags=["Notification Rules"]
)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=NotificationRule)
def create_notification(rule: NotificationRuleBase, db: Session = Depends(get_db)):
    return repository.create_notification_rule(db, rule)


@router.get("", response_model=List[NotificationRule])
def get_notifications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return repository.get_notification_rules(db, skip, limit)
