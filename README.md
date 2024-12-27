# 리스트를 사용한 집합 구현

## 🔍 프로젝트 개요

이 프로젝트는 Python의 기본 자료형인 `set`을 사용하지 않고, `list`를 이용해 직접 집합 자료구조를 구현하는 것을 목표로 합니다. 이를 통해 `list`와 `function`의 활용 방법을 익히고, 집합의 다양한 연산을 직접 구현해보는 기회를 제공합니다.  
특히, 이번 프로젝트에서 구현하는 집합은 **문자열(String) 데이터만 포함** 합니다.

---

## 🎯 주요 목표

1. Python의 `list`를 활용하여 **중복 제거 및 순서 무관** 특성을 가진 집합 자료구조를 구현합니다.
2. 다양한 집합 연산(합집합, 교집합, 차집합 등)을 직접 구현합니다.
3. 재귀(Recursion)와 같은 고급 프로그래밍 개념을 적용하여 **부분집합 생성** 등 복잡한 연산을 효율적으로 수행합니다.

---

## 🛠️ 구현할 주요 함수 및 동작

### Basic
- **`make_set(A)`**: 리스트 `A`에서 중복된 원소를 제거해 집합을 생성합니다.
- **`add(x, A)`**: 원소 `x`를 집합 `A`에 추가합니다.
- **`remove(x, A)`**: 원소 `x`를 집합 `A`에서 제거합니다.
- **`union(A, B)`**: 두 집합 `A`와 `B`의 합집합을 계산합니다.
- **`intersection(A, B)`**: 두 집합 `A`와 `B`의 교집합을 계산합니다.
- **`difference(A, B)`**: 집합 `A`에서 `B`를 뺀 차집합을 계산합니다.
- **`is_subset(A, B)`**: 집합 `A`가 집합 `B`의 부분집합인지 확인합니다.
- **`find(x, A)`**: 집합 `A`의 원소 중 `x`가 포함된 문자열을 찾습니다.
- **`get_subsets(A)`**: 집합 `A`의 모든 부분집합을 구합니다.
- **`equals(A, B)`**: 두 집합 `A`와 `B`가 동일한지 확인합니다.
- **`is_disjoint(A, B)`**: 두 집합 `A`와 `B`가 서로소인지 확인합니다.
- **`cartesian_product(A, B)`**: 두 집합 `A`와 `B`의 원소를 이용해 곱집합을 계산합니다.
- **`symmetric_difference(A, B)`**: 두 집합의 대칭 차집합을 계산합니다.

### Extended
- **`intersection3(A, B, C)`**: 세 집합 `A`, `B`, `C`의 교집합을 계산합니다.
- **`union3(A, B, C)`**: 세 집합 `A`, `B`, `C`의 합집합을 계산합니다.
- **`symmetric_difference3(A, B, C)`**: 세 집합의 대칭 차집합을 계산합니다.

---

## 🖥️ 프로그램 동작 시나리오

1. 사용자로부터 세 개의 집합 `A`, `B`, `C`를 입력받습니다.
   - 각 집합은 공백으로 구분된 문자열의 리스트 형태로 입력받습니다.
2. 입력받은 집합을 활용해 아래 연산을 수행합니다:
   - 합집합, 교집합, 차집합, 대칭 차집합
   - 부분집합 확인, 서로소 여부 확인
   - 곱집합 계산, 특정 문자열 검색
   - 부분집합 생성 및 출력
3. 추가적으로, 다음과 같은 확장 연산도 수행합니다:
   - 세 집합의 합집합, 교집합, 대칭 차집합
   - 특정 집합 관계(부분집합, 교집합 포함 여부 등) 확인

---

### 입력 예시
```
Input your set A elements:
a b c
Input your set B elements:
c python c b
Input your set C elements:
a c calculator
```

### 출력 예시
```
====================
A = {"a", "b", "c"}
B = {"c", "python", "b"}
Union of A and B = {"c", "python", "b", "a"}
Intersection of A and B = {"b", "c"}
A - B = {"a"}
B - A = {"python"}
Symmetric difference of A and B =  {"python", "a"}
List of cartesian product of A and B:
{"a", "c"} {"a", "python"} {"a", "b"} {"b", "c"} {"b", "python"} {"b", "b"} {"c", "c"} {"c", "python"} {"c", "b"}

...(생략)...

```

---

## 📂 프로젝트 구조
```
|-- ccp_project2/
|   |-- main.py             # 메인 프로그램 파일
|   |-- README.md           # 프로젝트 설명 파일
```
