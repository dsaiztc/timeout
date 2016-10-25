from timeout import timeout, TimeoutError
import time
import pytest


def test_timeout():
    @timeout(1)
    def my_task():
        time.sleep(1.5)

    with pytest.raises(TimeoutError) as excinfo:
        my_task()


def test_tryexcept():
    @timeout(1)
    def exception_catched():
        try:
            time.sleep(1.5)
        except TimeoutError:
            print('TimeoutError catched within the function')
            assert False

    try:
        exception_catched()
    except TimeoutError:
        print('TimeoutError catched outside the function')
        assert True
