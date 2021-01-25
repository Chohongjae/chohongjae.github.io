---
title: "라이브 스터디 11주차"
categories: 
  - LiveStudy
last_modified_at: 2021-01-25T23:00:00+09:00
---

# 목표
## Enum
- 자바의 열거형에 대해 학습하세요.
  

## 학습할 것
- [enum 정의하는 방법](enum-정의하는-방법)
- [enum이 제공하는 메소드 (values()와 valueOf())](느으아아앙)
- [java.lang.Enum](java.lang.Enum)
- [EnumSet](EnumSet)
- [EnumMap](EnumMap)

### Enumeration이란?
    Enumerations은 프로그래밍언어에서 명명된 상수 그룹을 나타내는 목적으로 사용된다.

### enum 정의하는 방법
    enum 타입이란 관련이 있는 "상수"의 집합을 정의하는 타입으로 클래스의 특수한 형식이다.
    자바5부터 enum 타입이 도입되었고, 변수, 메소드, 생성자를 추가하여 사용할 수 있다.
    
    enum의 선언은 매우 간단하다.
    
```java
public enum TaskType {
    PRIVATE, WORK
}
```

    enum의 상수는 지금까지의 상수와 동일하게 대문자로 정의한다.
    enum의 상수는 당연히 모두 static하며 final하다.
    
    모든 enum은 내부적으로 아래와 같은 class와 같다.
    
```java
public class TaskType {
    public static final TaskType PRIVATE = new TaskType();
    public static final TaskType WORK = new TaskType();
}
``` 
   
    위의 enum 타입의 TaskType enum을 사용하여 태스크를 표현하는 Task 클래스를 만들어보자.
    
```java
public class Task {
    private String id;
    private TaskType taskType;
    private String body;

    public Task(TaskType taskType, String body) {
         this.id = UUID.randomUUID().toString();
         this.taskType = taskType;
         this.body = body;    
    }

    public TaskType getTaskType() {
        return taskType;    
    }

    public void setTaskType(TaskType taskType) {
        this.taskType = taskType;
    }
}
```

    Task 클래스를 이용하는 쪽의 코드는 아래와 같다. 
    이렇게 enum 타입은 switch 문으로도 이용할 수 있다.
    
```java
public class TaskTest {
     public static void main(String[] args){
          Task task = new Task(TaskType.PRIVATE, "test");
          System.out.println(task.getTaskType() == TaskType.PRIVATE);
      
          switch(task.getTaskType()) {
              case PRIVATE:
                     System.out.println("private");
              case WORK:
                     System.out.println("work");
          }
     }        
}
```

    enum 타입은 클래스의 한 종류이기 때문에 다른 enum 값은 대입할 수 없어 타입 안전이 보장된다.
    또한 Enum 클래스에서 선언한 상수들은 클래스가 로드될 때 하나의 인스턴스로 생성되어 싱글톤 형태로 JVM에서 관리되게 된다.
    따라서 싱글톤으로 존재하는 것을 보장하기 때문에 우리는 enum 타입끼리의 비교는 
    eqauls() 메소드 대신 == 를 사용해 객체 비교를 할 수 있다.
    

### enum이 제공하는 메소드 (values()와 valueOf())
    java.lang.Enum 클래스를 상속한 enum 타입은 java.lang.Enum 클래스의 메소드를 사용할 수 있는데
    그 중에서 values()와 valueOf() 추가적으로 ordinal() 메소드에 대해 하나씩 알아보자.
    
    values() 메소드는 enum 안에 존재하는 모든 값들을 enum 타입 배열로 가져올 때 사용된다.
    
```java
public enum Task {
    PRIVATE, WORK
}


public class Test {
    public static void main(String[] args) {
        for (Task task : Task.values()){
            System.out.println(task);
        }
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210125livestudyweek11/values.png" alt=""> {% endraw %}

    valueOf() 메소드는 만일 특정한 문자열 값의 상수가 enum 타입으로 존재하면 반환한다.

```java
public enum Task {
    PRIVATE, WORK
}

public class Test {
    public static void main(String[] args) {
        Task task = Task.valueOf("PRIVATE");
        System.out.println(task);
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210125livestudyweek11/valueof.png" alt=""> {% endraw %}

    만약 해당 문자열 값의 상수가 존재하지 않으면 exception이 발생한다.
    
```java
public enum Task {
    PRIVATE, WORK
}

public class Test {
    public static void main(String[] args) {      
        Task task = Task.valueOf("PUBLIC");
        System.out.println(task);
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210125livestudyweek11/valueof2.png" alt=""> {% endraw %}

    ordinal() 메소드를 사용하면 해당 enum 상수집합의 index를 반환한다. 
    즉 원소에 열거된 순서를 정수 값으로 반환한다.


```java
public enum Task {
    PRIVATE, WORK
}

public class Test {
    public static void main(String[] args) {      
        System.out.println(Task.PRIVATE.ordinal());
        System.out.println(Task.WORK.ordinal());
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210125livestudyweek11/ordinal.png" alt=""> {% endraw %}

     
### java.lang.Enum
    모든 enum 타입은 실제로는 java.lang.Enum 클래스를 상속한 클래스이다.
    java.lang.Enum 클래스는 abstract class이기 때문에 해당 클래스의 객체를 생성할 수 없다.
    때문에 다중 상속이 불가능한 java에서는 더 이상 상속을 받을 수 없지만 인터페이스를 구현하는 것은 가능하다.
    
    java.lang.Enum 클래스를 상속한 클래스이므로 필드나 메서드를 정의할 수 있다.
    
    HTTP의 상태코드를 표현하는 HttpStatus를 만들어보자. 

```java
public enum HttpStatus {
    OK(200) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    }, 
    NOT_FOUND(404) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    },
    INTERNAL_SERVER_ERROR(500) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    };

    private final int value;

    HttpStatus(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
         
    public abstract void printValue(); 
    // 추상 메서드를 사용하면 상수에서 재정의 가능하다.
    // 추상 메서드를 사용하여 상수별로 유연한 메소드 사용이 가능해 확장성이 증가한다.
    
}
```
    
    위의 enum 타입을 활용해보자.
    
```java
public class Test {
    public static void main(String[] args) {
                HttpStatus ok = HttpStatus.OK;
        
                System.out.println(ok.getValue());
                ok.printValue();
                System.out.println(HttpStatus.OK == ok);
                System.out.println(HttpStatus.INTERNAL_SERVER_ERROR == ok);
    }
}
```
   
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210125livestudyweek11/abstract.png" alt=""> {% endraw %}
    
    위의 코드와 같이 각각의 상수는 속성과 행위를 가질 수 있다.
    또한 추상 메소드를 사용함으로써 상수안에 각 상수별로 특정 메소드 사용이 가능하다.

    중요한 점은 enum의 경우에는 다른 클래스들과 달리 일반적으로 생성자의 접근 제어자를 private으로 지정해야한다. 
    (Default로 private이기 때문에 생략가능하다.)
    왜냐하면 enum 타입은 고정된 상수들의 집합으로써, 런타임이 아닌 컴파일타임에 모든 값을 알고 있어야하기 때문이다.
    
    즉 다른 클래스에서 enum 타입에 접근해서 동적으로 값을 변경할 수 없기 때문에 생성자의 접근 제어자를 private으로 설정해야 하는 것이다.
     

### EnumSet
    EnumSet은 이름에서 알 수 있듯이 Set 인터페이스 기반으로 Enum의 열거요소들을
    가장 쉽고 빠르게 배열처럼 요소들을 다룰수 있는 기능을 제공한다.
    
    EnumSet은 기술상으로 원소갯수가 64개를 넘지 않을 경우에 겉은 Set 기반이지만 
    내부적으로 long 데이터형의 비트필드를 사용해서 메모리 공간도 적게 차지하고 속도가 빠르다는 장점이 있다. 
    
    HashSet의 경우에는 배열과 해쉬코드를 이용하는데 상황에 따라 다를수 있겠지만
    통상 비트연산을 이용하는 EnumSet보다는 속도면에서 훨씬 뒤떨어질수 밖에 없다.
    
    거기다 EnumSet은 Set을 기반으로 하지만 enum과 static 타입의 메소드들로 구성되어있어
    안정성을 최대한 추구하면서도 편리한 사용이 가능하다.
    
    아래의 사용 예시를 보자.

```java
import java.util.EnumSet;

public enum HttpStatus {
    OK(200) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    },
    NOT_FOUND(404) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    },
    INTERNAL_SERVER_ERROR(500) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    };

    private final int value;

    HttpStatus(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public abstract void printValue();

}

public class Test {
    public static void main(String[] args) {
        EnumSet<HttpStatus> es = EnumSet.allOf(HttpStatus.class); // allOf 메소드를 사용해 enum 타입인 HttpStatus의 요소들을 모두 가져오는 메소드이다.
        System.out.println(es); // [OK, NOT_FOUND, INTERNAL_SERVER_ERROR]

        EnumSet<HttpStatus> httpStatuses = EnumSet.copyOf(es); // 인자로 EnumSet을 받아 똑같은 EnumSet을 만드는, 복사하는 메소드이다.
        System.out.println(httpStatuses); // [OK, NOT_FOUND, INTERNAL_SERVER_ERROR]
        System.out.println(es.equals(httpStatuses)); // true

        EnumSet<HttpStatus> httpStatuses1 = EnumSet.noneOf(HttpStatus.class); // EnumSet을 비우는 메소드이다.
        System.out.println(httpStatuses1); // []

        EnumSet<HttpStatus> ok = EnumSet.of(HttpStatus.OK, HttpStatus.INTERNAL_SERVER_ERROR); // 인자로 전달된 enum 값들로만 EnumSet을 구성하는 메소드이다.
        System.out.println(ok); // [OK, INTERNAL_SERVER_ERROR]

        EnumSet<HttpStatus> httpStatuses2 = EnumSet.complementOf(ok); // 인자로 전달된 enum 타입의 "전체 값들중에서" 전달된 EnumSet의 요소들만 제외하고 EnumSet을 구성하는 메소드이다.
        System.out.println(httpStatuses2); // [NOT_FOUND]

        EnumSet<HttpStatus> range = EnumSet.range(HttpStatus.OK, HttpStatus.INTERNAL_SERVER_ERROR); // enum에 열거된 순서를 기준으로 구간을 정해서 EnumSet을 구성하는 메소드이다.
        System.out.println(range); // [OK, NOT_FOUND, INTERNAL_SERVER_ERROR]

        EnumSet<HttpStatus> range1 = EnumSet.range(HttpStatus.INTERNAL_SERVER_ERROR, HttpStatus.OK); // 열거된 순서에 맞지않으므로 Exception이 발생한다. (ok가 순서상 앞)
        System.out.println(range1); // Exception in thread "main" java.lang.IllegalArgumentException: INTERNAL_SERVER_ERROR > OK
    }
}
```

    실행 결과를 보자.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210125livestudyweek11/result.png" alt=""> {% endraw %}


### EnumMap
    EnumSet과 마찬가지로 Map 인터페이스 기반으로 Enum의 열거요소들을 가장 쉽고 빠르게 다룰수 있는 기능을 제공한다.
    마찬가지로 HashMap과 비교하여 더 효율적이다.
    
    EnumMap의 순서는 열거형의 키를 기반으로 자연적인 순서(natural order)를 따른다.
    여기서 자연적인 순서라함은 enum HttpStatus에서 열거한 순서대로 나열한다는 것을 말한다.
    예를 들어, enum HttpStatus에서 열거요소의 OK와 INTERNAL_SERVER_ERROR 바꿔놓으면
    모든 결과들은 이 둘의 순서가 뒤바뀌어서 출력될 것이다.
    
    따라서 put( ) 메소드를 이용해서 밸류값을 넣은 순서와 상관이 없다.
     
```java
import java.util.Collection;
import java.util.EnumMap;
import java.util.Set;


public enum HttpStatus {
    OK(200) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    },
    NOT_FOUND(404) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    },
    INTERNAL_SERVER_ERROR(500) {
        @Override
        public void printValue() {
            System.out.println(getValue());
        }
    };

    private final int value;

    HttpStatus(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public abstract void printValue();

}

public class Test {
    public static void main(String[] args) {
        EnumMap<HttpStatus, String> enumMap = new EnumMap<>(HttpStatus.class);
        enumMap.put(HttpStatus.OK, "OK_value");
        enumMap.put(HttpStatus.NOT_FOUND, "NOT_FOUND_value");
        enumMap.put(HttpStatus.INTERNAL_SERVER_ERROR, "INTERNAL_SERVER_ERROR_value");

        System.out.println(enumMap); // Map 형태로 구성되었다. {OK=OK, NOT_FOUND=NOT_FOUND, INTERNAL_SERVER_ERROR=INTERNAL_SERVER_ERROR}

        Set<HttpStatus> httpStatuses = enumMap.keySet(); // EnumMap의 key들을 Set타입으로 가져온다.
        System.out.println(httpStatuses); // [OK, NOT_FOUND, INTERNAL_SERVER_ERROR]

        Collection<String> values = enumMap.values(); // EnumMap의 value들을 가져온다.
        System.out.println(values); // [OK_value, NOT_FOUND_value, INTERNAL_SERVER_ERROR_value]
    }
}
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210125livestudyweek11/enummap.png" alt=""> {% endraw %}