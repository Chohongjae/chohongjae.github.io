def solution(dataSource, tags):
    from collections import defaultdict

    answer = []
    tmp = defaultdict(int)

    for tag in tags:
        for ds in dataSource:
            if tag in ds:
                tmp[ds[0]] += 1

    answer.extend([i[0] for i in sorted(tmp.items(), key=lambda x: (- x[1], x[0]))])
    return answer[:10]


if __name__ == "__main__":
    '''
    주어진 태그 중 하나 이상 동일한 태그를 가지는 문서들을 반환합니다
    주어진 태그를 가장 많이 포함하는 문서일수록 앞에 위치시킵니다
    포함하는 태그의 수가 동일할 때는 문서 이름을 사전식 순서(lexicographical order)로 정렬합니다
    페이지네이션(pagination) 기능을 적용하기 위해서 검색 결과는 정렬된 문서들 중 상위 10건만 반환합니다
    '''
    dataSource = [
        ["doc1", "t1", "t2", "t3"],
        ["doc2", "t0", "t2", "t3"],
        ["doc3", "t1", "t6", "t7"],
        ["doc4", "t1", "t2", "t4"],
        ["doc5", "t6", "t100", "t8"]
    ]

    tags = ["t1", "t2", "t3"]

    print(solution(dataSource, tags))
