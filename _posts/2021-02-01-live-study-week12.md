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
- [애노테이션 정의하는 방법](애노테이션-정의하는-방법)
- [@retention](@retention)
- [@target](@target)
- [@documented](@documented)
- [애노테이션 프로세서](애노테이션-프로세서)


### 애노테이션이란?
    Annotation이란 Java 1.5부터 등장한 기능으로 인터페이스를 기반으로 한 문법이다.
    사전적 의미로는 주석인데 주석처럼 코드에 달아 클래스에 특별한 의미를 부여하거나 기능을 주입할 수 있다.
    즉, 프로그램에게 추가적인 정보를 제공해주는 메타 데이터(데이터를 위한 데이터)라고 볼 수 있다.
    
    어노테이션에는 크게 세 가지 종류가 존재하는데 JDK에 내장되어 있는 built-in 어노테이션(ex: @Override),
    어노테이션에 대한 정보를 나타내기 위한 어노테이션인 Meta 어노테이션, 그리고 개발자가 직접 만들어 내는
    Custom 어노테이션이 있다.
    
    어노테이션의 쓰임으로는 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보 제공, 소프트웨어 개발툴이 빌드나 배치시
    코드를 자동으로 생성할 수 있도록 정보 제공, 마지막으로 실행시(런타임시)특정 기능을 실행하도록 정보를 제공등으로 사용할 수 있다.
    
### 애노테이션 정의하는 방법
    ㅇㄹ    

### @retention
    자바 컴파일러가 어노테이션 값들을 언제까지 유지할 것인지, 어느 시점까지 영향을 미칠 것인지를 결정한다.
    보통 어노테이션은 Runtime시에 많이 사용하므로 대부분의 어노테이션의 Retention 값은 RUNTIME으로 되어있다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/retention.png" alt=""> {% endraw %}
- [이미지 출처](https://honeyinfo7.tistory.com/56)

### @Target
    어떠한 값(클래스, 필드, 메서드)에 어노테이션을 적용할 것인지 결정한다.     

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/target.png" alt=""> {% endraw %}
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
```
    

### @documented
    @Documented 어노테이션을 사용하는 클래스의 JavaDoc 에 이 어노테이션의 존재를 표기하도록 지정한다.
    즉 어노테이션은 기본적으로 javadoc에 포함되지 않기 때문에 이 유형의 어노테이션이 javadoc 문서에 포함되어야 함을 나타낸다.
    
### 애노테이션 프로세서
    ㅇ    
    