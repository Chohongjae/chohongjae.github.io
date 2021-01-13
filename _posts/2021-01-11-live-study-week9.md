---
title: "라이브 스터디 9주차"
categories: 
  - LiveStudy
last_modified_at: 2021-01-11T23:00:00+09:00
---

# 목표
## 예외 처리
- 자바의 예외 처리에 대해 학습하세요.

## 학습할 것
- [자바에서 예외 처리 방법 (try, catch, throw, throws, finally)](#자바에서-예외-처리-방법-(try,-catch,-throw,-throws,-finally))
- [자바가 제공하는 예외 계층 구조](#자바가-제공하는-예외-계층-구조)
- [Exception과 Error의 차이는?](#Exception과-Error의-차이는?)
- [RuntimeException과 RE가 아닌 것의 차이는?](#RuntimeException과-RE가-아닌-것의-차이는?)
- [커스텀한 예외 만드는 방법](#커스텀한-예외-만드는-방법)

### 자바에서 예외 처리 방법 (try, catch, throw, throws, finally)
    자바에서 예외를 처리할 때 기본이 되는 것은 try~catch~finally 구문이다.
        
```java
try {
    // Exception이 발생할 수 있는 로직의 처리
} catch (SomeException e) {
    // SomeException 예외를 catch한 경우의 처리
} finally {
    // try~catch 블록을 종료할 때에 반드시 실행해야 하는 처리
    // 예외가 발생하든 안하든 실행된다.
}
```

    일반적으로 try 블록 안에 작성하는 처리는 적을수록 좋다.
    너무 장대한 처리를 try 블록 안에 넣어버리면 catch 블록에서 포착한 예외가
    어디에서 발생한 것인지 코드에서 찾기가 어렵게 되기 때문이다.

```text
finally 블록은 스트림이나 데이터베이스 접속처럼 사용 후에 반드시 해제해야 하는
리소스의 객체를 사용할 경우에 자주 이용된다.
시스템에서 취급하는 리소스의 양에는 제한이 있기 때문에 리소스를 해제하지 않고 반복해서 
실행하다 보면 시스템은 언젠가 리소스가 고갈되어 정지해 버린다.
```
    
```java
try {
    // SomeException 예외가 발생하는 코드를 포함하는 처리
} catch (SomeException | ClassNotFoundException | IllegalAccessException ex) {
    // SomeException, ClassNotFoundException, IllegalAccessException 예외를 catch한 경우의 처리
}
```

    또한 여러 예외가 발생하는 경우 여러개의 catch 블록을 작성하는 것도 가능하지만
    자바 7에서 도입된 "다중 캐치"를 이용하여 위에서 작성한 것과 같이 복잡한 catch 블록의 작성을 공통으로 처리할 수 있다.
    위에서 작성한 어느 예외가 발생해도 동일한 catch 블록에서 오류 처리를 실시하게 된다.


### try~with~resources
    만약 프로그램을 작성하면서 중복으로 여러 리소스를 사용하는 경우 try~catch~finally 블록에서 상당히 많은 중복이 발생할 수 있다.
    예를 들어 아래의 코드를 보자.


```java
FileInputStream fis = null;
try{
     fis = new FileInputStream("");
}catch(IOException e){
    // 예외처리
}finally {
    try {
        fis.close();
    }catch (IOException ie){
        
    }
}
```
    
    위와 같이 fis.close() 메소드도 IOException을 던지는 경우 finally 구문에서도 try~catch 구문을 작성해야하는 번거로움이 있다.
    저렇게 코드를 작성할 경우 개발자가 실수하기 쉽기 떄문에 자바 7부터 try~with~resources 구문이 도입되었다.
    아래의 코드를 보자.
    
```java
try (InputStream is = Files.newInputStream(path);
      OutputStream os = new FileOutputStream(toFile)) {
    // is, os 변수 사용 가능
} catch(IOException ex) {
    // 예외 처리
}
```
    
    이것만으로 해당 try catch 구문이 끝나면 InputStream과 OutputStream의 리소스 해제에 대한 처리가 끝이나게 된다.
    자바 7부터 InputStream 등의 리소스를 취급하는 클래스는 java.lang.AutoClosable 인터페이스
    또는 java.io.Closable 인터페이스를 구현하도록 되었는데 try 블록의 시작 시 () 안에
    AutoClosable 인터페이스의 구현 클래스를 선언해두면 해당 try~catch 블록의 종료 시의 처리에서
    실시할 close 메서드를 자동으로 호출하게 된다.
    
***즉 try에서 선언된 객체가 AutoCloseable 인터페이스를 구현하였다면 java는 try 구문이 종료될 때
(정상적으로 구문이 끝났을 때 혹은 예외가 발생했을 때 모두) 선언한 AutoCloseable 를 구현한 모든 객체의
close() 메소드를 호출해주는 것이다.***
    
### throw
    throw는 Exception을 강제로 "발생"시킬 때 사용하는 키워드이다.
    만약 어떤 연산을 하다가 예상치 못한 일이 발생했을 떄 Exception을 발생시켜 예외가 처리될 수 있도록 하는 것이다.
    throw로 발생시킨 Exception을 try~catch를 통해 잡지 못하면 프로그램은 중지된다.
    아래의 코드를 보자.
    
```java
public class Test {
    public static void main(String[] args) {
        Test test = new Test();
        test.throwException();
    }

    public void throwException() {
        try {
            throw new IllegalArgumentException("exception");
        } catch (IllegalArgumentException e) {
            e.printStackTrace();
        }
    }
}
```

    위에서 작성한 코드와 같이 throwException() 메소드에서 
    throw new IllegalArgumentException("exception") 로 IllegalArgumentException 을 발생시키고 있고
    해당 Exception을 try ~ catch를 통해 예외를 처리하고 있다.
     

### throws
    메서드 내부에서 예외가 발생했을 때 예외를 try - catch 문으로 잡아서 처리할 수 있지만
    경우에 따라서 현재 메서드를 호출한 메서드로 예외를 떠넘길 수 있다.
    
    예외를 떠넘기는 방법은 throws 키워드와 에러클래스를 메서드 시그니처에 붙여주면 된다.
    만약 떠넘겨야할 예외 종류가 여러개라면 쉼표(,) 를 기준으로 나열하여 선언하면 된다.
    
    해당 키워드를 통해 현재 메서드를 호출한 메서드로 예외를 떠넘길뿐만아니라 
    '현재 메서드를 사용하면 이와 같은 예외가 발생한다'라는 정보를 개발자는 알 수 있게 된다.
    아래의 코드를 보자.
    

```java
public class Test {
    public void throwException() throws IllegalAccessException {
        throw new IllegalAccessException("hi");

    }

    public void test() throws IllegalAccessException {
        throwException();
    }

    public static void main(String[] args) {
        Test test = new Test();
        try {
            test.test();
        } catch (IllegalAccessException a) {
            System.out.println("hi");
        }
    }
}
```

    위에서 작성한 코드와 같이 throwException() 메소드에서 exception이 발생하면
    throws IllegalAccessException 를 통해 throwException() 메소드를 호출한
    test() 메소드로 Exception을 떠넘기고 있고 test() 메소드 또한
    throws IllegalAccessException 를 통해 test() 메소드를 호출한
    main() 메소드로 Exception에 대한 처리를 떠넘기고 있다.
    
    만약 main() 메소드가 해당 Exception을 처리하지 않으면 Exception은 JVM까지 올라가 프로그램이 중지되는 것이다.

### 자바가 제공하는 예외 계층 구조
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210111livestudyweek9/예외계층구조.png" alt=""> {% endraw %}
- [이미지 출처](https://reference-m1.tistory.com/246)
    
    
    예외의 계층 구조를 알아보기 전에 우선 가장 상위에 있는 Throwable Class 에 대해 알아보자.
    
    
### Throwable Class
    대표적인 클래스인 Exception, Error, RuntimeException 클래스는 java.lang.Throwable 클래스의 서브 클래스로 작성되어 있다.
    즉 Throwable 클래스는 자바의 모든 오류 및 예외의 슈퍼 클래스다.
    이 클래스의 인스턴스 혹은 서브 클래스의 객체만 JVM에 의해 예외 혹은 Error로 인식될 수 있다.    

```text
자바에서 예외는 checked와 unchecked 두 가지로 나눌 수 있다.
```

### checked Exception
    RuntimeException 및 RuntimeException의 하위 클래스들을 제외한
    Exception의 하위 클래스, Throwable 및 Throwable의 서브 클래스들이 checked Exception에 속한다.
    
    checked Exception 클래스들은 복구가 가능한 예외들이기 때문에
    반드시 catch 문으로 예외를 잡거나, throws로 예외 처리를 떠넘겨야 한다. 
    이렇게 예외를 처리하지 않으면 컴파일 단계에서 확인이 가능하기 때문에 컴파일 에러가 발생한다.
    또한 checked Exception은 Exception 발생 시 트랜잭션을 rollback하지 않는다.
    
    
### unchecked Exception
    RuntimeException을 상속받은 하위 클래스들이 이에 해당된다.
    unchecked Exception은 명시적으로 예외처리를 강요받지 않아서 따로 catch 문으로 예외를 잡거나
    throws를 사용하여 에러 처리를 떠넘기지 않아도 컴파일 단계에서 에러가 발생하지 않고
    Exception 발생 시 실행 단계에서 확인이 가능하다.
    
    즉 프로그램에 오류가 있을 때 발생하도록 의도된 것이다.
    unchecked Exception Exception 발생시 트랜잭션을 rollback 한다.

    
### Exception과 Error의 차이는?
    자바에서는 예외를 크게 세 가지 종류로 나눌 수 있는데 그 중에서 우선 Exception과 Error의 차이에 대해 알아보자.

### Exception
    우선 Exception 클래스는 주로 프로그램 작성 시에 "예상할 수 있는" 비정상 상태를 통지하기 위해서 사용한다.
    Exception을 사용하면 예상되는 비정상 상태에 "대응하는 처리가 있는지" "컴파일 시에 체크"할 수 있기 때문에 견고한 애플리케이션을 만들 수 있다.
    Exception은 프로그램에서 catch 해서 처리하거나, 상위의 호출원에 대해 예외를 throw 떠넘기는 것이 필수다.
    만약 둘 중 어느 것도 행하지 않으면 컴파일 오류가 발생한다.

```java
1.
public List<String> readFile() throws IOException {
    // Exception이 발생할 수 있는 파일을 읽어들이는 로직
}

2.
public List<String> readFile() {
    try {
        // Exception이 발생할 수 있는 파일을 읽어들이는 로직
    } catch (IOException e) {
        e.printStackTrace();
    }
}
```
    
    1번 메소드와 같이 예외가 발생할 수 있는 로직이 들어가면 자신을 호출한 상위 메소드로 throws를 통해 예외를 떠넘기거나
    2번 메소드와 같이 해당 예외를 직접 catch 하여 처리하여야 한다.
    
    Exception 클래스를 계승한 예외의 예로는 IOExeption, SQLExeption 등이 있다.

### Error
    예외와는 달리 시스템의 동작을 계속할 수 없는, 일반적인 애플리케이션에서는 포착해서는 안되는 중대한 문제를 나타내는 클래스다.
    자바의 예외 메커니즘의 관점에서 볼 때 Error는 RuntimeException과 비슷하여 catch 블록도, throws 절도 기술할 필요가 없다.
    그러나 RuntimeException과 같은 의미로 기술할 필요가 없는 것이 아닌,
    "포착해야 할 것이 아닌, 시스템의 동작을 계속할 수 없는 상태" 이기 때문에
    애플리케이션이 비정상의 상태에 빠져 신속하게 프로그램을 종료시켜야 하는 상황인 것이다.
    
    예를 들어 유명한 Error 중에 하나로 OutOfMemoryError 클래스가 있는데 이것은 자바가 사용하는
    메모리가 부족하거나 혹은 스레드를 작성할 수 없을 때 등등 발생한다.
    이러한 오류는 로그 출력 조차도 할 수 없는 상태이기 때문에 프로그램에서 포착하여 처리할 수 있는 것이 아닌 것이다. 
    
### RuntimeException과 RE가 아닌 것의 차이는?
    RuntimeException 클래스는 "실행 시" 예외를 나타내는 클래스로써 이 클래스를 계승한 예외는
    프로그램 안에서 반드시 catch 를 통하여 예외를 포착하거나 throws로 떠넘길 필요가 없다.
    
    즉 RuntimeException과 RE가 아닌 것의 차이는 컴파일시의 예외 처리 체크를 하느냐 안 하느냐의 차이다.
    컴파일러는 RuntimeException을 제외한 모든 Exception 클래스들을 컴파일시 예외처리( try / catch )를 했는지 반드시 확인 한다.
    하지만 RuntimeException 클래스 부류가 발생했을 때는 ( try / catch )를 사용하지 않더라도 컴파일까지는 가능하다.  
    
### 커스텀한 예외 만드는 방법
    우선 사용자 정의 예외를 만들기 전에 다음의 두 가지 조건을 만족할 경우는 사용자 정의 예외를 만들어야 한다고 할 수 있다.

1. 업무에 특화한 처리인 경우(광범위하게 재사용할 것이 아닌 것)
2. 프레임워크나 시스템에서 공통적인 예외 처리를 하는 경우

    
    이러한 조건을 만족하는 경우에 사용자 정의 예외를 도입하면 다음의 장점이 있다.

1. 자바의 표준 API에 있는 예외 클래스와 구별함으로써 예외를 포착하는 쪽은 많은 예외를 의식하지 않아도 된다.
2. 업무 로직으로서 공통 처리를 만들 때 영향 범위를 국소화할 수 있다.

    
    사용자 정의 예외 클래스를 만드는 방법은 기존 표준 API에서 제공하는 예외를 상속하면 된다.
    보통의 경우 Exception 또는 RuntimeException 클래스를 상속받아 구현하는데
    보통 검사 예외인 경우 Exception 클래스를 상속받고,
    실행시 예외인 경우 RuntimeException 클래스를 상속받아서 작성하면 된다.
    
```java
public class CustomException extends Exception {
    public CustomException() {
        super();
    }
    
    public CustomException(String message) {
        super(message);
    }   
    
    public CustomException(Throwable ex) {
        super(ex);
    }      
    
    public CustomException(String message, Throwable ex) {
        super(message, ex);
    }
}
```
    
    맨 위 생성자와 같이 인자가 없는 생성자만을 구현하여 사용할수도 있지만 필요한 생성자들을 모두 구현하여 사용할수도 있다.
    보통 예외 클래스명은 XXXException과 같이 예외 클래스임을 알려주도록 네이밍하는 것이 관례이다.

```text
사용자 정의 예외도 기존 예외를 상속받은 것이기 때문에 표준 예외와 똑같이 사용할 수 있다.
```

```java
public class Test {
    public static void main(String[] args){
        ExceptionTest exceptionTest = new ExceptionTest();
        try {
            exceptionTest.test();
        } catch (CustomException e) {
            e.printStackTrace();
        }
    }
}

public class ExceptionTest {
    public void test() throws CustomException {
        throw new CustomException("사용자 정의 예외입니다.");
    }
}

public class CustomException extends Exception {
    public CustomException() {
        super();
    }
    
    public CustomException(String message) {
        super(message);
    }   
    
    public CustomException(Throwable ex) {
        super(ex);
    }      
    
    public CustomException(String message, Throwable ex) {
        super(message, ex);
    }
}
```    
    