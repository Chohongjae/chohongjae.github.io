---
title: "*args와 **kwargs 활용"
categories: 
  - python
last_modified_at: 2021-02-13T02:00:00+09:00
---

## *args
    *args는 *arguments의 줄임말이다.
    이 지시어는 여러 개(몇 개인지 모름)의 인자를 함수로 받고자 할 떄 사용된다.

```python
def test(**kwargs):
    print(args) // 튜플 형태의 (1, 2, 3, 4)
    

if __name__ == "__main__":
    test(1, 2, 3, 4)
```

## **kwargs
    kwargs는 keyword argument의 줄임말로 키워드를 제공한다.
    이 지시어는 key, value 형태의 여러 개(몇 개인지 모르)의 인자를 함수로 받고자 할 떄 사용된다.
    함수 내부에 딕셔너리 형태로 {"키" : "벨류"} 형태로 전달된다.

```python
def test(**kwargs):
    print(kwargs) // {'test': 1, 'test2': 2}

    a = {1: 2}
    b = {2: 3}
    print({**a, **b, **kwargs, "foo": "bar"}) // {1: 2, 2: 3, 'test': 1, 'test2': 2, 'foo': 'bar'} 이런식의 활용도 가능하다.

if __name__ == "__main__":
    test(test=1, test2=2)
```

    