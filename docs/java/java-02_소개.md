물론이죠! 😄 아래 내용을 한 번에 복사할 수 있도록 마크다운 형식으로 제공해드릴게요.
👉 이 내용을 `hello-java.md` 등으로 저장하시면 MkDocs에 바로 활용 가능합니다.

---

````markdown
# 🎉 즐거운 자바

## 👩‍🏫 강경미 (carami@nate.com), 👨‍🏫 김성박 (urstory@gmail.com)

---

# 👋 Hello

간단한 자바 프로그램을 작성해보며 구조를 살펴봅시다.

---

# 🔍 Hello.java 파일 분석하기

```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello");
    }
}
````

---

# 🧱 Hello.java의 3가지 중요한 부분

## ① 클래스 선언

```java
public class Hello {
    ...
}
```

* `public class`로 선언된 `Hello` 클래스
* **클래스 이름과 파일 이름은 반드시 같아야 합니다.**
  예: `Hello.java` (대소문자 구분!)

---

## ② 메서드 선언

```java
public static void main(String[] args) {
    ...
}
```

* 클래스는 \*\*필드(Field)\*\*와 \*\*메서드(Method)\*\*를 가질 수 있습니다.
* 위 코드는 **프로그램의 시작점**인 `main` 메서드입니다.
* Java 프로그램은 반드시 이 메서드를 포함해야 실행됩니다.

---

## ③ System.out.println()

```java
System.out.println("Hello");
```

* `System` 클래스가 가진 **out 필드**를 통해
* `println()` 메서드를 호출 → 화면에 출력!
* `"Hello"`는 문자열(String)이며, 큰따옴표까지 포함된 텍스트입니다.

📌 구분:

| 요소          | 의미        |
| ----------- | --------- |
| `System`    | 자바 내장 클래스 |
| `out`       | 출력 스트림 필드 |
| `println()` | 출력 메서드    |

---

# ⚙️ 컴파일 하기

```bash
javac Hello.java
```

* `javac`는 Java Compiler를 의미합니다.
* 컴파일이 성공하면 `Hello.class`라는 **바이트 코드 파일**이 생성됩니다.
* 컴파일 실패 시 오류 메시지가 출력됩니다.
* `Hello.class`는 사람이 보기 어려운 기계어 수준의 코드입니다.

---

# 🚀 JVM으로 실행하기

```bash
java Hello
```

* `java` 명령은 JVM(Java Virtual Machine)을 실행합니다.
* JVM은 `.class` 바이트 코드를 한 줄씩 읽고 실행합니다.
  👉 **인터프리터 방식**이라고 합니다.
* `java Hello` 명령에서는 `.class` 확장자를 **입력하지 않습니다.**

📝 예시:

| 명령어                | 설명                 |
| ------------------ | ------------------ |
| `javac Hello.java` | 소스 파일을 바이트 코드로 컴파일 |
| `java Hello`       | 컴파일된 클래스 실행        |

---

# ✏️ 연습 문제

본인의 정보를 출력하는 클래스를 만들어보세요.

예시:

```java
public class MyInfo {
    public static void main(String[] args) {
        System.out.println("이름: 홍길동");
        System.out.println("성별: 남성");
        System.out.println("이메일: hong@gmail.com");
    }
}
```

> 직접 작성하고 `javac`로 컴파일 → `java MyInfo`로 실행해보세요! 😊

---

# 🙏 감사합니다!

다음 강의에서는 변수와 데이터 타입에 대해 알아볼 예정입니다.

```

---
