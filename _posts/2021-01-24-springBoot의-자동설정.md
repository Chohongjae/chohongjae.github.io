---
title: "SpringBoot의 의존성 관리와 자동설정"
categories: 
  - spring
last_modified_at: 2021-01-24T23:00:00+09:00
---

### 스프링 부트의 자동설정
    우리는 스프링 부트 스타터를 이용하여 프로젝트에 필요한 라이브러리들을 효과적으로 관리할 수 있다.
    하지만 라이브러리만 추가한다고 해서 추가된 모듈을 바로 사용할 수 있는 것은 아니다.
    라이브러리들이 추가되고 나면 추가된 모듈을 사용할 수 있도록 스프링 설정파일에 빈 등록 및 의존성 주입을 적절히 처리해야 한다.
    하지만 스프링 부트는 이런 복잡한 설정을 자동으로 처리해준다.

### 빈(Bean)이란?
    빈은 스프링 IOC 컨테이너에 의해서 관리되는 객체를 스프링 빈이라고 부른다.
    이 객체는 싱글톤으로 생성하여 관리되는데 싱글톤이기 때문에 사용하는측에서 주입받는 빈은 모두 동일한 객체다.
    
    즉 스프링이 관리하는 객체로써 해당 빈들을 스프링이 주입해주기 때문에 우리는 불러서 사용만하면 되는 것이다.
    
### @Configuration
    @Configuration 어노테이션이 달린 클래스 파일은 ComponentScan이 이루어질 때 
    스프링 컨테이너에 해당 클래스가 빈으로 초기화되고, 이 클래스에 @Bean이 달린 메소드의 반환값 클래스도 같이 초기화 된다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210124springBoot의자동설정/configuration.png" alt=""> {% endraw %}        
    
### 자동설정이란?
    스프링 애플리케이션을 실행할 수 있는 수많은 빈들이 자동으로 등록되고 동작한 이유는 @SpringBootApplication 어노테이션에 있다.
    어떻게 스프링부트는 @SpringBootApplication 하나만으로 복잡한 설정들을 대신할 수 있을까?

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210124springBoot의자동설정/springbootapplication.png" alt=""> {% endraw %}
    
    사실은 @SpringBootApplication 이 포함하고 있는 @EnableAutoConfiguration 어노테이션 때문이다.
    @SpringBootApplication은 다음과 같이 복잡한 설정들로 구성되어 있다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210124springBoot의자동설정/springbootapplication2.png" alt=""> {% endraw %}

    그 중에서 우리는 @SpringBootConfiguration, @ComponentScan, @EnableAutoConfiguration에만 집중하면 된다.
    이 중에서 @SpringBootConfiguration 은 기존에 환경설정 빈 클래스를 표현하기 위해 사용했던 @Configuration과 동일하고,
    스프링 부트 환경설정 클래스임을 나타내기 위해 이름만 @SpringBoot를 추가한 @Configuration이다.
    
    우선 @ComponentScan에 대해 알아보자.
    
### @ComponentScan
    @ComponentScan은 스프링 컨테이너 초기화와 관련된 어노테이션이다.
    @Configuration, @Repository, @Service, @Controller, @RestController가 붙은 클래스를
    스프링 컨테이너에서 빈으로 등록하여 관리하는 역할, 해당 객체를 메모리에 올리는 역할을 한다.
    @ComponentScan을 사용하면 해당 어노테이션을 사용한 클래스를 기준으로 "하위" 클래스들을 컴포넌트 스캔하여
    빈으로 등록해서 스프링 컨테이너에서 관리하게 된다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210124springBoot의자동설정/componentscan.png" alt=""> {% endraw %}
    
    위의 사진에서 @ComponentScan 어노테이션이 달린 DemoApplication 클래스가 com.example.demo 패키지에 위치해있으므로
    com.example.demo 패키지 아래에 있는 @Configuration, @Repository, @Service,
    @Controller, @RestController가 붙은 클래스들만 빈으로 등록된다.
    상위 혹은 다른 패키지에 있는 클래스들은 @ComponentScan이 작동하지 않는다.
    
    다음으로 @EnableAutoConfiguration에 대해 알아보자.
    
### @EnableAutoConfiguration
    @EnableAutoConfiguration 이 자동설정과 관련된 어노테이션이다.
    스프링 부트는 스프링 컨테이너를 구동할 때 두 단계로 나누어 객체들을 초기화(생성) 한다.
    이렇게 두 단계로 나누어 빈들을 초기화하는 이유는 애플리케이션을 운영하기 위해서 두 종류의 빈이 필요하기 떄문이다.
    
    예를 들어 웹 어플리케이션에 파일 업로드 기능이 필요할 때, 우리는 MultiPartFile 객체를 이용해서
    업로드 가능한 컨트롤러를 구현해야 한다.
    실제로 파일 업로드 기능이 동작하기 위해서는 사용자가 업로드한 파일 정보가 MultiFile 객체에 
    설정되어야 하며, 이를 위해서 멀티파트 리졸버 객체가 반드시 필요하다.
    
    즉 파일 업로드가 동작하기 위해서는 DispatcherServlet으로부터 요청을 받을
    내가 만든 컨트롤러와 멀티파트 리졸버 객체를 매모리에 올리는 두 개의 객체 생성 과정이 필요한 것이다.
    
    결국 @ComponentScan은 내가 만든 @Controller 혹은 @RestController가 붙은 객체를 메모리에 올리고
    @EnableAutoConfiguration은 CommonsMultipartResolver 같이 스프링 부트가 지원하는 기능들을 제공하는
    객체들을 메모리에 올리는 작업을 처리한다.
    
```text
@EnableAutoConfiguration 어노테이션은 spring-boot-autoconfigure-<버전>.jar 파일에 위치하는데,
해당 파일의 META-INF 폴더에 spring.factories 파일은 스프링 부트의 메타데이터가 기록되어 있고,
스프링 부트는 이 파일의 설정을 참조하여 여러가지 빈을 생성한다. 
```

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210124springBoot의자동설정/spring.factories.png" alt=""> {% endraw %}

    위의 사진과 같이 org.springframework.boot.autoconfigure.EnableAutoConfiguration 이라는 
    키 값으로 많은 환경설정 클래스 파일들이 @Configuration을 가지고 있고 스프링 빈 설정 파일로써 관리된다.

