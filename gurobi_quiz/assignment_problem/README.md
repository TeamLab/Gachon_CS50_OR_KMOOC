# Assignment Problem
  ===================

아래 문제를 풀고, 이익(profit)의 최대값을 구하기 위한 Gurobi Code를 작성하시오.

[https://github.com/TeamLab/Gachon_CS50_OR_KMOOC/blob/master/gurobi_quiz/assignment_problem/assignment_problem.zip](https://github.com/TeamLab/Gachon_CS50_OR_KMOOC/blob/master/gurobi_quiz/assignment_problem/assignment_problem.zip)

다운로드를 위해 View Raw 또는 Download 버튼을 클릭합니다. 또는 [assignment_problem - 다운로드 링크](https://github.com/TeamLab/Gachon_CS50_OR_KMOOC/raw/master/gurobi_quiz/product_mix/product_mix_problem.zip) 를 클릭하면 자동으로 다운로드가 됩니다. 다운로드 된 assignment_problem.zip 파일을 작업 폴더로 이동한 후 압축해제 후 작업하길 바랍니다.

## PROBLEM DESCRIPTION
<img src=https://s3.ap-northeast-2.amazonaws.com/teamlab-gachon/assignment_problem.png>

단 과제의 원활한 진행을 위해,

1) modelling 함수에는 제시된 cost matrix를 사용하요 gurobi로 모델링한 모델을 return 함, 이때 모델의 minized cost는 원래 값의 두 배일 수 밖에없음(cost_matrix가 양방향임으로)
2) minimized_cost() 함수는 산출된 minimized_cost 값의 절반한 값을 리턴해줌