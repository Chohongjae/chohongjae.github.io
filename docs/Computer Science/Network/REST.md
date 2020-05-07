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