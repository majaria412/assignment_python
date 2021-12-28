# 🔍 Python Assignment

## 🔍 과제 내용: ATM Controller

본 과제에서 구현해야 할 것은 은행에서 사용되는 **ATM Controller**입니다. 물론 현업에 사용되는 모듈은 다소 복잡할 것이기 때문에 다음과 같은 전제를 먼저 제시하겠습니다.

- 돈의 최소 단위는 1달러입니다.
- 크레딧 카드가 ATM에 삽입되었을 때, 실제로 일어나는 세부 과정은 모두 넘어갑니다. 
오직 해당 크레딧 카드의 Pin Number가 프로그램에 Input으로 주어질 것입니다.

ATM Controller는 다음과 같은 기능을 지원해야 합니다.

### 📕 핀 번호 검증

해당 핀 번호가 유효한지 검증할 수 있어야 합니다. 
여기서 말하는 "유효"란 유저 데이터베이스에 Pin Number에 존재하냐를 묻는 것이 아닌, Pin Number 포맷 일치 여부를 의미합니다.

예를 들어 `XX-XX` 라는 포맷으로 정의가 되어있다면 `00-01`은 유효한 것이지만 `0-01`은 유효하지 않은 핀 넘버입니다.

해당 Controller를 사용하고자 하는 은행은 기존 시스템에서 이미 정의된 Pin Number Format을 사용하고 있을 것입니다. 때문에 우리는 검증을 위한 Rule을 직접 정의할 수 있도록 Interface를 제공해야 합니다.

### 📕 계정 선택

입력받은 핀 번호가 검증 과정을 통과했다면, 해당 핀 번호와 연결된 계정 정보를 조회합니다.

은행에 따라서 하나의 핀 번호에 하나의 계정이 할당될수도 있고, 복수의 계정이 할당될 수도 있습니다.

### 📕 계정 잔고 조회

선택된 계정의 잔고를 조회합니다. 

### 📕 입금, 출금

선택된 계정에 금액을 입금하거나, 출금합니다. 

즉,  Controller는 반드시 아래와 같은 프로세스로 작업을 수행해야 합니다.

**핀번호 입력 > 핀번호 검증 > 계정 선택 > 입금, 출금, 잔고조회**

## 🔍 구현 요구사항

해당 Controller 구현에 앞서, 반드시 아래와 같은 사항을 준수해야 합니다.

### 🔍 의존성 분리

우리는 ATM Controller를 구현하여, 새로운 은행에 해당 모듈을 도입시키고자 합니다. **새로운 은행이 어떠한 모듈을 사용하고, 어떤 데이터베이스와 어떠한 아키텍쳐로 시스템이 구성되어 있는지는 알 수 없습니다. 우리는 그 모두에 유연하게 대응할 수 있는 Controller를 구현**해야 합니다.

(예를 들어, 어떤 은행은 ORM을 사용할 것이고, 어떤 은행은 순수하게 Query로 Database와 통신할 수도 있습니다.)

때문에 해당 Controller는 **실제로 API로써 동작하는 Endpoint Side, Database와 통신하는 Model Side**와 완전히 별도로 분리된 모듈을 구현해야 합니다.

### 🔍 Controller 설계

본 과제는 위의 ATM의 기능을 순서대로 시나리오에 맞춰 수행하는 코드를 구현하라는 것이 아닙니다. 그러한 작업은 실제로 은행 시스템을 관리하는 개발자가 해야하는 것이고, 우리의 임무는 그러한 은행 내부 개발자들이 더 쉽고, 안전하게 모듈을 구현할 수 있도록 Controller를 Interface로써 제공해주는 것입니다.

때문에 여러분은 은행 개발자들이 Controller를 올바르게 사용할 수 있도록, 모듈에 독자적인 Rule을 설계해야 할 것입니다. 이러한 Rule은 어떠한 방식으로 해도 무방하지만, 개발자가 Controller의 사용 방법에 대해서 잘못 인지하더라도 Exception으로 그것을 올바르게 이끌어줄 수 있도록 도와주어야 합니다.

또한 여러분이 만든 Controller 사용 방법에 대해 간단한 메뉴얼과 샘플코드를 `README.md`에 작성해주십시오.

### 🔍 단위 테스트

구현한 Controller를 테스트하는 코드를 작성해주세요.

테스트를 위해 어떠한 방식으로라도 상관없으나, 굳이 이걸 직접 짜기 보단 Python의 기본 라이브러리인  `unittest` 프레임워크를 사용하는 것을 권장합니다.

unittest는 쉽게 코드를 테스트할 수 있게 도와줍니다. 아래의 좋은 예시가 있으니 참고바랍니다.

## 구현 내용

1. atm_controller.py
@ class 내부에 4개의 method를 사용
    1) 핀 번호 검증: check_pin_number()
    2) 계정 선택: find_accounts()
    3) 계정 잔고 조회: check_balance()
    4) 입금, 출금: make_transaction()

2. database.py
@ sqlite3 import, sql raw query 사용
    1) get_account()
    2) get_balance()
    3) update_balance()
    4) transaction_history()

3. exception.py

4. test.py

## 구조

1. 2개의 table: accounts(id, pin_num, acc_num, balance), transaction_event(id, balance, history)

2. 

### 주요 설계 포인트

## 실행환경 설절 방법

    ```commandline
    ```

## 과제 결과물 테스트 및 확인 방법

1. POSTMAN 확인
    ```commandline
    
    ```

2. 배포된 서버의 주소

    ```commandline
  
    ```

# Reference

