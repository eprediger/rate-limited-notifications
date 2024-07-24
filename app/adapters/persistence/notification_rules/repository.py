from sqlalchemy.orm import Session

from app.adapters.persistence.notification_rules import model
from app.domain.notification_rule import NotificationRule, NotificationRuleBase


def get_notification_rules(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.NotificationRule) \
        .offset(skip) \
        .limit(limit) \
        .all()


def create_notification_rule(db: Session, rule: NotificationRuleBase) -> NotificationRule:
    db_notification_rule = model.NotificationRule(
        type=rule.type,
        max_per_user=rule.max_per_user,
        period=rule.period
    )
    db.add(db_notification_rule)
    db.commit()
    db.refresh(db_notification_rule)

    return db_notification_rule


def get_notification_rule_by_type(db: Session, rule_type: str) -> NotificationRule:
    return db.query(model.NotificationRule) \
        .filter(model.NotificationRule.type == rule_type) \
        .first()
