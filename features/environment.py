from behave import fixture, use_fixture
from fastapi.testclient import TestClient

from app.adapters.persistence.database import Base, engine
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

def after_scenario(context, scenario):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
