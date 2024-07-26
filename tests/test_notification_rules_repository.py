import unittest

from app.adapters.persistence.database import Base, engine, SessionLocal
from app.adapters.persistence.notification_rules.repository import get_notification_rule_by_type, \
    create_notification_rule
from app.domain.notification_rule import NotificationRuleBase


class NotificationRulesRepositoryTest(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(engine)
        self.session = SessionLocal()

    def tearDown(self):
        self.session.rollback()
        Base.metadata.drop_all(engine)
        self.session.close()

    def test_repository_should_return_an_existent_notification_rule(self):
        expected_type = 'a-rule-type'
        create_notification_rule(self.session, NotificationRuleBase(type=expected_type,
                                                                    max_per_user=4,
                                                                    period="WEEKS"))

        notification_rule = get_notification_rule_by_type(self.session, expected_type)

        self.assertEqual(notification_rule.type, expected_type)
        self.assertEqual(notification_rule.max_per_user, 4)
        self.assertEqual(notification_rule.period, "WEEKS")


if __name__ == '__main__':
    unittest.main()
