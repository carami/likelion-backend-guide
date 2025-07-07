
# 🎉 즐거운 자바: Hello 프로그램 이해하기

## 👩‍🏫 강사 소개  
**강경미** (carami@nate.com)  
**김성박** (urstory@gmail.com)


## 🗂️ 강의 개요

- **주제:** 자바 언어의 기본 구조 이해 및 Hello.java 실행 실습  
- **목표:** 자바 프로그램의 구조(클래스, 메서드, 출력문)를 이해하고 작성/실행할 수 있다.  
- **시간:** 약 1시간  
- **준비물:**
  - VS Code 또는 IntelliJ
  - JDK 설치 완료 (버전 11 이상 추천)

---

## 👋 Hello.java 파일 분석

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

---

## 🧱 Hello.java의 3가지 핵심 요소

### ① 클래스 선언

```java
public class Hello {
    ...
}
```

- `public class`로 선언된 **Hello** 클래스
- **클래스 이름 = 파일 이름**이어야 함 → `Hello.java`
- 자바는 **대소문자 구분**

---

### ② main 메서드

```java
public static void main(String[] args) {
    ...
}
```

- 자바 프로그램의 **시작점**
- 모든 실행 가능한 자바 프로그램은 이 메서드를 포함해야 함
- `String[] args`는 **명령줄 인자**를 받을 수 있는 배열

---

### ③ System.out.println()

```java
System.out.println("Hello");
```

| 구성 요소 | 설명 |
|-----------|------|
| `System` | 자바 내장 클래스 |
| `out` | 출력 스트림 (필드) |
| `println()` | 출력 함수 (메서드) |

- `System.out`은 **출력 객체**
- `println()`은 **출력 메서드**
- 괄호 안의 `"Hello"`는 문자열(String) → 그대로 출력됨

---

## ⚙️ 컴파일하기

```bash
javac Hello.java
```

- `javac`는 자바 **컴파일러**
- `.java` 파일을 `.class` 파일로 **변환**
- 컴파일에 성공하면 `Hello.class` 파일 생성

---

## 🚀 JVM으로 실행하기

```bash
java Hello
```

- `java` 명령어는 JVM(Java Virtual Machine)을 실행
- `.class` 파일을 **한 줄씩 해석하며 실행** → **인터프리터 방식**
- 확장자 `.class`는 **입력하지 않음**

---

## 🧪 연습 문제

```java
public class MyInfo {
    public static void main(String[] args) {
        System.out.println("이름: 홍길동");
        System.out.println("성별: 남성");
        System.out.println("이메일: hong@example.com");
    }
}
```

- 직접 작성하고 컴파일 & 실행:  
  `javac MyInfo.java`  
  `java MyInfo`

---

## ✅ 학습 체크리스트

| 항목 | 확인 |
|------|------|
| `Hello.java` 코드 구조를 이해했다 | ⬜ |
| 클래스 이름과 파일명이 같아야 함을 기억했다 | ⬜ |
| main 메서드가 자바 프로그램의 시작점임을 이해했다 | ⬜ |
| println()의 역할과 출력 방식에 대해 이해했다 | ⬜ |
| 컴파일과 실행 명령어 차이를 숙지했다 | ⬜ |

---

## 💡 퀴즈

1. 자바 프로그램의 시작 메서드는?
   - a) run  
   - b) start  
   - c) main  
   - d) execute  

2. `System.out.println()`에서 `println`은 무엇인가?
   - a) 클래스  
   - b) 필드  
   - c) 메서드  
   - d) 상수  

3. 자바 컴파일러 명령어는?
   - a) java  
   - b) execute  
   - c) javac  
   - d) runjava



<details>
<summary>정답 보기</summary>

1️⃣ c) main  
2️⃣ c) 메서드  
3️⃣ c) javac

</details>


---

## 🔁 복습 질문

- 클래스 이름과 파일 이름은 어떤 규칙을 따라야 하나요?
- main 메서드는 어떤 역할을 하나요?
- JVM과 javac는 각각 어떤 기능을 하나요?
- 자바에서 문자열을 출력하려면 어떤 메서드를 사용하나요?

---

## 🙏 마무리

수고 많으셨습니다! 🎉  
다음 시간에는 **변수와 자료형**에 대해 배워볼 예정입니다.  
궁금한 점이 있으면 언제든지 질문하세요 😊

# Hello.java의 3가지 중요한 부분

1. 클래스 선언

```
public class Hello{
.......
}
```

- public class로 정의된 Hello 클래스
- public class의 클래스 이름과 파일이름은 같아야 한다. (중요! 대소문자 구분함): Hello.java

---

# Hello.java의 3가지 중요한 부분

2. 메소드 선언

```
   public static void main(String[] args){
        .......
    }
```

- 클래스는 필드(Field)와 메소드(Method)를 가질 수 있다.
- 프로그램이 실행하려면 반드시 가져야 하는 main메소드
- Java로 만든 프로그램이 실행되려면 위의 코드(code)를 가지고 있어야 한다. 프로그램 시작점이라고도 말한다.

---

# Hello.java의 3가지 중요한 부분

3. System클래스의 out. out이 가지고 있는 println()메소드를 이용해 출력하기

```
    System.out.println("Hello");
```

- System.out은 System이 가지고 있는 out이라는 의미이다.
- out.println은 out이 가지고 있는 println이라는 의미이다.
- println뒤에 괄호가 붙어 있는데, 이때 println메소드라고 말한다.
- out은 괄호가 붙지 않았는데, 이때 out필드라고 말한다.
- out이 가지고 있는 println메소드의 역할은 괄호안의 내용을 화면에 출력한다. 즉 "Hello"가 출력되게 된다. (이때 큰따옴표 안의 내용이 출력된다.), 큰따옴표까지 포함해서 문자열(String)이라고 말한다.

---

# 컴파일하기

- 컴파일을 하려면 반드시 javac라는 프로그램이 필요하다. javac는 자바 컴파일러(Compiler)를 말한다.
  `javac Hello.java`
- 터미널에서 위의 명령을 입력하면 Hello.java라는 파일을 읽어들여서 컴파일을 하게 된다.
- 컴파일을 성공하면 Hello.class파일이 생성되고, 컴파일이 실패하면 오류메시지가 보여진다.
- Hello.class파일을 `바이트(byte) 파일`이라고 말한다. Hello.java는 에디터로 열어보면, 사람이 알아들을 수 있는 말로 되어 있지만, Hello.class는 사람이 알아볼 수 없는 말로 되어 있다.

---

# JVM으로 실행하기

- 자바로 작성된 프로그램이라는 것은 컴파일된 클래스. 즉 바이트 파일을 의미한다.
- 작성된 바이트 파일을 실행하려면 JVM(Java Virtual Machine)이 필요하다. 이 JVM역할을 수행하는 것이 java명령이다.
- hwp파일을 읽어들이려면 아래한글 워드프로세서가 필요하고, psd파일을 읽어들이려면 포토샵 프로그램이 필요한 것과 같은 원리이다.
- JVM은 바이트 코드를 읽어들여 실행된다. 바이트 코드를 읽어들여 실행하기 위해서는 다음과 같은 명령을 실행한다. 이때 확장자 이름은 입력하면 안된다.
  `java Hello`
- java프로그램은 Hello클래스를 한 줄 읽고 해석 하고 실행하고, 한 줄 읽고 실행하고를 반복하면서 실행한다. 이렇게 한줄 한줄 읽어들이고 해석하면서 실행하는 방식을 인터프리터(interpreter)방식이라고 한다.

---

# 연습

- 본인의 이름, 성별, 이메일주소를 출력하는 클래스를 작성하고, 컴파일하고, 실행한다.

---

# 감사합니다.
