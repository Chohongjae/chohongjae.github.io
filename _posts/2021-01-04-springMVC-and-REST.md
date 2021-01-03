---
title: "springMVC와 REST"
categories: 
  - spring
last_modified_at: 2021-01-04T01:00:00+09:00
---

    Spring의 annotation 기반 MVC 프레임워크는 RESTful한 웹서비스를 만드는 과정을 단수화한다.
    전통적인 SpringMVC 컨트롤러와 RESTful 웹서비스 컨트롤러의 차이는 HTTP Response body가 생성되는 방식이다.
    전통적인 MVC 컨트롤러는 ViewResolver등을 통해 View 기술에 의존하지만
    RESTful 웹서비스 컨트롤러는 단순히 객체를 반환하고 객체 데이터는 json/xml로 http 응답에 직접 작성된다.
                       
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210104sprinmvcandrest/springmvc.png" alt=""> {% endraw %}
- 전통적인 SpringMVC의 동작 흐름
- [출처](https://www.genuitec.com/spring-frameworkrestcontroller-vs-controller/)
- [동작 흐름 설명](https://chohongjae.github.io/spring/springMVC/)

{% raw %} <img src="https://chohongjae.github.io/assets/img/20210101spring/spring-controller.png" alt=""> {% endraw %}
- 사용자의 요청이 오면 등록된 ViewResolver를 통해 사용자에게 text/html 타입의 응답을 보내주게 된다.


    또한 Spring 4.0 부터는 @RestController annotation을 사용하여 더욱 단순화된 프로세스가 도입되었다.

### Spring 3.x버전대의 @ResponseBody annotation
    위와 같은 전통적인 방식에서 벗어나 Spring 3.x부터 메소드마다 @ResponseBody annotation을 사용해
    ViewResolver가 해당하는 View를 찾지 않고 컨트롤러에서 직접 반환 값을 자동으로 Http response에 쓰고 반환할 수 있게 되었다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210104sprinmvcandrest/responsebody.png" alt=""> {% endraw %}

    Spring에는 백그라운드에 등록 된 HttpMessageConverters 목록이 있다.
    HTTPMessageConverter의 역할은 미리 정의 된 MIME 유형에 따라 클라이언트로부터 들어온 Request Body를
    특정 클래스로 변환 한 다음 클라이언트에게 다시 Response body로 변환하는 것이다.

### Spring 4.0 부터 도입된 @RestController annotation
    Spring 4.0부터는 @Controller 및 @ResponseBody annotation을 @RestController annotation으로 대체하였다.
    즉 @RestController annotation을 Controller class에 작성하면 더 이상 메소드마다
    @ResponseBody annotation을 작성할 필요가 없다.
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210104sprinmvcandrest/restcontroller.png" alt=""> {% endraw %}
    
    이와 같이 @RestController 를 사용하면 @Controller + @ResponseBody 를 사용했던 것처럼 
    Controller에서 return 되는 값을 View Page를 통해 출력되는 것이 아니라 HTTP ResponseBody에 직접 쓰여 반환되게 된다. 
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20210101spring/spring-rest-controller.png" alt=""> {% endraw %}

### 결론
    - 즉 @Controller 는 View Page를 반환하지만, @RestController는 객체(VO,DTO)를 반환하기만 하면,<br>
     객체데이터는 MessageConverter에 의해서 application/json 형식의 HTTP ResponseBody에 직접 작성되게 된다.

- [출처](https://www.genuitec.com/spring-frameworkrestcontroller-vs-controller/)