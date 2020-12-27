---
title: "라이브 스터디 6주차"
categories: 
  - LiveStudy
last_modified_at: 2020-12-27T23:00:00+09:00
---

# 목표
## 상속
- 자바의 상속에 대해 학습하세요.

## 학습할 것
- [자바 상속의 특징](#자바-상속의-특징)
- [super 키워드](#super-키워드)
- [메소드 오버라이딩](#메소드-오버라이딩)
- [다이나믹 메소드 디스패치 (Dynamic Method Dispatch)](#다이나믹-메소드-디스패치)
- [추상 클래스](#추상-클래스)
- [final 키워드](#final-키워드)
- [Object 클래스](#Object-클래스)

### 자바 상속의 특징

### super 키워드

    super란 자식 클래스에서 상속받은 부모 클래스의 멤버변수 및 메서드를 참조할 때 사용한다.
    인스턴스 변수의 이름과 지역 변수의 이름이 같은 경우 인스턴스 변수 앞에 this 키워드를 사용했듯이
    마찬가지로 부모 클래스의 멤버와 자식 클래스의 멤버 이름이 같은 경우 super 키워드를 사용한다.
    
    즉 이름이 다르면 부모 클래스의 멤버의 이름을 super 없이 호출할 수 있다.
    
```java
class Student extends Person{
    String name;
    int score;
    
    public Student(String name) {
        this(name, 0);
    }
    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
    
    String getName() {
        return getAge() + "/" + name; // 부모 클래스의 getAge 메서드 접근
    }
    
    void test(String age) {
        super.age = age; // super 키워드로 인자와 이름이 같은 age 필드에 접
    }
}
``` 

    어떠한 클래스의 인스턴스를 생성하면, 그 때 자신의 생성자만 실행이 되는것이 아니고, "부모의 생성자부터" 실행된다. 
    즉 new 연산자로 자식 객체를 생성하면, 자식 객체가 메모리에 올라갈때 부모 객체도 함께 메모리에 올라간다.
    이러한 부모 클래스의 생성자 호출은 모든 클래스의 부모 클래스인 Object 클래스의 생성자까지 계속 거슬러 올라가며 수행된다.

```java
public class Car{
    public Car() {
        System.out.println("Car의 기본생성자입니다.");
    }
}

public class Bus extends Car{
    public Bus(){
        System.out.println("Bus의 기본생성자입니다.");
    }
}

public class BusExam{
    public static void main(String args[]){
        Bus b = new Bus();
        // Car의 기본생성자입니다.
        // Bus의 기본생성자입니다.
    }
}
``` 

    이러한 부모 클래스의 생성자는 super() 연산으로 호출할 수 있고,
    부모 클래스의 멤버를 초기화하기 위해서는 자식 클래스의 생성자에서 부모 클래스의 생성자까지 호출해야만 한다.
    
    만약 부모의 생성자를 임의로 호출하지 않으면, 자바 컴파일러는 부모 클래스의 생성자를 명시적으로 호출하지 않는
    모든 자식 클래스의 생성자 첫 줄에 자동으로 super(); 명령문을 추가하여, 부모 클래스의 멤버를 초기화할 수 있도록 해준다.
    
    만약 부모 클래스의 생성자가 기본 생성자가 없다면(인자가 있는 생성자만 선언하여 자바 컴파일러가 자동으로 생성하지 않는 경우)
    자식 클래스의 생성자에서 직접 부모의 생성자를 호출해야 한다.
    
```java
public class Car{
    public Car(String name){
        System.out.println(name + " 을 받아들이는 생성자입니다.");
    }
}

public class Bus() extends Car {
    public Bus() {
        // super(); 컴파일 에러
        super("소방차"); // 문자열을 매개변수로 받는 부모 생성자를 호출하였다.
        System.out.println("Bus의 기본생성자입니다.");
    }
}

public class BusExam{
    public static void main(String args[]){
        Bus b = new Bus();
        // 소방차 을 받아들이는 생성자입니다.
        // Bus의 기본생성자입니다.
    }
}
```   
