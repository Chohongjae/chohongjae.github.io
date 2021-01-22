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

### Thread란?
    Thread란 한마디로 "프로세스 내에서 실행되는 여러 흐름의 단위"라고 할 수 있다.
    자바의 Thread는 JVM에 의해 스케줄되는 실행 단위 코드 블록이다.
    JVM은 Thread는 몇 개 존재하는지, Thread로 실행되는 프로그램 코드의 메모리 위치는 어디인지
    Thread의 상태는 무엇인지, Thread의 우선순위는 얼마인지등을 관리한다.
    

### Thread 클래스와 Runnable 인터페이스
    Multithreading을 사용하면 CPU의 사용을 최대한으로 끌어내어 프로그램의 여러 부분을 동시에 실행할 수 있다.
    Thread는 Thread class의 상속 혹은 Runnalbe interface의 구현을 통하여 만들 수 있다.
    
### Thread 클래스
    Thread class는 java.lang package에 있다.
    Thread class는 Runnable interface를 구현하고 있고, 우리가 Thread 클래스를 상속하여 클래스를 만들고
    run() 메소드를 오버라이딩하여 Threading을 수행할 수 있다.
    오버라이딩한 run() 메소드를 실행하기 위해서는 우리가 생성한 Thread 클래스의 start() 메소드를 호출하면 된다.

```java
class MultithreadingDemo extends Thread {
    
    @Override 
    public void run() 
    { 
        try { 
            System.out.println ("Thread " + Thread.currentThread().getId() + " is running");
        } catch (Exception e) {  
            System.out.println ("Exception is caught"); 
        } 
    } 
} 

public class Multithread { 
    public static void main(String[] args) { 
        int n = 8; // Number of threads 
        for (int i=0; i<n; i++) 
        { 
            MultithreadingDemo object = new MultithreadingDemo(); 
            object.start(); 
        } 
    } 
} 
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/thread.png" alt=""> {% endraw %}

### Runnable 인터페이스
    Thread 클래스와 마찬가지로 Runnable 인터페이스를 구현한 클래스를 생성하고 
    run() 메소드를 오버라이딩하고 start() 메소드를 호출하면 Threading을 수행할 수 있다.
    
    1. Runnable 인터페이스를 구현하는 클래스를 만든다.
    2. run() 메소드를 구현한다.
    3. 해당 클래스의 객체를 만든다.
    4. Thread 클래스의 객체를 Runnable 인터페이스를 구현한 클래스를 생성자에 인자로해서 만든다.
    5. 해당 객체의 start() 메소드를 호출한다.
    
    아래의 예시를 보자.
    
```java
class MultithreadingDemo implements Runnable {

    @Override
    public void run() {
        try {
            System.out.println ("Thread " + Thread.currentThread().getId() + " is running");
        } catch (Exception e) {
            System.out.println ("Exception is caught");
        }
    }
}

public class ThreadTest {
    public static void main(String[] args) {
        int n = 8; // Number of threads
        for (int i=0; i<n; i++)
        {
            Thread object = new Thread(new MultithreadingDemo());
            object.start();
        }
    }
}
```    

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/runnableInterface.png" alt=""> {% endraw %}


### Thread 클래스 VS Runnable 인터페이스
    1. 자바는 다중 상속이 불가능하기 때문에 Thread 클래스를 상속하면 다른 클래스를 상속받을 수 없지만,
    Runnable 인터페이스를 구현하면 다른 클래스를 상속받거나 구현할 수 있다.
    
    2. Thread 클래스를 상속받으면 Runnable 인터페이스에서 사용불가능한 yield(), interrupt() 등 
    내장 메소드등을 사용할 수 있다. 

### Thread 클래스의 메소드         
    - start() : Thread를 시작하기 위해 사용된다.
    - run() : Thread의 액션을 수행한다. start() 메소드를 호출할 때 불리게된다.
    - sleep() 현재 Thread를 특정 시간동안 재우기 위해서 사용된다.
    - yield(): Thread 스케쥴러에게 힌트를 주기 위해서 사용된다.
    - join(): 다른 Thread의 작업이 끝날때까지 해당 Thread를 대기시키고 싶을 때 사용된다.
    - getName(), setName(): thread의 네임을 가져오고 설정할 수 있다.
    - isDaemon(), setDaemon(): thread가 데몬 Thread인지 아닌지를 확인하는 boolean 값과 데몬으로 설정할 수 있는 메소드이다.
    - getPriority(), setPriority(): thread의 우선순위를 가져오고 우선순위를 변경할 수 있다.
    

### 쓰레드의 상태
    각각의 Thread는 Thread scheduler에 의한 상태 변화를 통해 아래 그림과 같은 LifeCycle을 갖는다. 

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/state.png" alt=""> {% endraw %}
- [이미지 출처](https://javagoal.com/thread-life-cycle-in-java/)

### NEW
    new 연산자를 통해 Thread 객체를 생성했을때 Thread가 갖는 첫번째 상태이다.
    NEW 상태에서 Thread는 살아있다고 고려되지 않고, Thread의 start() 메소드의 호출이 있어야 NEW 상태를 벗어나
    RUNNABLE 상태로 이동하며 살아있다고 판단된다.
    한 번 NEW 상태를 벗어난 Thread는 다시 되돌아올 수 없다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/newState.png" alt=""> {% endraw %}
- [이미지 출처](https://javagoal.com/thread-life-cycle-in-java/)    

### RUNNABLE
    start() 메소드가 호출된 스레드는 NEW 상태에서 RUNNABLE 상태로 이동하게 된다.
    Thread Scheduler는 RUNNABLE Thread Pool에 있는 Thread들을 대기시킬지 혹은 CPU 점유를 허락할지를 결정하게 된다.
    RUNNABLE 상태에 있는 Thread들은 살아있다고 간주되고, CPU를 점유할 자격이 있기 때문에
    RUNNABLE 이라는 범주안에서 CPU를 점유하면 실행 중, 그렇지 않으면 실행대기 상태로 나뉘게 된다. 
    
    Thread Scheduler는 각각의 Thread들에게 시간을 부여하고 해당 시간을 모두 사용하면 다른 Thread들이 CPU 사용에 대한 기회를 갖게된다. 
    즉 시간을 모두 사용한 Thread는 RUNNABLE Pool에서 실행을 대기하게 되고 CPU를 점유한 Thread는 RUNNING 상태를 갖게 되는 것이다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/runnable.png" alt=""> {% endraw %}
- [이미지 출처](https://javagoal.com/thread-life-cycle-in-java/)
     
### RUNNING
    RUNNING 상태는 실제로 존재하는 것이 아니라 RUNNABLE 상태의 부분으로써 Runnable Thread pool에 있는
    쓰레드가 CPU를 점유하였을때의 상태를 의미한다.
    
### TIMED WAITING
    RUNNABLE 상태에 있는 Thread는 TIMED WATING 상태로 특정 시간동안 혹은 알람을 받을 때까지 대기할 수 있고,
    그 동안 Thread Scheduler는 CPU를 점유할 준비가 되어있는 다른 Thread를 선택한다.
    
    Thread를 TIMED WAITING 상태로 만드는 메소드는 time 파라미터와 함께 sleep(time), wait(timeout),
    join(timeout), parkNanos(), parkUntil() 등이 있다.
    
### WAITING    
    어느 Thread가 WAITING 상태에 있음은, 다른 이유로 다른 Thread가 더 우선순위 있음을 의미한다.
    wait(), join(), park()메소드등으로 Thread를 WAITING 상태로 만들 수 있고,
    TIMED WAITING과의 차이점은 TIMED WAITING에 있는 Thread는 일정 시간이 지나면 다시 실행가능상태가 되지만 
    WAITING에 있는 Thread는 영원히 대기하며 쓰레드를 깨우기 전까지 실행되지 않는다.
    
### BLOCKED
    BLOCKED 상태에있는 Thread는 살아있다고 고려되지만 작업을 수행할 자격이 없이 Block된 상태를 말한다.
    
    예를 들어 어느한 Thread가 I/O 작업을 기다리고 있지만 I/O 작업이 이미 다른 스레드에 의해 사용되고 있을 때
    해당 Thread는 사용되고 있는 I/O 작업을 기다려야하며 BLOCKED 상태에 있게 된다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/blocked.png" alt=""> {% endraw %}
- [이미지 출처](https://javagoal.com/thread-life-cycle-in-java/)

### TERMINATED
    여러가지 이류로 Thread가 종료된, 죽은 상태를 의미한다.
    해당 상태는 CPU를 점유할 수 없는데 작업 실행을 완료하였거나 segmentation fault 혹은 실행 중 오류등에 의해서 종료될 수 있다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/getState.png" alt=""> {% endraw %}
- [이미지 출처](https://javagoal.com/thread-life-cycle-in-java/)


    이처럼 getState() 메소드를 통해 Thread의 상태를 알 수 있다. 
 
        
    
### 쓰레드의 우선순위
    MultiThreading 환경에서 각각의 Thread는 우선순위를 가지고 있다.
    이러한 Thread의 우선순위는 스케쥴링 알고리즘 중에서 "우선순위 방식, 우선순위 알고리즘"에서
    Thread Scheduler에게 Thread 실행의 순서를 결정하는 지표가 된다.
    
    쉽게 말해서 Thread Scheduler는 RUNNABLE Queue에서 CPU 점유를 기다리고있는 Thread들 중에서
    더 우선 순위가 높은 Thread가 생성되면 실행중인 Thread를 실행가능 상태로 만들고 가장 우선순위가 높은
    Tread에게 CPU를 넘기는 작업을 한다.
    
    계속해서 우선순위가 낮아 CPU를 할당받지 못하는 Thread는 기아상태가 되는데, 일정시간 CPU를 할당받지
    못하면 우선순위를 높여 실행될 수 있도록 만드는데 이러한 방법을 에이징이라고 한다.
    

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
    멀티스레드 환경에서는 스레드들이 병렬적으로 "객체"를 공유하며 작업하는 경우가 생기게 되는데,
    이러한 형태의 통신은 매우 효율적이지만 Thread 간섭 및 메모리 일관성의 오류가 발생하게 된다.
    만약 공유 객체가 immutable 하거나 모든 Thread들이 해당 자원을 읽기만 한다면 공유 객체의 상태는 변경되지않기 때문에 동기화의 필요성을 느끼지 못하지만
    Thread간 공유하는 "객체"가 서로의 작업에 영향을 미치는 경우에 우리는 공유 객체를 동시에 한 Thread만 접근할 수 있도록 동기화해야 한다.
    이를 방지하는 방법으로 자바는 동기화 메소드와 동기화 블록을 제공한다.
    
    우선 왜 동기화가 필요한지 아래의 예시를 보자.
    
```java
public class ThreadTest {
    private int value = 0;

    public void setValue(int value) {
        this.value = value;
        try {
            Thread.sleep(2000);
        } catch (Exception e) {
        }
        System.out.println(Thread.currentThread().getName() + "의 Value 값은 " + this.value + "입니다.");

    }

    public static void main(String args[]) {
        ThreadTest shareTread = new ThreadTest();
        Thread thred1 = new Thread(() -> {
            shareTread.setValue(100);

        });

        Thread thred2 = new Thread(() -> {
            shareTread.setValue(10);
        });
        thred1.setName("스레드 1");
        thred2.setName("스레드 2");
        thred1.start();
        thred2.start();
    }
}
```
    
    위의 코드는 thread1의 value는 100을 의도하였지만 Thread들간 값을 공유하며 서로의 결과에 영향을 미쳐, 
    아래와 같이 의도한 결과와 다른 결과가 나옴을 확인할 수 있다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/sync.png" alt=""> {% endraw %}
    
    이렇게 Thread간 공유하는 객체에 접근을 동기화 하기 위해서 상호 배제를 이루어야 하는데
    상호 배제는 자바에서 Thread 동기화를 이루는 가장 간단한 방법이다.
    상호 배제를 구현하는 방법에는 2가지가 있는데 우선 Lock과 동기화 메소드에 대해 알아보자.

### 자바에서의 Lock
    자바에서 모든 객체는 Lock이라는 개념을 가지고 있다. 여러 Thread가 공유 자원에 접근할 때
    공유 자원에 대한 Lock을 획득하려하고, 어느 한 Thread가 Lock을 획득해 해당 자원에 대한
    수행을 실행할 떄 나머지 Thread들은 해당 Thread가 작업을 완료해 Lock을 놓을때까지 대기하게 된다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/sync2.png" alt=""> {% endraw %}
- [이미지 출처](https://javagoal.com/synchronization-in-java/)  
    
### 동기화 메소드
    동기화 메소드는 Thread들간 간섭 및 메모리 일관성의 오류를 간단하게 해결해준다.
    만약 0.1초라도 먼저 Lock을 점유한(동기화 메소드에 접근한) 한 Thread가 동기화 메소드를 호출하는 동안
    다른 모든 Thread는 첫 번째 Thread가 해당 작업에 대해 완료해 Lock을 방출할 때까지 공유 객체의 실행을 기다려야 한다.
    
    아래의 예시를 보자.

```java
public class ThreadTest {
    public synchronized void getLine() {
        for (int i = 0; i < 3; i++) {
            System.out.println(i);
            try {
                Thread.sleep(400);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        ThreadTest obj = new ThreadTest();

        new Thread(obj::getLine).start();
        new Thread(obj::getLine).start();
    }
}
```    

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/syncMethod.png" alt=""> {% endraw %}

    위와 같이 함수에 synchronized를 걸면 그 함수가 포함된 해당 객체(this)에, 자신이 포함된 객체에 lock을 거는 것이다.
    만약 동기화 메소드를 사용하지 않고 public void getLine() 만으로 이루어진 메소드를 호출하였다면 어떻게 되었을까?
    
    아래의 결과를 보자.
    
```java
public class ThreadTest {
    public void getLine() {
        for (int i = 0; i < 3; i++) {
            System.out.println(i);
            try {
                Thread.sleep(400);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        ThreadTest obj = new ThreadTest();

        new Thread(obj::getLine).start();
        new Thread(obj::getLine).start();
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/syncMethod2.png" alt=""> {% endraw %}

    또한 동기화 메소드는 인스턴스 메소드 동기화와 스태틱 메소드 동기화 두 가지로 나뉜다.
    
    인스턴스 메소드의 동기화는 이 메소드를 가진 인스턴스(객체)를 기준으로 이루어진다.
    그렇기 때문에 한 시점에 여러 Thread들 중 오직 하나의 Thread만이 동기화된 인스턴스 메소드를 실행할 수 있고
    해당 객체의 메소드를 실행하려는 다른 Thread들은 대기하게 된다.
    
    따라서 만일 두개의 인스턴스(객체)가 있고, 각 Thread가 서로 다른 각각의 객체의 동기화된 메소드에 접근해도
    병렬적으로 실행이 될 수 있는 것이다.
    
    아래의 예시를 보자.
    
```java
public class ThreadTest {
    public synchronized void getLine() {
        for (int i = 0; i < 3; i++) {
            System.out.println(i);
            try {
                Thread.sleep(400);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        ThreadTest obj = new ThreadTest();
        ThreadTest obj2 = new ThreadTest();


        new Thread(obj::getLine).start();
        new Thread(obj2::getLine).start();
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/instanceMethod.png" alt=""> {% endraw %}

    스태틱 메소드 동기화 역시 선언문의 synchronized 키워드가 이 메소드의 동기화를 의미한다.
    반면에 스태틱 메소드 동기화는 이 메소드를 가진 클래스의 "클래스 객체"를 기준으로 이루어진다.
    JVM 안에 클래스 객체는 클래스 당 하나만 존재할 수 있으므로, 같은 클래스에 대해서는 오직 한 쓰레드만
    동기화된 스태틱 메소드를 실행할 수 있다.
    
    아래의 예시를 보자.

```java
public class ThreadTest {
    public static synchronized void getLine() {
        for (int i = 0; i < 3; i++) {
            System.out.println(i);
            try {
                Thread.sleep(400);
            } catch (Exception e) {
                System.out.println(e);
            }
        }
    }

    public static void main(String[] args) {
        new Thread(ThreadTest::getLine).start();
        new Thread(ThreadTest::getLine).start();
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/syncMethod.png" alt=""> {% endraw %}
    
### 동기화 블록
    만약 우리가 코드의 메소드 전체가 아니라 메소드의 일부만 동기화하고 싶다면 동기화 블록을 사용할 수 있다.
    인스턴스 동기화 메소드와 마찬가지로 공유되는 객체에 대한 동기화 블록은 어느 한 스레드만 동시에 들어올 수 있다.
     
    쉽게 말해서 동기화 블록 혹은 메소드에 어느 한 Thread가 들어오면, 해당 Thread는 Lock을 획득하게 되고,
    해당 동기화 블록, 메소드에 들어가려는 모든 Thread들은 해당 Thread의 작업이 "동기화 블록, 메소드에서" 완료되어 
    Lock의 소유를 포기할때까지 기다리게 되어 Race Condition을 예방할 수 있게 된다.
    
    동기화 메소드와의 차이점은 메소드 전체가 아니라 일부 영역만 동기화할 수 있다는 것이다.
    
```java
public void add(int value){
    // 동기화 블록을 벗어난 영역
    synchronized(this){
       this.count += value;   
    }
}
```

    위의 코드처럼 메소드안에 특정 영역만 synchronized 키워드를 사용하여 동기화할 수 있다.
    동기화 블록의 괄호 안에 this를 전달받고 있는데 this는 해당 메소드가 호출된 객체를 의미한다.
    이 객체를 모니터 객체라고 하는데 this를 전달하면 인스턴스 동기화 메소드와 같이
    여러 Thread에서 한 객체의 메소드에 한 Thread만 접근할 수 있다.
    
    즉 아래의 두 코드는 같은 기능을 수행한다.

```java
public class MyClass {

    public synchronized void log1(String msg1, String msg2){
       log.writeln(msg1);
       log.writeln(msg2);
    }

    public void log2(String msg1, String msg2){
       synchronized(this){
          log.writeln(msg1);
          log.writeln(msg2);
       }
    }
}
```
    
### 데드락
    데드락은 두개 이상의 스레드가 서로를 기다리면서 무한정 Blocked 상태에 들어간 것을 말한다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/deadLock.png" alt=""> {% endraw %}
- [이미지 출처](https://www.fun-coding.org/thread.html)

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/deadLock3.png" alt=""> {% endraw %}
- [이미지 출처](https://www.geeksforgeeks.org/deadlock-in-java-multithreading/)


    자바 MultiThreading 프로그램에서는 위에서 설명한 synchronized 키워드가 lock, monitor 등을
    기다리는 동안 thread를 block 하기 때문에 교착 상태가 발생할 수 있다.
    아래의 예시를 보자.
    
```java
public class ThreadTest {
    public static Object Lock1 = new Object();
    public static Object Lock2 = new Object();

    public static void main(String args[]) {
        ThreadDemo1 T1 = new ThreadDemo1();
        ThreadDemo2 T2 = new ThreadDemo2();
        T1.start();
        T2.start();
    }

    private static class ThreadDemo1 extends Thread {
        public void run() {
            synchronized (Lock1) {
                System.out.println("Thread 1: Holding lock 1...");

                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                }
                System.out.println("Thread 1: Waiting for lock 2...");

                synchronized (Lock2) {
                    System.out.println("Thread 1: Holding lock 1 & 2...");
                }
            }
        }
    }

    private static class ThreadDemo2 extends Thread {
        public void run() {
            synchronized (Lock2) {
                System.out.println("Thread 2: Holding lock 2...");

                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                }
                System.out.println("Thread 2: Waiting for lock 1...");

                synchronized (Lock1) {
                    System.out.println("Thread 2: Holding lock 1 & 2...");
                }
            }
        }
    }
}
```
    
    위와 같이 서로가 사용하는 자원에 접근하려하면 아래와 같이 교착상태가 발생하여 어느 Thread가 잠금을 해제 할 때까지 
    더이상 프로그램이 진행되지 않음을 확인할 수 있다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/deadLock2.png" alt=""> {% endraw %}

    터미널에서 Thread dump를 사용하여 데드락을 발견할 수 있는데 해당 구현은 확실하게 숙지하고 다시 작성하도록 하겠다.

### 데드락 회피하는 방법
    우리는 아래의 몇가지 방법을 통해 데드락을 피할 가능성을 높일 수 있다.
    
    1. 중첩 Lock을 피한다. : 데드락의 주요 이유로 여러 Thread에게 Lock을 주었을 때 발생하므로, 이미 한 Thread에 Lock
    을 주었다면 다른 Thread들에게 Lock을 주는 것을 피해야 한다.
    2. 불필요한 Lock을 피한다. : Lock을 필요로하는 Thread에게만 주어야지, 불필요하게 Lock을 제공해서는 안된다.
    3. join() 메소드를 사용해 Thread의 수행을 잠시 중지시킨다.

### 참조
- [https://javagoal.com/](https://javagoal.com/)
- [https://www.geeksforgeeks.org/method-block-synchronization-java/?ref=lbp](https://www.geeksforgeeks.org/method-block-synchronization-java/?ref=lbp)