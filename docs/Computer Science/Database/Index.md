# Index, 인덱스(Index)란 무엇인가?

- 인덱스는 RDBMS에서 검색속도를 높이기 위해 사용하는 하나의 기술로서, 말 그대로 책의 맨처음 혹은 맨뒤에 있는 ‘목차’에 주로 비유된다.<br>
이 비유를 그대로 가져와서 인덱스를 살펴본다면 데이터는 책의 내용이고 데이터가 저장된 레코드의 주소는 인덱스 목록에 있는 "페이지 번호(rowid)"가 될 것이다.<br>
DBMS도 데이터베이스 테이블의 모든 데이터를 검색해서 원하는 결과를 가져 오려면 시간이 오래 걸린다.(풀스캔)<br> 
그래서 칼럼의 값과 해당 레코드가 저장된 주소를 키와 값의 쌍으로 인덱스를 만들어 두고 사용자가 SELECT쿼리로 INDEX가 사용하는 쿼리를<br>
사용시 해당 TABLE을 검색하는것이 아니라 빠른 TREE로 정리해둔 인덱스 파일의 내용을 검색한다. 색인화 되어있는 INDEX 파일을<br>
검색하여 찾고자하는 데이터의 주소를 찾아 해당 데이터의 테이블에서 주소로 접근해 검색속도를 빠르게 하는 원리다.

   
        예시)
        책에서 어떠한 내용을 찾고싶을 때, 책의 "주요 내용"을 가나다 순으로 정리한 "목록"이 있으면 내가 원하는 특정 내용 더 찾기 쉬울 것이다.
        어느정도 두꺼운 책에서는 색인이라는 것을 제공해서 바로 이러한 편의성을 제공한다.
        이 때, 색인은 영어로 Index이며, DB의 그것과 완전히 동일한 역할을 한다.
        
        10000 페이지짜리 데이터베이스 서적이 다음과 같이 테이블에 저장되어있다고 가정하자.
        
        page	title
        1	Intro
        2	Intro
        3	Intro
        …	…
        512	SQL
        513	SQL
        …	…
        5544	Optimizer
        5545	Transaction
        5546	Transaction
        5547	Transaction
        …	…
        5700	Transaction
        5701	Transaction
        5702	ConcurrenctControl
        5703	ConcurrenctControl
        …	…
        9999	Outro
        10000	Outro
        
        Transaction 파트는 5545 페이지부터 5701 페이지 까지라는 것을 알 수 있다.
        검색 방식을 쿼리로 표현하면 다음과 같다. (테이블 명은 db_book이라 하자)
        
        SELECT	page
        FROM	db_book
        WHERE	title = 'Transaction';
        
        말그대로 db_book이라는 테이블에서 title이 ‘Transaction’ 이라는 page를 찾는 것이다.
        해당 페이지를 찾으려면 1번 페이지부터 5545번 페이지 까지 전부 확인해보고 나서야 Transaction 파트를 찾을 수 있을 것이다.
        그리고 DB 입장에서는 5545번 페이지 뿐 아니라 더 뒤쪽에도 ‘Transaction’ 이라는 키워드가 있을 수도 있다고 생각한다.(그리고 실제로 있다)
        결국 DB는 10000건의 데이터를 전체 검색하는 full scan을 수행하게 된다.
        
        full scan은 말그대로 테이블의 전체 데이터를 몽땅 순회하는 것이다.
        물론 사람의 경우라면 5545번 페이지를 찾고 검색을 중단하겠지만, 컴퓨터는 생각보다 그렇게 똑똑하지 않다.
        그리고 우리가 DB에게 원하는 정보는 Transaction 파트가 시작하는 5545번 페이지일 뿐, 나머지 페이지는 필요하지 않다.
        
        다음 테이블을 보자
        서점에 진열된 책들의 이름, 카테고리, 위치를 저장한 테이블이다.
        
        rowid	name	             category	location
        1	let’s start java	java	A
        2	python basic	         python	K
        3	js for seinor	    javascript	B
        4	let’s start java	java	C
        …	…	…	…
        4222	java? java!	    java	Z
        4223	pythonic thinking	python	A
        …	…	…	…
        9999	javavara	java	K
        10000	i love C++	C++	N
        
        10000권의 책이 있고, A~Z까지 랜덤한 위치에 진열되어있다.
        어떤 java 덕후가 서점에 방문해 카테고리가 java인 책을 전부 구매하려고 한다.
        카테고리가 java인 책의 이름과 위치를 전부 찾기위해 다음과 같이 쿼리했다.
        
        SELECT	name, location
        FROM	book_store
        WHERE	category = 'java'
        결과는 다음과 같을 것이다.
        
        name	location
        let’s start java	A
        let’s start java	C
        java? java!	Z
        javavara	K
        
        현재 인덱스가 없기 때문에, 10000개의 데이터를 모두 뒤져서 결과를 찾았을 것이다.(full scan)
        불쌍한 DB를 위해 인덱스를 만들어주자.
        
        category를 기준으로 데이터를 찾고있기 때문에, category를 기준으로 정렬해주자.
        그리고 DB가 쉽게 찾아갈 수 있도록 rowid를 같이 넣어주자.
        (다른 컬럼까지 모두 인덱스에 넣어버리면 결국 원본 테이블과 내용이 똑같아져 공간 낭비이므로, rowid만 넣어주는 것이다.
        책의 목차에도 제목과 페이지수만 적혀있을뿐, 전체 내용이 적혀있지는 않듯이)
        
        category	id
        …	…
        C++	10000
        …	…
        java	1
        java	4
        java	4222
        java	9999
        javascript	3
        …	…
        python	2
        python	4223
        …	…
        
        인덱스는 문자열 순서대로 정렬되어있기 때문에, ‘java’ 라는 문자열을 계속 검색하다가 ‘javascript’ 라는 문자열을 만나는 순간
        이제 더이상 ‘java’ 라는 문자열을 존재하지 않는다고 단정짓고 탐색을 종료할 수 있다.
        
        게다가 내부적으로 데이터를 B-Tree라는 구조에 저장하기 때문에, ‘java’라는 문자열을 찾아낼 때 맨 처음부터 순차적으로 조회하는 것 보다 훨씬 빠르다.
        # 가장 일반적으로 사용되는 인덱스 알고리즘은 B+-Tree 알고리즘이다. 
        # B+-Tree 인덱스는 칼럼의 값을 변형하지 않고(사실 값의 앞부분만 잘라서 관리한다.), 원래의 값을 이용해 인덱싱하는 알고리즘이다.
            1)컬럼값을 변형하지 않고, 원래 값을 기준으로 이용해서 인덱싱
            2)루트 노드, 브렌치 노드, 리프 노드로 나누어짐
            3)리프노드는 데이터가 저장된 레코드의 주소를 가지게 된다.
            
        그리고 찾아낸 rowid값을 기준으로 데이터베이스에 조회하면 그만이다.
        인덱스에서 찾아낸 rowid값은 1, 4, 4222, 9999 이므로 다음과 같이 검색하면 된다.
        
        SELECT	name, location
        FROM	book_store
        WHERE	rowid IN (1, 4, 4222, 9999)
        
        rowid는 사실 데이터를 삽입할 때 DB 내부에서 자동적으로 생성하는 값으로, 해당 row(행)의 고유한 주소 값을 가리킨다.
        따라서, rowid가 주어지면 DB는 해당 데이터의 위치가 어디있는지 일일이 찾지 않아도 rowid를 통해 "바로 접근"할 수 있다.



# Index 의 성능과 고려해야할 사항
- SELECT 쿼리의 성능을 월등히 향상시키는 INDEX 항상 좋은 것일까? 쿼리문의 성능을 향상시킨다는데, 모든 컬럼에 INDEX 를 생성해두면 빨라지지 않을까?<br>
  결론부터 말하자면 그렇지 않다. 우선, 첫번째 이유는 INDEX 를 생성하게 되면 INSERT, DELETE, UPDATE 쿼리문을 실행할 때 별도의 과정이<br>
  추가적으로 발생한다. 
  INSERT 의 경우 INDEX 에 대한 데이터도 추가해야 하므로, 테이블 생성시에 인덱스의 정보도 만들게되므로 그만큼 성능에 손실이 따른다. <br>
  DELETE 의 경우 INDEX 에 존재하는 값은 삭제하지 않고 사용 안한다는 표시로 남게 된다.<br>
  즉 row 의 수는 그대로인 것이다. 이 작업이 반복되면 어떻게 될까?

- 실제 데이터는 10 만건인데 데이터가 100 만건 있는 결과를 낳을 수도 있는 것이다. 이렇게 되면 인덱스는 더 이상<br>
  제 역할을 못하게 되는 것이다.<br>
  UPDATE 의 경우는 INSERT 의 경우, DELETE 의 경우의 문제점을 동시에 수반한다. <br>
  이전 데이터가 삭제되고 그 자리에 새 데이터가 들어오는 개념이기 때문이다. <br>
  즉 변경 전 데이터는 삭제되지 않고 insert 로 인한 split 도 발생하게 된다.<br>
  