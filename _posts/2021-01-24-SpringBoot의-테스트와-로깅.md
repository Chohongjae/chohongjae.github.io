---
title: "SpringBoot의 테스트와 로깅"
categories: 
  - spring
last_modified_at: 2021-01-24T23:10:00+09:00
---

### @SpringBootTest
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210124springBoot의테스트/springboottest.png" alt=""> {% endraw %}
    
    테스트 클래스 상단에 있는 @SpringBootTest 어노테이션은 메인 클래스에 선언된 @SpringBootApplication과 비슷한 어노테이션이다.
    사용자가 작성한 빈과 자동설정 빈들을 모두 초기화하듯이 @SpringBootTest 역시 테스트 케이스가 실행될 때
    테스트에 필요한 모든 설정과 빈들을 자동으로 초기화해준다.
    
    @SpringBootTest는 여러 속성을 가질 수 있는데, 각 속성의 의미는 다음과 같다.
    
- properties : 테스트가 실행되기 전에 테스트에 사용할 프로퍼티들을 'key=value' 형태로 추가하거나 properties 파일에 설정된 프로퍼티를 재정의한다.
- classes : 테스트할 클래스들을 등록한다. 만일 classes 속성을 생략하면 애플리케이션에 정의된 모든 빈들을 생성한다.
- webEnvironment : 애플리케이션이 실행될때, 웹과 관련된 환경을 설정할 수 있다. webEnvironment가 가지고 있는 상수와 의미를 알아보자.
    - MOCK : 모킹된 서블릿 컨테이너를 제공하기 때문에 내장 톰캣이 구동되지 않는다. 모킹된 서블릿 컨테이너를 사용해 컨트롤러를 테스트할 수 있다.
    - RANDOM_PORT : 랜덤한 포트로 내장 톰캣을 구동하여 실제 서블릿 컨테이너를 초기화한다. 정상적인 서블릿 테스트가 가능해 더 이상 목 객체를 사용할 수 없다.(하여 TestRestTemplate 객체 사용)
    - DEFINED_PORT : application.properties 파일에 설정된 서버 포트를 사용한다.
    - NONE : 서블릿 기반의 환경자체를 구성하지 않는다.
    

### 스프링 부트 로깅
    스프링 부트는 SLF4J라는 퍼사드를 이용하여 로그를 관리한다.
    퍼사드는 GoF 디자인 패턴 중 하나로서 복잡한 서브 시스템을 쉽게 사용할 수 있도록 간단하고 통일된 인터페이스를 제공한다.
    스프링 부트는 logging 스타터를 이용하여 Log4j, Logback등을 SLF4J의 구현체로 가지고 있고,
    이 중에서 Logback을 이용하여 로그를 출력한다.    
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210124springBoot의테스트/log.png" alt=""> {% endraw %}