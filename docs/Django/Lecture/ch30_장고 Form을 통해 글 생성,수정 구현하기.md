# 장고 Form을 통해 글 생성,수정 구현하기

- Django Form
    - 장고를 더욱 장고스럽게 만들어주는 주옥같은 Feature
    - 장고를 사용하면서 form을 사용하지 않는 것은 50%만 사용하는 것!
    - DRF의 Serializer도 장고 form의 컨셉을 그대로 차용
    - Model 클래스와 유사하게 Form 클래스를 정의
    - 주요 역할 : 커스텀 Form 클래스를 통해 ...
        - 입력폼 HTML 생성
        - 입력폼 값 검증 (Validation) 및 값 변환 (모델의 validation을 통해)
        - 검증을 통과한 값들을 사전타입으로 제공

- Django 스타일의 Form 처리
    - 폼 처리 시에 같은 URL (즉, 같은 View)에서 GET/POST로 나눠 처리
        - GET 방식 요청
            - 입력폼을 보여줍니다.
        - POST 방식 요청
            - 데이터를 입력받아 유효성 검증 과정을 거칩니다.
            - 검증 성공 시 : 해당 데이터를 저장하고 SUCCESS URL로 이동
            - 검증 실패 시 : 오류메세지와 함께 입력폼을 다시 보여줍니다.

- 구현순서
    - Form
        - 생성할 Model에 맞춰 Form 클래스를 정의
                
                from django import forms
                from .models import Item
                
                class ItemForm(forms.ModelForm):
                    class Meta:
                        model = Item
                        fields = "__all__"
        - ModelForm을 이용하면, Model 내역에 맞게, 손쉽게 정의 가능
    - View
        - Form 클래스를 활용하는, 범용 스타일로 구현
                
                from .forms import ItemForm
                
                ###생략
                if request.method == 'POST':
                    # 수정 view일때는 건네받은 item객체를 ItemForm()에 넣어준다.
                    # ItemForm(instance = item)
                    form = ItemForm(request.POST, request.FILES)
                    if form.is_valid():
                        item =form.save()
                        return redirect(item)
                else: 
                    #GET요청은 이게 끝
                    form = ItemForm()
                
                {{ form.as_table }} -> template.html                    
            - 하나의 View에서 하나의 Form, 하나의 Model을 다룹니다.
    - Template
        - 거의 모든 View를 커버할 수 있는, 범용 템플릿 코드로 구현
            - 개별 Form 위젯에
            - 물론 커스텀으로 만드실 수도 있습니다.

