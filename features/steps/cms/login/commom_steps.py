
from behave import then  # pylint: disable=no-name-in-module

from behave import *


@then("the result should be {result}")
def _then_result_should_be(context, result):
    assert str(context.result) == str(
        result
    ), f"Mismatch: [{str(context.result)}] - [{str(result)}]"
