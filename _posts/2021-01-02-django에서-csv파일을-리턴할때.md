---
title: "django에서 csv 파일을 리턴할 때"
categories: 
  - django
last_modified_at: 2021-01-02T02:00:00+09:00
---
```python
response.write(u'\ufeff'.encode('utf8'))
```
        
- csv파일을 생성하였는데 한글이 깨지는 경우 u'\ufeff'.encode('utf8')을 미리 넣어줘서 이파일이 'utf-8 with bom'이라는<br>
방식으로 인코딩 되어있다는 것을 명시적으로 알려주면 한글이 정상적으로 보이게 csv를 받을 수 있다.