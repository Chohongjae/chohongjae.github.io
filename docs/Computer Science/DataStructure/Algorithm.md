# 알고리즘

- 탐색
    1. 선형 탐색 : O(N) 
        - 앞에서부터 쭉 탐색
    2. 이분 탐색 : O(logN)
        - N이 2배 늘어날 때마다 단계가 1 증가, N을 계속 반으로 나누고 버리기 때문에 불필요한 검색을 줄일 수 있다.
        
- 정렬
    1. 버블정렬 : O(N^2) 
        - 큰 수를 계속해서 뒤로 보낸다. X, Y를 앞뒤로 비교하면서 크면 뒤로 보낸다.
    2. 선택정렬 : O(N^2)
        - 맨 앞수를 기준으로 뒤로가면서 제일 작은 수를 기준 맨 앞과 교체한다. 
        - 버블보다는 2배가량 빠르다
    3. 삽입정렬 : O(N^2)
        - 인덱스 "1"부터 뽑아서 자신의 왼쪽에 있는 숫자가 더 크면 빈자리로 시프트한다.<br>
        빈자리가 가장 왼쪽이거나 왼쪽에 있는 수가 뽑힌 수보다 작을 떄가지 반복한다.
        - O(N^2)이지만 시나리오(최선, 최악, 평균)에 따라 N^2, N^2/2, N단계가 걸릴 수 있다.
    4. 퀵 정렬 : O(N^2)
        - 대부분의 언어가 채택하고 있는 정렬방식으로 평균시나리오에서 O(nlogn)으로 효율적이다.<br>
        최악에서는 O(N^2) 분할 정복의 알고리즘의 하나이다.
        - 피벗을 기준으로 큰 값과 작은 값을 서로 교체하는 기법
    5. 병합 정렬
        - 배열의 크기가 2가 될 떄가지 분할 - > 2개의 값 비교 -> 다른 리스트와 비교하면서 병합하면서 정렬한다.
        - 공간이 필요하다.
        
- 해쉬
    - 검색에 O(1)이 드는 자료구조로, key, value 형태로 값을 저장한다.
    - 해쉬함수에 따라 변환된 메모리 주소가 겹칠 수 있는데 이를 충돌이라고하고, value에 배열로 값을 저장함으로써<br>
    충돌을 해결할 수 있다.
    
- 이진트리
    - 한 노드에 자식이 둘이면 왼쪽 자식은 부모보다 작고, 오른쪽 자식은 부모보다 커야한다.
    - 검색, 삽입, 삭제에 O(logN) 소요