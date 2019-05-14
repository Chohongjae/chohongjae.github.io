# URLConf와 정규 표현식

- django에서 request를 처리할 때
    - 보통 3가지 방식이 있다.
    - request.GET, POST는 넘어온 값들을 딕셔너리형태로 받는다
    - request.GET
        - request.GET.get('xx')
        - 거기서 이제 request.GET['question_id'] 혹은 request.GET.get('question_id') 혹은 예외처리하려면 request.GET.get('question_id','empty') 이런식으로 처리하면 된다.
    - request.body
        - content-type이 json 인 경우 request.body로 받는다.
        - POST방식으로 BODY에 값이담겨서넘어오면 request.body로 받는다.<br>
          그런데 request.body는 byte타입이기 때문에 unicode 형식만 처리할 수 있는 <br>
          json.loads()에 넣기전에 decode('utf-8')로 디코딩을 해주고 json.loads(request.body)로 처리해야 한다.
    - request.POST
        - content-type에는 여러 종류가 있는데 POST 방식에서는<br>
        application/x-www-form-urlencoded , text/plain , multipart/form-data등이 있다.<br>
        따라서 POST 방식으로 데이터를 보낼때는 위와 같이 컨텐츠 타입을 꼭 명시해줘야한다.<br>
        보통 작성하지 않는 경우는 1번의 컨텐츠 타입으로 셋팅된다.<br>
        1번의 컨텐츠 타입은, GET방식과 마찬가지로 BODY에 key 와 value 쌍으로 데이터를 넣는다. <br>
        똑같이 구분자 &를 쓴다.<br>
        2번의 컨텐츠 타입은, BODY에 단순 txt를 넣는다.<br>
        3번의 컨텐츠 타입은, 파일전송을 할때 많이 쓰는데 BODY의 데이터를 바이너리 데이터로 넣는다는걸 <br>알려준다.
        즉, application/x-www-form-urlencoded인 경우 request.POST로 처리한다.
    -     You're confusing form-encoded and JSON data here. <br>
          request.POST['foo'] is for form-encoded data.<br> 
          You are posting raw JSON, so you should use request.body.
        
- 즉, 클라이언트에서 POST로 넘어온 request를 처리할 때 
    - content_type이 application/x-www-form-urlencoded 인 경우 request.POST 사용
    - content_type이 application/json 인 경우 request.body 사용
    <br><br><br><br><br><br><br><br><br>
# URLConf
- GET요청일 때 polls/3 은 <"int:question_id"> 이런식으로 view에서 3을 (question_id)로 파라미터로 받고<br>
  polls/?question_id=3 일때는 request.GET['question_id'] 이런식으로 받는다!
    
- 요청이 들어오면 우선 urlpatterns상의 리스트를 처음부터 순차적으로 훑으며 url 매칭을 시도함.<br>
  매칭되는 다수의 패턴이 있더라도 처음 발견되는 url로 매칭된다.

- import url -> Django 1.xx 스타일 <br> import path, re_path -> Django 2.xx 스타일 

- path에서는 기본지원되는 path converters(ex: '<'int:year'>')를 통해 정규표현식을 간소화 할 수 있다.
<br>정규표현식을 '<'int:year'>' 이렇게 간략화 한다. 이런 형태는 숫자가 1회 이상 반복된다는 뜻! <br>
path는 정규표현식을 사용하지 않음. 횟수를 한정하고 싶으면 정규표현식을 사용한다.
<br>path일떄는 매핑된 converter의 to_python에 맞게 변환된 값이 전달된다.
<br>re_path에서는 1.xx 버전 그대로 정규표현식을 사용하고 모두 str 형태로 넘어간다.
<br>자주 사용되는 복잡한 패턴은 converter로 등록해서 재사용 가능

- 모든 url 끝에는 /를 붙여야하는 것이 장고의 규칙!

- 프로젝트를 처음 시작할때의 규칙으로 장고 앱을생성할때 url_patterns 위에 app_name = '앱이름' 을 넣어준다.<br>
현재 url_pattern에 대한 이름을정해주고 URL_REVERSE에서 사용하는데 view에서 url_reverse를 사용해서<br>
 url의 네임으로 리다이렉트할 때 사용된다!
    - django 에서는 namespace 를 제공한다. urls.py 파일을 열어서 app_name 이라는 변수명으로 이름을 적용한다.<br>
            
            -url.py
            from django.urls import path 
            from . import views 

            app_name = 'helloworld' 
            urlpatterns = [ 
                path('', views.index, name="index"),      
                path('<int:user_id>/', views.detail, name='detail'), 
                path('<int:user_id>/results/', views.results, name='results'), 
                path('<int:user_id>/vote/', views.vote, name='vote'),  
            ]
            
            -template.py
            <li><a href="{% url 'helloworld:detail' user.id %}">{{user.email}} [{{user.name}}]</a></li>
    - 즉, 'helloworld:detail' 이런식으로 사용하려면 'appname:url_name' 다 설정해줘야한다!
    - 프로젝트 url안에는 namespace, 앱 폴더 url안에는 name을 사용했는데, namespace는 앱을 구분해주는 기능이라고 생각하면 되고,<br> 
      앱 url안에 name은 각 url의 이름을 붙이는 기능이라고 생각하면된다.<br>
      이 기능을 사용해서 나중에 TDD 개발과 내부에서 라우팅시에 reverse('namespace:name')으로<br>
      url로 라우팅 가능하다.<br>
      앱에대한 alias url에대한 alias라 생각하면 될 듯하다.
      
            No. It is just that django gives you the option to name your views in case 
            you need to refer to them from your code, or your templates. 
            This is useful and good practice because you avoid hardcoding urls on your code or 
            inside your templates. Even if you change the actual url, you don't have to change anything else, 
            since you will refer to them by name.

            e.x with views:
            
            from django.http import HttpResponseRedirect
            from django.core.urlresolvers import reverse #this is deprecated in django 2.0+
            from django.urls import reverse #use this for django 2.0+
            
            def myview(request):
                passwords_url = reverse('passwords_api_root')  # this returns the string `/passwords/`
                return HttpResponseRedirect(passwords_url)
            
            - template.py
            <p>Please go <a href="{% url 'passwords_api_root' %}">here</a></p>
            
             
             
            

- view에서는 return이 아닌 raise 혹은 assert로 error를 반환해도 된다.