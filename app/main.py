from fastapi import FastAPI, status

from app.adapters.persistence.notification_rules.model import notification_rules
from app.adapters.http.notification_rules import notification_rules_controller
from app.domain.notification_rule import NotificationRule
from app.domain.period import Period
from app.domain.time_frame import TimeFrame

app = FastAPI(
    title="Rate-Limited Notification Service",
)

app.include_router(notification_rules_controller.router)
