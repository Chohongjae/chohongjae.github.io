# URL Reverse를 통해 유연하게 URL 문자열을 생성하기

- URL Dispatcher
    - 장고는 urls.py 변경을 통해 ‘각 뷰에 대한’ url이 변경되는 유연한 시스템을 갖고 있다.<br>
      그래서 url이 변경 되더라도 url reverse가 변경된 url을 추적한다. (누락의 위험이 적다)
    
            # "/blog/", "/blog/1/" 주소로 서비스하다가
            urlpatterns = [
                path('blog/', blog_views.post_list, name='post_list'),
                path('blog/<int:pk>/', blog_views.post_detail, name='post_detail'),
             ]
             
            # 다음과 같이 변경을 하면,
            # 이제 "/weblog/", "/weblog/1/"주소로 서비스하게 됩니다.
            urlpatterns = [
                path('weblog/', blog_views.post_list, name='post_list'),
                path('weblog/<int:pk>/', blog_views.post_detail, name='post_detail'),
             ]
             
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


- URL Reverse의 혜택
    - 개발자가 일일이 URL을 계산하지 않아도 됩니다. 만세 ~~~
    - URL이 변경되더라도, URL Reverse가 변경된 URL을 추적
        - 누락될 일이 없어요.

- URL Reverse가 없다면?
    - 직접 URL을 계산한다면 ~
        1. blog앱 Post목록을 볼려면, post_list 뷰를 호출해야하니깐,
        2. urls.py 를 뒤적뒤적거리며, URL계산계산
        3. 계산완료 ! -> /blog/ 주소를 쓰면 되겠네.

    - blog/templates/blog/layout.html 내에서의 링크
                
            <a href="/blog/"> 블로그 글 목록</a>
    - blog/templates/blog/post_form.html 내에서의 링크
            
            <a href="/blog/"> 블로그 글 목록</a>
    - blog/templates/blog/comment_form.html 내에서의 링크
            
            <a href="/blog/"> 블로그 글 목록</a>
                
    - 그런데, 이 blog앱을 다른 프로젝트에도 쓸려고 옮겼는 데, URL Prefix를 weblog로 쓰고 싶어요.<br>
    하나하나 다 바꿔줘야 하나? 그냥 안된다고 할 것인가? 아악 !!

- URL Reverse를 사용한다면?
    - URL 계산은 장고에게 양보하세요.
        1. blog앱 Post목록을 볼려면, post_list 뷰를 호출해야하니깐,
        2. urls.py 를 뒤적뒤적거리며, URL계산계산 (필요없음)
        3. 계산완료 ! à /blog/ 주소를 쓰면 되겠네. (필요없음)

    - blog/templates/blog/layout.html 내에서의 링크
            
            <a href="{% url "blog:post_list" %}"> 블로그 글 목록</a>
    - blog/templates/blog/post_form.html 내에서의 링크
            
            <a href="{% url "blog:post_list" %}"> 블로그 글 목록</a>
    - blog/templates/blog/comment_form.html 내에서의 링크
            
            <a href="{% url "blog:post_list" %}"> 블로그 글 목록</a>
            
    - 그런데, 이 blog앱을 다른 프로젝트에도 쓸려고 옮겼는 데, URL Prefix를 weblog로 쓰고 싶어요.<br>
      그냥 안된다고 할 것인가? 아악 !! 
      - 코드 변경 거의 없이 가능합니다.
    
    - namespace(=include당하는 대상의 app_name): urlname
        - url의 name은 view의 이름을 그대로 쓰는 경우가 많다.


- URL Reverse를 수행하는 4가지 함수 (1)
    -  url 템플릿태그
        - 내부적으로 reverse 함수를 사용
        - 계산된 문자열 URL 반환
        
                {% url "blog:post_detail" 100 %}
                {% url "blog:post_detail" pk=100 %}

    - reverse 함수
        - 매칭 URL이 없으면 NoReverseMatch 예외 발생
        - 다른 함수들과 다르게 reverse에서만 args, kwargs라고 이름을 붙여줘야 한다.
        - 계산된 문자열 URL 반환
        
                reverse('blog:post_detail', args=[100])
                reverse('blog:post_detail', kwargs={'pk': 100})

    - resolve_url 함수
        - 매핑 URL이 없으면 "인자 문자열"을 그대로 리턴
        - 내부적으로 reverse 함수를 사용
        - 계산된 문자열 URL 반환
        
                resolve_url('blog:post_detail', 100)
                resolve_url('blog:post_detail', pk=100)
                resolve_url('/blog/100'})

    - redirect 함수
        - 매칭 URL이 없으면 "인자 문자열"을 그대로 URL로 사용
        - 내부적으로 resolve_url 함수를 사용
        - HttpResponse 응답 반환

                redirect('blog:post_detail', 100)
                redirect('blog:post_detail', pk=100)
                redirect('/blog/100'})
                
- 모델 객체에 대한 detail 주소 계산
    - 매번 다음과 같은 코드로 하실 수도 있겠지만,
    - 모델 객체에 대한 detail 주소계산할일이 많다.
    - post를 만들었으면 글 자세히 보기 등의 다양한 detail 주소를 계산할 일이 많다.

            resolve_url('blog:post_detail', pk=post.pk)
            redirect('blog:post_detail', pk=post.pk)
            {% url 'blog:post_detail' post.pk %}
            
    - 다음과 같이 사용하실 수도 있습니다. 어떻게?

            resolve_url(post) == post.get_absolute_url()
            redirect(post) == post.get_absolute_url()
            {{ post.get_absolute_url }}

- 모델 클래스에 get_absolute_url() 구현
    - 실제 이러한 코드를 구현해주는 주체는 resolve_url 함수
    - resolve_url 함수는 가장 먼저 get_absolute_url() 함수의 존재여부를 체크하고, 존재할 경우 reverse를 수행하지 않고<br>
    그 리턴값을 즉시 리턴 (관련코드)
    
            # django/shortcuts.py
            
            def resolve_url(to, *args, **kwargs):
                if hasattr(to, 'get_absolute_url'):
                    # 인자로 받은 to객체에 대해서 'get_absolute_url'이 있는지 확인한다. 있으면 바로 호출 
                    return to.get_absolute_url()
                # 중략
                try:
                    return reverse(to, args=args, kwargs=kwargs)
                except NoReverseMatch:
                    # 코드 생략

- resolve_url/redirect를 위한 모델 클래스 추가 구현

        from django.urls import reverse
        class Post(models.Model):
            #중략
            def get_absolute_url(self):
                # 함수를 구현하고 url을 리턴하는데 현재 모델객체에 대한 detail view url을 리턴해주면 된다.
                return reverse('blog:post_detail', args[self.pk])



- 그 외 활용
    - CreateView / UpdateView
        - success_url을 제공하지 않을 경우, 해당 model instance 의 get_absolute_url 주소로 이동이 가능한지 체크하고,<br>
         이동이 가능할 경우 이동
        - 생성/수정하고나서 Detail화면으로 이동하는 것은 자연스러운 시나리오
    - 특정 모델에 대한 Detail뷰를 작성할 경우
        - Detail뷰에 대한 URLConf설정을 하자마자, 필히 get_absolute_url설정을 해주세요. 코드가 보다 간결해집니다.