# 🎉 IntelliJ로 자바 프로젝트 시작하기

## 👩‍🏫 강사 소개  
**강경미** (carami@nate.com)  
**김성박** (urstory@gmail.com)

---

## 🗂️ 강의 개요

- **주제:** IntelliJ IDEA를 사용한 자바 프로젝트 생성 및 실행  
- **목표:** IntelliJ에서 자바 프로젝트를 만들고, Hello.java를 작성하고 실행할 수 있다.  
- **시간:** 약 1시간  
- **준비물:**
  - IntelliJ IDEA 설치 (Ultimate or Community)
  - JDK 설치 완료
  - Git 설치 (선택)

---

## 💻 IDE란?

- **IDE (Integrated Development Environment)**: 코드 작성, 디버깅, 컴파일, 배포 등 개발을 위한 모든 도구를 통합한 환경
- 대표 IDE: Eclipse, IntelliJ IDEA  
- 참고: [위키백과 IDE 설명](https://ko.wikipedia.org/wiki/통합_개발_환경)

---

## 💡 IntelliJ IDEA 소개

- Jetbrains 사에서 만든 자바 개발용 IDE
- 버전:
  - ✅ **Community** (무료)
  - ✅ **Ultimate** (유료, 학생은 무료 인증 가능)
- 다운로드: [공식 IntelliJ 다운로드](https://www.jetbrains.com/ko-kr/idea/download/)

---

## 🍎 Mac에서 설치

- M1/M2 계열: **Apple Silicon 버전** 선택  
- Intel Mac: **Intel 버전** 선택
- 설치 방법:
  - `.dmg` 실행 후, 좌측 아이콘을 우측 `Applications` 폴더로 드래그

---

## 🪟 Windows에서 설치

- `.exe` 파일을 실행하여 설치 마법사 따라가기
- 설치 후 시작 메뉴에서 IntelliJ 실행

---

## ▶️ IntelliJ 처음 실행하기

- "Welcome to IntelliJ IDEA" 화면 → **New Project 클릭**
- 프레임워크 선택 없이 **Next** 클릭

---

## 📁 프로젝트 생성

- 이름: `HappyJava`  
- 저장 위치: 자바 프로젝트 전용 폴더를 생성해서 보관  
- 완료 후 Finish

---

## 🌐 한글 메뉴 설정

- 첫 실행 시, 로컬라이징 안내 팝업 등장  
- "확인" 누르면 메뉴가 **한글**로 바뀜  
- 영어로 쓰고 싶다면 "닫기"

---

## 📌 IntelliJ 프로젝트 구조

| 폴더/파일 | 설명 |
|-----------|------|
| `.idea` | 프로젝트 설정 폴더 (수정 금지) |
| `HappyJava.iml` | IntelliJ 설정 파일 (삭제 금지) |
| `src` | Java 코드 작성 위치 |

---

## ✏️ Hello.java 작성 방법

1. `src` 폴더 우클릭 → 새로 만들기 → Java 클래스 선택  
2. 이름: `Hello` 입력 (확장자 `.java`는 생략)

```java
public class Hello {
    public static void main(String[] args){
        System.out.println("Hello IntelliJ IDEA");
    }
}
```

---

## ▶️ Hello 실행 방법

1. `Hello.java` 파일 우클릭 → **실행 'Hello.main()'** 선택  
2. 아래쪽 콘솔에 실행 결과가 출력됨

💡 IntelliJ는 자동 컴파일 + 실행을 처리함

---

## 📂 컴파일 결과 확인

- 프로젝트 루트에 `out/` 폴더 생성됨  
- 클래스 파일 경로: `out/production/HappyJava/Hello.class`  
- 이 위치에서 `.class` 파일이 JVM에 의해 실행됨

---

## ✅ 학습 체크리스트

| 항목 | 완료 여부 |
|------|------------|
| IntelliJ 설치 및 실행을 완료했다 | ⬜ |
| 새 자바 프로젝트(HappyJava)를 만들었다 | ⬜ |
| Hello.java를 생성하고 편집할 수 있다 | ⬜ |
| 실행 결과를 IDE 콘솔에서 확인했다 | ⬜ |
| `out/` 폴더에서 클래스 파일 위치를 확인했다 | ⬜ |

---

## 🧪 실습 문제

1. 본인의 이름, 성별, 이메일을 출력하는 Java 클래스를 IntelliJ에서 작성하고 실행해보세요.  
   클래스 이름은 `MyInfo`로 하고, 출력 내용은 자유롭게!

```java
public class MyInfo {
    public static void main(String[] args){
        System.out.println("이름: 홍길동");
        System.out.println("성별: 남성");
        System.out.println("이메일: hong@example.com");
    }
}
```

---

## 💡 퀴즈

1. IntelliJ IDEA는 어떤 회사에서 개발했나요?  
   - a) Oracle  
   - b) Google  
   - c) Jetbrains  
   - d) Microsoft

2. 자바 파일을 작성하는 기본 폴더는?  
   - a) root  
   - b) out  
   - c) .idea  
   - d) src

3. 자바 클래스 실행 시 사용하는 기본 메서드는?  
   - a) start()  
   - b) begin()  
   - c) main()  
   - d) init()


<details>
<summary>정답 보기</summary>
 1️⃣ c) Jetbrains  
 2️⃣ d) src  
 3️⃣ c) main()
</details>
---

## 🔁 복습 질문

- IntelliJ에서 프로젝트를 만들 때 꼭 필요한 설정은 무엇인가요?
- Hello.java 파일은 어디에 생성하나요?
- 실행 결과는 어떤 방식으로 보여지나요?
- `.class` 파일은 어느 경로에 생성되며 무슨 역할을 하나요?

---

## 🙏 마무리

IntelliJ에서 자바를 실행하는 방법을 배웠어요 🎉  
다음 시간엔 **버전 관리(Git)** 또는 **자바 문법**을 이어서 배울 예정입니다.  
궁금한 점은 언제든 질문해 주세요 😊

