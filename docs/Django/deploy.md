# Deploy

>설정파일 구성이 완료되면 배포 쉘 스크립트 파일(.sh)을 만들어서 간단히 배포 할 수 있음.<br>
>sudo systemctl | grep nginx => 서비스 상태 확인<br>
>sudo systemctl start nginx(sudo service nginx start) => 서비스 시작<br>
>ps -ef | grep nginx => 현재 수행되고 있는 프로세스 상태 확인<br>
>netstat -nap => 열려있는 포트 확인


## 기본구조
- Web Client <-> Nginx(Web Server) <-> Socket <-> uWSGI <-> Django(Application Server)
- 웹서버와 uWSGI 사이에 port를 사용하지 않고 UNIX socket을 사용하면, overhead가 적어서 더 좋은 성능을 낼 수 있다.

## Nginx란?
- 일반적으로 웹 서버( Apache, Nginx )는 톰캣, PHP, Django, Node.js 등의 앞단에 배치되어<br> 프록시, 보안, 정적 파일 제공 등의 역할을 한다.<br>
  그런데 웹 서버는 PHP, Python, JavaScript 등의 언어를 해석할 능력이 없기 때문에 프로그래밍 언어를 해석할 수 있는<br> 인터페이스, 즉 CGI가 필요하다.

## CGI란?
- 웹서버와 애플리케이션 사이에서 interface(규칙)을 제공한다.Interface가 필요한 이유는<br> 웹서버가 다양하고 program 또한 다양하기 때문.

## WSGI란?
- python 애플리케이션과 웹 서버가 통신하기 위해 정의된 표준 인터페이스 스펙.<br>
  - uWSGI는 Python WSGI 서버중에 한가지.<br>
  일반적으로 production에서는 uwsgi만을 사용해서 서비스를 제공하지 않는다.<br>
  그 보다 앞에 Nginx Server를 둠으로써 Static Content는 Nginx Server가 핸들링 하도록 하고<br>
  나머지 Request는 Reverse Proxying을 통해서 uwsgi에게 전달하여 사용하게 된다.<br>
  Nginx와 같이 사용하므로서 얻는 이득중 가장 큰 장점은 Nginx가 가진 보다 향상된<br> Static Content(CSS,Javascript등)핸들링을 통해서
  서버에 발생되는 Load를 줄일 수 있다
- uwsgi는 uWSGI가 웹 서버와 통신하기 위해 구현된 프로토콜.

# 배포순서
1. pip install virtualenv
   - 가상환경 설치
2. virtualenv "가상환경 이름"
   - 가상환경 생성
3. source venv/bin/activate
   - 가상환경 접속
   - deactivate (가상환경 접속해제)
4. (venv)$ pip install uwsgi
   - 프로젝트 환경에 uWSGI 설치
    ````
    기존 서버 구동 방식은 python manage.py runserver 이였다면
    (venv)$ uwsgi --http :8000 --module (프로젝트명).wsgi 로 구동할 수 있다.
    
    명령어에 대해 설명하면
    http는 http 통신을 하겠다는 의미이며 8000포트를 사용한다는 것.
    http가 아닌 UNIX Socket 방식을 사용하고 싶다면 --socket :[port number]의 형태로 이용하면 된다.
    module은 wsgi 모듈을 통해서 실행하겠다는 의미이며
    단순하게 파일을 사용하려면 --wsgi-file [app.py(python 실행 파일 이름)]의 형태로도 사용가능.
    
    즉, 외부에서 8000 포트로 들어온 http요청을 uWSGI가 받아서
    그 요청을 처리하는 애플리케이션에(이 경우에는 Django) 넘겨주고 처리를 해준 후에 응답을 해준다.
    ````
5. manage.py가 있는 경로에서 vi (프로젝트 이름).ini
   - uwsgi 설정파일을 통해 쉽게 uwsgi를 실행할 수 있다.
   - uwsgi -i (프로젝트 이름).ini
    ```
    #(프로젝트 이름).ini file
    [uwsgi]
    
    # Django-related settings
    # the base directory (full path)
    chdir = /home/linku/LinkU/linku_backend (프로젝트 기본 경로)
    # the virtualenv (full path)
    home = /home/linku/.pyenv/versions/LinkU/ (가상환경이 위치한 폴더의 경로)
    # Django's wsgi file
    module = 프로젝트명.wsgi (django 프로젝트 생성시 생성되는 wsgi.py를 모듈로 불러온다.)
    
    # process-related settings
    # master
    master = true (uWSGI 프로세스를 master로 돌아가게 해준다.)
    # maximum number of worker processes
    processes = 4
    # the socket
    socket = /프로젝트 경로/프로젝트명.sock (UNIX socket 파일의 위치. 자동생성됌)
    # with appropriate permissions - may be needed
    chmod-socket = 666 (권한설정)
    # clear environment on exit
    vacuum = true (uWSGI를 통해서 생성된 파일들은 삭제하는 옵션.)
    touch-reload=프로젝트명.reload (프로젝트명.reload파일이 touch되면 감지하고 uwsgi를 리로드해주는 설정)
    # daemonize the process
    daemonize=/dev/null (데몬 백그라운드로 돌리기 위한 설정이며 log파일을 남길 경로를 지정해주면 된다. master=true 시 가능하다.)
    - daemonize가 없으면 콘솔을 빠져나오는 순간 접속한 pid가 kill되서 종료된다.    
    ```
6. 현재 구조 : web Client <-> socket <-> uWSGI <-> Django
7. nginx 설치
   - sudo apt-get update
   - sudo apt-get install nginx
   - nginx -v
8. cd /etc/nginx/sites-available/
9. vi 프로젝트명
    ```
    server {
    listen 80; (80번 포트로 오는 요청)
    server_name *.compute.amazonaws.com; (로 끝나는 주소로 들어오는 요청을 받겠다는 뜻)
    charset utf-8;
    client_max_body_size 128M; (파일전송을 사이즈를 늘리고 싶다면 설정) 

    location / {
        uwsgi_pass  unix:///uwsgi에서 설정한 sock파일; (.compute.amazonaws.com/ 의 주소로 오는 요청을 sock 파일에 담아 uWSGI 에 넘긴다는 뜻)
        include     uwsgi_params;
        }
    }
    ```
10. sudo ln -sf /etc/nginx/sites-available/프로젝트명 /etc/nginx/sites-enabled/프로젝트명
    - sites-available 에 있는 설정파일을 sites-enabled 폴더에 링크해준다.
    - sites-enabled폴더의 default 링크는 삭제해준다.
11. Nginx는 기본적으로 백그라운드에서 실행되도록 되어있다. <br>
    그렇지만 uWSGI는 서버에 접속할 때 마다 직접 실행을 해주어야한다.<br>
    service를 통해 root 권한으로 데몬을 띄우는 방법도 있지만 좋지 않은 방법이다.<br>
    특별한 이유가 아니고서는, root로 띄우지 않는다.<br>
    uwsgi를 ubuntu 권한으로 데몬으로 띄우도록 설정하는 것이 daemonize=/dev/null 설정<br>
    **(venv)$ uwsgi -i 프로젝트명.wsgi** 명령으로 uwsgi를 백그라운드에서 실행시킨다.
12. sudo service nginx start 로 nginx 시작
    - nginx는 설정파일이 바뀔때마다 재시작 해주어야 한다.
    - sudo service nginx reload == nr(# alias설정 시)
13. 소스 파일이 변경되었을 때 프로젝트명.ini파일의 touch-reload 설정으로<br> 프로젝트명.reload파일이 touch되면 감지하고 uwsgi를 리로드한다.
    - vi 프로젝트명.reload
    - 소스 파일이 변경되면 touch 프로젝트명.reload