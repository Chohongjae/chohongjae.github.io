# URLConf와 정규 표현식

- django에서 request를 처리하는 방식
    - url의 부분으로써의 파라미터(Parameters as part of url)
        - request url = users/3<br>
          urls.py -> users/<"int:user_id"><br>
          views.py -> user_id = 3<br>
                
                <fbv>
                def viewname(request, user_id):
                    user = User.objects.get(id=user_id)
                    #do something with this user
                    
                <cbc>
                class SampleView(TemplateView):
                    def get_context_data(self, **kwargs):
                        user = User.objects.get(id=kwargs['user_id'])
                        #do something with this user
                
    - GET 요청 - > request.GET 
          request url = polls/?question_id=3&question_name=test<br>
          urls.py -> polls/<br>
          views.py -> request.GET['question_id'] or request.GET.get('question_id') or request.GET['question_name']  
                
                url(r'^products/', 'viewname', name='urlname')
                def viewname(request):
                    price_lte = request.GET['price_lte']
                    #Code to filter products whose price is less than price_lte i.e. 5000
    
    - EX)

            - request url : https://localhost:8000/server/ad-api/test/4?id=3&pw=qwer123
            - django.urls.py : /server/ad-api/test/<int:pk>/                
            - django.views.py
                pk = 4
                request.GET['id'] = 3
                request.GET.get('id') = 3
                request.GET = <QueryDict: {'id': ['3']}>
                request.GET.get('id2', default='7') = 7 (예외처리)
      
    - POST 요청 - > request.POST
        - POST를 처리할때는 클라이언트로부터 넘어오는 데이터 형식에 따라 처리 방식이 달라진다.
        - body에 {} 이러한 형태의 json 타입(application/json)이 넘어오면 request.body로 처리하고
        - body에 id=3&pw=4 식의 &로 구분되는 key=value 형태의 데이터(application/x-www-form-urlencoded)가 넘어오면<br>
          request.POST로 처리한다.
        
        - request의 content-type에는 application/x-www-form-urlencoded, text/plain multipart/form-data등이 있다.<br>
          POST 방식으로 데이터를 보낼때는 위와 같이 컨텐츠 타입을 꼭 명시해줘야한다.<br>
          보통 작성하지 않는 경우는 application/x-www-form-urlencoded 컨텐츠 타입으로 셋팅된다.<br>
          - application/x-www-form-urlencoded 타입
            - GET방식과 마찬가지로 &로 구분지어지는 key 와 value 쌍 데이터가 전송된다.<br>
              request.POST로 받으면 되고 URL에는 전송되는 데이터가 표시되지 않는다.
            - In general case, url when sending post parameters doesnt contain anything related to parameters in the url    
              
                    ex) name_field=Default+name+for+team.&name_field2=Default+name+for+team2.
        
          - application/json 타입
            - content-type이 application/json 이고 BODY에 json형태의 값이 담겨서 넘어오면<br>
              request.body로 받는다. application/json은 대부분의 API에서 활용하는 Content-Type 헤더로써<br>
              HTTP 요청을 하게 되면 body에 담긴 데이터를 서버가 JSON 타입으로 변환(json.loads())해서 사용한다.<br>
              그런데 body에 담긴 값은 byte타입이기 때문에 unicode 형식만 처리할 수 있어서<br>
              json.loads()에 넣기전에 decode('utf-8')로 디코딩을 해주고 json.loads(request.body)로 처리해야 한다.<br>
              일반적인 HTML 폼으로 전송할 때는 x-www-form-urlencoded 또는 multipart/form-data로 전송된다.
        
                    You're confusing form-encoded and JSON data here. <br>
                    request.POST['foo'] is for form-encoded data.<br> 
                    You are posting raw JSON, so you should use request.body.
                    
          - text/plain은, BODY에 단순 txt를 넣는다.<br>
          - multipart/form-data은, 파일전송을 할때 많이 쓰는데 BODY의 데이터를 바이너리 데이터로 넣는다는걸 알려준다.
        
        - 즉, django에서 클라이언트에서 POST로 넘어온 request를 처리할 때 
        
                content_type이 application/x-www-form-urlencoded 인 경우 request.POST 사용
                content_type이 application/json 인 경우 request.body 사용

    <br><br><br>
    
# URLConf
- 모든 url 끝에는 /를 붙여야하는 것이 장고의 규칙!
- 요청이 들어오면 우선 urlpatterns상의 리스트를 처음부터 순차적으로 훑으며 url 매칭을 시도한다.<br>
  매칭되는 다수의 패턴이 있더라도 처음 발견되는 url로 매칭된다.

- import url -> Django 1.xx 스타일 <br> 
  import path, re_path -> Django 2.xx 스타일 

- path에서는 기본지원되는 path converters(ex: '<'int:year'>')를 통해 정규표현식을 간소화 할 수 있다.<br>
  정규표현식을 '<'int:year'>' 이렇게 간략화 한다. 이런 형태는 숫자가 1회 이상 반복된다는 뜻! <br>
  path는 정규표현식을 사용하지 않는데 횟수를 한정하고 싶으면 re_path를 사용해 정규표현식을 사용한다.<br>
  path일때는 매핑된 converter의 to_python에 맞게 변환된 값이 전달된다.<br>
  re_path에서는 1.xx 버전 그대로 정규표현식을 사용하고 모두 str 형태로 넘어간다.<br>
  자주 사용되는 복잡한 패턴은 converter로 등록해서 재사용 가능하다.

- 프로젝트를 처음 시작할때의 규칙으로 장고 앱을생성할때 url_patterns 위에 app_name = '앱이름' 을 넣어준다.<br>
  해당 앱을 호출하는 url에서 include에 name 형태를 쓰지말고 호출되는 앱의 urls.py 파일 내에 변수 app_name을<br>
  정의하면 그것이 django 에서는 제공하는 namespace 이다.<br>
  용도는 현재 url_pattern에 대한 이름을 정해주고 URL_REVERSE에서 사용하는데 view에서 url_reverse를 사용해서<br>
  url의 네임으로 리다이렉트할 때 사용된다!
    
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
            
            -template.html
            <li><a href="{% url 'helloworld:detail' user.id %}">{{user.email}} [{{user.name}}]</a></li>
    
    - 즉, 'helloworld:detail' 이런식으로 사용하려면 'appname:url_name' 다 설정해줘야한다!
    - 프로젝트 url안에는 namespace, 앱 폴더 url안에는 name을 사용했는데, namespace는 앱을 구분해주는<br>
      기능이라고 생각하면 되고, 앱 url안에 name은 각 url의 이름을 붙이는 기능이라고 생각하면된다.<br>
      이 기능을 사용해서 나중에 TDD 개발과 내부에서 라우팅시에 reverse('namespace:name')으로 url로 라우팅 가능하다.<br>
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



# request.data in DRF vs request.body in Django
    Aboout request.data
    REST framework introduces a Request object that extends the regular HttpRequest, 
    and provides more flexible request parsing. 
    The core functionality of the Request object is the request.data attribute, 
    which is similar to request.POST, but more useful for working with Web APIs.
    request.POST # Only handles form data. Only works for 'POST' method.
    request.data # Handles arbitrary data. Works for 'POST', 'PUT' and 'PATCH' methods.

    About request.body
    The raw HTTP request body as a byte string. This is useful for processing data 
    in different ways than conventional HTML forms: binary images, XML payload etc. 
    For processing conventional form data, use HttpRequest.POST.