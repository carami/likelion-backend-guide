# 4강: 자바 주석문과 Enum

> 강사: **강경미** (carami@nate.com)

---

## 📚 강의 개요

이번 강의에서는 자바 코드의 가독성과 유지보수성을 높이는 핵심 요소인 **주석문**과, 타입 안정성을 높이는 **Enum**에 대해 학습합니다.

**주제**

- 자바 주석문의 종류와 활용법
- Javadoc 문서화 방식
- Enum 타입과 고급 활용법

**학습 목표**

1. 주석문의 세 가지 종류를 구분하고 사용할 수 있다.
2. Javadoc의 주요 태그를 활용해 API 문서를 작성할 수 있다.
3. 기존 `final static` 상수 방식의 한계를 이해하고 Enum의 장점을 설명할 수 있다.
4. Enum에 생성자, 필드, 메소드를 추가해 활용할 수 있다.
5. `EnumMap`, `EnumSet`을 사용할 수 있다.

---

## 📖 목차

1. 주석문 (Comments)
2. Enum (열거 타입)
3. 학습 정리

---

## 1. 주석문 (Comments)

자바에서는 아래와 같은 주석 형태를 사용합니다.

| 종류     | 설명                                |
| -------- | ----------------------------------- |
| `//`     | 한 줄 주석                          |
| `/* */`  | 여러 줄 주석                        |
| `/** */` | Javadoc 주석 (API 문서 자동 생성용) |

### Javadoc 주요 태그

| 태그          | 설명                         |
| ------------- | ---------------------------- |
| `@param`      | 매개변수 설명                |
| `@return`     | 반환값 설명                  |
| `@author`     | 작성자                       |
| `@version`    | 버전 정보                    |
| `@since`      | 기능 추가 시점               |
| `@exception`  | 발생 가능한 예외 설명        |
| `@see`        | 관련 문서나 링크 참고        |
| `@deprecated` | 더 이상 사용되지 않음을 알림 |

> 💡 IntelliJ에서는 `Tools > Generate JavaDoc` 메뉴로 문서를 생성할 수 있어요.

---

## 2. Enum (열거 타입)

### 기존 상수 방식의 문제

```java
public class DayType {
    public static final int SUNDAY = 0;
    public static final int MONDAY = 1;
}
```

- 숫자 값이 의미를 설명하지 못함
- 타입 안정성이 부족함

### Enum으로 개선

```java
public enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}
```

- 의미가 명확하고 코드가 읽기 쉬움
- `switch`와 `==` 연산자로 쉽게 사용 가능

### 생성자와 필드를 가진 Enum

```java
public enum Gender {
    MALE("XY"), FEMALE("XX");

    private final String chromosome;

    private Gender(String chromosome) {
        this.chromosome = chromosome;
    }

    public void printChromosome() {
        System.out.println("염색체: " + chromosome);
    }
}
```

---

### Enum 유틸리티 클래스

| 클래스    | 특징 및 용도                              |
| --------- | ----------------------------------------- |
| `EnumMap` | Enum을 키로 사용하는 Map                  |
| `EnumSet` | Enum 값만 저장하는 Set, 내부적으로 효율적 |

```java
EnumSet<Day> weekends = EnumSet.of(Day.SATURDAY, Day.SUNDAY);
EnumMap<Day, String> labels = new EnumMap<>(Day.class);
```

---

### Enum + 추상 메소드 활용

```java
public enum Country {
    KOREA {
        public void print() {
            System.out.println("대한민국");
        }
    },
    JAPAN {
        public void print() {
            System.out.println("일본");
        }
    };

    public abstract void print();
}
```

---

## 📝 학습 정리

### ✅ 체크리스트

- [ ] 세 가지 주석 방식(`//`, `/* */`, `/** */`)의 차이를 설명할 수 있다.
- [ ] 주요 Javadoc 태그를 적절히 사용할 수 있다.
- [ ] Enum을 사용하여 코드 안정성과 가독성을 높일 수 있다.
- [ ] Enum에 생성자/필드/메서드를 추가할 수 있다.
- [ ] `EnumMap`, `EnumSet`의 장점을 설명할 수 있다.

---

## ❓ 퀴즈

**Q1.** Javadoc에서 메소드의 매개변수를 설명하는 태그는?
👉 `@param`

**Q2.** Enum의 특징으로 틀린 것은?
4\. `public` 생성자를 가질 수 있다. ❌
→ Enum 생성자는 외부에서 호출할 수 없으며 `private`이어야 합니다.

---

## 💬 생각해보기

1. "좋은 코드는 주석이 필요 없다"는 말에 대해 어떻게 생각하나요?
2. 요일, 등급, 결제수단 등을 Enum으로 표현할 때의 장점은?
3. Enum에 추상 메소드를 선언하고 각 상수에 구현하는 방식은 어떤 상황에서 유용할까요?

---
