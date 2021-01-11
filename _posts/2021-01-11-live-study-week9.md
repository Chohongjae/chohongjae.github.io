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
    자바에서 예외를 처리할 떄 기본이 되는 것은 try~catch~finally 구문이다.
        
```java
try {
    // Exception이 발생할 수 있는 로직의 처리
} catch (SomeException e) {
    // SomeException 예외를 catch한 경우의 처리
} finally {
    // try~catch 블록을 종료할 떄에 반드시 실행해야 하는 처리
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

    또한 여러 예외가 발생하는 경우 각각의 처리에 catch 블록을 작성하는 것도 가능하지만
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
    
    이것만으로 리소스 해제에 대한 처리가 끝이나게 된다.
    자바 7부터 InputStream 등의 리소스를 취급하는 클래스는
    java.lang.AutoClosable 인터페이스 또는 java.io.Closable 인터페이스를 구현하도록 되었다.
    
    그래서 try 블록의 시작 시 () 안에 AutoClosable 인터페이스의 구현 클래스를 선언해두면
    해당 try~catch 블록의 종료 시의 처리에서 실시할 close 메서드를 자동으로 호출하게 된다.
    
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
    
    예외를 떠넘기는 방법은 throws 키워드와 에러클래스를 메서드 뒤에 붙여주면 된다.
    만약 떠넘겨야할 예외 종류가 여러개라면 쉼표(,) 를 기준으로 나열하여 선언하면 된다.
    
    동시에 해당 키워드를 통해 '현재 메서드를 사용하면 이와 같은 예외가 발생한다'라는 정보를 개발자는 알 수 있게 된다.
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
    
    만약 main() 메소드가 해당 Exception을 처리하지 않으면
    Exception은 JVM까지 올라가 프로그램이 중지되는 것이다.
    
### 커스텀한 예외 만드는 방법    