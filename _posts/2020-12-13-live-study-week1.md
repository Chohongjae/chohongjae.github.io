---
title: "라이브 스터디 1주차"
categories: 
  - LiveStudy
last_modified_at: 2020-12-13T22:00:00+09:00
---

# 목표
## JVM은 무엇이며 자바 코드는 어떻게 실행하는 것인가
- 자바 소스 파일(.java)을 JVM으로 실행하는 과정 이해하기. 

## 학습할 것
- [JVM이란 무엇인가](#JVM이란-무엇인가)
- [컴파일 하는 방법](#컴파일-하는-방법)
- [실행하는 방법](#실행하는-방법)
- [바이트코드란 무엇인가](#바이트-코드란-무엇인가)
- [JIT 컴파일러란 무엇이며 어떻게 동작하는지](#JIT-컴파일러란-무엇인가)
- [JVM 구성 요소](#JVM-구성-요소)
- [JDK와 JRE의 차이](#JRE란)

### JVM이란 무엇인가
- JVM이란 write once, run everywhere 즉, OS마다 따로 코드를 작성해야하는 번거로움 없이 '플랫폼, OS에 독립적'으로 Java 프로그램을 작성하여 실행할 수 있게 해주는 표준이자 구현체이다.
{: style="font-size: 80%;"}
  
### 이러한 JVM은 어떻게 동작할까?
- 예를 들어 바로 기계어로 컴파일되는 C 프로그램은 CPU 제조사에 따라 해석할 수 있는 기계어가 다르기 때문에, H/W에 맞게 각각 컴파일되어야 한다.
    - 따라서 C 프로그램은 플랫폼에 종속적이다. 
- 반면에 Java 프로그램은 CPU가 해석할 수 있는 기계어가 아닌 "JVM이 해석 가능한" 가상 머신용 "바이트 코드"로 컴파일된다.
  JVM이 OS 의존적인 부분을 대신 처리하고, "바이트코드를" "OS에 특화된 코드로" 변환한다.
    - Java 프로그램은 플랫폼에 "독립적", JVM이 플랫폼에 "종속적"이다. 
    - 컴퓨터가 바로 인식할 수 있는 "바이너리 코드(컴퓨터가 인식할 수 있는 0과 1로 구성된 이진코드)"가 아닌 "바이트 코드"로 변환된다.
{: style="font-size: 80%;"}    
           
### 정리
1. Java 클래스 파일(.class)을 로드하고
2. 바이트 코드를 해석하고, OS에 특화된 기계어로 변환하며
3. 메모리 등의 자원을 할당하고 관리하며 정보를 처리하는 프로그램
{: style="font-size: 80%;"}
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/java프로그램이실행되는순서.png" alt=""> {% endraw %} 


### 기계어란?
- 기계어는 "CPU가 직접 해독하고 실행할 수 있는" 비트 단위(0과 1로 이루어짐)로 쓰인 컴퓨터 언어이다.
- 기계어가 이진코드로 이루어졌을 뿐이지, 모든 이진코드가 기계어인 것은 아니다. (바이너리 코드 != 기계어)
- 기계어는 특정한 언어가 아니다. 
   - 단지 CPU제조사에서 CPU를 만들 때 해당 CPU에서 사용하는 명령어 집합을 공개하는데, 이것을 '기계어'라고 부를 뿐이다.
   - 때문에 CPU가 변경되면 기계어가 달라진다. 같은 동작을 하는 명령어지만 완전히 다른 0과 1의 나열이 될 수 있다는 말이다. 
   - 같은 회사의 CPU라도 버전 별로 다른 명령을 포함할 수 있으며 다른 회사라도 같은 명령어 집합을 공유할 수도 있다.
{: style="font-size: 80%;"}
    
### 바이트 코드란 무엇인가
- "CPU"가 이해할 수 있는 언어가 "바이너리 코드"라면, "바이트 코드"는 "가상 머신"이 이해할 수 있는 바이너리 코드이다.
- 즉 고급언어로 작성된 "소스코드"를 가상 머신이 이해할 수 있는 중간 코드로 컴파일 되어 어떤 플렛폼에도 종속되지 않게 실행될 수 있는 "가상 머신용 기계어 코드"이다.
- 바이트 코드는 다시 실시간 번역기 또는 저스트 인 타임(just-in-time, JIT) 컴파일러에 의해 네이티브 코드로 변환된다.
{: style="font-size: 80%;"}
   
### 컴파일 하는 방법
- 컴파일이란 우리의 언어는 컴퓨터가 이해하지 못하므로 컴퓨터가 이해할 수 있도록 "통역"하는 작업을 말한다.
1. 자바 언어 사양(JLS)을 충족하는 자바 소스코드(*.java) 파일을 작성한다.
2. 자바 개발 키트(JDK)에 포함되어있는 자바 컴파일러(javac.exe)를 통해 자바 소스코드(.java)를 자바 가상 머신 사양(JVMS)을 충족하는 바이트코드(.class)로 컴파일 한다.
3. 바이트 코드로 작성된 *.class 파일이 생성된 것을 확인 할 수 있다.
{: style="font-size: 80%;"}    
  
### 실행하는 방법
    java Test // java.exe(자바 인터프리터로서 컴파일러로 생성된 바이트 코드를 해석하고 실행한다.)
    
### 역컴파일하는 방법
    javap Test // javap.exe(역어셈블러, 컴파일된 클래스 파일을 원래의 자바 소스코드로 변환한다.)

### JIT 컴파일러란 무엇인가
- JIT는 Just-In-Time의 약어로서 그림에서 볼 수 있듯이 JRE(실행엔진)안에 존재해서 프로그램을 실제 실행하는 시점에(런타임시) 해당 플랫폼에 맞는 기계어(native machine code)로 컴파일(번역)하는 컴파일 기법이다.
{: style="font-size: 80%;"}

{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/JIT.png" alt=""> {% endraw %}

### 그렇다면 이러한 JIT는 왜 쓰이고 어떻게 동작할까?
>자바 바이트 코드는 인터프리터 언어(interpreter language)이다.<br> 
인터프리터가 한줄씩 읽고 해석하고, 그에 해당하는 기능을 실행시키는 인터프리터 언어이기에
기기에서 직접 돌아가는 기계어로 컴파일 되는 C/C++와 같은 언어들로 만든 실행 파일에 비하면 실행 속도가 느리다.<br>
이러한 실행 속도를 개선하기 위해 같은 코드를 매번 새롭게 해석하는 대신, 인터프리팅하기 전에 미리 JIT 컴파일러가
"자주 등장하는 반복적인 코드"를 "네이티브 코드"로 미리 전부 바꿔두고 그 다음부터는 인터프리터가 미리 컴파일된 네이티브 코드를
바로 사용해 인터프리터의 느린 실행 성능을 개선할 수 있다.<br>
단점이라면 JIT 컴파일러가 컴파일하는 과정은 바이트코드를 하나씩 인터프리팅하는 것보다 훨씬 오래 걸리므로 
프로그램의 실행 시간이 매우 짧은 경우에는 초기 실행 속도와 메모리 사용량에서 손해를 보는 단점도 있다.
따라서, JIT 컴파일러를 사용하는 JVM들은 내부적으로 해당 메서드가 얼마나 자주 수행되는지 체크하고, 일정 정도를 넘을 때에만 JIT 컴파일을 수행한다.
{: style="font-size: 80%;"}

{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/JIT2.png" height="70%" alt=""> {% endraw %}

## JVM 구성 요소
- JVM은 크게 4가지 구성요소로 이루어져 있다.
{: style="font-size: 80%;"}

{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/JVM.png" height="50%" alt=""> {% endraw %}

## 클래스 로더 시스템
- 우리가 컴파일한 바이트코드(*.class)를 실행시점(RunTime)에 읽어들여서 메모리(Runtime Data Area)에 적절하게 배치하는 것이 클래스로더의 역할이다.
- 클래스 로더 시스템은 크게 3가지 로딩 -> 링크 -> 초기화의 순서로 일을 한다.
  - 로딩 : 클래스 로더가 .class 파일을 읽고 그 내용에 따라 적절한 바이너리 데이터를 만들고 메서드 영역에 저장, 로딩이 끝나면 해당 클래스 타입의 Class 객체를 생성하여 “힙" 영역에 저장.
  - 링크 : 바이트 코드들에 이상이 없는지, 보안 규칙을 위배하지 않는지 Verify, Prepare, Resolve 세 단계로 나누어서 확인한다.
  - 초기화 : static 변수의 값을 할당한다. static 블럭은 이때 실행된다.
{: style="font-size: 80%;"}
  
{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/classloader.png" height="70%" alt=""> {% endraw %}
- Java 9부터 모듈 시스템인 Jigsaw가 도입되었기 때문에 아래 사진에서 각 클래스로더의 구조나 동작에 변경이 있었다.
{: style="font-size: 80%;"}
  
### BootStrap ClassLoader
- 3가지 기본 클래스로더 중 최상위 우선순위를 가진 클래스 로더로서 그 중 Object, String 같은 최상위 클래스들을 로딩한다.
- lib/modules에 있는 클래스들을 로드한다.
{: style="font-size: 80%;"}
  
### Extension ClassLoader -> (JDK9) PlatformLoader
- 기본 자바 API를 제외한 확장 클래스들을 로드한다. 다양한 보안 확장 기능등을 여기에서 로드하게 된다.
{: style="font-size: 80%;"}

### Application ClassLoader -> (JDK9) System ClassLoader
- 부트스트랩 클래스 로더와 익스텐션 클래스 로더가 JVM 자체의 구성 요소들을 로드하는 것이라 한다면,
  시스템 클래스 로더는 애플리케이션의 클래스들을 로그한다고 할 수 있다. 사용자가 지정한 $CLASSPATH 내의 클래스들을 로드한다.
{: style="font-size: 80%;"}
  
### 클래스 로더가 지켜야할 세가지 원칙
{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/classloader2.png" height="70%" alt=""> {% endraw %}

- Delegation
  - 하위 클래스(로더)는 자신이 로딩하지 않고 상위 클래스에게 로딩을 위임한다.
  - 최상위 클래스까지 위임한 후 로딩 여부를 체크하며 내려온다.
  - 최종적으로 ClassNotFoundException까지 발생시킬 수 있다.
{: style="font-size: 80%;"}
    
- Visibility
  - 하위 클래스로더는 상위 클래스로더의 내용을 볼 수 있지만 반대로는 볼 수 없다.
  - 하위 클래스는 상위 클래스를 바라볼 수 있어야하며, 반대로 상위 클래스는 하위 클래스 로딩을 볼 수 없다는 계층적 원칙
  - 만약에 개발자가 만든 클래스를 로딩하는 애플리케이션 클래스로더가 부트스트랩 클래스로더에 의해 로딩된 String.class를 볼 수 없다면 애플리케이션은 String.class를 사용할 수 없을 것이다.
  - 따라서 하위에서는 상위를 볼 수 있어야 애플리케이션이 제대로 동작할 수 있다.
{: style="font-size: 80%;"}
    
- Uniquesness
  - 유일성 원칙은 하위 클래스로더는 상위 클래스로더가 로딩한 클래스를 다시 로딩하지 않게 해서 로딩된 클래스의 유일성을 보장하는 것이다. 
  - 유일성을 식별하는 기준은 클래스의 binary name인데, toString()으로 찍다보면 가끔 보이는 java.lang.String, javax.swing.JSpinner$DefaultEditor, java.security.KeyStore$Builder$FileBuilder$1, java.net.URLClassLoader$3$1 이런 것들이 바로 binary name이다.
{: style="font-size: 80%;"}

        
### 메모리(Runtime Data Areas)
- JVM이 프로세스로써 수행되기 위해 OS로부터 할당받는 메모리 영역이다. 목적에 따라 크게 5가지 블럭으로 나뉘어있다.
    - 메소드 영역 : "클래스 수준의 정보" (클래스 이름, 부모 클래스 이름, 메소드, 변수) 저장.
      - JVM이 읽어들인 클래스와 인터페이스 대한 런타임 상수 풀, 멤버 변수(필드), 클래스 변수(Static 변수), 생성자와 메소드를 저장하는 공간이다.
      - 모든 Thread 공유
    - 힙 영역 : 객체를 저장한다. "인스턴스"들이 다 힙에 저장된다.
      - 모든 Thread 공유
    - 스택 영역 : "메소드"가 호출될 때마다 스택 프레임이라 불리는 블럭이 하나씩 생성되고 메소드 실행이 완료되면 삭제된다.
      - 쓰레드 마다 생성되어 저장된 정보를 공유하지 않는다.
    - PC 영역 : 쓰레드 내 현재 실행할 스택 프레임을 가리키는 포인터가 생성된다.
      - 쓰레드 마다 생성되어 저장된 정보를 공유하지 않는다.
    - 네이티브 메소드 영역 : 다른 언어(C, C++)의 메소드 호출을 위해 할당되는 구역, 언어에 맞게 Stack이 생성된다.
      - 쓰레드 마다 생성되어 저장된 정보를 공유하지 않는다.
{: style="font-size: 80%;"}

### 궁금한 점
- 프로세스가 생성되면 운영체제는 메모리를 프로세서에게 할당한다. 그 영역은 코드 세그먼트, 데이터 세그먼트,
  스택 세그먼트, 힙 세그먼트로 나뉘는데 이 세그먼트들과 JVM의 Runtime Data Areas는 별개인 것인가?
  OS에서 JVM에게 메모리를 할당하고 JVM은 그 메모리를 다시 위의 5가지(메소드, 힙, 스택, PC, 네이티브..) 영역으로 나누는 것인가?
  (2021.02.25)
{: style="font-size: 80%;"}

### 실행 엔진
- Class Loader를 통해 JVM 내의 Runtime Data Areas에 배치된 바이트 코드를 명령어 단위로 읽어서 실행한다.
- 두가지 방식의 조합을 통해 실행하는데
    - JIT 컴파일러 : 인터프리터의 단점을 보완하기 위해 도입, 위에서 설명
    - 인터프리터 : 바이트코드 명령어를 하나씩 읽어서 해석하고 실행한다. 이 과정에서 바이트코드가 네이티브, 바이너리 코드로 변환된다.
- GC : 실행엔진의 제일 중요한 부분으로 더이상 참조되지 않는 객체를 모아서 정리한다.
{: style="font-size: 80%;"}

### 그래서 자바는 인터프리어 언어인가, 컴파일 언어인가?
- 원래 인터프리터의 의미는 고급언어로 작성된 프로그램을 한즐씩 번역해서 OS에서 인식하는 기계어로 번역하는 역할을 한다.
- 자바 인터프리터는 컴파일된 자바 바이트코드를 한 줄씩 해석하여 기계어로 번역함.
- 반면에 컴파일러는 고급언어로 작성된 프로그램을 목적프로그램으로 번역 후 링킹(Linking) 작업을 통해 실행 프로그램을 생성.
{: style="font-size: 80%;"}

> 그럼 자바는 javac로 컴파일 하고 java로 중간언어(클래스파일)을 한줄 씩 자바 인터프리터가 번역하므로 컴파일언어 이면서 인터프리터 언어이다.
{: style="font-size: 80%;"}

### GC
- C/C++ 프로그래밍을 할 때 메모리 누수(Memory Leak)를 막기 위해 객체를 생성한 후 사용자하지 않는 객체의 메모리를 프로그래머가 직접 해제 해주어야 했다.
- 하지만 JVM에서 GC의 스케줄링을 담당함으로서 Java 프로그래머들에게는 메모리를 관리해야하는 부담을 줄여주게된다. 즉, 일반적인 개발 작업간에는 메모리 할당/해제를 직접 프로그래밍하지 않아도 된다는 이야기다.
- GC에 대해서 알아보기 전에 'stop-the-world'라는 용어를 알아야한다. 
  - 'stop-the-world'란, GC를 실행하기 위해 JVM이 애플리케이션 실행을 멈추는 것으로 어떤 GC 알고리즘을 사용하더라도 'stop-the-world'는 발생하게 되는데, 대개의 경우 GC 튜닝은 이 'stop-the-world' 시간을 줄이는 것이다.
- 기본적으로 JVM의 메모리는 총 5가지 영역(class, stack, heap, native method, PC)으로 나뉘는데, GC는 힙 메모리만 다룬다.
{: style="font-size: 80%;"}
  
{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/gc.png" height="70%" alt=""> {% endraw %}

### GC가 일어나는 과정
- 현재 열심히 사용중인 객체를 메모리에서 제거해버린다면, 프로그램이 정상적으로 실행되지 않을 것이다.
- 때문에, GC를 위해서는 우선 메모리에 있는 객체가 현재 사용중인지 사용중이 아닌지를 구분할 수 있어야 한다.
- JVM에서는 오래된 객체를 구분하기 위해 메모리를 여러 영역으로 나눈다.
{: style="font-size: 80%;"}

{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/gc2.png" height="70%" alt=""> {% endraw %}

- 처음 생성된 객체는 Young Generation 영역의 일부인 Eden 영역에 위치하게된다.
- 그리고 Minor GC가 발생하게 되면, 사용하지 않는 다시말하면 다른 곳에서 참조되지 않는 객체는 메모리에서 제거된다.
- Eden 영역에서 살아남은 객체는 Young Generation 영역의 또다른 일부인 Survivor 영역으로 이동하게된다. 
- Survivor 영역은 Survivor1 영역과 Survivor2 영역으로 구성되어 있는데, 
  Minor GC가 발생할 때마다 Survivor1 영역에서 Survivor2 영역으로 또는 Survivor2 영역에서 Survivor1 영역으로 객체가 이동하게되며, 
  이 과정에서 더이상 참조되지 않는 객체는 메모리에서 제거된다.
- Minor GC가 발생하는 동안 Survivor1, Survivor2 영역을 오가며 살아남은 객체들은 최종적으로 Old Generation 영역으로 옮겨지며,
Old Generation 영역에 있다가 미사용된다고 식별되는 객체들은 Full GC를 통해 메모리에서 제거된다.
{: style="font-size: 80%;"}

### Young Generation 영역에서 오래동안 살아남은 객체는 Old Generation 영역으로 옮겨지는데, 오래되었다는 기준은 무엇일까?
>오래되었다고 하는 기준은 Young Generation 영역에서 Minor GC 가 발생하는 동안 얼마나 오래 살아남았는지로 판단한다. 
각 객체는 Minor GC에서 살아남은 횟수를 기록하는 age bit 를 가지고 있으며, Minor GC가 발생할 때마다 age bit 값은 1씩 증가 하게되며, 
age bit 값이 MaxTenuringThreshold 라는 설정값을 초과하게 되는 경우 Old Generation 영역을 객체가 이동 되는 것이다. 
또는 Age bit가 MaxTenuringThreshold 초과하기 전이라도 Survivor 영역의 메모리가 부족할 경우에는 미리 Old Generation 으로 객체가 옮겨질 수도 있다.
{: style="font-size: 80%;"}


> JDK9부터 기본 가비지 수집기는 G1GC(가비지 우선 가비지 수집기)이고, 실험적 기능으로 stop-the-world 시간을 줄이기 위해 ZGC를 사용할 수 있다.
{: style="font-size: 80%;"}

### 4-1. JNI(Java Native Interface)
- 자바 애플리케이션에서 C, C++, 어셈블리로 작성된 Native 키워드를 사용한 함수를 사용할 수 있는 방법 제공
{: style="font-size: 80%;"}
### 4-2. 네이티브 메소드 라이브러리
- C, C++로 작성 된 라이브러리
{: style="font-size: 80%;"}
  

### JRE란
- JRE(Java Runtime Enviroment)란 컴파일된 자바 프로그램을 실행(JRE의 목적)시킬 수 있는 자바 실행 환경이다.
- JVM + JVM이 자바 프로그램을 동작시킬 때 필요한 핵심 라이브러리 파일 + 자바 런타임 환경에서 사용하는 프로퍼티 세팅이나 리소스 파일을 가지고 있다.
- JRE는 *.class 파일을 JVM으로 로딩시키는 역할을 하고, JVM은 *.class 파일을 해석해 실행할 수 있는 상태로 만든다.
{: style="font-size: 80%;"}

{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/jre.png" height="70%" alt=""> {% endraw %}    

### JDK란
- JDK(Java Development kit)란 자바 애플리케이션 개발 환경이다. 
- JRE(자바 실행 환경 / JVM) + 소스 파일의 컴파일러 및 디버거 등 자바 애플리케이션을 개발하기 위한 도구(javac, java등)가 포함되어 있다.
- JDK를 설치하면 JRE도 같이 설치가 되기 때문에, JDK = JRE + @ 이다.
{: style="font-size: 80%;"}
    
{% raw %} <img src="https://chohongjae.github.io/assets/img/20201213livestudyweek1/jdk.png" height="70%" alt=""> {% endraw %}        


# 전체적인 흐름
- 자바 소스파일을 Java Complier 가 바이트 코드(*.class)로 변환한다.
- JRE가 바이트 코드를 JVM으로 로딩하고, JVM의 Class Loader 가 Runtime Data Area 에 클래스 파일을 적재 시킨다.
- 실행엔진이 자바 메모리에 적재된 클래스 들을 기계어로 변환해 명령어 단위로 실행하고
- Garbage Collector 는 Heap 영역에 적재된 객체들 중에서 참조되지 않은 객체를 제거한다.
{: style="font-size: 80%;"}