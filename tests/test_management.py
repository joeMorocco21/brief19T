import pytest
import sys

def test_passed():
    assert 2 == 2

def test_failed():
    assert 2 == 3

@pytest.fixture
def fixture():
    yield
    assert False

def test_errored(fixture):
    assert 2 == 2


@pytest.mark.skip(reason='this is broken')
def test_skipped():
    pass

@pytest.mark.skipif(sys.platform == 'linux', reason='windows attitude')
def test_skipped_conditionally():
    pass


@pytest.mark.xfail(sys.platform == 'linux', reason='windows attitude')
def test_expected_to_fail():
    assert False

@pytest.mark.xfail(strict=True)
def test_expected_to_fail_but_pass():
    pass

