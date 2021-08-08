""" This module contains a set of dummy tests which are
supposed to trigger pytest hooks"""

import pytest


@pytest.fixture
def fixture_yield():
    print("setup fixture")
    yield "yileding"
    print("finalize fixture")


@pytest.fixture()
def fixture_finalizer(request):
    def finalizer():
        return "finalizer"

    request.addfinalizer(finalizer)
    return "actual fixture with explicit finalizer"


@pytest.mark.parametrize("param1", range(5))
def test_me_one(param1):
    pass


def test_fail_intentionally():
    assert False
