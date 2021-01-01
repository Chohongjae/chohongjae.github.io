---
title: "spring MVC란?"
categories: 
  - spring
last_modified_at: 2021-01-01T01:00:00+09:00
---

# Spring MVC
    spring MVC란 Front Controller Pattern에 기초한 spring 프레임워크에서 제공하는 웹 모듈이다.
    MVC 패턴에 기초하여 웹 프로그래밍을 할 수 있게 해주는 프레임워크인 것이다. 
    
- Model : 모델은 뷰가 렌더링하는데 필요한 데이터이다. 예를 들어 사용자가 요청한 상품 목록이나, 주문 내역이 이에 해당된다.
- View : 웹 어플리케이션에서 뷰(View)는 실제로 보이는 부분이며, 모델을 사용해 렌더링한다. 뷰는 JSP, JSF, PDF, XML등으로 결과를 표현한다.
- Controller : 컨트롤러는 사용자의 액션에 응답하는 컴포넌트다. 컨트롤러는 모델을 업데이트하고, 다른 액션들을 수행한다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210101spring/spring-mvc-model2.png" alt=""> {% endraw %}
- Spring MVC의 아키텍쳐
- [이미지 출처](https://www.edwith.org/boostcourse-web/lecture/16762)

- Spring MVC(MVC Model2)의 아키텍쳐

        클라이언트가 보내는 모든 요청을 Front Controller라는 Servlet Class가 받아서
        Controller Class(또는 handler Class)에게 위임한다.(Front Controller는 딱 하나만 존재하며, 요청만 받고 실제 일은 처리하지 않음)
        요청의 실제 처리는 Controller Class(또는 handler Class)에게 위임함으로써, 관련된 URL은 하나의 Class에서 처리하도록 한다.
        Controller가 자바 bean 등을 이용해서 결과를 만들어내고, 만들어진 결과를 Model에 담아서 Front Controller에게 보내면
        Front Controller가 알맞은 View에게 Model을 전달해서 결과를 출력한다.
        Model2의 발전된 형태가 Spring framework의 모듈중 하나인 Web Module에 구현되어있다.
        이러한 Web Module을 Spring MVC라고 한다.
