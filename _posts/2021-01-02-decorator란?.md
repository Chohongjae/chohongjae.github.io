---
title: "decorator란?"
categories: 
  - python
last_modified_at: 2021-01-02T02:00:00+09:00
---
    decorator를 한마디로 얘기하자면, 대상 함수를 wrapping 하고, 이 wrapping 된 함수의 앞뒤에
    추가적으로 꾸며질 구문들을 정의해서 손쉽게 재사용 가능하게 해주는 것이다.
    
```python
def datetime_decorator(func):
    def decorated():
        print datetime.datetime.now()
        func()
        print datetime.datetime.now()
        return decorated

@datetime_decorator
def main():
    print('hi')
```

    decorator 선언된 부분을 자세히 설명하면, 먼저 decorator 역할을 하는 함수를 정의하고,
    이 함수에서 decorator가 적용될 함수를 인자로 받는다.
    python 은 함수의 인자로 다른 함수를 받을 수 있다는 특징을 이용하는 것이다.
    
    decorator 역할을 하는 함수 내부에 또 한번 함수를 선언(nested function)하여
    여기에 추가적인 작업(시간 출력) 을 선언해 주는 것이다.
    nested 함수를 return 해주면 된다.
    마지막으로, main 함수들의 앞에 @를 붙여 decorator 역할을 하는 함수를 호출해 준다.
    
    노파심에 이야기하면, decorator가 꾸며주는 기능이라고 해서 대상 함수의 수행 중간에 끼어드는 구문은 할 수 없다.  
    decorator는 원래 작업의 앞 뒤에 추가적인 작업을 손쉽게 사용 가능하도록 도와주는 역할이라는 것이다.  
    class 형태로도 구현이 가능하다.

```python
class DatetimeDecorator:
    def __init__(self, f):
        self.func = f
    def __call__(self, *args, **kwargs):
        print datetime.datetime.now()
        self.func(*args, **kwargs)
        print datetime.datetime.now()

class MainClass:
    @DatetimeDecorator
    def main_function_1():
        print "MAIN FUNCTION 1 START"
```