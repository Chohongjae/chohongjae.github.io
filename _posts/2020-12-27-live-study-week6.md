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
    자바에는 클래스를 정의할 때 특정 클래스를 베이스로 해서 해당 클래스를 "확장"하는 식으로 새로운 클래스를
    정의할 수 있는 "상속"이라는 메커니즘이 있다. 말 그대로 자식이 부모로부터 무언가를 물려받는 것인데
    부모 클래스를 상속하면 자식 클래스는 부모 클래스의 기능을 이용할 수 있다.
    
### extends 키워드
    클래스를 상속받으려면 extends 키워드를 사용한다.
    다음의 코드와 같이 SuperClass 클래스를 부모 클래스(슈퍼 클래스)로 하고,
    SubClass 클래스는 부모를 extends 한 자식 클래스(서브 클래스)로 하여 정의하면
    SubClass 클래스 쪽에서 SuperClass 클래스의 메서드인 superMethod를 이용할 수 있게 된다. 
    
```java
public class SuperClass {
    public SuperClass() {}

    public void superMethod() {}
} 
```

```java
public class SubClass extends SuperClass {
    public SubClass() {
        super(); // 생략 가능하다, 만약 부모의 생성자를 임의로 호출하지 않으면, 자바 컴파일러는 부모 클래스의 생성자를 명시적으로 호출하지 않는
        // 모든 자식 클래스의 생성자 첫 줄에 자동으로 super(); 명령문을 추가하여, 부모 클래스의 멤버를 초기화할 수 있도록 해준다. 
    }
    
    public static void main(String[] args){
        SubClass subClass = new SubClass();
        subClass.superMethod(); // SuperClass 클래스의 메서드를 사용할 수 있다.
    }
} 
```

    또한 super.메서드명() 으로 작성함으로써 부모 클래스의 메서드를 호출할 수 있다.
    오버라이드하고 있지 않은 메서드(부모 클래스에만 존재하는)를 호출할 때는 일반적으로 super를 생략하고,
    오버라이드하고 있는 메서드의 부모 메서드를 호출하고 싶은 경우에 super를 붙이면 된다.
    
    보통 자식 클래스는 부모 클래스로부터 상속받은 메소드 외에 자신의 메소드를 구현함으로써 좀 더많은 기능을 갖도록 설계된다. 
    
### IS-A 관계
    SubClass 클래스는 SuperClass 클래스를 상속받았다. 
    즉, SubClass는 SuperClass의 하위 개념이라고 할 수 있다.
    이런 경우 SubClass는 SuperClass에 포함되기 때문에 "SubClass는 SuperClass이다"라고 표현할 수 있다.
    
    자바는 이러한 관계를 IS-A 관계라고 표현한다. 즉 "SubClass is a SuperClass" 과 같이 말할 수 있는 관계를 IS-A 관계라고 한다.
    이렇게 IS-A 관계(상속관계)에 있을 때 자식 객체는 부모 클래스의 자료형인 것처럼 사용할 수 있다.
    즉, 다음과 같은 코딩이 가능하다.
    
```java
SuperClass subClass = new SubClass();
```

    하지만 이 반대의 경우, 즉 부모 클래스로 만들어진 객체를 자식 클래스의 자료형으로는 사용할 수 없다.
    다음의 코드는 컴파일 오류가 발생한다.
    
```java
SubClass subClass = new SuperClass();  // 컴파일 오류: 부모 클래스로 만든 객체는 자식 클래스의 자료형으로 사용할 수 없다.
```  
    
    즉 "SubClass로 만든 객체는 SuperClass 자료형이다."만 성립할 수 있는 것이다.

### 다중 상속
    다중 상속은 클래스가 동시에 하나 이상의 클래스를 상속받는 것을 뜻한다.
    C++, 파이썬 등 많은 언어들이 다중 상속을 지원하지만 자바는 다중 상속을 지원하지 않는다.
    
    만약 자바가 다중 상속을 지원한다면 다음과 같은 코드가 만들어 질 수 있을 것이다.

```java
class A {
    public void msg() {
        System.out.println("A message");
    }
}

class B {
    public void msg() {
        System.out.println("B message");
    }
}

class C extends A, B {
    public static void main(String[] args) {
        C test = new C();
        test.msg();
    }
}
```

    자바가 다중 상속을 지원한다고 가정하고 A, B 라는 클래스를 위와 같이 동시에 상속(extends A, B)하도록 했다. (실제로는 동작할 수 없는 코드이다.)
    위 main 메소드에서 test.msg(); 실행 시 A 클래스의 msg 메소드를 실행해야 할까? 아니면 B 클래스의 msg 메소드를 실행해야 할까?
    다중 상속을 지원하게 되면 이렇듯 애매모호한 부분이 생기게 된다. 자바는 이러한 불명확한 부분을 애초에 잘라 낸 언어이다.
    ※ 다중상속을 지원하는 다른 언어들은 이렇게 동일한 메소드를 상속받는 경우 우선순위등을 적용하여 해결한다.
    

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

### 메소드 오버라이딩
    메소드 오버라이딩이란 부모 클래스의 메소드를 자식 클래스가 동일한 형태로 또 다시 구현하는 행위를 말하는데
    자식 클래스가 부모 클래스의 메소드와 동일한 입출력의 형태와 이름의 메소드를 재정의하면 자식 클래스가 구현한 메소드가
    더 높은 우선순위를 갖게 되어 호출시 자식 클래스의 메소드가 호출되게 된다.

```java
public class Car{
    public void printName() {
        System.out.println("Car 입니다.");
    }
}

public class Bus() extends Car {
    @Override
    public void printName() {
        System.out.println("Car 중 Bus 입니다.");
    }   
}

public class BusExam{
    public static void main(String args[]){
        Bus b = new Bus();
        b.printName(); // "Car 중 Bus 입니다."
    }
}
```

### 추상 클래스
    우선 한마디로 추상 클래스는 계승될 것을 전제로 한 클래스다.
    예를 들어 A클래스, B클래스, C클래스가 있고 이 클래스들에 비슷한 필드와 메서드가 있을 때
    공통적인 부분을 추출해 만든 클래스를 추상 클래스라 한다.
    
    구체적인 예를 들어보면, 키보드라는 클래스가 있을 때 A 제조사의 키보드와 B 제조사의 키보드, C 제조사의 키보드는
    각 제조사만의 스타일대로 키보드를 제작할 것이다. 하지만 키보드는 버튼이라는 필드와 클릭이라는 행위, 메소드는 모든 제조사의
    키보드가 공통적으로 가지고 있을 것이다. 그럼 버튼이라는 필드와 클릭이라는 메소드가 키보드라는 추상 클래스안에 존재하면 되는 것이다.

```java
public abstract class Keyboard{
    public String button;
    
    public void print() {
        System.out.println("키보드입니다.");
    }   
    
    public abstract void click();
}

public class AKeyboard() extends Keyboard {
    @Override
    public void click() {
        System.out.println("딸깍"); // 반드시 click() 메소드를 구현해야 한다.
    }   
}

public class BKeyboard() extends Keyboard{
    @Override
    public void click() {
        System.out.println("딸깍딸깍"); // 반드시 click() 메소드를 구현해야 한다.
    }
    
    public static void main(String[] args){
      AKeyboard aKeyboard = new AKeyboard();
      BKeyboard bKeyboard = new BKeyboard();
 
      aKeyboard.click(); // 딸깍
      bKeyboard.click(); // 딸깍딸깍
    }

}
```

    즉, 추상 클래스는 실체 클래스들의 공통적인 부분을 모아놓은, 어느정도 규격을 잡아놓은 클래스라고 이해하면 된다.
    그렇기 때문에 추상 클래스는 실제 객체를 생성할 수 없고 실체 클래스들의 부모 역할을 하는 것이다.

### 추상 클래스는 왜, 언제 사용할까?
1. 같은 기능을 하는 클래스들의 필드와 메서드 이름을 통일하여 유지보수성을 높이고 통일성을 유지하기 위해 사용한다.
2. 필드 및 메소드의 설계 시간을 줄이고 구현에만 집중하고자 사용한다.
3. 규격에 맞게 소스가 구현되어 있기 때문에 해당 규격에 대한 구현부만 수정하면 손 쉽게 수정이 가능하기 때문에 사용한다.
   
## 추상 클래스의 특징
1. 클래스 및 메소드에 abstract 수식자를 지정함으로써 추상 클래스 및 추상 메소드를 정의할 수 있다.
2. 추상 클래스는 new 연산자를 이용하여 객체를 생성할 수 없다.
3. 추상 클래스는 새로운 일반 클래스를 위한 "부모 클래스의 용도로만" 사용된다.
4. 추상 클래스는 단일 상속만 가능하며 "일반 변수 및 일반 메소드"를 가질 수 있다.
5. 추상 클래스는 동일한 부모를 가지는 클래스를 묶는 개념으로 상속을 받아서 기능을 확장시키는 것이 목적이다.
6. 추상 클래스를 상속받은 클래스에서는 추상 메소드를 반드시 구현해야 한다.

### final 키워드 
    final 키워드는 변수를 변경할 수 없도록 하기 위한 수식자다.
    변수를 선언 시에 final 키워드를 붙여서 초기화하면 초기화 시에 지정한 값대로 고정할 수 있다. (반드시 선언과 동시에 초기화가 되어야 한다.)
    즉, 인스턴스 메서드등에서 변경할 수 없도록 하고 싶은 경우에 이 final 키워드를 지정하면 된다.
    
    일반적으로 final 변수는 프로그램 전체에 걸쳐 사용되는 경우가 많아서,
    클래스에 static 키워드와 함께 정의되어 사용되는데 static 키워드와 final 키워드 모두를 붙인 필드를 일반적으로 "상수"라고 한다.
    
```java
public class Fruit {
    static final int COUNT = 10;
    final int FOO = 123;
}
```

    메소드에도 final 키워드를 사용할 수 있는데 final 메소드는 오버라이딩이 불가능하다.
    즉, 상속 받은 그대로 사용해야 한다.
    
```java
public class Fruit {
    public final void hello() {
        System.out.println("HI");
    }
}

public class Banana extends Fruit {
//    @Override
//    public final void hello() {     -> Cannot override the final method 오류가 발생한다.
//    }   
}
```  

    마지막으로 final 키워드는 클래스에도 사용할 수 있다.
    final 키워드를 사용한 클래스는 상속이 불가능하다.
    즉, subclass를 만들 수 없다.
    
```java
public final class Fruit {
    public final void hello() {
        System.out.println("HI");
    }
}

public class Banana extends Fruit { // The type Banana cannot subclass the final class Fruit 오류가 발생한다.
}
```
    
    주로 final 메소드와 클래스는 라이브러리 형태의 프로젝트를 작성할 떄 사용되는데
    자신이 작성한 메소드와 클래스를 다른 사람이 상속 받아서 사용하지 못하게 금지하고 싶을 떄 사용한다.
    
### Object 클래스
    자바에서 만드는 모든 클래스는 Object라는 클래스를 암시적으로 상속받게 되어 있다. 
    그 이유는 모든 클래스가 공통으로 포함하고 있어야 하는 기능을 제공하기 위해서다.
    
    사실 우리가 위에서 만든 Banana 클래스는 다음과 기능적으로 완전히 동일하다.
    하지만 굳이 아래 코드처럼 Object 클래스를 상속하도록 코딩하지 않아도 자바에서 만들어지는 모든 클래스는
    Object 클래스를 자동으로 상속받게끔 되어 있다.

```java
public class Banana extends Object {
}
```

    따라서 자바에서 만드는 모든 객체는 Object 자료형으로 사용할 수 있다.
    즉, 다음과 같이 코딩하는 것이 가능하다.
    
```java
Object banana = new Banana();
```

    아래 그림은 Object 클래스가 제공하는 메소드 목록이다.
    즉 자바의 객체는 아래의 메소드들을 반드시 가지고 있다고 할 수 있다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20201227livestudyweek6/object메소드.png" alt=""> {% endraw %}
- [이미지 출처](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html)

### toString
    toString은 객체를 문자로 표현하는 메소드이다.
    해당 메소드를 호출하거나 System.out.println()으로 객체를 호출하면 패키지와 클래스명 그리고 고유한 식별 값이 나오는데
    이 정보를 toString() 메소드를 오버라이딩 함으로써 더욱 유용하게 만들 수 있다.
    
```java
System.out.println(banana);
System.out.println(banana.toString());
```

### equals
    equals는 객체와 객체가 같은 값, 내용인지를 비교하는 API이다.
    반면에 == 연산자는 비교하고자 하는 대상의 주소값을 비교한다.