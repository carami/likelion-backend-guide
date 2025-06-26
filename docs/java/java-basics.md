---
marp: true
---

# 즐거운 자바

## 강경미(carami@nate.com), 김성박 (urstory@gmail.com)

---

# Hello

---

# Hello.java 파일 분석하기

```
public class Hello{
    public static void main(String[] args){
        System.out.println("Hello");
    }

}
```

---

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
