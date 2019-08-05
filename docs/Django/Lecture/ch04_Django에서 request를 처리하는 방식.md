# Django에서 request를 처리하는 방식

- Django에서 request를 처리하는 방식
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
          views.py -> request.GET['question_id'] or request.GET.get('question_id') or<br>
           request.GET['question_name']  
                
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
        - body에 id=3&pw=4 식의 &로 구분되는 key=value 형태의 데이터(application/x-www-form-urlencoded)가<br> 
          넘어오면 request.POST로 처리한다.
        
        - request의 content-type에는 application/x-www-form-urlencoded, text/plain multipart/form-data등이 있다.<br>
          POST 방식으로 데이터를 보낼때는 위와 같이 컨텐츠 타입을 꼭 명시해줘야한다.<br>
          보통 작성하지 않는 경우는 application/x-www-form-urlencoded 컨텐츠 타입으로 셋팅된다.<br>
          - application/x-www-form-urlencoded 타입
            - GET방식과 마찬가지로 &로 구분지어지는 key 와 value 쌍 데이터가 전송된다.<br>
              request.POST로 받으면 되고 URL에는 전송되는 데이터가 표시되지 않는다.
            - In general case, url when sending post parameters doesnt contain anything related to<br>
              parameters in the url    
              
                    ex) name_field=Default+name+for+team.&name_field2=Default+name+for+team2.
        
          - application/json 타입
            - content-type이 application/json 이고 BODY에 json형태의 값이 담겨서 넘어오면<br>
              request.body로 받는다. application/json은 대부분의 API에서 활용하는 Content-Type 헤더로써<br>
              HTTP 요청을 하게 되면 body에 담긴 데이터를 서버가 JSON 타입으로 변환(json.loads())해서<br>
              사용한다.<br>
              그런데 body에 담긴 값은 byte타입이기 때문에 unicode 형식만 처리할 수 있어서<br>
              json.loads()에 넣기전에 decode('utf-8')로 디코딩을 해주고 json.loads(request.body)로<br>
              처리해야 한다.<br>
              일반적인 HTML 폼으로 전송할 때는 x-www-form-urlencoded 또는 multipart/form-data로 전송된다.
        
                    You're confusing form-encoded and JSON data here. <br>
                    request.POST['foo'] is for form-encoded data.<br> 
                    You are posting raw JSON, so you should use request.body.
                    
          - text/plain은, BODY에 단순 txt를 넣는다.<br>
          - multipart/form-data은, 파일전송을 할때 많이 쓰는데 BODY의 데이터를 바이너리 데이터로<br>
            넣는다는걸 알려준다.
        
        - 즉, django에서 클라이언트에서 POST로 넘어온 request를 처리할 때 
        
                content_type이 application/x-www-form-urlencoded 인 경우 request.POST 사용
                content_type이 application/json 인 경우 request.body 사용

    <br><br><br>

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
