- requests 모듈을 사용할 때
    - get 요청일 때(params 사용)
     
            payload = {'key1': 'value1', 'key2': 'value2'}
            r = requests.get('http://httpbin.org/get', params=payload)
            = > http://httpbin.org/get?key2=value2&key1=value1
    - post 요청일 때(data 사용)
            
            예1) 딕셔너리 형식
            payload = {'key1': 'value1', 'key2': 'value2'}
            r = requests.post("http://httpbin.org/post", data=payload)
            print(r.text)
            
            예2) json 형식
            import json
            url = 'https://api.github.com/some/endpoint'
            payload = {'some': 'data'}
            r = requests.post(url, data=json.dumps(payload))
            
            예3) json 파라미터
            url = 'https://api.github.com/some/endpoint'
            payload = {'some': 'data'}
            r = requests.post(url, json=payload)

- List Comprehensions

        1. if 사용 -> [x for x in b if x == 1]
        2. if else 사용 -> [' ' if b == ' '  else '개굴' for b in a]



- print문에서 다음 번 출력이 바로 뒤에 오게하고싶을때는 
    
        print('hi',end=' ')

- 두개의 리스트를 순서대로 짝지어서 딕셔너리를 만들 때 
    
        dict(zip(a, b))

- from optparse import OptionParser 을 사용하면 커맨드 라인에서 실행할 때 option값을 파싱해준다.

- ERROR 처리
    1. try - except:

			try - except 사용시 정확한 에러이름을 모를경우, except Exception as e -> e로 error를 받아올 수 있다.
	2. raise:
    
            error를 직접 발생시키고 싶을 때는 raise를 사용함
            EX) if '1' == '2':
                    pass
                else:
                    raise Exception('1과 2는 다릅니다.')
	3. assert:
    
            assert 조건, '에러문구' -> 조건이 거짓일 경우 에러문구가 표시됌

	 
- 딕셔너리의 key의 이름을 바꾸고 싶을때          

       keys_in_keys = list(keys.keys())   
       for i in keys_in_keys: 
           if i not in dic.keys():           
               del keys[i]                
       for i,j in keys.items():
           dic[j] = dic.pop(i)
        for i in dic.keys():
          dic[i] = str(dic[i])
          
- Pandas DataFrame
    1. 데이터프레임 행 뒤집기
  
            data.iloc[::-1]
    2. 데이터프레임 값에의해 정렬하고 오름차순 정렬
    
            df1 = df1.sort_values(by=['time'], ascending=[True])
    3. 데이터프레임 인덱스 안보이게 프린트
       
            print(df1.to_string(index=False))
    4. 데이터프레임 컬럼 순서 바꾸기
  
            cols = ['c'] + [x for x in df.columns if x != 'c']
            df = df[cols]
    5. 데이터프레임 인덱스 설정
  
            df1 = df1.set_index('time')
            
- from urllib.parse import urlparse, urljoin 을 사용하면 url 파싱할 수 있음.

- csv파일을 리턴할때 

        response.write(u'\ufeff'.encode('utf8'))
        
    - u'\ufeff'.encode('utf8')을 미리 넣어줘서 이파일이 'utf-8 with bom'이라는 방식으로 인코딩 되어있다는 것을<br>
    명시적으로 알려주면 한글이 정상적으로 보이게 csv를 받을 수 있다.

- filter의 사용
    - filter란 무엇인가를 걸러낸다는 뜻으로, filter 함수도 동일한 의미를 가진다. <br>
    filter 함수는 첫 번째 인수로 함수 이름을, 두 번째 인수로 그 함수에 차례로 들어갈<br>
    반복 가능한 자료형을 받는다. 그리고 두 번째 인수인 반복 가능한 자료형 요소들이<br>
    첫 번째 인수인 함수에 입력되었을 때 리턴값이 참인 것만 묶어서(걸러내서) 돌려준다.

            def positive(x):
                return x > 0
            print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
            list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
            
            
- literable(이터러블) 이란?
    - iterable 의 의미는 member를 하나씩 차례로 반환 가능한 object를 말한다.<br> 
    iterable 의 예로는 sequence type인 list, str, tuple 이 대표적이다. 
    <br>우리가 당연하게 사용했던 위와 같은 for 문은 사실 range() 로 생성된 list가 iterable 하기 때문에<Br> 순차적으로 member들을 불러서 사용이 가능했던 것이다.<br> 
    non-sequence type 인 dict 나 file 도 iterable 하다고 할 수 있다. <br>dict 또한 for 문을 이용해 순차적으로접근이 가능하다.
    <br>iterable 은 for loop 말고도, zip(), map()과 같이 sequence 한 특징을 필요로 하는 작업에 유용하게 사용된다.
    <br>zip() 이나 map() 함수의 경우 iterable 을 argument 로 받는 것으로 정의되어 있다.
    
- list의 extend(리스트 확장)
    - extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 된다.
        
            >>> a = [1,2,3]
            >>> a.extend([4,5])
            >>> a
            [1, 2, 3, 4, 5]
            >>> b = [6, 7]
            >>> a.extend(b)
            >>> a
            [1, 2, 3, 4, 5, 6, 7]
            
- decorator란?
    - decorator를 한마디로 얘기하자면, 대상 함수를 wrapping 하고, 이 wrapping 된 함수의 앞뒤에<br>
     추가적으로 꾸며질 구문 들을 정의해서 손쉽게 재사용 가능하게 해주는 것이다.

            ex)def datetime_decorator(func):
                    def decorated():
                        print datetime.datetime.now()
                        func()
                        print datetime.datetime.now()
                    return decorated
            
            @datetime_decorator
            def main():
                print('hi')
    - decorator 선언된 부분을 자세히 설명하면, 먼저 decorator 역할을 하는 함수를 정의하고,<br>
     이 함수에서 decorator가 적용될 함수를 인자로 받는다.<br>
     python 은 함수의 인자로 다른 함수를 받을 수 있다는 특징을 이용하는 것이다.<br>
     decorator 역할을 하는 함수 내부에 또 한번 함수를 선언(nested function)하여 여기에<br>
     추가적인 작업(시간 출력) 을 선언해 주는 것이다.
     <br>nested 함수를 return 해주면 된다.
     <br>마지막으로, main 함수들의 앞에 @를 붙여 decorator 역할을 하는 함수를 호출해 준다.<br>
     그러면 끝
     <br>노파심에 이야기하면, decorator가 꾸며주는 기능이라고 해서 대상 함수의 수행 중간에<br>
     끼어드는 구문은 할 수 없다.  
     decorator는 원래 작업의 앞 뒤에 추가적인 작업을 손쉽게 사용 가능하도록 도와주는 역할이라는 것이다.  
     class 형태로도 구현이 가능하다.
     
            class DatetimeDecorator:
                def __init__(self, f):
                    self.func = f
                def __call__(self, *args, **kwargs):
                    print datetime.datetime.now()
                    self.func(*args, **kwargs)
                    print datetime.datetime.now()
            
            class MainClass:
                @DatetimeDecorator
                def main_function_1():
                    print "MAIN FUNCTION 1 START"
                
- for문의 for else
    - http://www.mukgee.com/?p=93
	- 기본적으로 for문 에 break 가 포함 되어 있을때 사용가능한데 for문을 순회 하던 중<br>
	 break를 만나면 for문을 빠져나오는건 일반적인 언어와 같지만 break 문을 만나지 않았다면<br>
	 for문 종료 이후 else 문이 실행된다.
	 
            for a in range(0,5):
                print(a)
	 
                if a == 6:
	                break;
	        else:
	            print ("else statement is called")
	 
    - 위의 경우 처럼 for else 문을 사용한다면 flag 같은 변수를 사용하지 않아도 되서 코드가 훨씬 깔끔해 진다.
      <br>else의 들여쓰기는 for와 일치해야 합니다.
      
- GENERATOR와 AIOHTTP AIOHTTP, ABSTRAT CLASS 등등 인스턴스변수 클래스변수등등정리

- 인스턴스 변수 & 클래스 변수
- 인스턴스 메소드 & 클래스 메소드 & 스태틱 메소드
    
        - 스태틱 메소드의 사용방법에 대해서 알아보도록 하겠습니다. 
        많은 사람들이 클래스 메소드와 스태틱 메소드를 혼동하는데, 이 강좌에서 인스턴스 메소드, 클래스 메소드, 
        스태틱 메소드 이 세 가지 메소드의 개념을 확실히 잡고 가도록 하죠. 
        이 세 가지 메소드는 모두 클래스 안에서 정의 됩니다. 인스턴스 메소드는 인스턴스를 통해서 호출이 되고, 
        첫 번째 인자로 인스턴스 자신을 자동으로 전달합니다. 관습적으로 이 인수를 'self'라고 칭합니다. 
        클래스 메소드는 클래스를 통해서 호출이 되고 "@classmethod"라는 데코레이터로 정의합니다.
        첫 번째 인자로는 클래스 자신이 자동으로 전달되고 이 인수를 관습적으로 'cls'라고 칭합니다.
        스태틱 메소드는 앞서 설명한 두 메소드와는 틀리게 인스턴스나 클래스를 첫 번째 인자로
        받지 않습니다. 스태틱 메소드는 클래스 안에서 정의되어 클래스 네임스페이스 안에는 있을뿐
        일반 함수와 전혀 다를게 없습니다. 하지만 클래스와 연관성이 있는 함수를 클래스 안에 정의하여
        클래스나 인스턴스를 통해서 호출하여 조금 편하게 쓸 수가 있는 것 입니다.
        staticmethod에서는 부모클래스의 클래스속성 값을 가져오지만, classmethod에서는
        cls인자를 활용하여 cls의 클래스속성을 가져오는 것을 알 수 있습니다.
        classmethod와 static메소드의 차이는 상속에서 두드러지게 차이가 납니다.

 - 세트들끼리의 집합을 찾기 위해서는 
            
        - 교집합    
        a = set()
        b = set()
        set.intersection(a,b)
        혹은 a.intersection(b) 식으로 사용하면 된다.
        
        - 합집합
        a = set()
        b = set()
        set.union(a,b)
        혹은 a.union(b) 식으로 사용하면 된다.
 
 - 파일과 디렉토리 경로 나누기
 
 
        현재 작업 폴더 얻기 : os.getcwd() # "C:\Temp"
        
        디렉토리 변경 : os.chdir("C:\Tmp")
        
        특정 경로에 대해 절대 경로 얻기 : 
        os.path.abspath(".\\Scripts") 
        # "C:\Python35\Scripts"
        
        경로 중 디렉토리명만 얻기	: 
        os.path.dirname("C:/Python35/Scripts/pip.exe") 
        # "C:/Python35/Scripts"
        
        경로 중 파일명만 얻기 :
        if os.path.isfile("C:/Python35/Scripts/pip.exe"):
           print(os.path.basename("C:/Python35/Scripts/pip.exe"))
        # "pip.exe"
        
        경로 중 디렉토리명과 파일명을 나누어 얻기	: 
        dir, file = os.path.split("C:/Python35/Scripts/pip.exe")
        
        파일 각 경로를 나눠 리스트로 리턴하기(os.path.sep은 OS별 경로 분리자)	
        "C:\Python35\Scripts\pip.exe".split(os.path.sep)
        # ['C:', 'Python35', 'Scripts', 'pip.exe']
        
        경로를 병합하여 새 경로 생성 : 
        os.path.join('C:\Tmp', 'a', 'b') 
        # "C:\Tmp\a\b"
        
        디렉토리 안의 파일/서브디렉토리 리스트 : os.listdir("C:\Python35")
        
        파일 혹은 디렉토리 경로가 존재하는지 체크하기 : os.path.exists("C:\Python35")
        
        디렉토리 경로가 존재하는지 체크하기 : os.path.isdir("C:\Python35")
        
        파일 경로가 존재하는지 체크하기 : os.path.isfile("C:\Python35\python.exe")
        
        파일의 크기 : os.path.getsize("C:\Python35\python.exe")
