from concurrent.futures import ThreadPoolExecutor, TimeoutError
import functools

def timeout(timeout_sec):
    """Timeout decorator, parameter in seconds."""
    def timeout_decorator(item):
        """Wrap the original function."""
        @functools.wraps(item)
        def func_wrapper(*args, **kwargs):
            """Closure for function."""
            executor = ThreadPoolExecutor(max_workers=1)
            future = executor.submit(item, *args, **kwargs)
            return future.result(timeout=timeout_sec)
        return func_wrapper
    return timeout_decorator
