from behave import given, when, then, use_step_matcher

from steps.notification_rules_creation_steps import create_notification

use_step_matcher("cfparse")

@given("that a notification rule exists")
def step_impl(context):
    new_notification = create_notification()
    context.response = context.client.post(
        "/notification-rules",
        json=new_notification
    )


@when("I query the notification rules")
def step_impl(context):
    context.response = context.client.get("/notification-rules")


@then("I should receive them successfully")
def step_impl(context):
    assert context.response.status_code == 200
