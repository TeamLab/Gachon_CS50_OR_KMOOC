## Autograder 설치와 Lab Assignment 다운로드 하기
Lab Assignment 제출을 위해서는 아래와 같은 프로세스를 통해 환경설정을 해주어야 합니다

### Git 설치하기
- 코드 관리 도구인 Git을 설치하여 Autograder 모듈을 다운로드 하여야 합니다.
- Git에 대한 내용은 본 강의 범위를 벗어 나므로 아래 영상을 참고하시기 바랍니다.
    - Git 설치하기(5분 47초) - https://www.youtube.com/watch?v=JBN_hjgR1KQ&list=PLBHVuYlKEkULuUe_Ca3wiaFon6dPWIWAZ&t=11s&index=1
    - 다운로드 사이트 - https://github.com/

### 가상환경 실행
- 코딩 환경 구성을 위해 이미 만들어 둔 가상환경을 호출합니다.
- 윈도우에서는 `CMD창`, Mac OS에서는 `Terminal`에서 실행합니다.
```commandline
activate or_kmooc
```
### Autograder 설치
- 숙제 제출 모듈인 Autograder를 설치합니다.
- 윈도우에서는 `CMD창`, Mac OS에서는 `Terminal`에서 실행합니다.
```commandline
pip install git+https://github.com/TeamLab/or_mooc_autograder
```

### Template 다운로드
- python 파일 또는 jupyter notebook 파일을 생성하여 아래 코드를 실행 시킵니다.

```python
import gachon_autograder_client as g_autograder

THE_TEMLABIO_ID = "#YOUR_ID"
PASSWORD = "#YOUR_PASSWORD"
ASSIGNMENT_NAME = "nb_test"

g_autograder.get_assignment(THE_TEMLABIO_ID , PASSWORD, ASSIGNMENT_NAME)
```

### 코드 수정
- 지시에 따라 코드를 수정합니다.

### K-MOOC 제출
- K-MOOC 사이트내 코드 제출 기능을 활용하여 숙제를 제출합니다.
