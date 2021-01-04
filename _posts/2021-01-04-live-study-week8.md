---
title: "라이브 스터디 8주차"
categories: 
  - LiveStudy
last_modified_at: 2021-01-04T23:00:00+09:00
---

# 목표
## 상속
- 자바의 인터페이스에 대해 학습하세요.

## 학습할 것
- [인터페이스 정의하는 방법](#인터페이스-정의하는-방법)
- [인터페이스 구현하는 방법](#인터페이스-구현하는-방법)
- [인터페이스 레퍼런스를 통해 구현체를 사용하는 방법](#인터페이스-레퍼런스를-통해-구현체를-사용하는-방법)
- [인터페이스 상속](#인터페이스-상속)
- [인터페이스의 기본 메소드 (Default Method), 자바 8](#인터페이스의-기본-메소드-(Default-Method),-자바-8)
- [인터페이스의 static 메소드, 자바 8](#인터페이스의-static-메소드,-자바-8)
- [인터페이스의 private 메소드, 자바 9](#인터페이스의-private-메소드,-자바-9)


### 인터페이스 정의하는 방법
    인터페이스란 구체적인 구현을 잘라내어 확장성을 높이기 위해 객체의 동작(메서드)만을 규정하는 역할을 한다.
    인터페이스를 선언하려면 interface 키워드를 사용한다.

```java
public interface Foo {
    String say();                                            
}
```
    
    인터페이스는 반드시 public 이므로 인터페이스명의 앞에 쓰는 public은 생략 가능하다.
    또한 인터페이스의 메서드도 public abstract 메서드만 정의할 수 있는데 모두 생략해서 기술할 수 있다. 

### 인터페이스 구현하는 방법
    1. 인터페이스는 implements 키워드를 이용해서 클래스를 선언하고 클래스에 실제 메서드의 처리를 정의한다.
    
```java
public class Bar implements Foo {
    @Override
    public String say() {
       System.out.println("Bar");                
    }                                      
}
```

    인터페이스에는 메서드뿐만아니라 상수(public static final 필드)를 정의하는 것도 가능하다.
    또한 public static final도 생략이 가능하다.
    
```java
interface Foo{
   int number = 10;
}
```
    
    2. 인터페이스는 또한 익명 클래스로 구현이 가능한데, 익명 클래스란 이름이 없는 클래스의 정의와
    인스턴스화를 한 번에 작성하는 클래스를 말한다.
    주로 인스턴스를 구현한 처리나 추상 클래스를 계승한 처리를 국소적으로 사용하고 싶은 경우에 익명 클래스를 사용한다.

```java
interface Foo{
   int number = 10;
   String say();
}

public class AnonymousClass {
    public static void main(String[] args){
        Foo foo = new Foo() {
        @Override public String say() {
            return "hello";
    }};
}        
}
```
    
    위와 같이 익명클래스는 부모 클래스를 new 로 생성하는 기술에 뒤이어 메서드나 필드의 정의를 기술해서 사용한다.
    이렇게 익명 클래스를 사용하면 클래스를 특정한 한곳에서만 사용하는 경우는 이름이 있는 클래스르 정의하는 것 보다
    코드를 간결하게 해주는 장점이 있다.
    
    또한 아래와 같이 자바 8에서 도입된 람다식을 사용하면 더욱 간단하게 줄일 수 있다.
    
```java
interface Foo{
   int number = 10;
   String say();
}

public class AnonymousClass {
    public static void main(String[] args){
        Foo foo = ()-> "hello";            
    }        
}
```
     

### 정리
- 인터페이스는 반드시 public 이므로 생략 가능하다.
- 모든 메서드는 public abstract 이어야 하며, 이를 생략할 수 있다.(static, default 메서드는 예외, JDK 1.8~)
- 모든 멤버변수는 public static final 이어야 하며, 이를 생략할 수 있다.

### 인터페이스 레퍼런스를 통해 구현체를 사용하는 방법
    dfd
    
### 인터페이스 상속
    클래스끼리는 하나의 클래스만 상속이 되는 반면, 인터페이스끼리는 다중 상속이 가능하다.
    또한 여러개의 인터페이스를 상속받은 인터페이스를 클래스에 적용할 땐 상속된 인터페이스들의
    모든 메소드를 구현해야 한다.

```java
interface InterfaceTest1 {
      int a =110;
      void method1();
}

public interface InterfaceTest2 {
      void method2();
      void method3();
}

public interface InterfaceTest3 extends InterfaceTest1, InterfaceTest2{
}

public class InterfaceTestClass implements InterfaceTest3{
      int b = a; //여기서 a는 InterfaceTest1의 멤버 변수 a 이다.
      
      //InterfaceTest1,2,3의 모든 메서드를 구현해줘야 한다.
      @Override
      public void method1() { /* 구현 */
            System.out.println(a);
      }
      @Override
      public void method2() { /* 구현 */
            System.out.println(a);}

      @Override
      public void method3() { /* 구현 */
            System.out.println(a);  }

}
```

    또한 아래와 같이 여러개의 인터페이스들을 implements 할 수 있다.

```java
public class InterfaceTestClass implements InterfaceTest1, InterfaceTest2{ /* 구현 */ }
```
    
    앞서 말했듯이 클래스는 다중 상속이 불가능하다. 하지만 인터페이스를 이용하여 다중 상속처럼 사용할 수 있다.
    
```java
public class Tv {

      protected boolean power;
      protected int channel;
      protected int volume;
      public void power(){power = !power;}
      public void channelUp(){channel++;}
      public void channelDown(){channel--;}
      public void volumeUp(){volume++;}
      public void volumeDown(){volume--;}
}

public class VCR {

      protected int counter;
       
      public void play() {
          System.out.println("play");
      }
      public void stop() {
          System.out.println("stop");
      }
      public void setCounter(int counter) {
        this.counter = counter;
      }
      public int getCounter() {
        return counter;
      }
}

public interface IVCR {
      void play();
      void stop();
      void setCounter(int counter);
      int getCounter();
}

public class TVCR extends Tv implements IVCR{
      
      VCR vcr = new VCR(); //VCR객체를 이용하여 메서드를 호출한다.
      
      @Override
      public void play() {
            vcr.play();
      }
      @Override
      public void stop() {
            vcr.stop();
      }
      @Override
      public void setCounter(int counter) {
            vcr.setCounter(counter);
      }
      @Override
      public int getCounter() {
            return vcr.getCounter();
      }
}
```    
     
     VCR 클래스와 TV 클래스를 동시에 상속해 TVCR 이라는 클래스를 만들려고 한다.
     하지만 다중 상속은 안되기 때문에 인터페이스를 이용하여 다중상속처럼 만들었다.
     
     1. VCR에서 사용되는 메서드를 그대로 이름을 따와 IVCR이라는 인터페이스를 만들었다.
     2. 최종적으로 구현하려는 TVCR클래스에 TV클래스를 상속하고 IVCR이라는 인터페이스의 메서드를 TVCR클래스에서 구현하겠다고 implements로 선언했다.
     3. VCR클래스의 인스턴스를 생성하여 오바라이딩된 IVCR의 메서드에서 VCR의 메서드를 호출한다.
     
     위와 같이 만들면 TV클래스와 VCR클래스의 모든 메서드와 멤버를 사용할 수 있다. 즉 다중상속과 같아진다.
     
    
### 인터페이스의 기본 메소드 (Default Method), 자바 8
    자바 8부터는 인터페이스가 자바의 8이전 버전과의 호환성을 위해 Default 구현을 가질 수 있게 되었다.
    자세히 설명하자면 어떠한 인터페이스에 새로운 메소드를 추가하고자 할 때
    인터페이스이기 때문에 해당 인터페이스를 구현한 클래스들은 새로 추가된 메소드를 모두 구현해야한다.
    하지만 현실적으로 그런것은 불가능하기 때문에 Default 메소드를 사용해 새로 추가된 메소드를
    사용하길 원하거나 오버라이딩이 가능하기 때문에 오버라이딩하기를 원하는 클래스만 구현하여 실행할 수 있게 된 것이다.
 
 **즉 인터페이스에 신규 메소드를 모든 구현 클래스 수정없이 추가하고자 만들어진 것이다.**
 
```java
public interface IPrinterable {
    public void print();
    public default void cancel(){
        System.out.println("Printer Cancel");
    };
}

public class InkJetPrinter implements IPrinterable {

    @Override
    public void print() {
        System.out.println("InkJetPrinter Print");

    }

    @Override
    public void cancel() {
        System.out.println("InkJetPrinter Cancel");
       
    }

}

public class LaserPrinter implements IPrinterable{

    @Override
    public void print() {
        System.out.println("LaserPrinter Print");
       
    }

    // cancel Method No Override!! But No Error!!

}

public class DefaultMethodExample {

    public static void main(String[] args) {
        IPrinterable printer1 = new InkJetPrinter();
        IPrinterable printer2 = new LaserPrinter();
        
        printer1.print(); // "InkJetPrinter Print"
        printer1.cancel(); // "InkJetPrinter Cancel"
       
        printer2.print(); // "LaserPrinter Print"
        printer2.cancel(); // "Printer Cancel"
    }
}
```

    그래서 아래와 같이 java.util.List 인터페이스에는 다음과 같은 "구현"이 들어간 메서드가 추가될 수 있다.
    
```java
public interface List<E> extends Collection<E> {
    default void sort(Comparator<? super E> c) {
        Object[] a = this.toArray();
        Arrays.sort(a, (Comparator) c);
        ListIterator<E> i = this.listIterator();
        for (Object e : a) {
            i.next();
            i.set((E) e);
        }
    }
}
```
    
    
### 인터페이스의 static 메소드, 자바 8
    자바 8부터 인터페이스가 메서드의 구현을 지닐 수 있으므로 static 메서드도 정의할 수 있다.
    마찬가지로 인스턴스를 생성하지 않고 인터페이스의 클래스명으로 메소드를 호출한다.
    오버라이드가 불가하다.

```java
public interface Foo {
    static void say() {
        System.out.println("HI");                
    }
}

public class Test {
    public static void main(String[] args){
      Foo.say(); // HI
    }    
}
```

    이렇게 인터페이스에 static 메서드를 정의할 수 있게 됨으로써 인터페이스를 구현하는 클래스의 
    인스턴스를 반환하는 팩토리 메서드를 인터페이스에 정의할 수 있게 되었다.
    
### 팩토리 메서드
    팩토리 메서드란 객체를 생성해서 반환하는 메서드를 말한다.
    일반적으로 반환값의 타입은 인터페이스 또는 추상 클래스로 하여 생성된 객체가 무엇인지를 
    의식하지 않도록 해서 처리의 공통화 및 재사용성을 높이는데 사용된다.
    
    우리는 인터페이스를 사용할 때 인터페이스를 통해서만 조작을 실시하기 때문에 구현 클래스를
    지정할 필요는 있지만 액세스할 필요는 없다.
    그렇기 때문에 구현 클래스 쪽도 전체 클래스를 public으로 지정할 필요가 없다.
    
    그래서 우리는 인터페이스의 static 메소드를 사용하면 인터페이스의 구현 클래스를 "은닉"할 수 있고
    사용하는쪽에서는 구현 클래스를 신경쓰지 않아도 된다.

```java
public interface Foo {
    static void say() {
        System.out.println("HI");                
    }   
    
    void hello();

    
    static Foo newInstance(String message) {
        return new DefaultFoo(message);                
    }    
}

class DefaultFoo implements Foo {
    private String message;
    
    public DefaultFoo(String message) {
         this.message = message;    
    }

    @Override
    public void hello() {
      System.out.println("hello");
    }
}

public class Test {
    public static void main(String[] args){
      Foo foo = Foo.newInstance("hi");
      foo.hello(); // hello
    }        
}
```

    static 메소드를 사용함으로써 인터페이스만을 알고 있으면 되고 접근 제한자에 의한
    가시성의 정의도 의미있게 된다.
    
    
### 인터페이스의 private 메소드, 자바 9
    private 접근자는 알다시피 클래스내에서만 접근이 가능하다.
    자바 9버전 부터는 default 메소드처럼 "내부 구현을 해야하는" private method 와 private static method를 지원하여
    내부에서만(default 메소드에서) 사용하는 method를 정의할 수 있어 캡슐화를 유지할 수 있다.
    
```java
interface Java9Interface {
   void method1();
   default void method2() {
      method4();
      method5();
      System.out.println("Inside default method");
   }
   static void method3() {
      method5();    //  static method inside other static method
      System.out.println("Inside static method");
   }
   private void method4() {    // private method
      System.out.println("Inside private method");
   }
   private static void method5() {    // private static method
      System.out.println("Inside private static method");
   }
}

public class PrivateStaticMethodTest implements Java9Interface {
   @Override
   public void method1() {
       System.out.println("Inside abstract method");
   }
   public static void main(String args[]) {
      Java9Interface instance = new PrivateStaticMethodTest();
      instance.method1();
      instance.method2();
      Java9Interface.method3();
   }
}
```

    
    
    