
# Lab #3 - Your own linear programming solver with Python
----------------------------------------------
Copyright 2017 © document created by TeamLab.Gachon@gmail.com

## Introduction
세 번째 랩에 오신 여러분을 환영합니다. 이번 랩은 여러분이 지금까지 gurobi에 의지하여 수행했던 LP 문제를 여러분들 만의 gurobi를 개발하여 해결하는 과제입니다. 설레이시죠? 그렇다면 여러분은 코딩덕후입니다. 막 클래스명 만들고 싶은 요구도 생기고 그럴거라고 믿습니다.구루비는 솔직히 구리잖아요? 좋습니다. 지금부터 여러분들의 Linear Programming Solver. 간단히 gachon lp solver를 만들어 봅시다. 이름이 더 구려진다고요?

## Lab download
이번 숙제부터는 이미 "gachon-autograder-client"를 설치했다고 가정해서 해당 파일에 설치에 대한 설명은 없이 바로 진행합니다.
먼저 Lab Template 파일을 다운로드 받으세요.

아래 링크를 클릭해서 다운로드 받을 수 있습니다. 사실 이를 더 권장합니다.

[downlad](https://github.com/TeamLab/Gachon_CS50_OR_KMOOC/blob/master/assignment/ps3/ps3.zip) - https://github.com/TeamLab/Gachon_CS50_OR_KMOOC/blob/master/assignment/ps3/ps3.zip

다운로드 받고나면 해당 디렉토리에 "gachon_lp_solver.py" 파일이 생성됩니다. 지금까지 lab과는 달리 본 lab은 py 파일을 직접 수정해가며 코딩할 수 있습니다. 해결해야할 "gachon_lp_solver.py"는 "GachonLPSolver"라는 class의 구현을 목적으로 합니다.

## GachonLPSolver
GachonLPSolver Class의 구현을 위해 기본적으로 아래와 같은 사항을 이해해야합니다. 혹시 Class-Object 개념이 약하다면 아래 영상을 참고하시기 바랍니다.
- https://www.youtube.com/watch?v=fi8TGRfDXU0&t=47s&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=50
- https://www.youtube.com/watch?v=cXNV45sx_iY&t=763s&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=51
- https://www.youtube.com/watch?v=8Q9N8E0RpDg&t=1s&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=52
- https://www.youtube.com/watch?v=s2NOU8vMMDU&t=1035s&list=PLBHVuYlKEkUJvRVv9_je9j3BpHwGHSZHz&index=53

### 1. Class의 멤버 변수
Class의 멤버 변수는 Class가 객체화(instance화) 되었을 때, 데이터를 저장하는 변수들로 일반적으로 python에서는 객체 초기화의 특수 목적을 가진 "__init__" 함수에 정의됩니다. GachonLPSolver Class에서 사용되는 객체의 멤버 변수들은 아래 표와 같습니다.

변수명 | 변수용도
--------------------|--------------------------
self._model_name  | string type으로 lp 문제의 모델의 이름이 저장되는 변수
self._objective_variables | 목적함수의 계수 값이 numpy array 형태로 저장되는 변수 ex) 30x + 20y = Z ==> [30 20]
self._optimize_setting | LP 문제의 유형을 저장하는 변수로 최대화 문제일 경우, GachonLPSolver.MAXIMIZE, 최소화 문제일 경우 GachonLPSolver.MINIMIZE를 할당함. 단 본 Lab은 최대화 문제만 해결하는 것을 목적으로 함
self._constraints_coefficient_matrix | 각 제약식의 계수와 rhs를 numpy array 형태로 저장하는 변수, 단 계수가 0일 경우에는 반드시 0이 해당 변수의 자리에 해당되어야만 함. 예) x + y + 0*z = 37  ==> [1 1 0 37]
self._constraints_sign_list | 제약식의 부호를 각 제약식 순서대로 저장한 리스트 타입으로 저장하는 변수, 저장형태는 정수형으로 GachonLPSolver의 클래스 변수를 사용함. 예) <= GachonLPSolver.LESSEQUAL ,  >= GachonLPSolver.GRATERQUAL, = GachonLPSolver.EQUAL
self._standard_form_matrix | 목적함수와 제약식의 정보를 바탕으로 standard form matrix를 numpy array 형태로 저장하는 변수
self._basic_variables_index | basic variable의 self._standard_form_matrix 상 index를 list 형태로 저장하는 변수
self._non_basic_variables_index | non-basic variable의 self._standard_form_matrix 상 index를 list 형태로 저장하는 변수

__init__ 함수의 형태는 아래와 같으며, 첫번째 argument인 self는 instance 자체를 의미하므로 실제 호출시에는 변수를 할당할 필요가 없습니다.

```python
def __init__(self, model_name):
    self._model_name = model_name
    # 이하 생략
```

__init__ 함수를 사용하여, GachonLPSolver class의 인스턴스를 생성하는 코드는 다음과 같습니다.


```python
from gachon_lp_solver import GachonLPSolver # gachon_lp_solver 파일(모듈)에서 GachonLPSolver  class를 import

lpsover = GachonLPSolver("test_example") #GachonLPSolver class의 첫 번째 argument인 model_name에 "test_example" 를 할당함
lpsover.model_name
```




    'test_example'



### 2. Class의 함수

실제 본 Lab에서 구현이 필요한 함수는 아래와 같습니다.

함수명 | 함수용도
--------------------|--------------------------
set_objective_variables | List Type인 목적함수의 계수 벡터 objective_coefficient_vector와 1과 0의 값을 받는 optimize_setting 변수를 argument로 받아  self._objective_variables와 self._optimize_setting 변수를 설정하는 함수
add_constraints | list 또는 numpy array type의 제약식 계수 vector constraints_coefficient_vector와 제약식의 sign, 제약식의 우변상수인 rhs 를 argument로 받아 제약식이 추가될 떄 마다, self._constraints_coefficient_matrix 구성하는 함수
update | 목적함수와 모든 제약식을 입력 받은 후, numpy array 타입인 self._standard_form_matrix 를 완성하는 함수
optimize | simplex algorithm을 사용하여, self._standard_form_matrix 를 optimized standard form matrix로 변환하는 함수
gauss_jordan_elimination_process | self._standard_form_matrix 에서 pivot row와 column이 설정된 후 해당 row를 기준으로 다른 row를 소거해주는 프로세스, 이미 작성되어 있음
get_z_value | 최적화된 self._standard_form_matrix에서 z 값을 반환함
get_objective_variables | 최적화된 self._standard_form_matrix에서 목적함수의 결과값을 출력함

### 3. Test 함수

본 Lab은 기존 lab과 달리 Test가 되는 함수를 작성하는 것이 아니라 class의 함수를 작성하면 test가 통과하게 된다. 본 lab의 test 함수는 모듈(파일)내에 위치해 있으며, 따로 수정할 필요는 없다. Test가 진행되는 내용은 아래와 같습니다.

함수명 | 함수용도
--------------------|--------------------------
model_name | class 함수가 제대로 동작하는지 확인함. 별다른 조치없이 pass가 됨
set_objective_variables (1점) | class 함수중 set_objective_variables을 검사함. self._objective_variables 변수가 정확히 설정되었는지 확인함
add_constraints (1점) | class 함수중 add_constraints을 검사함. self._constraints_coefficient_matrix와 self._constraints_sign_list 변수가 정확히 설정되었는지 확인함
update (1점) | update 함수를 검사함, self._standard_form_matrix 가 맞게 설정되었는지 확인함
optimize_easy (2점) | optimize, get_z_value, get_objective_variables 를 검사함. self._standard_form_matrix 가 최적화 된후 z value와 목적계수의 결과값이 제대로 나오는지 확인함, 부등식이 GachonLPSolver.LESSEQUAL 만 포함된 간단한 모델만 실행시킴
optimize_hard (2점) | optimize, get_z_value, get_objective_variables 를 검사함. self._standard_form_matrix 가 최적화 된후 z value와 목적계수의 결과값이 제대로 나오는지 확인함, 부등식이 GachonLPSolver.GRATERQUAL도 포함된 복잡한 모델도 실행시킴

##  Problem Description

$$
\begin{align}
z = 30x_1 + & 40 x_2 \\
2x_1 + x_2  & \le 8 \\
x_1 + 3x_2  & \le 8 \\
x_1, x_2 & \ge 0 \\
\end{align}
$$

### set_objective_variables

set_objective_variables은 입력된 list 값을 argument로 numpy array 값을 저장합니다. Argument로 입력된 값 중 목적함수의 계수 벡터는 self._objective_variables에 저장되고, optimize_setting은 self._optimize_setting에 저장된다. self._optimize_setting Value는 GachonLPSolver.MAXIMIZE 또는 GachonLPSolver.MINIMIZE만 할당 한다고 가정합니다. 단 MINIMIZE에 대한 별도의 처리는 없습니다.


```python
import numpy as np
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

lpsolver = GachonLPSolver("test_example")
lpsolver.model_name

objective_coefficient_vector = np.array([30, 40])
lpsolver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lpsolver.objective_variables
```




    array([30, 40])



### add_constraints

제약식을 추가한다. 제약식을 추가할 때 argument는 세가지로 제약식의 좌변의 계수 vector, 등식, 우변의 상수값(rhs)를 각각 constraints_coefficient_vector, sign, rhs로 할당한다.constraints_coefficient_vector는 numpy 타입 또는 list 타입이며, sign의 값은 -1 , 0 , 1의 값이 할당된다. sign의 값은 GachonLPSolver.LESSEQUAL, GachonLPSolver.EQUAL, GachonLPSolver.GRATERQUAL의 값만 할당이 가능하다. rhs 값은 실수값(또는 정수값)이 할당된다. <br />
각 변수가 할당되면, 함수내에서는 self._constraints_coefficient_matrix 변수에 제약식의 계수 vector와 rhs 값을 행렬로 추가한다.<br />
즉 새로운 제약조건이 입력될 때 마다, 기존 self._constraints_coefficient_matrix 를 추가한다. <br />
이 때 사용하는 함수로 numpy의 vstack 함수를 사용할 것을 권장한다. <br />
sign의 값은  self._constraints_sign_list 변수에 list 형태로 추가한다


```python
import numpy as np
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

lpsolver = GachonLPSolver("test_example")
lpsolver.model_name

objective_coefficient_vector = np.array([30, 40])
lpsolver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lpsolver.add_constraints([2, 1], GachonLPSolver.LESSEQUAL, 8)
lpsolver.add_constraints([1, 3], GachonLPSolver.LESSEQUAL, 8)

lpsolver.constraints_coefficient_matrix
```




    array([[2, 1, 8],
           [1, 3, 8]])




```python
lpsover.constraints_sign_list
```




    []



### update

set_objective_variables은 입력된 list 값을 argument로 numpy array 값을 저장한다.<br/>
update 함수가 호출되면, 함수 내에서는 self._standard_form_matrix를 standard form 형태로 완성한다.<br />
이때 사용되는 변수들은 self._objective_variables, self._constraints_coefficient_matrix 이며, contraints 갯수에 맞춰 matrix의 사이즈를 조절하고 identify 행렬을 추가해야 한다. standrad form matrix의 첫 번째 row는 목적함수의 vector가 두 번째 row 이하는 제약식의 vector가 들어간다. <br/>
standard form이 만들어 지면, self._standard_form_matrix의 index를 기준으로  self._non_basic_variables_index와 self._basic_variables_index 변수에 각각 non basic variable과 basic variable의 초기 index 값을 저장한다.


```python
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

lpsolver = GachonLPSolver("test_example")
lpsolver.model_name

objective_coefficient_vector = np.array([30, 40])
lpsolver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lpsolver.add_constraints([2, 1], GachonLPSolver.LESSEQUAL, 8)
lpsolver.add_constraints([1, 3], GachonLPSolver.LESSEQUAL, 8)

lpsolver.update()
lpsolver.standard_form_matrix
```




    array([[  1., -30., -40.,   0.,   0.,   0.],
           [  0.,   2.,   1.,   1.,   0.,   8.],
           [  0.,   1.,   3.,   0.,   1.,   8.]])



### optimize

최적화된 standard form matrix를 산출한다. simplex algorithm에 의해 진행되는 optimize는 다음과 같다.

1. 현재 loop 종료 가능한 조건인지 확인한다. 종료 가능한 조건은 row 0의 non-basic variable 계수가 모두 0보다 클때 이다.
2. Entering variable를 선정한다. entering variable은 row0의 non-basic variable중 가장 작은 값을 의미한다.
3. Exit variable을 선정한다. <br/>
exit variable은 entering variable의 index의 있는 non-basic variable중 계수와 rhs를 나눴을 때 ratio가 0보다 크면서 가장 작은 값이다.
4. 선정된 pivot value(entering variable의 column, exit variable의 row)를 기준으로 ERO(gauss-jordan)을 실행한다.
5. Entering variable의 index를 self._basic_variables_index 에, exit variable의 index를 self._non_basic_variables_index에 추가한다. <br/>단 교환되는 두 값의 index는 교환당하는 값의 index와 1:1로 변경되어야 한다(기존 index에 영향을 주지 않는다)
6. 종료조건까지 실행한다.


```python
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

lpsolver = GachonLPSolver("test_example")
lpsolver.model_name

objective_coefficient_vector = [30, 40]
lpsolver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lpsolver.add_constraints([2, 1], GachonLPSolver.LESSEQUAL, 8)
lpsolver.add_constraints([1, 3], GachonLPSolver.LESSEQUAL, 8)

lpsolver.update()
lpsolver.optimize()

lpsolver.standard_form_matrix
```




    array([[   1. ,    0. ,    0. ,   10. ,   10. ,  160. ],
           [   0. ,    1. ,    0. ,    0.6,   -0.2,    3.2],
           [   0. ,    0. ,    1. ,   -0.2,    0.4,    1.6]])




```python
lpsolver.get_z_value()
```




    160.0




```python
lpsolver.get_objective_variables()
```




    [3.2000000000000002, 1.5999999999999999]



### Test example #1


```python
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

lpsolver = GachonLPSolver("test_example")
objective_coefficient_vector = [60, 30, 20]

lpsolver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lpsolver.add_constraints([8, 6, 1], GachonLPSolver.LESSEQUAL, 48)
lpsolver.add_constraints([4, 2, 1.5], GachonLPSolver.LESSEQUAL, 20)
lpsolver.add_constraints([2, 1.5, 0.5], GachonLPSolver.LESSEQUAL, 8)
lpsolver.add_constraints([0, 1, 0], GachonLPSolver.LESSEQUAL, 5)

lpsolver.update()
lpsolver.standard_form_matrix
# [[  1.  -60.  -30.  -20.    0.    0.    0.    0.    0. ]
#  [  0.    8.    6.    1.    1.    0.    0.    0.   48. ]
#  [  0.    4.    2.    1.5   0.    1.    0.    0.   20. ]
#  [  0.    2.    1.5   0.5   0.    0.    1.    0.    8. ]
#  [  0.    0.    1.    0.    0.    0.    0.    1.    5. ]]
```




    array([[  1. , -60. , -30. , -20. ,   0. ,   0. ,   0. ,   0. ,   0. ],
           [  0. ,   8. ,   6. ,   1. ,   1. ,   0. ,   0. ,   0. ,  48. ],
           [  0. ,   4. ,   2. ,   1.5,   0. ,   1. ,   0. ,   0. ,  20. ],
           [  0. ,   2. ,   1.5,   0.5,   0. ,   0. ,   1. ,   0. ,   8. ],
           [  0. ,   0. ,   1. ,   0. ,   0. ,   0. ,   0. ,   1. ,   5. ]])




```python
lpsolver.optimize()
print(lpsolver.standard_form_matrix)
# [[   1.      0.      5.      0.      0.     10.     10.      0.    280.  ]
#  [   0.      0.     -2.      0.      1.      2.     -8.      0.     24.  ]
#  [   0.      0.     -2.      1.      0.      2.     -4.      0.      8.  ]
#  [   0.      1.      1.25    0.      0.     -0.5     1.5     0.      2.  ]
#  [   0.      0.      1.      0.      0.      0.      0.      1.      5.  ]]
```

    [[   1.      0.      5.      0.      0.     10.     10.      0.    280.  ]
     [   0.      0.     -2.      0.      1.      2.     -8.      0.     24.  ]
     [   0.      0.     -2.      1.      0.      2.     -4.      0.      8.  ]
     [   0.      1.      1.25    0.      0.     -0.5     1.5     0.      2.  ]
     [   0.      0.      1.      0.      0.      0.      0.      1.      5.  ]]
    

    D:\workspace\gachon_OR_Class_lasbs\ps3\gachon_lp_solver.py:75: RuntimeWarning: divide by zero encountered in true_divide
      ratio_test_vector = self._standard_form_matrix[1:, -1] / (self._standard_form_matrix[1:, target_bv_index])



```python
lpsolver.get_z_value() # 280.0
```




    280.0




```python
lpsolver.get_objective_variables() # [2.0, 0, 8.0]
```




    [2.0, 0, 8.0]



### Test example #2


```python
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

model_name = "example_model"
lp_solver = GachonLPSolver(model_name)
objective_coefficient_vector = np.array([3, 2])
lp_solver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lp_solver.add_constraints([2, 1], GachonLPSolver.LESSEQUAL, 100)
lp_solver.add_constraints([1, 1], GachonLPSolver.LESSEQUAL, 80)
lp_solver.add_constraints([1, 0], GachonLPSolver.LESSEQUAL, 40)

lp_solver.update()
print(lp_solver.standard_form_matrix)

# [[   1.   -3.   -2.    0.    0.    0.    0.]
#  [   0.    2.    1.    1.    0.    0.  100.]
#  [   0.    1.    1.    0.    1.    0.   80.]
#  [   0.    1.    0.    0.    0.    1.   40.]]
```

    [[   1.   -3.   -2.    0.    0.    0.    0.]
     [   0.    2.    1.    1.    0.    0.  100.]
     [   0.    1.    1.    0.    1.    0.   80.]
     [   0.    1.    0.    0.    0.    1.   40.]]



```python
lp_solver.optimize()
print(lp_solver.standard_form_matrix)

# [[   1.    0.    0.    1.    1.    0.  180.]
#  [   0.    0.    1.   -1.    2.    0.   60.]
#  [   0.    0.    0.   -1.    1.    1.   20.]
#  [   0.    1.    0.    1.   -1.    0.   20.]]
```

    [[   1.   -3.   -2.    0.    0.    0.    0.]
     [   0.    2.    1.    1.    0.    0.  100.]
     [   0.    1.    1.    0.    1.    0.   80.]
     [   0.    1.    0.    0.    0.    1.   40.]]
    [[   1.    0.   -2.    0.    0.    3.  120.]
     [   0.    0.    1.    1.    0.   -2.   20.]
     [   0.    0.    1.    0.    1.   -1.   40.]
     [   0.    1.    0.    0.    0.    1.   40.]]
    [[   1.    0.    0.    2.    0.   -1.  160.]
     [   0.    0.    1.    1.    0.   -2.   20.]
     [   0.    0.    0.   -1.    1.    1.   20.]
     [   0.    1.    0.    0.    0.    1.   40.]]
    [[   1.    0.    0.    1.    1.    0.  180.]
     [   0.    0.    1.   -1.    2.    0.   60.]
     [   0.    0.    0.   -1.    1.    1.   20.]
     [   0.    1.    0.    1.   -1.    0.   20.]]
    [[   1.    0.    0.    1.    1.    0.  180.]
     [   0.    0.    1.   -1.    2.    0.   60.]
     [   0.    0.    0.   -1.    1.    1.   20.]
     [   0.    1.    0.    1.   -1.    0.   20.]]
    

    D:\workspace\gachon_OR_Class_lasbs\ps3\gachon_lp_solver.py:76: RuntimeWarning: divide by zero encountered in true_divide
      ratio_test_vector[ratio_test_vector <= 0] = float('Inf')



```python
print(lp_solver.get_z_value())
```

    180.0



```python
print(lp_solver.get_objective_variables())
```

    [20.0, 60.0]


### Test example #3


```python
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

model_name = "example_model"
lp_solver = GachonLPSolver(model_name)
objective_coefficient_vector = np.array([20, 15])
lp_solver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lp_solver.add_constraints([1, 0], GachonLPSolver.LESSEQUAL, 100)
lp_solver.add_constraints([0, 1], GachonLPSolver.LESSEQUAL, 100)
lp_solver.add_constraints([50, 35], GachonLPSolver.LESSEQUAL, 6000)
lp_solver.add_constraints([20, 15], GachonLPSolver.GRATERQUAL, 2000)

lp_solver.update()
lp_solver.standard_form_matrix

# array([[  1.00000000e+00,  -2.00000000e+01,  -1.50000000e+01,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00],
#        [  0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
#           1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#          -0.00000000e+00,   1.00000000e+02],
#        [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
#           0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
#          -0.00000000e+00,   1.00000000e+02],
#        [  0.00000000e+00,   5.00000000e+01,   3.50000000e+01,
#           0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
#          -0.00000000e+00,   6.00000000e+03],
#        [  0.00000000e+00,   2.00000000e+01,   1.50000000e+01,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#          -1.00000000e+00,   2.00000000e+03]])
```




    array([[  1.00000000e+00,  -2.00000000e+01,  -1.50000000e+01,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00],
           [  0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
              1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
             -0.00000000e+00,   1.00000000e+02],
           [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
              0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
             -0.00000000e+00,   1.00000000e+02],
           [  0.00000000e+00,   5.00000000e+01,   3.50000000e+01,
              0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
             -0.00000000e+00,   6.00000000e+03],
           [  0.00000000e+00,   2.00000000e+01,   1.50000000e+01,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
             -1.00000000e+00,   2.00000000e+03]])




```python
lp_solver.optimize()
print(lp_solver.standard_form_matrix)

# [[  1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     1.00000000e+00   4.00000000e-01   0.00000000e+00   2.50000000e+03]
#  [  0.00000000e+00   1.00000000e+00   0.00000000e+00   0.00000000e+00
#    -7.00000000e-01   2.00000000e-02  -0.00000000e+00   5.00000000e+01]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
#     7.00000000e-01  -2.00000000e-02   0.00000000e+00   5.00000000e+01]
#  [  0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
#     1.00000000e+00  -3.46944695e-18   0.00000000e+00   1.00000000e+02]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#    -1.00000000e+00  -4.00000000e-01  -1.00000000e+00  -5.00000000e+02]]
```

    [[  1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        1.00000000e+00   4.00000000e-01   0.00000000e+00   2.50000000e+03]
     [  0.00000000e+00   1.00000000e+00   0.00000000e+00   0.00000000e+00
       -7.00000000e-01   2.00000000e-02  -0.00000000e+00   5.00000000e+01]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
        7.00000000e-01  -2.00000000e-02   0.00000000e+00   5.00000000e+01]
     [  0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
        1.00000000e+00  -3.46944695e-18   0.00000000e+00   1.00000000e+02]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
       -1.00000000e+00  -4.00000000e-01  -1.00000000e+00  -5.00000000e+02]]
    

    D:\workspace\gachon_OR_Class_lasbs\ps3\gachon_lp_solver.py:75: RuntimeWarning: divide by zero encountered in true_divide
      ratio_test_vector = self._standard_form_matrix[1:, -1] / (self._standard_form_matrix[1:, target_bv_index])



```python
lp_solver.get_z_value()

# 2500.0
```




    2500.0




```python
lp_solver.get_objective_variables()

# [50.0, 100.0]
```




    [50.0, 100.0]



### Test example #4


```python
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

model_name = "example_model"
lp_solver = GachonLPSolver(model_name)
objective_coefficient_vector = np.array([13, 16, 16, 14, 39])
lp_solver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lp_solver.add_constraints([11, 53, 5, 5, 29], GachonLPSolver.LESSEQUAL, 40)
lp_solver.add_constraints([3, 6, 5, 1, 34], GachonLPSolver.LESSEQUAL, 20)
lp_solver.add_constraints([1, 0, 0, 0, 0], GachonLPSolver.LESSEQUAL, 1)
lp_solver.add_constraints([0, 1, 0, 0, 0], GachonLPSolver.LESSEQUAL, 1)
lp_solver.add_constraints([0, 0, 1, 0, 0], GachonLPSolver.LESSEQUAL, 1)
lp_solver.add_constraints([0, 0, 0, 1, 0], GachonLPSolver.LESSEQUAL, 1)
lp_solver.add_constraints([0, 0, 0, 0, 1], GachonLPSolver.LESSEQUAL, 1)

lp_solver.update()
lp_solver.standard_form_matrix

# array([[  1., -13., -16., -16., -14., -39.,   0.,   0.,   0.,   0.,   0.,
#           0.,   0.,   0.],
#        [  0.,  11.,  53.,   5.,   5.,  29.,   1.,   0.,   0.,   0.,   0.,
#           0.,   0.,  40.],
#        [  0.,   3.,   6.,   5.,   1.,  34.,   0.,   1.,   0.,   0.,   0.,
#           0.,   0.,  20.],
#        [  0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,
#           0.,   0.,   1.],
#        [  0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,
#           0.,   0.,   1.],
#        [  0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,
#           0.,   0.,   1.],
#        [  0.,   0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,
#           1.,   0.,   1.],
#        [  0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,
#           0.,   1.,   1.]])
```




    array([[  1., -13., -16., -16., -14., -39.,   0.,   0.,   0.,   0.,   0.,
              0.,   0.,   0.],
           [  0.,  11.,  53.,   5.,   5.,  29.,   1.,   0.,   0.,   0.,   0.,
              0.,   0.,  40.],
           [  0.,   3.,   6.,   5.,   1.,  34.,   0.,   1.,   0.,   0.,   0.,
              0.,   0.,  20.],
           [  0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,
              0.,   0.,   1.],
           [  0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,   0.,
              0.,   0.,   1.],
           [  0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,   1.,
              0.,   0.,   1.],
           [  0.,   0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,   0.,
              1.,   0.,   1.],
           [  0.,   0.,   0.,   0.,   0.,   1.,   0.,   0.,   0.,   0.,   0.,
              0.,   1.,   1.]])




```python
lp_solver.optimize()
print(lp_solver.standard_form_matrix)

# [[  1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   1.90417690e-01   9.84643735e-01
#     7.95147420e+00   0.00000000e+00   1.01246929e+01   1.20632678e+01
#     0.00000000e+00   5.74490172e+01]
#  [  0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   2.08845209e-02  -1.78132678e-02
#    -1.76289926e-01   0.00000000e+00  -1.53562654e-02  -8.66093366e-02
#     0.00000000e+00   2.00859951e-01]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   1.00000000e+00  -3.68550369e-03   3.25552826e-02
#    -5.71253071e-02   0.00000000e+00  -1.44348894e-01  -1.41277641e-02
#     0.00000000e+00   2.88083538e-01]
#  [  0.00000000e+00   1.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   1.00000000e+00]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00  -2.08845209e-02   1.78132678e-02
#     1.76289926e-01   1.00000000e+00   1.53562654e-02   8.66093366e-02
#     0.00000000e+00   7.99140049e-01]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
#     0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
#     0.00000000e+00   1.00000000e+00]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
#     0.00000000e+00   1.00000000e+00]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   3.68550369e-03  -3.25552826e-02
#     5.71253071e-02   0.00000000e+00   1.44348894e-01   1.41277641e-02
#     1.00000000e+00   7.11916462e-01]]
```

    [[  1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   1.90417690e-01   9.84643735e-01
        7.95147420e+00   0.00000000e+00   1.01246929e+01   1.20632678e+01
        0.00000000e+00   5.74490172e+01]
     [  0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   2.08845209e-02  -1.78132678e-02
       -1.76289926e-01   0.00000000e+00  -1.53562654e-02  -8.66093366e-02
        0.00000000e+00   2.00859951e-01]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   1.00000000e+00  -3.68550369e-03   3.25552826e-02
       -5.71253071e-02   0.00000000e+00  -1.44348894e-01  -1.41277641e-02
        0.00000000e+00   2.88083538e-01]
     [  0.00000000e+00   1.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   1.00000000e+00]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00  -2.08845209e-02   1.78132678e-02
        1.76289926e-01   1.00000000e+00   1.53562654e-02   8.66093366e-02
        0.00000000e+00   7.99140049e-01]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
        0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
        0.00000000e+00   1.00000000e+00]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
        0.00000000e+00   1.00000000e+00]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   3.68550369e-03  -3.25552826e-02
        5.71253071e-02   0.00000000e+00   1.44348894e-01   1.41277641e-02
        1.00000000e+00   7.11916462e-01]]
    

    D:\workspace\gachon_OR_Class_lasbs\ps3\gachon_lp_solver.py:75: RuntimeWarning: divide by zero encountered in true_divide
      ratio_test_vector = self._standard_form_matrix[1:, -1] / (self._standard_form_matrix[1:, target_bv_index])



```python
lp_solver.get_z_value()

# 57.449017199017206
```




    57.449017199017206




```python
lp_solver.get_objective_variables()

# [1.0, 0.20085995085995084, 1.0, 1.0, 0.28808353808353804]
```




    [1.0, 0.20085995085995084, 1.0, 1.0, 0.28808353808353804]



### Test example #5


```python
import importlib
import gachon_lp_solver
from gachon_lp_solver import GachonLPSolver
importlib.reload(gachon_lp_solver) # gachon_lp_solver.py이 수정되면 다시 호출하는 모듈

model_name = "example_model"
lp_solver = GachonLPSolver(model_name)
objective_coefficient_vector = np.array([5000, 8500, 2400, 2800])
lp_solver.set_objective_variables(objective_coefficient_vector, GachonLPSolver.MAXIMIZE)
lp_solver.add_constraints([1, 0, 0, 0], GachonLPSolver.LESSEQUAL, 12)
lp_solver.add_constraints([0, 1, 0, 0], GachonLPSolver.LESSEQUAL, 5)
lp_solver.add_constraints([0, 0, 1, 0], GachonLPSolver.LESSEQUAL, 25)
lp_solver.add_constraints([0, 0, 0, 1], GachonLPSolver.LESSEQUAL, 20)
lp_solver.add_constraints([800, 925, 290, 380], GachonLPSolver.LESSEQUAL, 8000)
lp_solver.add_constraints([0, 0, 1, 1], GachonLPSolver.GRATERQUAL, 5)
lp_solver.add_constraints([0, 0, 290, 380], GachonLPSolver.LESSEQUAL, 1800)

lp_solver.update()
lp_solver.standard_form_matrix

# array([[  1.00000000e+00,  -5.00000000e+03,  -8.50000000e+03,
#          -2.40000000e+03,  -2.80000000e+03,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00],
#        [  0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
#           1.20000000e+01],
#        [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
#           5.00000000e+00],
#        [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
#           2.50000000e+01],
#        [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
#           0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
#           2.00000000e+01],
#        [  0.00000000e+00,   8.00000000e+02,   9.25000000e+02,
#           2.90000000e+02,   3.80000000e+02,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           1.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
#           8.00000000e+03],
#        [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           1.00000000e+00,   1.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,  -1.00000000e+00,   0.00000000e+00,
#           5.00000000e+00],
#        [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           2.90000000e+02,   3.80000000e+02,   0.00000000e+00,
#           0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
#           0.00000000e+00,  -0.00000000e+00,   1.00000000e+00,
#           1.80000000e+03]])
```




    array([[  1.00000000e+00,  -5.00000000e+03,  -8.50000000e+03,
             -2.40000000e+03,  -2.80000000e+03,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00],
           [  0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
              1.20000000e+01],
           [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
              5.00000000e+00],
           [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              1.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
              0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
              2.50000000e+01],
           [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,   1.00000000e+00,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   1.00000000e+00,
              0.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
              2.00000000e+01],
           [  0.00000000e+00,   8.00000000e+02,   9.25000000e+02,
              2.90000000e+02,   3.80000000e+02,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              1.00000000e+00,  -0.00000000e+00,   0.00000000e+00,
              8.00000000e+03],
           [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              1.00000000e+00,   1.00000000e+00,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,  -1.00000000e+00,   0.00000000e+00,
              5.00000000e+00],
           [  0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              2.90000000e+02,   3.80000000e+02,   0.00000000e+00,
              0.00000000e+00,   0.00000000e+00,   0.00000000e+00,
              0.00000000e+00,  -0.00000000e+00,   1.00000000e+00,
              1.80000000e+03]])




```python
lp_solver.optimize()
print(lp_solver.standard_form_matrix)

# [[  1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     3.44827586e+02   0.00000000e+00   2.71875000e+03   0.00000000e+00
#     0.00000000e+00   6.25000000e+00   0.00000000e+00   2.02586207e+00
#     6.72403017e+04]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     1.38777878e-17   1.00000000e+00   1.15625000e+00   0.00000000e+00
#     0.00000000e+00  -1.25000000e-03   0.00000000e+00   1.25000000e-03
#     1.00312500e+01]
#  [  0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     5.00000000e+00]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#    -1.31034483e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
#     0.00000000e+00   0.00000000e+00   0.00000000e+00  -3.44827586e-03
#     1.87931034e+01]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     2.00000000e+01]
#  [  0.00000000e+00   1.00000000e+00   0.00000000e+00   0.00000000e+00
#    -1.38777878e-17   0.00000000e+00  -1.15625000e+00   0.00000000e+00
#     0.00000000e+00   1.25000000e-03   0.00000000e+00  -1.25000000e-03
#     1.96875000e+00]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
#     1.31034483e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   0.00000000e+00   3.44827586e-03
#     6.20689655e+00]
#  [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     3.10344828e-01   0.00000000e+00   0.00000000e+00   0.00000000e+00
#     0.00000000e+00   0.00000000e+00   1.00000000e+00   3.44827586e-03
#     1.20689655e+00]]
```

    [[  1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        3.44827586e+02   0.00000000e+00   2.71875000e+03   0.00000000e+00
        0.00000000e+00   6.25000000e+00   0.00000000e+00   2.02586207e+00
        6.72403017e+04]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        1.38777878e-17   1.00000000e+00   1.15625000e+00   0.00000000e+00
        0.00000000e+00  -1.25000000e-03   0.00000000e+00   1.25000000e-03
        1.00312500e+01]
     [  0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   1.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        5.00000000e+00]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
       -1.31034483e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
        0.00000000e+00   0.00000000e+00   0.00000000e+00  -3.44827586e-03
        1.87931034e+01]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        1.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        2.00000000e+01]
     [  0.00000000e+00   1.00000000e+00   0.00000000e+00   0.00000000e+00
       -1.38777878e-17   0.00000000e+00  -1.15625000e+00   0.00000000e+00
        0.00000000e+00   1.25000000e-03   0.00000000e+00  -1.25000000e-03
        1.96875000e+00]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   1.00000000e+00
        1.31034483e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   0.00000000e+00   3.44827586e-03
        6.20689655e+00]
     [  0.00000000e+00   0.00000000e+00   0.00000000e+00   0.00000000e+00
        3.10344828e-01   0.00000000e+00   0.00000000e+00   0.00000000e+00
        0.00000000e+00   0.00000000e+00   1.00000000e+00   3.44827586e-03
        1.20689655e+00]]
    

    D:\workspace\gachon_OR_Class_lasbs\ps3\gachon_lp_solver.py:75: RuntimeWarning: divide by zero encountered in true_divide
      ratio_test_vector = self._standard_form_matrix[1:, -1] / (self._standard_form_matrix[1:, target_bv_index])



```python
lp_solver.get_z_value()

# 67240.301724137928
```




    67240.301724137928




```python
lp_solver.get_objective_variables()

# [1.96875, 5.0, 6.2068965517241379, 0]
```




    [1.96875, 5.0, 6.2068965517241379, 0]



## 결과 제출 하기

문제없이 숙제를 제출하면 아래 결과가 모두 PASS로 표시 될 것입니다


```python
import gachon_autograder_client as g_autograder

THE_TEMLABIO_ID = "#YOUR_ID"
PASSWORD = "#YOUR_PASSWORD"
ASSIGNMENT_FILE_NAME = "gachon_lp_solver.py" 

g_autograder.submit_assignment(THE_TEMLABIO_ID , PASSWORD, ASSIGNMENT_FILE_NAME)
```

    -------------------- | ---------- | -------------------- 
           Function Name |    Passed? |             Feedback 
    -------------------- | ---------- | -------------------- 
              model_name |       PASS |             Good Job 
                  update |    Not Yet |   Check Your Grammar 
    set_objective_variables |    Not Yet |   Check Your Grammar 
           optimize_easy |    Not Yet |     Check Your Logic 
           optimize_hard |    Not Yet |   Check Your Grammar 
         add_constraints |    Not Yet |   Check Your Grammar 
    -------------------- | ---------- | -------------------- 


## Next Work

처음으로 알고리즘을 Class로 만들어 코딩으로 구현하는 일을 실행해 보았습니다. 실제로 우리가 사용하는 다양한 패키지들은 이런식으로 누군가 한땀 한땀 정의해서 사용하고 있습니다. 이제 여러분들도 여러분들만의 패키지를 만들 실력이 되었습니다. 기분 좋지 않은세요? 자기 자신이 한단계 성장했다고 느낄거라고 믿습니다.

> Human knowledge belongs to the world - from movie 'Password' -
