---
title: "라이브 스터디 5주차"
categories: 
  - LiveStudy
last_modified_at: 2020-12-15T23:00:00+09:00
---

# 목표
## 클래스
- 자바의 Class에 대해 학습하세요.

## 학습할 것
- [클래스 정의하는 방법](#클래스-정의하는-방법)
- [객체 만드는 방법 (new 키워드 이해하기)](#객체-만드는-방법-(new-키워드-이해하기))
- [메소드 정의하는 방법](#메소드-정의하는-방법)
- [생성자 정의하는 방법](#생성자-정의하는-방법)
- [this 키워드 이해하기](#this-키워드-이해하기)

### 클래스 정의하는 방법
    자바에서는 어떤 프로그래밍이든 클래스 안에 속해있는데 클래스란 변수나 메서드를 모아둔 틀 또는 그릇과 같은 것이다.
    프로그램을 만들 때는 구조를 파악하기 쉽도록 프로그램을 분할하는데 그때 우선 클래스 단위로의 분할을 고려한다.
    
    예를 들면 학생의 점수를 관리하는 프로그램은 '학생' 이라는 개념을 클래스화 한다.
    
```java
class Student {
    String name;
    int score;
    static final int MAX_SCORE = 100;
}
```

    클래스는 class 블록 내에 유지시킬 변수를 선언하여 만든다.
    클래스가 갖는 변수를 '필드' 라고 부른다. ex) name, score, MAX_SCORE(상수 필드)
    
### 객체 만드는 방법 (new 키워드 이해하기)
    필드와 메서드를 작성하면 클래스는 만들어진다. 
    단, 클래스의 선언만으로는 아직 물건을 담을 틀만 존재하는 상태다.
    실제로 프로그램에서 사용하려면 이 틀을 이용해서 실제 물건을 만든 후에 이용할 필요가 있다.
    이 실제 물건을 '객체' 또는 '인스턴스'라고 한다.

    자바 언어의 특징중 new를 사용해 메모리를 할당하는 기능이 있다.
    힙(Heap) 영역에 저장할 공간을 할당해서 참조 값을 객체에게 반환하여 주는 것인데
    힙은 참조형 공간으로써 해제 하기전까지 할당된 메모리는 삭제되지 않는다.
    
```java
Student(자료형) hongjae(참조변수);  
hongjae(참조변수) = new(인스턴스 생성, 메모리할당) Student()(생성자 호출 및 초기화);
```
    
    위에 선언을 보면
    1. Student라는 타입, 자료형으로 hongjae라는 객체를 선언한다.
    2. Student 클래스의 생성자가 클래스를 초기화한다.
    3. new 연산자를 사용하여 Student()를 힙(heap) 영역에 할당하고 주소를 hongjae라는 변수에 저장한다.
    
    즉 new 연산자를 통해 Heap 영역에 데이터를 저장할 공간을 할당받고 그 공간의 참조값을 객체에게 반환함으로써
    클래스 타입의 인스턴스(객체)를 생성해주는 역할을 하는 것이다.
    
### 메소드 정의하는 방법
    메서드는 처리를 기술하는 블록이다.
    메서드는 다음의 형태로 클래스 안에 선언한다.
    
    <수식자> <반환값의 타입> <메서드의 이름> (<인수1의 타입><인수1의 이름>, <인수2의 타입><인수2의 이름>....)
    
```java
public String getName(String name, int age)
```

    메서드는 호출할 때 값을 건넬 수 있고 이 값을 '인수' 라고 부른다.
    인수는 몇 개라도 기술할 수 있으며 인수를 건네지 않는 것도 가능하다.
    
    메서드를 호출한 후 결괏값을 호출자에게 반환할 수 있고 이 값을 '반환값'이라고 한다.
    반환값이 없는 경우는 타입으로 'void'를 지정하고 void 이외의 타입을 지정한 경우, 
    해당 메서드에 return문을 사용해서 타입이 일치하는 값을 반드시 반환할 필요가 있다.
    
```java
public String getName(String name, int age) {
    return name;
}

public void test() {
    System.out.println("Hello World");
}
```   

### 메서드 오버로딩
    하나의 클래스 안에서는 동일 명칭의 메서드를 복수 정의할 수 없다.
    단, 인수의 타입이나 인수의 수가 다르면 동일 명칭의 메서드를 정의할 수 있다.
    이러한 정의를 메서드의 '오버로딩' 이라고 부른다.
    다음의 소스코드에서는 인수에 int 타입이 지정된 경우는 위쪽의 메소드가 호출되고
    인수의 지정이 없는 경우는 아래쪽의 메소드가 호출된다.
    
```java
void printScore(int score) {
    System.out.println(score);
}

void printScore() {
    printScore(MAX_SCORE);
}
```

### main 메서드
    메서드에는 'main' 메서드라는 특별한 메서드가 있다.
    이 메서드는 자바 프로그램을 실행했을 때 호출되는 프로그램의 시작점인 메서드이며
    자바 프로그램에는 반드시 존재해야 한다.  
    
```java
public static void main(String[] args) {
  // 처리내용을 작성한다.
}
``` 

    main 메서드의 경우 프로그램을 호출할 때의 커맨드 인수의 값이 들어있고
    배열 또는 가변 길이 인수 형식으로 받아들일 수 있다.
    
### 생성자 정의하는 방법
    실제 프로그램에서는 인스턴스를 생성하는 시점에 설정을 읽어들이거나 필드를 초기화하는 등 여러가지 처리를 하는 경우가 있다.
    그러한 때는 '생성자'를 선언하는데 '생성자'는 인스턴스를 '생성'할 때 호출되는 처리다.
    
    이러한 생성자는 두 가지 특징이 있다.
    
    1. 메서드명이 클래스명과 동일하다.
    2. 반환값의 선언이 존재하지 않는다.
    
```java
class Student {
    String name;
    
    public Student(String name) {
        this.name = name;
    }
}
``` 
    
    위의 소스코드는 생성자에서 필드를 '초기화'하고 있는 예다.
    생성자에서도 일반 메서드와 동일하게 오버로딩이 가능하다.
    즉, 인수가 다른 생성자를 여러 개 정의할 수 있다.
    
```java
class Student {
    String name;
    int score;
    
    public Student(String name) {
        this.name = name;
    }
    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
    
    public static void main(String[] args){
      Student hongjae = new Student("홍제");
      Student hongjae2 = new Student("홍제", 100);
    }
}
``` 

    객체의 필드는 생성자를 이용하는 방식과 메소드 혹은 직접 접근하는 방식을 통해
    값을 설정할 수 있는데 결과는 변함이 없고 다른 것은 값을 설정하는 타이밍뿐이다.
    보통 인스턴스 생성 시점에 값이 결정되고 나중에 변하지 않는 변수는
        -> 생성자에서 지정한다.
    값이 나중에 변하는 것은
        -> 메서드나 필드를 통하여 값을 설정한다. 
#
    인스턴스를 생성할 때 반드시 생성자를 호출하는데 생성자를 정의하지 않고도 생성자는 호출이 될 수 있다.
    어떻게 호출이 된 것일까? 
    그 이유는 클래스를 정의할 때 생성자를 생략하면 컴파일러가 자동적으로
    기본 생성자(Default Constructor)를 생성하여 주기 때문이다.
 
    
***이러한 컴파일러가 자동으로 생성하는 기본 생성자는 클래스에 생성자가 하나도 정의되어 있지 않아야 생성된다.<br>
만약 매개변수를 가지는 생성자를 하나라도 선언했다면, 자바 컴파일러는 기본 생성자를 추가하지 않는다.***
    
### this 키워드 이해하기
    인스턴스에서 필드에 값을 대입하거나 메서드를 호출할 때는 마침표(.)를 통해 접근하였다.
    하지만 클래스의 메서드 안에서 클래스의 필드를 접근할 때는 마침표(.)를 사용하지 않는다.
    
    이러한 자기 자신의 인스턴스 안에 있는 필드나 메서드를 사용할 경우는 특수한 인스턴스로
    자기 자신을 나타내는 this를 쓰고, 마침표(.)로 연결하는 식으로 기술한다.
    
    또한 this는 생략이 가능하기 때문에 생략해도 문제가 없는 경우는 간략한 작성을 위해서 생략하는 편이 좋다.
    그러나 상황에 따라 필드와 다른 변수의 이름이 동일한 경우는 명시적으로 this를 붙일 필요가 있다.
    
```java
class Student {
    String name;
    int score;
    
    public Student(String name) {
        // 인수와 필드의 이름이 동일하므로 name을 사용하면 필드가 아닌 인수쪽이 사용된다.
        // 따라서 필드를 사용하고 싶은 경우는 명시적으로 this를 붙인다.
        this.name = name; 
    }
    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
    
    String getName() {
        return name; // this 생략
    }   
}
``` 

    또한 this() 연산은 현재 클래스에 정의된 생성자를 부를때 사용된다.
    
```java
class Student {
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
        return name; // this 생략
    }   
}
``` 

### super 키워드 이해하기
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
    
    
## 과제
    1. int 값을 가지고 있는 이진 트리를 나타내는 Node 라는 클래스를 정의하세요.
    2. int value, Node left, right를 가지고 있어야 합니다.
    3. BinrayTree라는 클래스를 정의하고 주어진 노드를 기준으로 출력하는 bfs(Node node)와 dfs(Node node) 메소드를 구현하세요.
    4. DFS는 왼쪽, 루트, 오른쪽 순으로 순회하세요.


   