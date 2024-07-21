from behave import given, when, then, use_step_matcher

use_step_matcher("cfparse")

def create_notification(replacement: dict):
    example_course = {
        "type": "Status",
        "max_per_user": 1,
        "time_frame": {
            "amount": 1,
            "period": "MINUTES"
        }
    }

    example_course.update(replacement)

    return example_course

@given('the type is "{type}"')
def step_impl(context, type):
    context.vars["new_notification"] = {}
    context.vars["new_notification"]["type"] = type


@given('the maximum number of emails is "{max_per_user:d}"')
def step_impl(context, max_per_user):
    context.vars["new_notification"]["max_per_user"] = max_per_user


@given('the time frame is "{amount:d}" "{period}"')
def step_impl(context, amount, period):
    context.vars["new_notification"]["time_frame"] = {
        "amount": amount,
        "period": period.upper()
    }
    print(context.vars["new_notification"])


@when("I create the notification")
def step_impl(context):
    context.response = context.client.post(
        "/notification-rules",
        json=context.vars["new_notification"]
    )


@then("I get the notification created successfully")
def step_impl(context):
    request = context.vars['new_notification']
    response_body = context.response.json()

    assert context.response.status_code == 201
    for key in request:
        assert request[key] == response_body[key]

@given(u'a new notification where the key "{key_name}" has value "{value}"')
def step_impl(context, key_name, value):
    replacement = {
        key_name: value
    }

    if key_name == "type" and value == "-":
        replacement[key_name] = ""

    context.vars["new_notification"] = create_notification(replacement)

@then(u'I get a validation error message')
def step_impl(context):
    print(context.vars["new_notification"])
    assert context.response.status_code == 422

