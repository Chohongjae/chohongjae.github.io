---
title: "독립적으로 실행가능한 JAR"
categories: 
  - spring
last_modified_at: 2021-01-24T23:10:00+09:00
---

### JAR 파일 하나로 실행
    스프링 부트로 작성한 어플리케이션을 빌드하여 jar파일로 생성한 후 압축을 해제하면 lib 폴더에
    dependency로 등록된 모든 라이브러리들이 jar파일로 들어있는 것을 확인할 수 있다.
    기본적으로 JAR 파일은 또 다른 JAR 파일을 포함할 수 없다.

### 과거에는 "uber" jar 사용    
    JAR 파일들이 제공하는 클래스들을 굳이 사용하고 싶다면 JAR 파일들을 모두 압축 해제하고
    특정 폴더에 통합한 다음 다시 JAR파일로 압축하면 된다. 
    하지만 이런식으로 JAR파일을 관리한다면 파일이 많아질수록 관리하기가 복잡해질 것이다.

### 스프링 부트의 전략    
    스프링 부트는 패키징된 JAR 파일 안에 있는 또 다른 JAR 파일을 읽어서 클래스들을 로딩하는 유틸리티 클래스를 제공한다.

- org.springframework.boot.loader.jar.jarFile 이라는 로더 클래스가 애플리케이션에서 
lib 폴더에 있는 수 많은 JAR 파일들을 사용할 수 있도록 로딩해주는 역할을 한다.
- org.springframework.boot.loader.Launcher 클래스가 우리의 main 메소드를 가지고 있는 클래스를 실행한다.
