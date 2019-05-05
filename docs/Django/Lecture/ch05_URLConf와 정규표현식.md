# URLConf와 정규 표현식

- 클라이언트에서 POST로 넘어온 request를 처리할 때 
    - content_type이 application/x-www-form-urlencoded 인 경우 request.POST 사용
    - content_type이 application/json 인 경우 request.body 사용
    
- 요청이 들어오면 우선 urlpatterns상의 리스트를 처음부터 순차적으로 훑으며 url 매칭을 시도함.
<br>매칭되는 다수의 패턴이 있더라도 처음 발견되는 url로 매칭된다.

- import url -> Django 1.xx 스타일 <br> import path, re_path -> Django 2.xx 스타일 

- path에서는 기본지원되는 path converters(ex: '<'int:year'>')를 통해 정규표현식을 간소화 할 수 있다.
<br>정규표현식을 '<'int:year'>' 이렇게 간략화 한다. 이런 형태는 숫자가 1회 이상 반복된다는 뜻! <br>
path는 정규표현식을 사용하지 않음. 횟수를 한정하고 싶으면 정규표현식을 사용한다.
<br>path일떄는 매핑된 converter의 to_python에 맞게 변환된 값이 전달된다.
<br>re_path에서는 1.xx 버전 그대로 정규표현식을 사용하고 모두 str 형태로 넘어간다.
<br>자주 사용되는 복잡한 패턴은 converter로 등록해서 재사용 가능

- 모든 url 끝에는 /를 붙여야하는 것이 장고의 규칙!

- 프로젝트를 처음 시작할때의 규칙으로 
장고 앱을생성할때 url_patterns 위에 app_name = '앱이름' 을 넣어준다.
<br>현재 url_pattern에 대한 이름을정해주고 URL_REVERSE에서 사용하는데 
view에서 url_reverse를 사용해서<br> url의 네임으로 리다이렉트할 때 사용된다!
- view에서는 return이 아닌 raise 혹은 assert로 error를 반환해도 된다.