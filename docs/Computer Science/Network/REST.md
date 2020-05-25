# REST 란?

- REST 란 “Representational State Transfer” 의 약자이다. 월드 와이드 웹과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 아키텍처의 한 형식이다.<br>
이런 REST의 형식을 잘 따른 시스템을 RESTful 이라고 부른다.
- 한 줄로 HTTP URI 를 통해 자원을 명시하고 HTTP Method를 통해 해당 자원의 대한 CRUD Operation을 적용한 아키텍처라고 할 수 있다.


            URI는 인터넷 상의 자원을 식별하기 위한 문자열의 구성쯤으로 해석 될 수 있겠다.
            http://en.wikipedia.org/wiki/URL
            URI의 한 형태인 URL은 인터넷 상의 "자원 위치"를 나타낸다.

            URL는 URI의 한 형태로, 바꿔 말하면 URI는 URL을 포함 하는 개념이다.
            (URI > URL)
            '자원의 위치'라는 것은 결국은 '하나의 파일 위치'를 나타내는 것임을 명심하자.

            http://img0.gmodules.com/ig/images/korea/logo.gif
            이와 같은 형식은 logo.gif라는 인터넷상의 자원 위치를 의미 한다.
            이는 URI이면서도 URL라고 말할 수 있다.

            http://endic.naver.com/endic.nhn?docid=1232950
            여기서 URL은 endic.nhn의 위치를 표기한 http://endic.naver.com/endic.nhn 까지이다.
            내가 원하는 정보에 도달 하기위해서는 ?docid=1232950라는 식별자(Identifier)가 필요한 것이다.


- Restful 하기 위해서는 아키텍처 스타일에 맞는 제약조건을 만족해야 한다. 즉 REST라는 아키텍처 스타일이 있는거고<br>
RESTful API라는 말은 REST 아키텍처 원칙을 모두 만족하는 API라는 뜻이다.<br>

            
            1. Client/Server
            
            2. Stateless : 각 요청에 클라이언트의 context가 서버에 저장되어서는 안된다.
            
            3. Cacheable : 클라이언트는 응답을 캐싱할 수 있어야 한다.
            
            4. Layered System : 클라이언트는 서버에 직접 연결되었는지 미들웨어에 연결되었는지 알 필요가 없어야 한다.
            
            5. Code on demand(option) : 서버에서 코드를 클라이언트에게 보내서 실행하게 할 수 있어야 한다.
            
            6. uniform interface : 1) 자원은 유일하게 식별가능해야하고, 2) HTTP Method로 표현을 담아야 하고, 
            3) 메세지는 스스로를 설명(self-descriptive)해야하고, 4) 하이퍼링크를 통해서 애플리케이션의 상태가 전이(HATEOAS)되어야 한다.
            
            왜 uniform interface에 강조가 되어있냐면, 1~5번의 제약 조건은 HTTP를 기반으로하는 REST는 HTTP에서 이미
            충분히 지켜지고 있는 부분이라서 비교적 덜 주의를 기울여도 된다.
            
            즉 메세지 스스로 메세지에 대한 설명, 메세지만 보고도 클라이언트는 해석이 가능해야 하고
            하이퍼미디어 링크를 통해 애플리케이션 상태 변화가 가능해야 한다.
            (링크를 전달해서 클라이언트에서 해당 링크로 요청을 보낼 수 있어야 한다.)
            RESTful하려면 저 uniform interface를 잘 지켜야 한다.
          
            그렇지 않으면 Rest api가 아닌 Web api, http api가 맞는 표현이다.





## REST 구성요소
- 자원(Resource) , URI
    - 모든 자원은 고유한 ID를 가지고 ID는 서버에 존재하고 클라이언트는 각 자원의 상태를 조작하기 위해 요청을 보낸다.<br>
     HTTP에서 이러한 자원을 구별하는 ID는 ‘Students/1’ 같은 HTTP URI 이다.
              
- 행위(Verb) , Method
    - 클라이언트는 URI를 이용해 자원을 지정하고 자원을 조작하기 위해 Method를 사용한다.<br>
     HTTP 프로토콜에서는 GET , POST , PUT , DELETE 같은 Method를 제공한다.
- 표현(Representation)
    - 클라이언트가 서버로 요청을 보냈을 때 서버가 응답으로 보내주는 자원의 상태를 Representation이라고 한다.<br>
     REST에서 하나의 자원은 JSON , XML , TEXT , RSS 등 여러형태의 Representation으로 나타낼수 있다.




## REST의 장단점
- 장점
    - 쉬운 사용
    - HTTP 프로토콜 인프라를 그대로 사용하므로 별도의 인프라를 구축할 필요가 없다.
    - 클라이언트-서버 역할의 명확한 분리
    - 클라이언트는 REST API를 통해 서버와 정보를 주고받는다. REST의 특징인 Stateless에 따라 서버는 클라이언트의 Context를 유지할 필요가 없다.
    - 특정 데이터 표현을 사용가능
    - REST API는 헤더 부분에 URI 처리 메소드를 명시하고 필요한 실제 데이터를 ‘body’에 표현할 수 있도록 분리시켰다.<br>
     JSON , XML 등 원하는 Representation 언어로 사용 가능하다.
- 단점
    - 메소드의 한계
    - REST는 HTTP 메소드를 이용하여 URI를 표현한다. 이러한 표현은 쉬운 사용이 가능하다는 장점이 있지만 반대로 메소드 형태가 제한적인 단점이 있다.
    - 표준이 없음
    - REST는 설계 가이드 일 뿐이지 표준이 아니다. 명확한 표준이 없다.