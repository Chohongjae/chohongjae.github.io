---
title: "for문의 for-else 사용법"
categories: 
  - python
last_modified_at: 2021-01-02T03:00:00+09:00
---

    기본적으로 for문 에 break 가 포함 되어 있을때 사용가능한데 for문을 순회 하던 중
    break를 만나면 for문을 빠져나오는건 일반적인 언어와 같지만 break 문을 만나지 않았다면
    for문 종료 이후 else 문이 실행된다.

```python
for a in range(0,5):
    print(a)
    if a == 6:
        break;
else:
    print ("else statement is called")
```
    
    실행결과 
    0
    1
    2
    3
    4
    else statement is called
    
    위의 경우 처럼 for else 문을 사용한다면 flag 같은 변수를 사용하지 않아도 되서 코드가 훨씬 깔끔해 진다.
    else의 들여쓰기는 for와 일치해야 한다.

- http://www.mukgee.com/?p=93