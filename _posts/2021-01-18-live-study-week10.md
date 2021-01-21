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
    

### Thread 클래스와 Runnable 인터페이스
    Thread 클래스는 java의 Multi Threading의 가장 중요한 클래스이다.
    Thread는 Thread class 혹은 Runnalbe interface를 통하여 만들 수 있다.
    
### Thread 클래스
    Thread class는 java.lang package에 있다.
    Thread class는 Runnable interface를 구현하고 있고 우리는 Thread 클래스를 사용함으로써 Thread를 만들 수 있다.

- start() : 스레드를 시작하기 위해 사용된다.
- run() : 스레드의 액션을 수행한다. start()메소드를 호출할때 불리게된다.
- sleep() 현재스레드를 특정시간동안 재우기위해서 사용ㄴ된다.
- yield() The yield() method is used to give the hint to the thread scheduler. If the current thread is not doing anything important and any other threads need to be run, they should run. Otherwise, the current thread will continue to run. For more detail, you can visit here.
- join()The join() method belongs to Thread class. The join() method is used when we want one thread to wait until another thread completes its execution. For more detail, you can visit here.
- getName(), setName()This method returns the name of the thread. It is a public and final method. Its return type is String. For more detail, you can visit here.  his method is used to set the name of the thread. It is a public, final and synchronized method. Its return type is void it means it doesn’t return anything. For more detail, you can visit here.
- isDaemon(), setDaemon()This method returns a boolean value either true or false. This method is used to check whether the thread is daemon thread or not. It is a public and final method. Its return type is boolean  This method is used to set a thread as daemon thread. You can mark any user thread as a daemon thread bypassing the value true (setDaemon(true)) in a parameter. If I have a Daemon thread and you can make it user thread bypassing the value false setDaemon(false))
- getPriority(), setPriority()This method returns the priority of the thread. It is a public and final method. Its return type is int. This method is used to set the priority of a thread. Its return type is void it means it doesn’t return anything.


        
        

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
    멀티스레드 환경에서는 스레드들이 병렬적으로 객체를 공유하며 작업하는 경우가 생기게 되는데, 이러한 형태의 통신은
    매우 효율적이지만 Thread 간섭 및 메모리 일관성의 오류가 발생하게 된다.
    만약 공유 객체가 immutable 하거나 모든 Thread들이 해당 자원을 읽기만 한다면 
    공유 객체의 상태는 변경되지않기 때문에 동기화의 필요성을 느끼지 못하지만
    Thread간 공유하는 객체가 서로의 작업에 영향을 미치는 경우에 우리는 공유 객체를 동시에 한 Thread만\
    접근할 수 있도록 동기화해야 한다.
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
    
    위의 코드는 Thread들간 값을 공유하며 서로의 결과에 영향을 미쳐, 아래와 같이 의도한 결과와 다른 결과가 나옴을 확인할 수 있다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/sync.png" alt=""> {% endraw %}

### 동기화 메소드
    동기화 메소드는 Thread들간 간섭 및 메모리 일관성의 오류를 간단하게 해결해준다.
    둘 이상의 Thread들에게 공유되는 자원이라면 동기화 메소드는 모든 읽기, 쓰기 행동을
    해당 동기화 메소드 안에서 이루어지게 한다.
    만약 한 Thread가 동기화 메소드를 호출하는 동안 다른 모든 Thread는 첫 번째 Thread가
    해당 작업에 대해 완료할 때까지 기다려야 한다.
    아래의 예시를 보자.

```java
public class ThreadTest {
    public static void main(String[] args) {
        Line obj = new Line();
        
        Train train1 = new Train(obj);
        Train train2 = new Train(obj);
        
        train1.start();
        train2.start();
    }

    static class Line {
        synchronized public void getLine() {
            for (int i = 0; i < 3; i++) {
                System.out.println(i);
                try {
                    Thread.sleep(400);
                } catch (Exception e) {
                    System.out.println(e);
                }
            }
        }
    }

    static class Train extends Thread {
        Line line;

        Train(Line line) {
            this.line = line;
        }

        @Override
        public void run() {
            line.getLine();
        }
    }
}
```    

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/syncMethod.png" alt=""> {% endraw %}

    만약 동기화 메소드를 사용하지 않고 public void getLine() 만으로 이루어진 메소드를 호출하였다면 결과는
    0
    0
    1
    1
    2
    2 와 같은 식으로 나왔을 것이다.
    
### 동기화 블록
    

    

### 데드락
    데드락은 두개 이상의 스레드가 서로를 기다리면서 무한정 Blocked 상태에 들어간 것을 말한다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118livestudyweek10/deadLock.png" alt=""> {% endraw %}
- [이미지 출처](https://www.fun-coding.org/thread.html)


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

    

### 참조
- [https://javagoal.com/](https://javagoal.com/)
- [https://www.geeksforgeeks.org/method-block-synchronization-java/?ref=lbp](https://www.geeksforgeeks.org/method-block-synchronization-java/?ref=lbp)