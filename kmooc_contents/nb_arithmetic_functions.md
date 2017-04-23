
Lab #0 - jupyter notebook autograder test
=======

Copyright 2017 © document created by TeamLab.Gachon@gmail.com

## Introduction
많이 달라진 프로그래밍 환경에 놀란 것도 잠시, 첫 번째 Lab을 수행하게 됩니다. 첫 번째 랩은 전혀 어렵지 않습니다. 단지 `atom`이 아닌 jupyter notebook(a.k.a ipython notebook) 환경에서 Lab을 제출 하는 것을 배우게 됩니다. 아마 TEAMLAB의 Python MOOCf를 들은 수강생이라면 전혀 어렵지 않게 제출할 수 있을 것 입니다.

먼저  Lab Template 파일을 다운로드 받으십다. 다운로드를 받기 위해서는 python 파일 또는 jupyter notebook 파일을 생성하여 아래 코드를 실행 시켜야 한다.


```python
import gachon_autograder_client as g_autograder

THE_TEMLABIO_ID = "#YOUR_ID"
PASSWORD = "#YOUR_PASSWORD"
ASSIGNMENT_NAME = "nb_test"

g_autograder.get_assignment(THE_TEMLABIO_ID , PASSWORD, ASSIGNMENT_NAME)
```

위 소스 코드를 .py 파일 또는 jupyter notebook에 입력하여 파이썬으로 실행 시키면 "nb_arithmetic_functions.ipynb" 파일이 생성되며, `jupyter notebook`으로 실행하거나, 콘솔창(cmd)에서 해당 파일이 있는 폴더로 이동 후 아래와 같이 입력하면 해당 파일이 실행 될 것입니다.

```
jupyter notebook nb_arithmetic_functions.ipynb
```

## nb_arithmetic_functions 코드 구조

본 Lab은 단순히 autograder를 테스트하기 위한 Lab으로 두 함수만 수행 할 수 있게 작성하면 됩니다.

함수명           | 역할 
--------       | ---
addition      | 정수 또는 실수 형태로 입력되는 두 변수 a,b 의 합을 반환함
minus  | 정수 또는 실수 형태로 입력되는 두 변수 a,b 의 차를 반환함

이제 아래 두 함수의 실행 결과 값이 올바르게 나오도록 다음 함수를 수정하시기 바랍니다. 

### Problem #1 - addition 함수


```python
def addition(a, b):
    result = None
    return result
```


```python
# 실행결과
print (addition(5, 3))
print (addition(10, 5))
```

    8
    15
    

### Problem #2 -  minus 함수


```python
def minus(a, b):
    result = None
    return result
```


```python
# 실행결과
print (minus(5, 3))
print (minus(10, 5))
```

    2
    5
    

## 결과 제출 하기

본 Lab이 쉬우니 숙제 제출도 어렵지 않습니다. 본 Lab의 숙제 제출은 다음의 코드를 수행하면, 채점 결과를 자동으로 제공해 줍니다.
문제없이 숙제를 제출하면 아래 결과가 모두 PASS로 표시 될 것 입니다. K-MOOC 사용자는 따로 K-MOOC 사이트를 통해 제출해야 하니 이점 유의하시기 바랍니다.


```python
import gachon_autograder_client as g_autograder

THE_TEMLABIO_ID = "#YOUR_ID"
PASSWORD = "#YOUR_PASSWORD"
ASSIGNMENT_FILE_NAME = "nb_arithmetic_functions.ipynb"

g_autograder.submit_assignment(THE_TEMLABIO_ID, PASSWORD, ASSIGNMENT_FILE_NAME)
```

    -------------------- | ---------- | -------------------- 
           Function Name |    Passed? |             Feedback 
    -------------------- | ---------- | -------------------- 
                   minus |       PASS |             Good Job 
                addition |       PASS |             Good Job 
    -------------------- | ---------- | -------------------- 
    

## Next Work
처음 Lab은 워밍업입니다. 두 번째 Lab도 비교적 평이하니 즐거운 마음으로 임하시길 바랍니다. Enjoy

> **Human knowledge belongs to the world** - from movie 'Password' -
