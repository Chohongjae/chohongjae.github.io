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
    MultiThreading 환경에서 각각의 Thread는 우선순위를 가지고 있다.
    이러한 Thread의 우선순위는 Thread Scheduler에게 Thread 실행의 순서를 결정하는 지표가 되는데
    쉽게 말해서 Thread Scheduler는 RUNNABLE Queue에서 CPU 점유를 기다리고있는 Thread들중에서
    가장 우선순위가 높은 스레드에게 CPU를 사용하도록 결정하는 것이다. 


```text
우선순위는 단순히 JVM혹은 유저로부터 할당된 숫자일뿐이다.
이러한 숫자는 우선순위를 의미하고 JVM에 의해서 가장 먼저 만들어진 Main Thread의 기본적인 우선 순위는 5인데
여느 다른 스레드가 생성될 때 해당 스레드는 항상 Main Thread의 자식 스레드이기 때문에 나머지 모든 자식 스레드의
우선 순위는 Main Thread로부터 상속된다.

아래의 예시를 보자.
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/childThread.png" alt=""> {% endraw %}

    위의 예시를 보면 우리는 setPriority(int value) 메소드를 통해 Thread에게 우선순의를 부여할 수 있고,
    getPriority() 메소드를 통해 Thread의 우선순의를 가져올 수 있다.
    
    위에서 확인할 수 있는
    public static int MIN_PRIORITY는 Thread가 가질 수 있는 최소의 값이고 값은 1이다.
    public static int NORM_PRIORITY는 JVM에 의해서 생성된 Main Thread에게 정해지는 기본적인 우선순위 값이고 기본값은 5이다.
    public static int MAX_PRIORITY는 Thread가 가질 수 있는 최대의 값이고 값은 10이다.
    
    Thread가 가질 수 있는 값의 범위는 1과 10사이이고 만약 해당 범위를 벗어난다면 IllegalArgumentException Exception이 발생하게 된다.


### Main 쓰레드
    알다시피 모든 자바 프로그램은 "public static void main"이라는 Main Method를 가지고 있다. 
    이러한 Main Method는 프로그램 실행의 진입점인데 JVM이 진입점을 통해 자바 프로그램을 실행할때
    JVM은 하나의 스레드를 생성하고, 실행시키는데 이 스레드는 프로그램이 시작할때 실행되는 단 하나의 스레드이기 때문에
    보통 프로그램의 Main Thread라고 불린다.
    Main Thread는 다른 Thread 생성 여부에 관계없이 존재하고 JVM은 각 Thread들에 스택을 할당해
    각각의 스택에 데이터를 저장할 수 있게 한다.
    
    이러한 Main Thread 흐름 안에서 싱글 스레드가 아닌 멀티 스레드 어플리케이션은 필요에 따라
    Main Thread를 "통해서" 다른 자식 작업 스레드들이 생겨나고 병렬로 코드를 실행할 수 있다.
    또한 Main Thread는 다양한 종료 작업을 수행하기 때문에 실행을 완료하는 마지막 스레드이고
    Main Thread가 종료되면 프로그램 실행은 종료된다.
      
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/mainThread.png" alt=""> {% endraw %}
- [이미지 출처](https://www.geeksforgeeks.org/main-thread-java/)

```text
JVM에 의해서 만들어진 Thread를 우리는 컨트롤 할 수 있는데 Thread를 컨트롤하기 위해서는 Thread class에서
currentThread() 메소드를 호출함으로써 해당 Thread에 대한 참조를 얻어야 한다.
``` 
      
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/threadName.png" alt=""> {% endraw %}

    위의 코드를 보면 currentThread()를 호출하여 현재 스레드(코드상에서는 메인 스레드)에 대한 참조를 가져오고
    해당 스레드의 이름을 출력하고 setName()을 통하여 이름을 변경하고 변경이 되는 것을 확인할 수 있다.
    또한 deprecated 된 메소드인 stop()을 사용하여 스레드를 중지하였기 때문에
    "쓰레드가 살아있나요?" 는 출력되지 않는 것을 확인할 수 있다.

    
### 동기화

### 데드락