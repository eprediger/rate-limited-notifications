from behave import given, when, then


@given(u'a rule with type "{rule_type}"')
def step_impl(context, rule_type):
    context.execute_steps(f'Given the type is "{rule_type}"')


@given(u'this notification rule exists')
def step_impl(context):
    context.execute_steps("When I create the notification")


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


@when(u'it has no prior notification sent within the rule period')
def step_impl(context):
    pass


@given(u'it has a prior notification sent')
def step_impl(context):
    context.execute_steps('When I send the notification')


@then(u'I get a successful response with the sent notification')
def step_impl(context):
    assert context.response.status_code == 201


@then(u'I get an erroneous response for exceeding the rate limit')
def step_impl(context):
    assert context.response.status_code == 429


@then(u'I get and erroneous response for a non-existent type')
def step_impl(context):
    assert context.response.status_code == 400
