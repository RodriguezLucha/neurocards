from pytest_bdd import given, scenarios, then, when

scenarios("basic.feature")


@given("The application is running")
def the_app_is_running(app_driver):
    assert app_driver.app_is_running()
    pass


@when("I load the homepage")
def i_load_the_page():
    pass


@then("I see something")
def i_see_something():
    pass
