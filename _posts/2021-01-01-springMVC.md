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
    
        컨트롤러 중에서도, 맨 앞단에서 유저의 유청을 받는 컨트롤러를 프론트 컨트롤러라고 한다.
        DispatcherServlet 객체가 이 역할을 한다.
        본격적으로 로직에 들어오기 전에, 요청에 대한 선처리 작업을 수행한다.
        ex. 지역 정보 결정, 멀티파트 파일 업로드 처리 등

2. 그러면 DispatcherServlet이 HandlerMapping에게 그 요청을 보내고, HandlerMapping은 그 일을 해줄 Controller를 찾는다.
  
        프론트 컨트롤러는 요청을 핸들러 매핑을 통해 해당 요청을 어떤 핸들러가 처리해야하는지를 매핑한다.
        
3. 그러고나서 HandlerMapping은 DispatcherServlet에게 그 Controller를 알려주고,
        
        HandlerMapping 객체가 핸들러 매핑에 대한 정보를 담고있다.

4. DispatcherServlet은 HandlerAdapter에게 찾은 Controller의 어떤 메서드를 쓸건지 HandlerAdapter에게 물어본다.
   HandlerAdapter 는 Controller 에 있는 메소드를 찾고,
   
        이렇게 매핑된 핸들러를 실제로 실행하는 역할은 핸들러 어댑터가 담당한다.
        HandlerAdapter 객체가 이 역할을 한다.

5. Controller는 그 메서드를 수행한다. 이때 Service, DAO 등의 객체를 이용해 DB작업을 보통한다.

        컨트롤러는 해당 요청을 처리하는 로직을 담고있다.
        보통 요청의 종류 혹은 로직의 분류에 따라 내부적으로 Service 단위로 나누어 모듈화 한다.
        각 서비스에서는 DB 접근할 수 있는 Repository 객체를 이용하여 데이터에 접근할 수 있다.

6. 찾은 메서드로 작업을 하고나면 결과를 HandlerAdapter에게 보내주는데, 이때 보통 ModelAndView라는 놈을 이용해서
데이터(Model) 와 View 이름을 리턴해준다.

7. HandlerAdapter는 그 값을 DispatcherServlet에게 리턴해준다.

8. DispatcherServlet이 View 이름을 ViewResolver에게 주고 이름을 통해 View를 찾게한다.

9. ViewResolver은 해당하는 View 를 찾고 , 그 View에서는 만들어진 데이터(Model) 값으로 화면의 내용을 구성해서 클라이언트에게 보여준다.

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210101spring/springmvc.png" alt=""> {% endraw %}

