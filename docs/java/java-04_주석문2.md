
# 4강: 자바 주석문과 Enum

* **강사**: 강경미(carami@nate.com), 김성박(urstory@gmail.com)
* **작성일**: 2025-07-07

---

## 📚 강의 개요

이번 강의에서는 자바 코드의 가독성과 유지보수성을 높이는 핵심 요소인 **주석문(Comments)**과, 타입에 안전한 상수를 정의하는 **열거 타입(Enum)**에 대해 깊이 있게 학습합니다.

* **주제**: 자바 주석문의 종류와 활용법, Javadoc을 이용한 문서화, Enum 타입의 개념과 고급 활용법
* **학습 목표**:
    1.  주석문의 세 가지 종류를 구분하고 상황에 맞게 올바르게 사용할 수 있다.
    2.  Javadoc의 개념과 주요 태그를 이해하고, API 문서를 생성할 수 있다.
    3.  기존 `final static` 상수 방식의 문제점을 이해하고 Enum의 필요성을 설명할 수 있다.
    4.  Enum을 정의하고 생성자, 필드, 메소드를 추가하여 비즈니스 로직에 활용할 수 있다.
    5.  `EnumMap`, `EnumSet` 등 Enum 관련 유틸리티 클래스를 사용하여 코드를 효율적으로 작성할 수 있다.

---

## 📖 목차

1.  [주석문 (Comments)](#1-주석문-comments)
    * [자바의 주석문 종류](#자바의-주석문-종류)
    * [Javadoc 주석문과 태그](#javadoc-주석문과-태그)
    * [좋은 주석을 작성하는 방법](#좋은-주석을-작성하는-방법)
2.  [Enum (열거 타입)](#2-enum-열거-타입)
    * [상수 사용의 문제점](#상수-사용의-문제점)
    * [Enum 타입 사용하기](#enum-타입-사용하기)
    * [Enum 타입의 주요 특징](#enum-타입의-주요-특징)
    * [Enum에 생성자, 필드, 메소드 추가하기](#enum에-생성자-필드-메소드-추가하기)
    * [Enum과 유틸리티 클래스 (EnumMap, EnumSet)](#enum과-유틸리티-클래스-enummap-enumset)
    * [Enum의 고급 활용 (인터페이스, 추상 메소드)](#enum의-고급-활용-인터페이스-추상-메소드)
3.  [📝 학습 정리](#-학습-정리)
    * [학습 확인 체크리스트](#학습-확인-체크리스트)
    * [퀴즈로 복습하기](#퀴즈로-복습하기)
    * [생각해보기 (복습 질문)](#생각해보기-복습-질문)

---

## 1. 주석문 (Comments)

주석문은 프로그램의 실행에는 영향을 주지 않지만, 코드에 대한 설명을 붙여 가독성을 높이고 다른 개발자와의 협업을 돕는 중요한 요소입니다.

### 자바의 주석문 종류

자바는 세 가지 형태의 주석을 제공합니다.

| 주석 기호         | 설명                                                                 | 사용 예                                 |
| ----------------- | -------------------------------------------------------------------- | --------------------------------------- |
| `//`              | 기호부터 해당 줄의 끝까지 주석으로 처리됩니다. (한 줄 주석)            | `int count = 10; // 카운터 변수`       |
| `/* ... */`       | `/*` 와 `*/` 사이의 모든 내용을 주석으로 처리합니다. (여러 줄 주석) | `/* 이 부분은<br>여러 줄에 걸쳐<br>설명합니다. */` |
| `/** ... */`      | `javadoc` 도구를 통해 API 문서로 생성될 수 있는 특별한 주석입니다.     | `/** Book 클래스 */`                 |

<br>

💻 **실습 예제 1: 일반 주석 활용**

```java
public class Book {
    /*
        title과 price를 필드로 선언하였습니다.
        이처럼 여러 줄에 걸쳐 주석을 작성할 수 있습니다.
    */
    private String title;
    private int price; // 가격 필드

    // 필드의 값을 수정하고 얻기 위한 메소드 (Setter, Getter)
    // 이런 메소드들을 '프로퍼티(Property)'라고도 부릅니다.
    public int getPrice() {
        return this.price; // this는 현재 인스턴스를 참조하는 예약어입니다.
    }

    public void setPrice(int price) { // 매개변수 price는 지역 변수입니다.
        this.price = price;
    }
    // ... 이하 생략
}
````

### Javadoc 주석문과 태그

Javadoc 주석(`/** ... */`)은 클래스, 메소드, 필드 선언부 바로 위에 작성하여 코드의 명세를 문서화하는 데 사용됩니다. 특정 `@` 태그를 사용하여 구조적인 정보를 제공할 수 있습니다.

| 태그          | 설명                                                              |
| :------------ | :---------------------------------------------------------------- |
| `@author`     | 작성자 이름                                                       |
| `@version`    | 클래스나 메소드의 버전 정보                                       |
| `@since`      | 해당 기능이 추가된 시점 (버전, 날짜 등)                           |
| `@param`      | 메소드의 매개변수에 대한 설명                                     |
| `@return`     | 메소드의 반환값에 대한 설명                                       |
| `@exception`  | 발생할 수 있는 예외(Exception)에 대한 설명                        |
| `@deprecated` | 더 이상 사용되지 않거나, 삭제될 예정임을 알림                      |
| `@see`        | 관련 있는 다른 클래스나 메소드, 외부 링크를 참조시킬 때 사용       |

\<br\>

💻 **실습 예제 2: Javadoc 주석 활용**

```java
/**
 * 책 한 권의 정보를 담기 위한 클래스입니다.
 *
 * @author urstory(김성박)
 * @since 2022.03
 * @version 1.0
 */
public class Book {
    private String title;
    private int price;

    /**
     * 책의 가격을 설정합니다.
     * @param price 책의 가격 (음수일 수 없음)
     */
    public void setPrice(int price) {
        this.price = price;
    }

    /**
     * 책의 제목을 반환합니다.
     * @return 책의 제목
     */
    public String getTitle() {
        return title;
    }
}
```

💡 **Tip:** IntelliJ와 같은 IDE에서는 `shift` 키를 두 번 눌러 `Generate Javadoc`을 실행하면 Javadoc 문서를 쉽게 생성할 수 있습니다.

### 좋은 주석을 작성하는 방법

  - **코드로 말하기**: 주석이 없어도 이해할 수 있도록 클래스, 메소드, 변수 이름을 명확하게 작성하는 것이 최선입니다.
  - **왜(Why)를 설명하기**: '무엇을 하는지'보다 '왜 이 코드가 필요한지', '왜 이런 방식을 선택했는지'와 같은 비즈니스 로직이나 설계 의도를 설명하는 것이 더 가치 있습니다.
  - **Javadoc 적극 활용하기**: 외부에 공개되는 API(Public Class, Method)에는 Javadoc 주석을 충실히 작성하여 사용자에게 정확한 정보를 제공해야 합니다.

-----

## 2\. Enum (열거 타입)

`Enum`(Enumeration)은 서로 연관된 **상수들의 집합**을 정의할 때 사용하는 특별한 데이터 타입입니다. JDK 5부터 도입되었으며, 상수를 훨씬 더 안전하고 의미 있게 사용할 수 있게 해줍니다.

### 상수 사용의 문제점

Enum이 없던 시절에는 `public final static int` 와 같은 방식으로 상수를 정의했습니다.

```java
// 😥 기존 방식의 문제점
public class DayType {
    public final static int SUNDAY = 0;
    public final static int MONDAY = 1;
    // ...
}

int today = DayType.SUNDAY; // today는 0
int myValue = 100; // 요일과 관련 없는 임의의 정수도 할당 가능!
```

이 방식은 다음과 같은 **치명적인 단점**이 있습니다.

  * **타입 안전성(Type-Safety) 부재**: 변수에 정해진 상수 값 외에 다른 어떤 정수 값도 할당될 수 있어 오류 발생 가능성이 높습니다.
  * **의미 불명확**: `today` 변수의 값이 `0`일 때, 이것이 `SUNDAY`를 의미하는지 코드를 보지 않으면 알기 어렵습니다.

### Enum 타입 사용하기

Enum은 이러한 문제를 완벽하게 해결합니다.

```java
// ✨ Enum을 사용한 개선
public enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}
```

  - **사용법**: 클래스처럼 필드로 선언하고, 정해진 상수 값만 할당할 수 있습니다.

<!-- end list -->

```java
public class Today {
    private Day day; // Day 타입의 필드

    public void setDay(Day day) {
        this.day = day;
    }
    //...
}

// Enum 값 할당
Today today = new Today();
today.setDay(Day.SUNDAY); // O, 타입에 안전함!
// today.setDay(100); // X, 컴파일 오류 발생!
```

✅ **핵심**: Enum을 사용하면 변수에 할당할 수 있는 값을 특정 상수들로 **강제**할 수 있어 \*\*타입 안전성(Type-Safety)\*\*이 보장됩니다.

### Enum 타입의 주요 특징

  * **`switch`문과 완벽한 조합**: `switch`문에서 사용하면 코드가 매우 간결하고 가독성이 높아집니다.
    ```java
    Day day = Day.SUNDAY;
    switch(day) {
        case SUNDAY: // Day.SUNDAY가 아닌 SUNDAY로 사용
            System.out.println("일요일입니다.");
            break;
        case MONDAY:
            System.out.println("월요일입니다.");
            break;
        default:
            System.out.println("그 밖의 요일");
    }
    ```
  * **동등 비교**: Enum 값들은 `==` 연산자로 비교하는 것이 안전하고 권장됩니다. (`day1 == Day.MONDAY`)

### Enum에 생성자, 필드, 메소드 추가하기

Enum은 단순한 상수의 나열을 넘어, 자체적으로 **생성자, 필드, 메소드**를 가질 수 있는 완전한 객체입니다.

```java
public enum Gender {
    // 각 상수가 생성자를 호출하여 고유한 값을 가짐
    MALE("XY"),
    FEMALE("XX");

    private final String chromosome; // 염색체 필드

    // Enum 생성자는 반드시 private 이어야 함
    private Gender(String chromosome) {
        this.chromosome = chromosome;
    }

    // 일반 메소드 추가 가능
    public void printChromosome() {
        System.out.println("염색체 정보 : " + chromosome);
    }

    @Override
    public String toString() {
        return "염색체: " + chromosome;
    }
}

// 사용 예시
Gender gender = Gender.MALE;
System.out.println(gender); // 출력: 염색체: XY
gender.printChromosome(); // 출력: 염색체 정보 : XY
```

### Enum과 유틸리티 클래스 (EnumMap, EnumSet)

  - **`EnumMap`**: Enum을 키(Key)로 사용하는 특화된 `Map`입니다. 매우 빠르고 효율적으로 동작합니다.
    ```java
    EnumMap<Day, String> schedule = new EnumMap<>(Day.class);
    schedule.put(Day.FRIDAY, "불금!!");
    schedule.put(Day.MONDAY, "월요병...");
    System.out.println(schedule.get(Day.MONDAY)); // 출력: 월요병...
    ```
  - **`EnumSet`**: Enum을 저장하는 특화된 `Set`입니다. 내부적으로 비트 벡터를 사용하여 메모리 효율이 높고 성능이 뛰어납니다.
    ```java
    // 월, 화, 수만 포함하는 Set 생성
    EnumSet<Day> weekday = EnumSet.range(Day.MONDAY, Day.WEDNESDAY);
    for (Day day : weekday) {
        System.out.println(day); // MONDAY, TUESDAY, WEDNESDAY 출력
    }
    ```

### Enum의 고급 활용 (인터페이스, 추상 메소드)

Enum은 인터페이스를 구현하거나, 내부에 추상 메소드를 선언하여 각 상수마다 다른 동작을 구현하게 할 수도 있습니다.

```java
// 각 상수마다 다른 동작을 하도록 강제하는 방법
public enum Country {
    KOREA {
        @Override
        public void printCapital() {
            System.out.println("대한민국의 수도는 서울입니다.");
        }
    },
    JAPAN {
        @Override
        public void printCapital() {
            System.out.println("일본의 수도는 도쿄입니다.");
        }
    };

    // 추상 메소드 선언
    public abstract void printCapital();
}

// 사용 예시
Country country = Country.KOREA;
country.printCapital(); // 출력: 대한민국의 수도는 서울입니다.
```

-----

## 📝 학습 정리

### 학습 확인 체크리스트

  - [ ] 한 줄 주석(`//`)과 여러 줄 주석(`/* */`)의 차이점을 이해했나요?
  - [ ] Javadoc 주석(`/** */`)을 사용하여 클래스와 메소드에 설명을 붙일 수 있나요?
  - [ ] `@param`, `@return`, `@author` Javadoc 태그를 올바르게 사용할 수 있나요?
  - [ ] `final static` 상수의 타입 안전성 문제를 설명할 수 있나요?
  - [ ] `enum` 키워드를 사용하여 열거 타입을 정의할 수 있나요?
  - [ ] Enum에 private 생성자와 필드를 추가하여 각 상수에 고유한 값을 부여할 수 있나요?
  - [ ] `EnumMap`과 `EnumSet`의 용도와 장점을 이해했나요?

### 퀴즈로 복습하기

❓ **Quiz 1.** 다음 중 Javadoc 주석에서 메소드의 매개변수를 설명하는 태그는 무엇인가요?

\<details\>
\<summary\>정답 확인\</summary\>
\<p\>

**정답: 3. `@param`**

`@param` 태그는 메소드가 받는 인자(매개변수)의 이름과 그에 대한 설명을 명시하는 데 사용됩니다.

\</p\>
\</details\>

1.  `@return`
2.  `@author`
3.  `@param`
4.  `@since`

-----

❓ **Quiz 2.** Enum의 특징으로 **틀린** 것을 고르세요.

\<details\>
\<summary\>정답 확인\</summary\>
\<p\>

**정답: 4번**

Enum의 생성자는 외부에서 호출할 수 없으며, 반드시 `private` 접근 제어자를 가져야 합니다. (명시적으로 `private`을 쓰지 않아도 컴파일러가 자동으로 `private`으로 간주합니다.)

\</p\>
\</details\>

1.  타입에 안전한 상수 집합을 정의할 수 있다.
2.  `switch` 문에서 사용할 수 있어 가독성이 좋다.
3.  `==` 연산자로 안전하게 비교할 수 있다.
4.  `public` 생성자를 가질 수 있다.

-----

❓ **Quiz 3.** `EnumSet.range(Day.MONDAY, Day.WEDNESDAY)`의 결과로 생성된 `EnumSet`에 포함되지 **않는** 요일은 무엇인가요?

\<details\>
\<summary\>정답 확인\</summary\>
\<p\>

**정답: 4. `THURSDAY`**

`EnumSet.range()` 메소드는 시작 상수부터 끝 상수를 **포함**하는 범위의 모든 상수를 Set으로 만듭니다. 따라서 `MONDAY`, `TUESDAY`, `WEDNESDAY`가 포함되고, `THURSDAY`는 포함되지 않습니다.

\</p\>
\</details\>

1.  `MONDAY`
2.  `TUESDAY`
3.  `WEDNESDAY`
4.  `THURSDAY`

### 생각해보기 (복습 질문)

1.  "좋은 코드는 주석이 필요 없다"는 말에 대해 어떻게 생각하시나요? 여러분이 생각하는 '좋은 주석'이란 무엇인가요?
2.  프로젝트에서 요일, 회원 등급(예: BRONZE, SILVER, GOLD), 결제 수단(예: CARD, CASH, BANK\_TRANSFER) 등을 관리해야 할 때, `String` 이나 `int` 대신 `Enum`을 사용하면 어떤 구체적인 이점들이 있을까요?
3.  Enum에 추상 메소드를 선언하고 각 상수에서 구현하는 방식은 `switch` 문을 사용하는 것과 비교했을 때 어떤 장단점이 있을까요? (객체 지향적 관점에서 생각해보세요.)

<!-- end list -->
