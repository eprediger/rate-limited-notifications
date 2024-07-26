from behave import given, when, then

from notification_rules_creation_steps import create_notification_rule


@given('a notification rule with type "{notification_type}"')
def step_impl(context, notification_type):
    notification_rule = create_notification_rule({"type": notification_type})
    context.response = context.client.post(
        "/notification-rules",
        json=notification_rule
    )

@given(u'the type "{notification_type}"')
def step_impl(context, notification_type):
    context.vars["notification:type"] = notification_type


@given(u'the user with id "{user_id}"')
def step_impl(context, user_id):
    context.vars["notification:user_id"] = user_id


@given(u'the message "{message}"')
def step_impl(context, message):
    context.vars["notification:message"] = message


@when(u'I send the notification')
def step_impl(context):
    notification = {
        "type": context.vars["notification:type"],
        "user_id": context.vars["notification:user_id"],
        "message": context.vars["notification:message"]
    }
    context.response = context.client.post(
        "/notifications",
        json=notification
    )


@when(u'it doesn\'t have any previous notification sent in rule period')
def step_impl(context):
    pass


@then(u'I get a successful response with the sent notification')
def step_impl(context):
    assert context.response.status_code == 201
