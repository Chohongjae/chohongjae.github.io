---
title: "스프링과 JPA"
categories: 
  - spring
last_modified_at: 2021-01-31T23:00:00+09:00
---

### 스프링과 JPA
    데이터베이스 연동에 사용되는 기술은 전통적인 JDBC에서부터, 스프링 DAO, 마이바티스, 하이버네이트와 같은 ORM에 이르기까지 매우 다양하다.
    이중에서 하이버네이트 같은 ORM은 애플리케이션에서 사용하는 SQL까지도 프레임워크에서 제공하기 때문에
    개발자가 처리해야 할 일들을 엄청나게 줄여준다.
    
    이런 "ORM들을" 보다 쉽게 사용할 수 있도록 표준화 시킨 것이 JPA(java persistence API)이다.    
    즉 JPA는 자바 어플리케이션에서 "ORM을 통해 RDBMS를 사용하는 방식"을 정의한 인터페이스, 하이버네이트는 그러한 JPA의 구현체이다.

    스프링 데이터 JPA는 스프링 부트에서 이런 JPA를 쉽게 사용할 수 있도록 지원하는 모듈이다.
    따라서 스프링 데이터 JPA를 사용하면 JPA를 사용하는데 필요한 라이브러리나 XML 설정은 신경 쓸 필요가 없다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210131spring과jpa/datajpa.png" alt=""> {% endraw %}
- [이미지 출처](https://suhwan.dev/2019/02/24/jpa-vs-hibernate-vs-spring-data-jpa/)


### SQL을 직접 다루는 기술
    데이터베이스 연동 기술은 애플리케이션에서 SQL을 다루는 방식에 따라 구분된다.
    예를 들어 마이바티스 같은 프페임워크는 SQL을 개발자가 직접 XML 파일에 등록해서 사용한다.
    이러한 SQL을 직접 다루는 기술들은 테이블의 작은 변화에도 너무나 많은 코드를 수정해야하는 번거로움이 있다.
    
    반면에 하이버네이트 같은 "ORM"은 프레임워크에서 SQL을 생성하기 때문에 개발자가 직접 SQL에 관여하지 않는다.
    
### JPA 개념
    하이버네이트는 비록 자바 표준은 아니지만 가장 많은 개발자들이 사용하는 ORM이고,
    하이버네이트 개발자들이 중심이 되어 만든 "ORM 표준"이 바로 JPA인 것이다.
    
    JPA가 제공하는 "인터페이스"를 이용하여 데이터베이스의 대한 구현을 처리하면 실제로 실행될때는 JPA를 구현한 구현체가 동작하는 것이고,
    JPA를 구현한 구현체는 하이버네이트, EclipseLink, DataNucleus 등 여러가지가 있는데 
    스프링 부트에서는 기본적으로 하이버네이트를 JPA 구현체로 이용한다.    
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210131spring과jpa/jpa.png" alt=""> {% endraw %}

### JPA의 동작 원리
    JPA는 자바 애플리케이션과 JDBC 사이에 존재하면서 JDBC의 복잡한 절차를 JDBC API를 이용해서 대신 처리해준다.
    따라서 개발자는 JDBC의 복잡한 API를 모르고도 데이터베이스를 사용할 수 있는 것이다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210131spring과jpa/jpa3.png" alt=""> {% endraw %}
- [이미지 출처](https://skyblue300a.tistory.com/7)

### JPA가 제공하는 어노테이션
- Entity : @Entity가 설정된 클래스를 엔티티라하며, 클래스 이름과 동일한 테이블과 매핑된다.(자바 클래스를 JPA가 관리하는 엔티티로 인식하게 한다.)
- Table : 엔티티 이름과 테이블 이름이 다른 경우, name 속성을 사용하여 매핑한다. 같은 경우 생략
- Id : 테이블의 기본 키를 매핑한다. 필수 어노테이션
- GeneratedValue : @Id가 선언된 필드에 기본 키 값을 자동으로 할당한다. 설정된 데이터베이스에 따라 JPA가 옵션을 결정한다.
- Transient : 해당 변수를 테이블의 필드와 매핑되지 않도록 처리한다. 매핑 대상에서 제외한다.
{: style="font-size: 80%;"}

### hibernate.dialect
    우리가 데이터베이스에 연동하기 위해 SQL을 작성할 때 데이터베이스에 따라서 SQL 문법이 약간씩 다르게 된다.
    따라서 데이터베이스에 따라서 SQL을 달리해줘야 하고, 데이터베이스가 변경되면 데이터베이스마다 달라지는 부분을 모두 찾아서 수정해야한다.
    
    하지만 JPA의 가장 큰 장점 중 하나는 특정 데이터베이스에 최적화된 SQL 구문을 특정 데이터베이스에 따라서 자동으로 생성한다는 것이다.
    이렇게 어떤 데이터베이스의 최적화된 SQL을 생성할지에 대한 설정 옵션이 hibernate.dialect 속성이다.
    JPA 구현체가 사용할 dialect 클래스를 지정하는 것이고, 어떤 Dialect가 설정되느냐에 따라 생성되는 SQL이 달라진다.
    즉 해당 속성을 H2Dialect 클래스로 설정하면 H2용 SQL이 만들어지고, OracleDialect 로 변경하면 오라클용 SQL이 만들어진다.


### JPA 구현체 설정
    앞서 말했듯이 JPA는 "다양한 ORM 프레임워크"를 동일한 방법으로 사용하기 위한 인터페이스 불과하다.
    따라서 JPA르 사용했을 때 실질적으로 기능을 제공할 JPA 구현체에 대한 설정이 반드시 필요하다.
    스프링 부트에서는 기본적으로 JPA의 구현체로 Hibernate를 사용하고 Hibernate에 대한 추가 설정은
    application.properties 파일등에서 가능하다.
 
- hibernate.show_sql : 하이버네이트가 생성한 SQL을 콘솔에 출력한다.
- hibernate.format_sql : 생성한 SQL을 출력할 때, 보기 좋은 포멧으로 출력한다.
- hibernate.id.new_generator_mappings : 키 생성 전략을 사용한다. (테이블의 키값을 자동으로 증가시키려면, true로 설정한다.)
- hibernate.hbm2ddl.auto : 테이블 생성이나 변경, 삭제 같은 DDL 구문을 자동으로 실행할지 지정한다.
    - create : 애플리케이션을 실행할 때, 기존 테이블을 삭제하고 엔티티에 설정된 매핑 정보를 참조하여 새로운 테이블을 생성한다.
    - create-drop : create와 같지만 애플리케이션이 종료되기 직전에 생성된 테이블을 삭제한다. (삭제->생성->삭제)
    - update : 기존에 사용중인 테이블이 있으면 테이블을 생성하지 않고 재사용한다. 없을 때만 새롭게 생성한다. 매핑 설정이 변경되면 변경된 내용만 업데이트한다.
{: style="font-size: 80%;"}
    
    
    
    