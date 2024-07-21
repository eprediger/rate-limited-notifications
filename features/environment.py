from behave import fixture, use_fixture
from fastapi.testclient import TestClient
from app.main import app

@fixture
def app_client(context, *args, **kwargs):
    context.client = TestClient(app)
    yield context.client

def before_scenario(context, scenario):
    if "todo" in scenario.effective_tags:
        scenario.skip("Marked with @todo")
        return


def before_feature(context, feature):
    if "todo" in feature.tags:
        feature.skip("Marked with @todo")
        return

    use_fixture(app_client, context)
    context.vars = {}
