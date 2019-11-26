# URLConf와 정규 표현식

- import url -> Django 1.xx 스타일 <br> 
  import path, re_path -> Django 2.xx 스타일

- 모든 url 끝에는 / 를 붙여야하는 것이 장고의 규칙이다.
- 프로젝트/settings.py에서 최상위 URLConf 모듈을 지정("ROOT_URLCONF") 한다.
    - 최초의 urlpattrns로부터 inclue를 통해, TREE 구조로 확장된다.
- 요청이 들어오면 우선 urlpatterns상의 리스트를 처음부터 순차적으로 훑으며 url 매칭을 시도한다.
  - 매칭되는 다수의 패턴이 있더라도 처음 발견되는 url로 매칭된다.
  - 매칭되는 URL이 없을 경우, 404 page not found 응답을 발생

 - path에서는 기본지원되는 path converters(ex: '<'int:year'>')를 통해 정규표현식을 간소화 할 수 있다.
    - <int: year> 는 r"[0-9]+" 과 같아서 숫자가 1회 이상 반복된다는 뜻이다.
    - 기본지원되는 path converter로는 String converter, Int converter, Slug converter, UUID converter등이 있고,<br>
      필요하다면 커스텀 converter를 만들면 된다.
    - 자주 사용되는 복잡한 패턴은 converter로 등록해서 재사용 가능하다.

- path는 정규표현식을 사용하지 않는데 횟수를 한정하고 싶으면 re_path를 사용해 정규표현식을 사용한다.<br>
  path일때는 매핑된 converter의 def to_python()에 맞게 변환된 값이 전달된다.<br>
  re_path에서는 1.xx 버전 그대로 정규표현식을 사용하고 모두 str 형태로 넘어간다.<br>
  
