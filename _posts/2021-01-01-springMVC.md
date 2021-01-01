---
title: "spring MVC란?"
categories: 
  - spring
last_modified_at: 2021-01-01T01:00:00+09:00
---
### Spring MVC
    spring MVC란 Front Controller Pattern에 기초한 spring 프레임워크에서 제공하는 웹 모듈이다.
    MVC 패턴에 기초하여 웹 프로그래밍을 할 수 있게 해주는 프레임워크인 것이다. 
    
- Model : 모델은 뷰가 렌더링하는데 필요한 데이터이다. 예를 들어 사용자가 요청한 상품 목록이나, 주문 내역이 이에 해당된다.
- View : 웹 어플리케이션에서 뷰(View)는 실제로 보이는 부분이며, 모델을 사용해 렌더링한다. 뷰는 JSP, JSF, PDF, XML등으로 결과를 표현한다.
- Controller : 컨트롤러는 사용자의 액션에 응답하는 컴포넌트다. 컨트롤러는 모델을 업데이트하고, 다른 액션들을 수행한다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210101spring/spring-mvc-model2.png" alt=""> {% endraw %}

### Spring MVC 아키텍처 흐름
    클라이언트가 보내는 모든 요청을 Front Controller라는 Servlet Class가 받아서
    Controller Class(또는 handler Class)에게 위임한다. 
    (Front Controller는 딱 하나만 존재하며, 요청만 받고 실제 일은 처리하지 않음)
    
    요청의 실제 처리는 Controller Class에게 위임함으로써, 관련된 URL은 하나의 Class에서 처리하도록 한다.
    Controller가 자바 bean 등을 이용해서 결과를 만들어내고,
    만들어진 결과를 Model에 담아서 Front Controller에게 보내면
    Front Controller가 알맞은 View에게 Model을 전달해서 결과를 출력한다.


### 실제 동작 흐름
    요청 -> 프론트 컨트롤러 -> 핸들러 매핑 -> 핸들러 어댑터 -> 컨트롤러 -> 로직 수행(서비스) -> 컨트롤러 -> 뷰 리졸버 -> 응답(jsp, html)

1. 클라이언트의 요청을 DispatcherServlet이 맨 앞단에서 받는다.
    
        SpringMVC에서 가장 중추적인 역할을 담당한다고 할 수 있는데, 클라이언트의 모든 Request를 맨 앞단에서 접수'만' 한다.
        Front Controller의 역할을 하고 있는 것이고, dispatch의 뜻은 '보내다, 파견하다'인데
        즉, 클라이언트의 모든 요청을 받아들여서 그 일에 대한 처리를
        다른 전문가들에게 보내서 위임하는 역할을 하는 컨트롤러이다.
        
        또한 본격적으로 로직에 들어오기 전에, 요청에 대한 선처리 작업을 수행한다.
        ex. 지역 정보 결정, 멀티파트 파일 업로드 처리 등

2. 그러면 DispatcherServlet이 HandlerMapping에게 그 요청을 보내고, HandlerMapping은 그 일을 해줄 Controller를 찾는다.
  
        프론트 컨트롤러는 요청을 핸들러 매핑을 통해 해당 요청을 어떤 핸들러가 처리해야하는지를 매핑한다.
        즉, HandlerMapping은 사용자의 Request를 처리할 Controller가 누구인지 DispatcherServlet에게 알려준다.
        
3. 그러고나서 HandlerMapping은 DispatcherServlet에게 그 Controller를 알려주고,
        
        HandlerMapping 객체가 핸들러 매핑에 대한 정보를 담고있다.

4. DispatcherServlet은 HandlerAdapter에게 찾은 Controller의 어떤 메서드를 쓸건지 HandlerAdapter에게 물어본다.
   HandlerAdapter 는 Controller 에 있는 메소드를 찾고,
   
        이렇게 매핑된 핸들러를 실제로 실행하는 역할은 핸들러 어댑터가 담당한다.
        즉, HandlerAdapter는 사용자의 request를 처리해줄 Controller를 "호출"하고 "결과를 받아온다".

5. Controller는 그 메서드를 수행한다. 이때 Service, DAO 등의 객체를 이용해 비즈니스 로직을 처리한다.

        컨트롤러는 해당 요청을 처리하는 로직을 담고있다.
        보통 요청의 종류 혹은 로직의 분류에 따라 내부적으로 Service 단위로 나누어 모듈화 한다.
        각 서비스에서는 DB 접근할 수 있는 Repository 객체를 이용하여 데이터에 접근할 수 있다.

6. 찾은 메서드로 작업을 하고나면 결과를 HandlerAdapter에게 보내주고, ModelAndView를 이용해서 데이터(Model)와 View 이름을 리턴한다.

7. HandlerAdapter는 그 값을 DispatcherServlet에게 리턴하고 다시 ViewResolver에게 View 이름을 통해 View를 찾게한다.

8. ViewResolver은 View 이름을 통해 해당하는 View 를 찾고, 그 View에서는 만들어진 데이터(Model) 값으로 화면의 내용을 구성해서 클라이언트에게 보여준다.

        즉, ViewResolver는 사용자의 요청에 적합한 View를 찾아서 반환하고 결과를 보여줄 수 있게 한다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210101spring/springmvc.png" alt=""> {% endraw %}
    
    위의 그림은 SpringMVC의 실제 동작 흐름이고 파란색으로 색칠된 영역은 이미 스프링이 만들어 놓은 부분이고
    보라색과 떄때로 연두색 부분만 개발자가 작성하면 된다.  
    
### 정리
    Spring MVC 프레임워크는 디커플된 웹 애플리케이션 개발 방법을 제공한다. 
    Dispatcher Servlet, ModelAndView, View Resolver 와 같은 단순개념을 이용해서
    웹 애플리케이션 개발을 쉽게 할 수 있도록 해준다.