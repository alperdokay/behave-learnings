from behave import *
from door import Door

door = Door()

@given('the door is closed')
def step_impl(context):
    assert door.status == "Close"

@when('open the door')
def step_impl(context):
    door.open()

@then('the door is open')
def step_impl(context):
    assert door.status == "Open"