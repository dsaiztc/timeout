from timeout import timeout, TimeoutError
import time
import pytest

def test_timeout():
    @timeout(1)
    def my_task():
        time.sleep(1.5)

    with pytest.raises(TimeoutError) as excinfo:
        my_task()
