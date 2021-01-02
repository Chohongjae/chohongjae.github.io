---
title: "Spring Boot vs. Spring MVC vs. Spring 비교"
categories: 
  - spring
last_modified_at: 2021-01-02T23:00:00+09:00
---



***- learn what problems they solve, and where they're best applied.***<br> 
***- The most important thing that you will learn is that Spring, Spring MVC, and Spring Boot are not competing for the same space.***<br>
***- They solve different problems and they solve them very well.***

    Spring, Spring MVC, Spring Boot 는 중복되는 부분을 다루지 않고 각각의 모듈들은
    "서로 다른 문제들"을 해결하면서도 그 문제들을 매우 잘 해결한다.
      
### Spring이 해결하는 핵심 문제는 무엇일까?
    스프링 프레임워크의 가장 중요한 특징은 의존성 주입(Dependency Injection)이다. 
    모든 스프링 모듈들의 핵심에는 의존성 주입이나 IOC(Inversion of Control)가 있다.
    DI 나 IOC 를 적절히 사용하면, 우리는 "느슨하게 결합된 애플리케이션들을 개발"할 수 있기 때문이다.
    또한 느슨하게 결합된 애플리케이션들은 단위테스트를 하기 쉽다. 
    
    또한 스프링 프레임워크의 가장 훌륭한 점은 이미 해결된 문제를 해결하려고 시도하지 않는다는 것이다.
    스프링 프레임워크가 하는 모든 것은 훌륭한 솔루션을 제공하는 프레임워크들을 훌륭하게 통합해 주는 일이다.
    
### Spring MVC 프레임워크가 해결하는 핵심 문제는 무엇일까?
    Spring MVC 프레임워크는 디커플된 웹 애플리케이션 개발 방법을 제공한다.
    Dispatcher Servlet, ModelAndView, View Resolver와 같은 단순개념을 이용해서
    "웹 애플리케이션 개발을 쉽게" 할 수 있도록 해준다.
    
### Spring Boot가 해결하는 핵심 문제는 무엇일까?
    스프링 기반 애플리케이션들은 많은 환경설정을 포함한다.
    예를 들어 우리가 Spring MVC 를 사용할 때 아래와 같이 Component Scan, Dispatcher Servlet,
    View Resolver등에 대한 많은 설정들이 필요하다.
    
```java
<bean
    class="org.springframework.web.servlet.view.InternalResourceViewResolver">
    <property name="prefix">
        <value>/WEB-INF/views/</value>
    </property>
    <property name="suffix">
        <value>.jsp</value>
    </property>
</bean>
<mvc:resources mapping="/webjars/**" location="/webjars/"/>
```

    아래 코드는 웹 애플리케이션에서의 일반적인 디스패쳐 서블릿을 설정을 보여준다.
    
```java
<servlet>
        <servlet-name>dispatcher</servlet-name>
        <servlet-class>
            org.springframework.web.servlet.DispatcherServlet
        </servlet-class>
        <init-param>
            <param-name>contextConfigLocation</param-name>
            <param-value>/WEB-INF/todo-servlet.xml</param-value>
        </init-param>
        <load-on-startup>1</load-on-startup>
    </servlet>
    <servlet-mapping>
        <servlet-name>dispatcher</servlet-name>
        <url-pattern>/</url-pattern>
    </servlet-mapping>
```

    Spring Boot는 이에 대한 새로운 문제의식을 제시한다.
    예를 들어 Spring MVC jar가 애플리케이션에 추가될 때, 우리가 일부 빈들을 자동으로 설정할 수 있을까?
      - Hibernate jar 가 클래스 패스상에 있을 경우 Data Source를 자동으로 구성하는 것은 어떨까?
      - Spring MVC jar 가 클래스 패스상에 있을 경우 Dispatcher Servlet 을 자동으로 구성하는 것은 어떨까?

***Spring boot는 이러한 문제를 해결하기 위해 Auto Configuration 이라 불리는 자동 환경<br>
구성으로 프레임워크로 애플리케이션을 구성하는 데 필요한 기본 구성을 자동으로 제공한다.***<br>
***또한 기본적인 자동 구성을 오버라이드하기 위한 대비도 제공된다.***


    또한 Spring Boot는 starter들을 제공하는데 공식 문서에서는 스타터들에 대해 아래와 같이 기술한다.

***스타터들은 애플리케이션에 포함할 수 있는 편리한 dependency descriptors(의존성 서술자들(?))이다.
샘플 코드를 검색하고 종속성 설명자를 복사하여 붙여 넣을 필요없이 스프링과 관련 기술에 대해 올인원으로 얻을 수 있다.
예를들어 데이터베이스 접근을 위해 JPA를 사용하고 싶다면 프로젝트에 spring-boot-starter-data-jpa 종속성을 포함시키기만 하면 된다.***


### Spring Boot Starter Web을 통한 예시
    Restful 서비스를 구성하기 위해 웹 애플리케이션을 개발하고 싶다며 Spring Boot Start Web을 선택할 수 있다.

```java
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```
    
    위와 같이 종속성을 추가하면 아래와 같이 애플리케이션에 또 다른 종속성들이 자동으로 추가된다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210102spring-springboot-springmvc/spring-boot-start-web.png" alt=""> {% endraw %}    

    종속성들은 다음과 같이 분류 될 수 있다. 
       • Spring: core, beans, context, aop
       • Web MVC: (Spring MVC)
       • Jackson: for JSON Binding
       • Validation: Hibernate Validator, Validation API
       • Embedded Servlet Container: Tomcat
       • Logging: logback, slf4j
       
    보통 웹 애플리케이션은 위 종속성들을 모두 사용할 것이다.
    Spring Boot Starter Web을 사용하면 미리 위와 같은 미리 패키지된 종속성들을 가져와서 사용할 수 있게 해준다.
    따라서 우리는 이 종속성들 및 이것들이 호환하는 버전들에 대해 걱정하지 않아도 된다.
    
### Spring Boot Starter 프로젝트 예시 리스트
    Spring Boot Starter Web 에서 살펴보았듯이 스타터 프로젝트들은 특정 애플리케이션 개발을 빠르게 시작할 수 있도록 도와 준다.
    
- spring-boot-starter-web-services: SOAP Web Services
- spring-boot-starter-web: Web and RESTful applications
- spring-boot-starter-test: Unit testing and Integration Testing
- spring-boot-starter-jdbc: Traditional JDBC
- spring-boot-starter-hateoas: Add HATEOAS features to your services
- spring-boot-starter-security: Authentication and Authorization using Spring Security
- spring-boot-starter-data-jpa: Spring Data JPA with Hibernate
- spring-boot-starter-cache: Enabling Spring Framework’s caching support
- spring-boot-starter-data-rest: Expose Simple REST Services using Spring Data REST
- spring-boot-starter-actuator: 애플리케이션을 추적하거나 모니터링하는 등의 기능을 사용할 수 있도록 해준다. 
- spring-boot-starter-undertow, spring-boot-starter-jetty, spring-boot-starter-tomcat: 내장된 서블릿 컨테이너를 선택할 수 있도록 해준다.(서버가 애플리케이션에 통합되기 때문에 우리는 서버에 설치되는 별도의 애플리케이션 서버를 가질 필요가 없다.)
- spring-boot-starter-logging: logback 을 사용해서 로깅할 수 있도록 해준다.
- spring-boot-starter-log4j2: Log4j2 를 사용해서 로깅할 수 있도록 해준다.

### 결론
    
    
- [출처](https://dzone.com/articles/spring-boot-vs-spring-mvc-vs-spring-how-do-they-compare)