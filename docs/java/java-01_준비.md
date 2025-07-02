# 🎉 즐거운 자바

## 👩‍🏫 강사 소개  
**강경미** (carami@nate.com), **김성박** (urstory@gmail.com)

---

## 🗂️ 강의 개요

- **주제:** 자바 언어 소개 및 JDK 설치
- **목표:** 자바의 기초 개념을 이해하고, 개발환경을 구축할 수 있다.
- **시간:** 약 2시간
- **준비물:**
  - VS Code 또는 IntelliJ
  - Git, JDK 21 설치 준비

---

## 🧠 JAVA 언어의 특징과 JDK 설치

### 자바 프로그래밍을 공부하는 이유

- ✅ 기업에서 서버 프로그래밍 시 가장 많이 사용하는 언어

---

### 자바 언어의 특징

- 객체지향 언어
- 자바 언어는 느리지만, 버전업되면서 다른 언어들의 장점을 흡수하고 있다 (**모던 자바**)
  - ✅ **람다(Lambda)** : 함수형 프로그래밍
  - ✅ **Stream API** : 복잡한 데이터 처리도 선언적으로 작성 가능
  - ✅ **병렬 프로그래밍** : 멀티코어 CPU 활용

---

## 💻 자바 프로그램 작성과 실행 (개요)

- JDK (Java Development Kit)를 설치해야 함
- 여러 종류의 JDK:
  - OpenJDK, Oracle JDK, Azul Zulu, Amazon Corretto, Adoptium Temurin
- 추천: [✅ Adoptium Temurin 다운로드 사이트](https://adoptium.net/)
  - Windows: `OpenJDK 21 (MSI Installer)`
  - Mac: `OpenJDK 21 (PKG Installer)`

---

## 🔧 Git 설치 및 환경 설정

```bash
git config --global user.name "이름"
git config --global user.email "이메일"
git config --global core.autocrlf true
```

---

## 🛠️ JDK 21 설치 개요

- 초보자는 JDK 8도 충분하지만, 기업들은 보통 11 이상 사용
- ✅ JDK 17 (2023년 LTS)  
- ✅ JDK 21 (2024년 LTS) → 더 긴 유지보수 기간  

---

## 🍎 Mac에서 JDK 21 설치

### 설치

- `.pkg` 파일 다운로드 후 설치

### 환경 변수 설정

```bash
echo $0          # 사용 쉘 확인 (zsh 또는 bash)
code ~/.zshrc    # zsh일 경우
code ~/.bashrc   # bash일 경우
```

```bash
# 마지막 줄에 추가
export JAVA_HOME=$(/usr/libexec/java_home -v 21)
export PATH=$PATH:$JAVA_HOME/bin
```

### 설치 확인

```bash
java --version
javac -version
```

---

## 🪟 윈도우에서 JDK 21 설치

- `.msi` 파일 다운로드 후 설치
- 환경변수 설정:  
  👉 [JAVA_HOME 설정 방법 (Windows)](https://vmpo.tistory.com/6)

---

## ✍️ 자바 첫 프로그램 작성

### 코드 작성

```bash
code Hello.java
```

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
```

### 컴파일 & 실행

```bash
javac Hello.java
ls -la
java Hello
```

---

## 🐞 설치 중 자주 발생하는 문제

- `javac` 명령어가 인식되지 않음 → 환경 변수 미설정
- Mac에서 `Permission denied` → 실행 권한 문제
- Git이 작동 안 됨 → 재부팅 또는 설치 재확인

---

## ✅ 학습 체크리스트

| 항목 | 확인 |
|------|------|
| JDK 종류와 특징을 이해했다 | ⬜ |
| Git 설치 및 사용자 정보 설정을 완료했다 | ⬜ |
| JDK를 설치하고 환경변수 설정을 완료했다 | ⬜ |
| Hello.java를 작성하고 실행에 성공했다 | ⬜ |
| java와 javac 명령어 차이를 이해했다 | ⬜ |

---

## 🧪 실습 문제

1. Git 사용자 정보 설정
2. Hello.java 작성 후 컴파일 및 실행
3. JAVA_HOME 설정 상태 확인
4. 자신만의 메시지를 출력하는 자바 클래스 작성

---
## 💡 퀴즈

1. 자바를 실행하는 프로그램은?  

   - a) JVM  
   - b) JDK  
   - c) JRE  
   - d) IntelliJ  

2. 자바의 특징이 아닌 것은?  

   - a) 객체지향  
   - b) 병렬 프로그래밍  
   - c) 플랫폼 의존성 큼  
   - d) 안정성 높음  

3. javac Hello.java 명령어의 역할은?  

   - a) 실행  
   - b) 컴파일  
   - c) 변수 설정  
   - d) 클래스 만들기  

<details>
<summary>정답 보기</summary>

1️⃣ a) JVM  
2️⃣ c) 플랫폼 의존성 큼  
3️⃣ b) 컴파일  

</details>
---

## 🔁 복습 질문

- 자바는 어떤 프로그래밍 패러다임을 따르나요?
- JDK와 JRE의 차이는?
- javac와 java 명령어의 차이는?
- Mac에서 JAVA_HOME은 어떻게 설정하나요?

---

## 🔗 참고 자료

- [자바 공식 문서](https://docs.oracle.com/en/java/javase/)
- [Git 공식 문서](https://git-scm.com/book/ko/v2)
- [Mac JAVA_HOME 설정 방법](https://stackoverflow.com/questions/135688/setting-the-java-home-environment-variable-in-macos)

---

## 🙏 마무리

고생 많으셨습니다! 🎉  
다음 시간엔 **변수와 자료형**을 함께 학습합니다.