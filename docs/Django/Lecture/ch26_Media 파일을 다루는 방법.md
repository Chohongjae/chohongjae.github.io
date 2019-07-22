# media 파일을 다루는 방법

- static & media 파일
    - static 파일
        - 개발 리소스로서의 정적인 파일(js, css, image 등)
        - 웹 주소를 통해 접근하고자 할 때 static 파일이라 한다.
        - 외부로 공개되지 않는 파일들(static파일이 아닌)은 개별적으로 관리하면 된다.
        - 앱 / 프로젝트 단위로 저장/서빙
        - ex) 특정 blog 앱만을 위한 image, css
        - ex) 전체 프로젝트 전반적으로 사용되는 파일들은 별도의 상위 디렉토리에서 관리
    - media 파일
        - filefield / imagefield를 통해 저장한 모든 파일
        - DB필드에는 저장경로만(문자열)을 저장하며, 파일은 파일 스토리지에 저장
        - 미디어 파일은 프로젝트단위로 저장 / 서빙
        - django-storages를 통해 aws, azure로의 저장이 지원 된다 찾아볼것!!(스태틱도마찬가지)
        
- Media 파일 처리 순서
    1. views에서의 인자인 requests.FILES == HttpRequest.FILES를 통해 파일이 전달
    2. 뷰 로직이나 폼 로직을 통해, 유효성 검증을 수행하고,
    3. FileField/ImageField 필드에 ”경로(문자열)”를 저장하고,
    4. settings.MEDIA_ROOT 경로에 파일을 저장합니다.
    5. 파일을 찾을때도 settings.MEDIA_ROOT 하위에서 찾는다. 
    
- Media 파일, 관련 settings 예시
    - 각 설정의 디폴트 값
        - MEDIA_URL = “”
            - 각 media 파일에 대한 URL Prefix
                - 필드명.url 속성에 의해서 참조되는 설정
        - MEDIA_ROOT = “”
            - 파일필드를 통한 저장 시에, 실제 파일을 저장할 ROOT 경로
        - 기본 설정이 "" 빈문자열이고 settings에 정의되어있지 않기 때문에 저 상태로 파일 업로드시<br>
        manage.py가 있는 경로에 upload되게 된다.
        
- 추천 settings
    - MEDIA_URL = ‘/media/’
        - 여기서 별로 바꿀이유가 없다.
    - MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        - 개발시에는 별로 바꿀이유가 없다.

- FileField와 ImageField
    - FileField(기본)
        - File Storage API를 통해 파일을 저장
            - 장고에서는 File System Storage(로컬)만 지원. django-storages를 통해 확장(s3, azure...) 지원.
        - 해당 필드를 옵션 필드로 두고자 할 경우, blank=True 옵션 적용
    - ImageField (FileField 상속)
        - Pillow (이미지 처리 라이브러리)를 통해 이미지 width/height 획득
            - Pillow 미설치 시에, ImageField를 추가한 makemigrations 수행에 실패합니다.
    - 위 필드를 상속받은 커스텀 필드를 만드실 수도 있습니다.
        - ex) PDFField, ExcelField 등
        
- 모델 필드 예시


    class Post(models.Model):
        author_name = models.CharField(max_length=20)
        title = models.CharField(max_length=100)
        content = models.TextField()
        photo = models.ImageField(blank=True)
        # 나중에 필드를 추가한경우 photo필드에 대해서 기존 레코드들에 어떻게 적용할지 물어본다.
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
        
- 사용할 만한 필드 옵션
    - blank 옵션
        - 업로드 옵션처리 여부
        - 디폴트: False(필수란 뜻)
    - upload_to 옵션
        - settings.MEDIA_ROOT 하위에서 저장한 파일명/경로명 결정
        - 디폴트 : upload_to를 설정하지 않으면 파일명 그대로 settings.MEDIA_ROOT 에 저장
            - 추천) 성능을 위해, 한 디렉토리에 너무 많은 파일들이 저장되지 않도록 조정하기
        - 동일 파일명으로 저장 시에, 파일명에 더미 문자열을 붙여 파일 덮어쓰기 방지
        
- 파일 업로드 시에 HTML Form enctype
    - form method는 필히 POST로 지정
        - GET의 경우 enctype이 “application/x-www-form-urlencoded”로 고정
    - form enctype을 필히 “multipart/form-data”로 지정
        - "applicaiton/x-www-form-urlencoded”의 경우, 파일명만 전송
        
        
            <form action="" method="post" enctype="multipart/form-data">
                {% csrf_token %}
                <table>
                    {{ form.as_table }}
                </table>
                <input type="submit" />
            </form>
            
- upload_to 인자
    - 파일 저장 시에 upload_to 함수를 호출하여, 저장 경로를 계산
        - 파일 저장 후에 upload_to 인자를 변경한다고 해서, DB에 이미 저장된 경로값이 갱신되진 않습니다.
    - 인자 유형
        - 문자열로 지정
            - 파일을 저장할 “중간 디렉토리 경로”로서 활용
            - EX) 'A/B/C' = > /media/A/B/C/파일명
            - 실제 DB에는 'A/B/C/파일명' 으로 저장된다.
    - 함수로 지정
        - “중간 디렉토리 경로” 및 “파일명”까지 결정 가능
        
- 파일 저장경로
    - travel-20181225.jpg 파일을 업로드할 경우
        - MEDIA_ROOT경로/travel-20181225.jpg 경로에 저장되며,
        - DB에는 “travel-20181225.jpg” 문자열을 저장합니다.
        
- 파일 저장 경로 / 커스텀(upload_to 옵션)
    - 한 디렉토리에 파일을 너무 많이 몰아둘 경우, OS 파일찾기 성능 저하.<br>
     디렉토리 Depth가 깊어지는 것은 성능에 큰 영향 없음.
    - 필드 별로, 다른 디렉토리 저장경로를 가지기
        - 대책 1) 필드 별로 다른 디렉토리에 저장
            - photo = models.ImageField(upload_to=“blog”)
                - blog 디렉토리밑에 쌓인다.
            - photo = models.ImageField(upload_to=“blog/photo”)
                - blog/photo 디렉토리밑에 쌓인다.
            - 별로 좋지못한 방법, 다 같은 장소에 쌓이기 때문
        - 대책 2) 업로드 시간대 별로 다른 디렉토리에 저장(좋은 방법)
            - upload_to에서 strftime 포맷팅을 지원
            - photo = models.ImageField(upload_to=“blog/%Y/%m/%d”)
            
- uuid를 통한 파일명 정하기 예시


    import os
    from uuid import uuid4
    from django.utils import timezone
    def uuid_name_upload_to(instance, filename):
        app_label = instance.__class__._meta.app_label # 앱 별로
        cls_name = instance.__class__.__name__.lower() # 모델 별로
        ymd_path = timezone.now().strftime('%Y/%m/%d’) # 업로드하는 년/월/일 별로
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower() # 확장자 추출하고, 소문자로 변환
        return '/'.join([app_label, cls_name, ymd_path, uuid_name[:2], uuid_name + extension,])
        
- 템플릿에서 media URL 처리 예시
    - 필드의 .url 속성을 활용하세요.
        - 내부적으로 settings.MEDIA_URL과 조합을 처리
            - <img src="{{ post.photo.url }}" %}" />
        - 필드에 저장된 경로에 없을 경우, .url 계산에 실패함에 유의. <br>
        그러니 안전하게 필드명 저장유무를 체크
            - {% if post.photo %}
            - <img src="{{ post.photo.url }}" %}" />
            - {% endif %}
    - 참고
        - 파일 시스템 상의 절대경로가 필요하다면, .path 속성을 활용하세요.(파일이 로컬에 있을때만 사용가능)
            - settings.MEDIA_ROOT와 조합

- 개발환경에서의 media 파일 서빙
    - static 파일과 다르게, media 파일에 대해서 장고 개발서버에서 서빙 미지원
    - 개발 편의성 목적으로 직접 서빙 Rule 추가 가능

    
    from django.conf import settings
    from django.conf.urls.static import static
    # 중략
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
- File Upload Handler
    - 파일크기가 2.5MB 이하일 경우
        - 메모리에 담겨 전달
        - MemoryFileUploadHandler
    - 파일크기가 2.5MB 초과일 경우
        - 디스크에 담겨 전달
        - TemporaryFileUploadHandler
    - 관련 설정
        - settings.FILE_UPLOAD_MAX_MEMORY_SIZE
            -> 2.5MB