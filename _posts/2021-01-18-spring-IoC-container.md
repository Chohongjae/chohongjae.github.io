---
title: "Spring IoC Container란?"
categories: 
  - spring
last_modified_at: 2021-01-18T23:00:00+09:00
---

### Spring IoC Container란?
    DI가 가능하기 위해서 우리는 각각의 비즈니스 로직에 따라 DI를 필요로하는 객체들을 서로 연결시켜줘야 한다.
    하지만 이러한 연결에 대해 이해하기 전에 DI를 필요로하는 객체들은 어디에 위치해야 할까?
    그 곳이 바로 Spring Container이다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118스프링컨테이너/container.png" alt=""> {% endraw %}
- [이미지 출처](https://medium.com/lifeinhurry/what-is-spring-container-spring-core-9f6755966fe9)
    
    
    
    Spring Container는 Spring Framework의 핵심이다.
    컨테이너는 객체(Bean)를 만들고, 연결하고, 구성하고, 생성부터 파괴까지 전체 수명주기를 관리하는 컨테이너, 통, 그릇이라고 볼 수 있다.
    DI(의존성 주입)는 IOC 컨테이너 안에 있는 빈들끼리만 가능하기 때문에 이러한 컨테이너를 통해
    시스템 전반에서 언제든지 빈에 대한 사용이 가능하다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118스프링컨테이너/container2.png" alt=""> {% endraw %}
- [이미지 출처](https://private.tistory.com/39)
    
    이러한 스프링 컨테이너는 두가지 종류로 구분될 수 있다.
    
    
    
### Bean Factories
    영어 그대로 빈 공장이다.
    기본적인 DI를 제공하는 컨테이너의 기본 타입으로 빈 객체를 생성하고 관리한다.
    org.springframework.beans.factory.BeanFactory에 정의되어 있다.

    
### ApplicationContext
    Bean Factories와 유사하지만 향상된 형태의 컨테이너로서 다음과 같은 추가 기능을 제공한다. 
        - 국제화 지원 텍스트 메시지 관리
        - 이미지 파일 로드
        - 리스너로 등록된 빈에게 이벤트 발생 통보
    
```text
스프링은 다양한 타입의 Application Context를 제공하는데 요즘의 자바 어플리케이션은 어노테이션을 사용하는 것이 표준으로
자리잡아가고 있다. 그래서 우리는 대부분 컴포넌트를 구성하기 위해서 어노테이션을 사용하고 그것은 ApplicationContext 중에서도
AnnotationConfigApplicationContext을 로딩한다.
```

```java
ApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
context.getBeanDefinitionNames()
```

    위의 코드와 같이 applicationContext를 사용하여 우리는 Spring IoC Container에 있는 빈들을 가져올 수 있다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210118스프링컨테이너/container3.png" alt=""> {% endraw %}
- [이미지 출처](https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/beans.html)

    
    위의 그림은 어떻게 스프링이 작동하는지에 대해 설명하고 있다.
    우리가 작성한 POJO 클래스들이 Configuration Metadata와 결합되고,
    다음으로 ApplicationContext가 생성되고 초기화되면서 실행가능한 스프링 어플리케이션은 구동되게 된다. 


### Bean의 라이프사이클
    InitializingBean, DisposableBean 이 인터페이스들을 구현하게 되면 빈 초기화 과정과 빈의 소멸 과정을 처리할 수 있다.
    또한 해당 인터페이스의 구현이 아니라 @PostConstruct, @PreDestroy를 붙인 메소드를 작성해도 동일한 과정을 처리할 수 있다. 
        
    