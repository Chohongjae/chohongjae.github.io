---
title: "라이브 스터디 12주차"
categories: 
  - LiveStudy
last_modified_at: 2021-02-01T23:00:00+09:00
---

# 목표
## 애노테이션
- 자바의 애노테이션에 대해 학습하세요.
  

## 학습할 것
- [애노테이션 정의하는 방법](#애노테이션-정의하는-방법)
- [@Retention](#@Retention)
- [@Target](#@Target)
- [@Documented](#@Doucmented)
- [애노테이션 프로세서](#애노테이션-프로세서)


## 애노테이션이란?
    Annotation이란 Java 1.5부터 등장한 기능으로 인터페이스를 기반으로 한 문법이다.
    사전적 의미로는 주석으로 주석처럼 클래스, 메소드, 필드등에 특별한 의미를 부여하거나 기능을 주입할 수 있다.
    즉, 프로그램에게 추가적인 정보를 제공해주는 메타 데이터(데이터를 위한 데이터)라고 볼 수 있다.

### 자바에서 제공하는 어노테이션
    빌트인으로 자바에서 아래와 같은 어노테이션을 제공한다.

1. 코드에 적용되는 어노테이션(ex: @Override, @Deprecated)
2. 다른 어노테이션에 적용되는 Meta 어노테이션(ex: @Retention, @Documented, @Target)
{: style="font-size: 80%;"}
    
### 어노테이션의 쓰임
    이러한 어노테이션은 크게 세 가지 종류로 활용될 수 있다.

1. 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보 제공
2. 소프트웨어 개발툴이 빌드나 배치시 코드를 자동으로 생성할 수 있도록 정보 제공
3. 마지막으로 실행시(런타임시)특정 기능을 실행하도록 정보를 제공등으로 사용할 수 있다.
{: style="font-size: 80%;"}

아래의 코드는 우리가 자주 사용하는 어노테이션들이다.

```java
public class Person {
    private String name;
    private Integer age;

    @Deprecated
    public Integer getAge() {
        if (age == null) {
            return 0;
        }
        return age;
    }

    @Override
    public String toString() {
        return "Person(name=" + name + ", age=" + age + ")";
    }
}
```
    설명을 위해 불필요한 생성자, 메소드는 생략했다.
    위의 getAge() 메소드에 붙어있는 @Deprecated 어노테이션은 해당 어노테이션이 붙어있는 메소드나
    필드를 사용하면 빌드할 때 워닝 메세지를 보여주는 즉, 컴파일러에게 이 메소드 혹은 필드는 없어질 것을
    알려주는 추가적인 정보를 제공하는 어노테이션이다.
    
    또한 toString() 메소드에 달린 @Override 어노테이션을 확인할 수 있는데,
    "상속의 관계에 있는 클래스 간에 하위 클래스가 상위 클래스와 '완전 동일한' 메소드를 덮어쓴다"는 의미로 사용하는 어노테이션이다.
    상위 클래스의 메소드를 해당 어노테이션 없이도 오버라이딩 할 수 있지만, 어노테이션을 사용함으로써 컴파일러에게
    오버라이딩하는 메소드라는 정보를 전달해 오타 혹은 작성 문법 에러, 시그니처 오류등을 컴파일러가 잡아낼 수 있는 효과를 낼 수 있다.
    
## 애노테이션 정의하는 방법
    인터페이스를 정의하는 것과 유사하다.
    @interface를 사용해서 어노테이션을 정의하며, 그 뒤에 사용할 어노테이션의 이름을 작성한다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/annotest.png" width="85%" alt=""> {% endraw %}
    
    이렇게 생성한 어노테이션은 아래와 같이 사용한다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/annotest2.png" width="85%" alt=""> {% endraw %}
    
    어노테이션은 엘리먼트를 멤버로 가질 수 있다.
    각 엘리먼트는 타입과 이름으로 구성되며, 디폴트 값을 가질 수 있다.
    엘리먼트의 타입으로 primitive type, String, enum, 그리고 이들의 배열 타입을 사용할 수 있다.
    엘리먼트의 이름 뒤에는 메소드를 작성하는 것처럼 ()를 붙여야 한다.
    
```java
@Target({ElementType.METHOD, ElementType.TYPE})
public @interface TestAnnotation {
    String element1();
    int element2() default 5;
    String[] element3() default {"test"};
}

@TestAnnotation(element1 = "test")
public class AnnotationClassTest {
    
    @TestAnnotation(element1 = "test1", element2 = 6)
    public void AnnotationMethodTest() {
    }
    
    @TestAnnotation(element1 = "test1", element2 = 6, element3 = {"test", "test4"})
    public void AnnotationMethodTest() {
    }
}
```

    어노테이션은 기본 엘리먼트인 value를 여러 타입으로 가질 수 있다.
    
```java
@Target({ElementType.TYPE})
public @interface ValueAnnotation {
    String value();
    int element1() default 3;
}

@ValueAnnotation("hi")
public class Test {
}
```

    value 엘리먼트를 가진 어노테이션을 코드에서 적용할 떄는 위와 같이 값만 기술할 수 있다.
    이 값은 기본 엘리먼트인 value 값으로 자동 설정된다.
    만약 value 엘리먼트와 다른 엘리먼트에 값을 동시에 주고 싶다면 아래와 같이 이름을 지정하여 값을 부여해야 한다.
    
```java
@Target({ElementType.TYPE})
public @interface ValueAnnotation {
    int[] value();
    int element1() default 3;
}

@ValueAnnotation(value = {1, 2}, element1 = 5)
public class Test {
}
```    

## 런타임 시 어노테이션 정보 사용하기
    어노테이션은 단지 주석일 뿐이라 그 자체로는 아무런 동작을 하지 않는다.
    따라서 프로그램에 추가적인 작업을 하기 위해서는 리플랙션을 이용하여 엘리먼트 값을 읽고 처리해야 한다.
    간단하게 리플렉션을 사용하여 어노테이션의 엘리먼트 값들을 가져와 보자.

```java
@Target({ElementType.METHOD, ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
public @interface AnnotationTest {
    int value() default 5;
    String test();
}


public class Person {
    private String name;
    
    @AnnotationTest(test = "hi")
    public String getName() {
        return name;
    }

    public static void main(String[] args) throws NoSuchMethodException {
        Arrays.stream(Person.class.getDeclaredMethod("getName").getAnnotations()).forEach(System.out::println);
        AnnotationTest annotation = Person.class.getDeclaredMethod("getName").getAnnotation(AnnotationTest.class);
        System.out.println(annotation.value());
        System.out.println(annotation.test());
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/annotest3.png" width="85%" alt=""> {% endraw %}

    리플렉션을 사용하여 Person 클래스의 getName 이름을 가진 메소드를 가져왔고,
    해당 메소드에 달린 어노테이션들을 모두 가져와 출력하였다.
    
    또한 getName 이름을 가진 메소드에 달린 AnnotationTest 어노테이션을 가져왔고(없으면 null),
    value 엘리먼트와 test 엘리먼트를 출력하였다.


## @Retention
    자바 컴파일러가 어노테이션 값들을 언제까지 유지할 것인지, 어느 시점까지 영향을 미칠 것인지를 결정한다.
    즉 어노테이션의 LifeTime이다.
    코드 자동 생성 툴을 개발하지 않는 이상, 우리가 만드는 대부분의 애노태이션은 보통 어노테이션은
    Runtime시에 사용하기 위한 용도로 만들어 진다.
    그래서 대부분의 어노테이션의 Retention 값은 RUNTIME으로 되어있다.
    
### SOURCE
- 소스상에서만 어노테이션 정보를 유지한다.
{: style="font-size: 80%;"}
- 소스 코드를 분석할 때만 의미가 있으며, 바이트 코드 파일에는 정보가 남지 않는다.
{: style="font-size: 80%;"}

### CLASS
- 바이트 코드 파일까지 어노테이션 정보를 유지한다.
{: style="font-size: 80%;"}
- 하지만 리플렉션을 이용해서 어노테이션 정보를 얻을 수는 없다.
{: style="font-size: 80%;"}

### RUNTIME
- 바이트 코드 파일까지 어노테이션 정보를 유지한다.
{: style="font-size: 80%;"}
- 리플렉션을 이용해서 런타임에 어노테이션 정보를 얻어올 수 있다.
{: style="font-size: 80%;"}

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/retention.png" width="85%" alt=""> {% endraw %}
- [이미지 출처](https://honeyinfo7.tistory.com/56)

## @Target
    어떠한 값(클래스, 필드, 메서드)에 어노테이션을 적용할 것인지 결정한다.
    즉 어노테이션을 적용할 위치를 결정한다.
    @Target의 기본 엘리먼트인 value는 ElementType 배열을 값으로 가진다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/target.png" width="85%" alt=""> {% endraw %}
- [이미지 출처](https://honeyinfo7.tistory.com/56)


### @Target과 @Rentention 사용 예시

```java
package myannotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {
	String value() default "-";
	int number() default 15;
}

// @MyAnnotation -> @Target에 TYPE이 없어 클래스에 적용할 수 없다.
public class Test {
    
    @MyAnnotation("hi") // value = "hi", number = 15
    public void test() {
    }  
}
```

> 메소드에만 어노테이션을 적용하고 바이트 코드 파일까지 어노테이션 정보를 유지하며 리플렉션을 이용해서 런타임에 어노테이션 정보를 얻어올 수 있다.
{: style="font-size: 80%;"}

## @Doucmented
    @Documented가 달린 어노테이션을 사용하는 elements의 JavaDoc에 이 어노테이션의 존재를 표기하도록 지정한다.
    즉 어노테이션은 기본적으로 JavaDoc에 포함되지 않기 때문에 @Doucmented가 달려있는 어노테이션을 사용하는 elements의 
    JavaDoc을 생성할때 해당 어노테이션도 JavaDoc에 문서에 포함되어야함을 나타낸다.

### @Doucmented가 달린 어노테이션을 사용하는 getName() 메소드의 @JavaDoc

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented3.png" width="50%" alt=""> {% endraw %}
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented5.png" width="95%" alt=""> {% endraw %}

### @Doucmented가 달리지 않은 어노테이션을 사용하는 getName() 메소드의 @JavaDoc

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented.png" width="50%" alt=""> {% endraw %}
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented4.png" width="95%" alt=""> {% endraw %}     
    
## 애노테이션 프로세서
    자바가 제공하는 기능으로, "컴파일 시점"에 특정한 애노테이션이 붙어있는 소스코드를 참조해서 
    애노테이션에 정의된 액션(새로운 소스코드를 생성하거나, 기존의 코드를 수정하거나, resource 파일 생성)등의 작업을 할 수 있는 기능이다.
    즉 컴파일 단계에서 어노테이션을 분석하고 처리하기 위해 자바 컴파일러에 동봉된 hook이다.
    
    이러한 어노테이션 프로세서를 이용하면 컴파일 단계에서 소스를 조작할 수 있게 되므로 이와 관련된 라이브러리는
    Annotation Processor을 사용한다고 생각하면 되고 실제로 Lombok, JPA 등등 꽤 많은 라이브러리에서 사용하고 있다.
    간단하게 애노테이션 프로세서를 사용하는 Lombok에 대해 알아보자.

### Lombok
    전에 어노테이션을 설명하면서 작성한 Person 클래스를 다시 봐보자.

```java
public class Person {
    private String name;
    private Integer age;

    public Person(String name) {
        this(name, null);
    }

    public Person(String name, Integer age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public void setAge(Integer age) {
        this.age = age;
    }

    @Deprecated
    public Integer getAge() {
        if (age == null) {
            return 0;
        }
        return age;
    }

    @Override
    public String toString() {
        return "Person(name=" + name + ", age=" + age + ")";
    }
}
```

    이 클래스에는 자바빈 규약(정보 은닉)을 지키기 위해 멤버변수에 직접 접근하지 않고
    getter/setter 를 통해 멤버변수의 값을 접근, 변경하고 있다.
    만약 멤버 변수가 더 늘어나게 된다면 여러가지 번거로운 준비코드는 끝없이 늘어나게 될 것이다.
    이렇게 소스가 길어지면 가독성이 늘어나고 개발자가 실수하는 부분이 생길 것이다.
    
    하지만 Lombok을 사용한다면 위의 소스는 아래와 같이 변한다.

```java
@Getter
@Setter
@ToString
@AllArgsConstructor
public class Person {
    private String name;
    private Integer age;

    public Person(String name) {
        this(name, null);
    }
}
```    
    
    위의 코드처럼 번거로운 준비코드를 @Getter, @Setter, @AllArgsConstructor 어노테이션으로 처리할 수 있다.
    이러한 롬복의 동작원리는 앞서 말했듯이 Lombok 어노테이션이 부착된 소스코드를 컴파일 시점에 참조하여 
    어노테이션 프로세서로 등록된 롬복 프로세서가 어노테이션을 확인하고 소스코드의 AST(Abstraction Syntax Tree)를 조작하여
    바이트 코드에 새로운 소스를 생성해내는 것이다.
    
    하지만 공개된 API가 아닌 컴파일러 내부 클래스를 사용하여 기존의 소스 코드를 조작하는 방식이기 때문에 해킹이라고 불리지만
    그럼에도 불구하고 엄청난 편리한 때문에 널리 쓰이고 있으며, 대안이 몇가지 있지만 롬복의 모든 기능과 편의성을 대체하지는 못하고 있다.
    
    
    
## 궁금한 점
    만약 커스텀 애노테이션 생성시 @Target으로 어노테이션을 적용할 위치를 결정하지 않으면 어떻게 될까?
    애노테이션을 사용하는 곳마다 위치가 정해질까?     
    