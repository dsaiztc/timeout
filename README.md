# timeout
Set a maximum execution time for your functions with a simple decorator.

## Motivation
There are some use cases where you might need to limit the amount of time required by a specific function.

- Maybe you have a limited amount of time to execute a task (some said AWS Lambda?)
- Or maybe you just want to make sure tasks don't get *blocked* by some external resource (like a *busy* database)

Those were basically the problem I wanted to get resolved. And that's why I embed some *collective intelligence* (a.k.a. StarOverflow) into this package.

### AWS Lambda
[AWS Lambda](https://aws.amazon.com/lambda/) is awesome, but still has a maximum execution time of **5 min**. That's usually enough for the kind of tasks it was conceived, but I needed a *fail-safe* mechanism.

You always have the option to check for the remaining time with `context.get_remaining_time_in_millis()`, but that might not be applicable in every situation.

## Install
This package uses the `concurrent.futures` package available in the standard library of **Python 3.x**. For **Python 2.6 and 2.7** users please install the backport https://github.com/agronholm/pythonfutures.

```
$ python setup.py install
```

## Use
```python
from timeout import timeout, TimeoutError

@timeout(60)
def monstrous_task():
    """This task should take less than 1 minute, otherwise the execution will be stopped"""
    pass

def main():
    try:
        monstrous_task()
    except TimeoutError:
        print('Task timed out (> 1min)')
```
