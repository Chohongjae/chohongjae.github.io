# HTTP의 GET과 POST 비교
- 둘 다 HTTP 프로토콜을 이용해서 서버에 무엇인가를 요청할 때 사용하는 방식이다.<br>
하지만 둘의 특징을 제대로 이해하여 기술의 목적에 맞게 알맞은 용도에 사용해야한다.

## GET
- 우선 GET 방식은 요청하는 데이터가 url 에 담겨서 전송된다.<br>
 때문에 url 상에 ? 뒤에 데이터가 붙어 request 를 보내게 되는 것이다. 이러한 방식은 url 이라는 공간에 담겨가기<br>
 때문에 전송할 수 있는 데이터의 크기가 제한적이다. 또 보안이 필요한 데이터에 대해서는 데이터가 그대로 url 에 노출되므로<br>
 GET방식은 적절하지 않다. (ex. password)

## POST
- POST 방식의 request 는 HTTP Message의 Body 부분에 데이터가 담겨서 전송된다.<br>
 때문에 바이너리 데이터를 요청하는 경우 POST 방식으로 보내야 하는 것처럼 데이터 크기가 GET 방식보다<br>
 크고 보안면에서 낫다.(하지만 보안적인 측면에서는 암호화를 하지 않는 이상 고만고만하다.)

<br>
- 그렇다면 이러한 특성을 이해한 뒤에는 어디에 적용되는지를 알아봐야 그 차이를 극명하게 이해할 수 있다.<br>
 우선 GET 은 가져오는 것이다. 서버에서 어떤 데이터를 가져와서 보여준다거나 하는 용도이지 서버의 값이나 상태 등을 변경하지 않는다.<br>
 이러한 개념을 멱등성이라 한다. SELECT 적인 성향을 갖고 있다고 볼 수 있는 것이다. 
 
- 반면에 POST 는 서버의 값이나 상태를 변경하기 위해서 또는 추가하기 위해서 사용된다.

- 부수적인 차이점을 좀 더 살펴보자면 GET 방식의 요청은 브라우저에서 Caching 할 수 있다.<br>
때문에 GET 방식으로 요청한다면 기존에 caching 되었던 데이터가 응답될 가능성이 존재한다.

## PUT
- 전체 업데이트

## PATCH
- 부분 업데이트


# HTTP와 HTTPS
- HTTP 의 문제점


            1.HTTP 는 평문 통신이기 때문에 도청이 가능하다.
            2.통신 상대를 확인하지 않기 때문에 위장이 가능하다.
            3.완전성을 증명할 수 없기 때문에 변조가 가능하다.
            위 세 가지는 다른 암호화하지 않은 프로토콜에도 공통되는 문제점들이다.

## 보안 방법
- 통신 자체를 암호화 SSL(Secure Socket Layer) or TLS(Transport Layer Security)라는 다른 프로토콜을<br>
조합함으로써 HTTP 의 통신 내용을 암호화할 수 있다. SSL 을 조합한 HTTP 를<br>
HTTPS(HTTP Secure) or HTTP over SSL이라고 부른다.


## HTTPS
- HTTP 에 암호화와 인증, 그리고 완전성 보호를 더한 HTTPS
- HTTPS는 SSL 의 껍질을 덮어쓴 HTTP 라고 할 수 있다. 즉, HTTPS 는 새로운 애플리케이션 계층의 프로토콜이 아니라는 것이다.<br>
HTTP 통신하는 소켓 부분을 SSL(Secure Socket Layer) or TLS(Transport Layer Security)라는 프로토콜로 대체하는 것 뿐이다.<br>
HTTP 는 원래 TCP 와 직접 통신했지만, HTTPS 에서 HTTP 는 SSL 과 통신하고 SSL 이 TCP 와 통신 하게 된다.<br>
SSL 을 사용한 HTTPS 는 암호화와 증명서, 안전성 보호를 이용할 수 있게 된다.

## 모든 웹 페이지에서 HTTPS 를 사용하지 않는 이유
- 평문 통신에 비해서 암호화 통신은 CPU 나 메모리 등 리소스가 많이 필요하다. 통신할 때마다 암호화를 하면 많은 리소스를 소비하기 때문에<br>
서버 한 대당 처리할 수 있는 리퀘스트의 수가 줄어들게 된다. 그렇기 때문에 민감한 정보를 다룰 때만 HTTPS 에 의한 암호화 통신을 사용한다.


# 상태코드

            10x : 정보 확인

            20x : 통신 성공
            200	OK	요청 성공(GET)
            201	Create	생성 성공(POST)
            202	Accepted	요청 접수O, 리소스 처리X
            204	No Contents	요청 성공O, 내용 없음

            30x : 리다이렉트
            300	Multiple Choice	요청 URI에 여러 리소스가 존재
            301	Move Permanently	요청 URI가 새 위치로 옮겨감
            304	Not Modified	요청 URI의 내용이 변경X

            40x : 클라이언트 오류
            400	Bad Request	API에서 정의되지 않은 요청 들어옴
            401	Unauthorized	인증 오류
            403	Forbidden	권한 밖의 접근 시도
            404	Not Found	요청 URI에 대한 리소스 존재X

            50x : 서버 오류
            500	Internal Server Error	서버 내부 오류