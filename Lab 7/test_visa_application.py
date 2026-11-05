from hypothesis import given, strategies as st
from visa_application import (
    parse_application,
    processing_average,
    payable_fee
)


@given(st.text() | st.none())
def test_parse_application_no_crash(s):
    try:
        result = parse_application(s)
        assert isinstance(result, tuple)
        assert len(result) == 2
    except Exception as e:
        assert False, f"parse_application crashed with: {e}"


@given(st.text() | st.none())
def test_processing_average_no_crash(s):
    try:
        result = processing_average(s)
        assert isinstance(result, int)
    except Exception as e:
        assert False, f"processing_average crashed with: {e}"


@given(st.text() | st.none())
def test_payable_fee_no_crash(s):
    try:
        result = payable_fee(s)
        assert isinstance(result, (int, float))
    except Exception as e:
        assert False, f"payable_fee crashed with: {e}"