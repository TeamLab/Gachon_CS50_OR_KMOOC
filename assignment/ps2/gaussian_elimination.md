
# Lab #2 - Gaussian Elimination with python
----------------------------------------------
Copyright 2017 © document created by TeamLab.Gachon@gmail.com

## Introduction
두 번째 랩을 하면서 한문제 한문제 묘한 쾌감과 만족감을 느꼈다면, 당신은 데이터와 코딩에 대한 기본적으로 맞는 성향을 가진 사람입니다. 이번 LAB은 Operation Research의 가장 핵심 알고리즘 중에 하나인 가우스-조단 소거법(Gauss-Jordan Elimination)을 코드로 작성하는 일 입니다. 가우스 소거법은 O.R.의 핵심 알고리즘인 Simplex 기법의 모태가 되는 알고리즘으로 거의 모든 선형 방정식 풀이에 활용되고 있습니다. 

뭔가 복잡해 보이는 프로세스를 간단히 코드로 만든다는 것은 어려우면서 가슴 뛰는 일 입니다. 역시 즐거운 마음으로 도전하시기 바랍니다.

## 숙제 다운로드 받기
먼저  Lab Template 파일을 다운로드 받으셔야 합니다. 다운로드를 받기 위해서는 python 파일 또는 jupyter notebook 파일을 생성하여 아래 코드를 실행 시켜야 한다.


```python
import gachon_autograder_client as g_autograder

THE_TEMLABIO_ID = "#YOUR_ID"
PASSWORD = "#YOUR_PASSWORD"
ASSIGNMENT_NAME = "gaussian_elimination" 

g_autograder.get_assignment(THE_TEMLABIO_ID , PASSWORD, ASSIGNMENT_NAME)
```

위 소스 코드를 .py 파일 또는 jupyter notebook에 입력하여 파이썬으로 실행 시키면 "gaussian_elimination.ipynb" 파일이 생성되며, jupyter notebook으로 실행하거나, 콘솔창(cmd)에서 해당 파일이 있는 폴더로 이동 후 아래와 같이 입력하면 해당 파일이 실행 될 것 입니다.

```bash
jupyter notebook gaussian_elimination.ipynb
```

## gaussian_elimination.py 코드 구조

본 Lab은 이전 Lab과 다르게 크게 3 Part로 구성되어 있고, 각각의 Part의 세부적인 문제가 주어져 있습니다. 각각의 Part의 세부적인 목적은 아래와 같습니다.

Part명 | Part 내용
--------------------|--------------------------
vector operation | gauss elimination에서 사용하는 가장 기초적인 vector 연산을 위한 함수들이 있음
gauss elimination module | gauss elimination 과정에서 실행 되어야 할 주요 기초 함수들이 있음
gauss elimination solution | vector operation과 gauss elimination module을 활용하여 실제 gauss elimination process를 실행하는 함수

본 Lab에서는 위의 세 가지 Part를 모두 실행하여 실제 사용가능한 gauss elimination 코드를 작성하는 것에 그 목적을 두고 있습니다.

### Part #1 - vector operation (point 1)

함수명 | 함수내용
--------------------|--------------------------
vector_scalar_multiplication | $$
  \alpha \times
  \left[\begin{array}{r}
    x & y & z \\
  \end{array}\right] =
  \left[\begin{array}{r}
    \alpha \times x & \alpha \times y & \alpha \times z \\
  \end{array}\right]
$$
vector_add_operation | $$
  \left[\begin{array}{r}
    a & b & c \\
  \end{array}\right] + 
  \left[\begin{array}{r}
    x & y & z \\
  \end{array}\right] =
  \left[\begin{array}{r}
    a+x & b+y & c+z \\
  \end{array}\right]
$$
vector_subtract_operation | $$
  \left[\begin{array}{r}
    a & b & c \\
  \end{array}\right] - 
  \left[\begin{array}{r}
    x & y & z \\
  \end{array}\right] =
  \left[\begin{array}{r}
    a-x & b-y & c-z \\
  \end{array}\right]
$$


```python
def vector_scalar_multiplication(scalar_value, row_vector):
    return None
```


```python
def vector_add_operation(vector_1, vector_2):
    return None
```


```python
def vector_subtract_operation(vector_1, vector_2):
    return None
```


```python
vector_a = [3, 2, 3]
vector_b = [5, 5, 4]
vector_c = [1, 2, 3]

print (vector_add_operation(vector_a, vector_c)) # Expected value: [4, 4, 6]
print (vector_subtract_operation(vector_b, vector_c)) # Expected value: [4, 3, 1]
print (vector_subtract_operation(vector_a, vector_c)) # Expected value: [2, 0, 0]
print (vector_scalar_multiplication(5, vector_c)) # Expected value: [5, 10, 15]
```

    [4, 4, 6]
    [4, 3, 1]
    [2, 0, 0]
    [5, 10, 15]
    

### Part #2 - gauss elimination module (point 3)

함수명 | 함수내용
--------------------|--------------------------
get_max_row_position | 주어진 Matrix에서 기준이 되는 Column number element value가 가장 큰 Row number를 반환함(//이해가 잘 안되요! Row number보다 Row number index가 맞는것 같아요), 단 반환되는 Row number 현재 처리되고 있는 row number보다 값이 커야 함 
divided_by_pivot_value | row_vector를 주어진 (1/pivot_value) 값으로 scalar-vector product한 row_vector를 반환함, 단 이때 pivot_value로 인해 1이되는 element는 음수가 될 수 없음 (반드시 pivot element는 양수 1이어야 함) 
swap_row | 주어진 matrix에 변경할 두 row number가 주어지면 해당 두 row가 교체 된 새로운 matrix를 반환함. 이 때 입력된 matrix는 완전히 새로운 matrix를 만들어 주어진 matrix의 값을 복사하고 두 row를 교환후 변경된 matrix가 반환됨(기존 argument로 입력된 matrix를 반환하지 않음)
gauss_jordan_elimination_process | 주어진 matrix에서 pivot_row_position의 값을 사용하여 다른 row vector의 column position element를 모두 0으로 만드는 함수, pivot 값과 target이 되는 row vector의 값에 따라 vector addition과 subtraction이 결정됨


```python
def get_max_row_position(target_matrix, current_row_position, current_column_position):
    return None
```


```python
matrix_X = [[12,7,3], [4 ,5,6], [7 ,8,9]]
matrix_Y = [[5,8,1,2], [6,7,3,0], [4,5,9,1]]

print (get_max_row_position(matrix_X, 0, 0)) # Expected value : 0 # 12 > 4 > 7 matrix_X[0].index(12)
print (get_max_row_position(matrix_Y, 0, 2)) # Expected value : 2 # 1 < 3 < 9 matrix_Y[2].index(9)
```


```python
def divided_by_pivot_value(row_vector, pivot_value):
    return None
```


```python
vector_c = [0, -2, 4]
pivot_value = -2

divided_by_pivot_value(vector_c, pivot_value)
```




    [-0.0, 1.0, -2.0]




```python
def swap_row(matrix, source_row_number, target_row_number):
    return None
```


```python
matrix_X = [[12,7,3], [4 ,5,6], [7 ,8,9]]

print(swap_row(matrix_X, 1, 2)) # expected value : [[12, 7, 3], [7, 8, 9], [4, 5, 6]] 
print(swap_row(matrix_X, 2, 1)) # expected value : [[12, 7, 3], [7, 8, 9], [4, 5, 6]] 
print(swap_row(matrix_X, 1, 0)) # expected value : [[4, 5, 6], [12, 7, 3], [7, 8, 9]]
```

    [[12, 7, 3], [7, 8, 9], [4, 5, 6]]
    [[12, 7, 3], [7, 8, 9], [4, 5, 6]]
    [[4, 5, 6], [12, 7, 3], [7, 8, 9]]
    


```python
def gauss_jordan_elimination_process(target_matrix, pivot_row_position, column_position ):
    return None
```


```python
matrix_X = [[1,7,3], [4 ,5,6], [7 ,8,9]]
print(gauss_jordan_elimination_process(matrix_X, 0, 0)) # expected value : [[1, 7, 3], [0.0, 23.0, 6.0], [0.0, 41.0, 12.0]]

matrix_X = [[1,7,3], [0,1,6], [0 ,8,9]]
print(gauss_jordan_elimination_process(matrix_X, 1, 1)) # expected value : [[-1.0, 0.0, 39.0], [0, 1, 6], [0.0, 0.0, 39.0]]

matrix_X = [[1,0,3], [0,1,-6], [0 ,0,1]]
print(gauss_jordan_elimination_process(matrix_X, 2, 2)) # expected value : [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0, 0, 1]]
```

    [[1, 7, 3], [0.0, 23.0, 6.0], [0.0, 41.0, 12.0]]
    [[-1.0, 0.0, 39.0], [0, 1, 6], [0.0, 0.0, 39.0]]
    [[-1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0, 0, 1]]
    

### Part #3 - gauss elimination solution (point 3)

마지막 단계는 앞서 사용한 많은 모듈들을 합쳐서 하나의 gauss elimination solution을 작성하는 것이다. gauss elimination solution은 아래와 같은 순서를 따릅니다.

1. 입력되는 matrix의 전체 row 수를 측정한다.
2. matrix의 0번째 row 부터 한줄씩 pivot row를 증가한다.
3. 현재의 pivot column에서 가장 큰 값이 다른 row에 위치한다면 두 row의 위치를 변경한다.
4. pivot row와 pivot column이 결정됐다면, 해당 pivot value로 pivot row vector를 나눠준다.
5. 4)의 식으로 산출된 pivot row vector로 나머지 row vector들의 pivot column을 0으로 만들어준다.
6. matrix의 마지막 row까지 모든 연산을 실시한다.
7. 최종 산출된 값에서 pivot 값이 -1.0이라면 1.0으로 변경하여 산출한다.
8. 최종 기약 행 사디리꼴 행렬을 반환한다



```python
def gauss_elimination_solution(target_matrix):
    return None
```


```python
target_matrix = [[1.0,1.0,-1.0,8.0], [-3.0,-1.0,2.0,-11.0], [-2.0,1.0,2.0,-3.0]]
print (gauss_elimination_solution(target_matrix)) 
# Expected value : [[1.0, 0.0, 0.0, -0.666666666666667], [0.0, 1.0, 0.0, 4.333333333333333], [0.0, 0.0, 1.0, -4.333333333333334]]

target_matrix = [[-3.0,2.0,-6.0,6.0], [5.0,7.0,-5.0,3.0], [1.0,4.0,-2.0,1.0]]
print (gauss_elimination_solution(target_matrix))
# Expected value : [[1.0, -0.0, -0.0, -0.09302325581395321], [0.0, 1.0, 0.0, -0.24418604651162812], [-0.0, -0.0, 1.0, -1.0348837209302326]]
```

    [[1.0, 0.0, 0.0, -0.666666666666667], [0.0, 1.0, 0.0, 4.333333333333333], [0.0, 0.0, 1.0, -4.333333333333334]]
    [[1.0, 0, 0, -0.09302325581395321], [0.0, 1.0, 0.0, -0.24418604651162812], [-0.0, -0.0, 1.0, -1.0348837209302326]]
    

## 결과 제출 하기

문제없이 숙제를 제출하면 아래 결과가 모두 PASS로 표시 될 것 입니다.


```python
import gachon_autograder_client as g_autograder

THE_TEMLABIO_ID = "#YOUR_ID"
PASSWORD = "#YOUR_PASSWORD"
ASSIGNMENT_FILE_NAME = "gaussian_elimination.ipynb"

g_autograder.submit_assignment(THE_TEMLABIO_ID , PASSWORD, ASSIGNMENT_NAME)
```

## Next Work
이 숙제는 사실 상당히 어려운 숙제입니다. 그리고 제출자 또한 대부분의 수강자가 스스로 못할 것이라고 생각합니다. 혹시 스스로 모든 문제를 해결 했다면, 당신은 정말 대단한 사람입니다. 멋쟁이 우후훗.

한 동안 (코딩은) 쉽니다. 고생하셨습니다.

> **Human knowledge belongs to the world** - from movie 'Password' -
