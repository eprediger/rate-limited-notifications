from pydantic import BaseModel, PositiveInt, constr

from app.domain.period import Period


class NotificationRuleBase(BaseModel):
    type: constr(min_length=1)
    max_per_user: PositiveInt
    amount: PositiveInt
    period: Period

class NotificationRule(NotificationRuleBase):
    id: int

    class Config:
        orm_mode = True
