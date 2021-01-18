---
title: "라이브 스터디 10주차"
categories: 
  - LiveStudy
last_modified_at: 2021-01-18T23:00:00+09:00
---

# 목표
## 멀티쓰레드 프로그래밍
- 자바의 멀티쓰레드 프로그래밍에 대해 학습하세요.

## 학습할 것
- [Thread 클래스와 Runnable 인터페이스](#Thread-클래스와-Runnable-인터페이스)
- [쓰레드의 상태](#쓰레드의-상태)
- [쓰레드의 우선순위](#쓰레드의-우선순위)
- [Main 쓰레드](#Main-쓰레드)
- [동기화](#동기화)
- [데드락](#데드락)

### Thread 클래스와 Runnable 인터페이스

### 쓰레드의 상태

### 쓰레드의 우선순위

### Main 쓰레드
    모든 자바 프로그램이 시작되면 하나의 스레드가 즉시 실행되는데 이 스레드는 프로그램이 시작할때 실행되는
    단 하나의 스레드이기 때문에 보통 프로그램의 Main Thread라고 불린다.
    이러한 Main Thread 흐름 안에서 싱글 스레드가 아닌 멀티 스레드 어플리케이션은 필요에 따라
    Main Thread를 통해서 다른 자식 작업 스레드들이 생겨나고 병렬로 코드를 실행할 수 있다.
    또한 Main Thread는 다양한 종료 작업을 수행하기 때문에 종종 실행을 완료하는 마지막 스레드이기도 하다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/mainThread.png" alt=""> {% endraw %}
- [이미지 출처](https://www.geeksforgeeks.org/main-thread-java/)

```text
Thread를 컨트롤하기 위해서는 Thread class에서 currentThread() 메소드를 호출함으로써 해당 Thread에 대한 참조를 얻어야 한다.
``` 
      
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/threadName.png" alt=""> {% endraw %}

    위의 코드를 보면 currentThread()를 호출하여 현재 스레드(코드상에서는 메인 스레드)에 대한 참조를 가져오고
    해당 스레드의 이름을 출력하고 setName()을 통하여 이름을 변경하고 변경이 되는 것을 확인할 수 있다.
    또한 deprecated 된 메소드인 stop()을 사용하여 스레드를 중지하였기 때문에
    "쓰레드가 살아있나요?" 는 출력되지 않는 것을 확인할 수 있다.

    
```text
Main Thread의 기본적인 우선 순위는 5이고 나머지 모든 자식 스레드의 우선 순위는 Main Thread로부터 상속된다.
아래의 예시를 보자.
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210111livestudyweek10/childThread.png" alt=""> {% endraw %}

    Main Thread는 JVM에 의해서 만들어지고 스레드가 만들어지면 프로그램의 main() 메소드의 존재를 확인하고 클래스를 초기화하는 작업을 한다. 
    
### 동기화

### 데드락