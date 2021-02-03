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
- [@Retention](@Retention)
- [@Target](@Target)
- [@documented](@documented)
- [애노테이션 프로세서](애노테이션-프로세서)


## 애노테이션이란?
    Annotation이란 Java 1.5부터 등장한 기능으로 인터페이스를 기반으로 한 문법이다.
    사전적 의미로는 주석인데 주석처럼 코드에 달아 클래스에 특별한 의미를 부여하거나 기능을 주입할 수 있다.
    즉, 프로그램에게 추가적인 정보를 제공해주는 메타 데이터(데이터를 위한 데이터)라고 볼 수 있다.
    
    어노테이션에는 크게 세 가지 종류가 존재한다.
    1. JDK에 내장되어 있는 built-in 어노테이션(ex: @Override, @Deprecated)
    2. 어노테이션에 대한 정보를 나타내기 위한 어노테이션인 Meta 어노테이션
    3. 그리고 개발자가 직접 만들어 내는 Custom 어노테이션이 있다.
    
    어노테이션의 쓰임으로는 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보 제공,
    소프트웨어 개발툴이 빌드나 배치시 코드를 자동으로 생성할 수 있도록 정보 제공,
    마지막으로 실행시(런타임시)특정 기능을 실행하도록 정보를 제공등으로 사용할 수 있다.
    
    어노테이션을 사용하면 AOP(Aspect Oriented Programming)을 편리하게 구성할 수 있다.

    
## 애노테이션 정의하는 방법
    

## @Retention
    자바 컴파일러가 어노테이션 값들을 언제까지 유지할 것인지, 어느 시점까지 영향을 미칠 것인지를 결정한다.
    보통 어노테이션은 Runtime시에 많이 사용하므로 대부분의 어노테이션의 Retention 값은 RUNTIME으로 되어있다.
    즉 어노테이션의 LifeTime이다.

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
    즉 적용할 위치를 결정한다.     

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
```

> 메소드에 어노테이션을 적용하고 바이트 코드 파일까지 어노테이션 정보를 유지하며 리플렉션을 이용해서 런타임에 어노테이션 정보를 얻어올 수 있다.
{: style="font-size: 80%;"}

## @documented
    @Documented 어노테이션을 사용하는 클래스의 JavaDoc에 이 어노테이션의 존재를 표기하도록 지정한다.
    즉 어노테이션은 기본적으로 JavaDoc에 포함되지 않기 때문에 @Doucmented가 달려있는 어노테이션을 사용하는 클래스의 
    JavaDoc을 생성할때 해당 어노테이션도 JavaDoc에 문서에 포함되어야함을 나타낸다.

### @Doucmented가 달린 어노테이션을 사용하는 클래스의 @JavaDoc

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented3.png" width="50%" alt=""> {% endraw %}
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented5.png" width="95%" alt=""> {% endraw %}

### @Doucmented가 달리지 않은 어노테이션을 사용하는 클래스의 @JavaDoc

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented.png" width="50%" alt=""> {% endraw %}
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210202livestudyweek12/documented4.png" width="95%" alt=""> {% endraw %}     
    
## 애노테이션 프로세서
    
    