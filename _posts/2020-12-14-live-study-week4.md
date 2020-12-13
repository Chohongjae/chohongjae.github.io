---
title: "라이브 스터디 4주차"
categories: 
  - LiveStudy
last_modified_at: 2020-12-14T22:00:00+09:00
---

# 목표
## 제어문
- 자바가 제공하는 제어문을 학습하세요.

## 학습할 것
- [선택문](#선택문)
- [반복문](#반복문)


### 선택문
    조건에 따라 처리를 나눌 경우(분기) 선택문을 이용하는데 자바에서는 다음의 선택문이 있다.
    조건 분기 -> if문, switch 문
    
## if문
    조건에 따라 처리르 분리하여 조건이 일치할 떄만 처리를 실행할 경우에 if문을 사용한다.
    '조건'에는 boolean의 변수나 결과가 boolean이 되는 식을 작성할 수 있다.
    이 조건식이 true 인 경우에 한해서 if 블록 안에 쓰여진 처리를 실행한다.
    또한 else 블록을 작성함으로써 조건에 일치하지 않은 경우에 실시하는 처리를 작성할 수 있다.
    
```java
int month = LocalDateTime.now().getMonthValue();

if (month == 1) {
    System.out.println("1월입니다.");
} else if (month == 2){
    System.out.println("2월입니다.");
} else {
    System.out.println("1월도 2월도 아닙니다.");
}
```

## switch문
    변수의 값(또는 식의 계산 결과)에 따라 처리를 나누는 제어 구문으로 switch문이 있다.

```java
switch(변수) {
    case 값1:
        // 값 1에 일치한 경우에 처리
    case 값2:
        // 값 2에 일치한 경우에 처리
        break;
    default:
        // 어느 조건에도 일치하지 못한 경우에 처리
        break;
}
```  

    switch에 사용하는 변수(또는 계산 결과)로는 다음과 같은 것들을 이용할 수 있다.
    - 숫자값
    - enum 타입
    - 문자열(자바 7이상)
    
    이 변수가 case의 옆에 쓰인 값에 일치하는 경우 그 다음에 작성된 처리를 실행하며 실행은 break가 있는 부분까지 계속된다.
    위의 예에서는 변수가 값1에 일치한 경우에는 값1의 처리를 실시하고 break가 없으므로 값2의 처리도 계속해서 실시한다.
    어느 조건에도 일치하지 못한 경우에는 default에 기재된 처리를 실시하고 default는 생략 가능하다.
    
- [자바 14에 새롭게 생긴 switch 표현식의 사용방법](https://github.com/Chohongjae/javaStudy/blob/main/live-study/week3.md#Java-13.-switch-%EC%97%B0%EC%82%B0%EC%9E%90)

### 반복문
    처리의 반복을 실시하기 위해서 반복문을 사용하고 자바에는 다음의 반복문이 있다.
    반복 처리 -> for문, while문, do-while문 
   
## for문 / for-each문
```java
처리를 반복해서 실시할 경우에 사용하는 제어 구문으로 for문이 있다.

for(초기화; 반복 조건; 증감문) {
    // 반복해서 실시할 처리
}
  
처음 한 번만 '초기화'를 실시한 후 '반복 조건'에 일치하는 동안은 처리를 반복해서 실시한다.
그리고 처리가 끝날 때마다 '업데이트 처리'를 실시한다.

int sum = 0;
for(int i = 0; i <= 10; i++) {
    sum += i;
}
System.out.println(sum);
```  
```java
이외에도 for를 사용한 반복 처리가 하나 더 있는데 for-each문이라고 불리는 것으로
배열이나 컬렉션의 요소를 하나씩 취득하여 처리할 때 쓰인다.

int[] numbers = {1, 2, 3, 4, 5, ,6, 7}
for(int number: numbers) { // (요소의 타입 변수 : 배열 또는 컬렉션)
    System.out.println(number);
}
```

## while문 / do-while문
    
```java
while문이나 do-while문은 조건에 일치하는 동안 반복해서 처리를 실시할 때 이용하는 제어 구문이다.

while(조건) {
    // 반복해서 실시할 처리
}

do {
    // 반복해서 실시할 처리
}while(조건)
    
둘 다 '조건'에 일치하는 동안에만 처리를 반복하는데 둘의 차이는 '조건 판정을 반복 처리 전에 실시할지 반복 처리 후에 할지에 대한 차이'다.
예를들어 조건이 false인 경우 while 문에서는 한번도 처리를 실시하지 않지만, do-while문은 적어도 한 번은 처리를 실행한다.
```    

## 과제 1
- [과제 코드1](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/HomeWork1.java)
- [과제 코드2](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/GitHubDashBoard.java)
- [테스트 코드](https://github.com/Chohongjae/javaTraining/blob/master/src/test/groovy/com/chongjae/javaTraining/liveStudy/week4/GitHubDashBoardTest.groovy)
## 과제 2
- [ListNode](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/ListNode.java)
- [ListNode를 사용한 LinkedList](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/LinkedList.java)
- [LinkedList 테스트](https://github.com/Chohongjae/javaTraining/blob/master/src/test/groovy/com/chongjae/javaTraining/liveStudy/week4/LinkedListTest.groovy)
## 과제 3
- [배열을 사용한 스택](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/Stack.java)
- [배열을 사용한 스택 테스트](https://github.com/Chohongjae/javaTraining/blob/master/src/test/java/com/chongjae/javaTraining/liveStudy/week4/StackTest.java)
## 과제 4
- [ListNode를 사용한 스택](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/ListNodeStack.java)
- [ListNode를 사용한 스택 테스트](https://github.com/Chohongjae/javaTraining/blob/master/src/test/java/com/chongjae/javaTraining/liveStudy/week4/ListNodeStackTest.java)
## 과제 5
- [배열을 사용한 큐](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/Queue.java)
- [배열을 사용한 큐 테스트](https://github.com/Chohongjae/javaTraining/blob/master/src/test/groovy/com/chongjae/javaTraining/liveStudy/week4/QueueTest.groovy)
- [ListNode를 사용한 큐](https://github.com/Chohongjae/javaTraining/blob/master/src/main/java/com/chongjae/javaTraining/liveStudy/week4/ListNodeQueue.java)
- [ListNode를 사용한 큐 테스트](https://github.com/Chohongjae/javaTraining/blob/master/src/test/groovy/com/chongjae/javaTraining/liveStudy/week4/ListNodeQueueTest.groovy)
