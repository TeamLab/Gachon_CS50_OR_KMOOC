# Product Mix Problem
아래 문제를 풀고, 이익(profit)의 최대값을 구하기 위한 Gurobi Code를 작성하시오.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 다운받아야 합니다. Chrome 또는 익스플로러와 같은 웹 브라우저 주소창에 아래 주소를 입력합니다.

https://github.com/TeamLab/Gachon_CS50_OR_KMOOC/blob/master/gurobi_quiz/media_selection/media_selection.zip

다운로드를 위해 View Raw 또는 Download 버튼을 클릭합니다. 또는 [meida selection problem - 다운로드 링크](https://github.com/TeamLab/Gachon_CS50_OR_KMOOC/raw/master/gurobi_quiz/media_selection/media_selection.zip) 를 클릭하면 자동으로 다운로드가 됩니다. 다운로드 된 파일을 작업 폴더로 이동한 후 압축해제 후 작업하길 바랍니다.

## Problem Description
A company has budgeted up to $8000 per week for local advertisement. The money is to be allocated among four promotional media: TV spots, newspaper ads, and two types of radio advertisements. The company goal is to reach the largest possible high-potential audience through the various media. The following table presents the number of potential customers reached by making use of advertisement in each of the four media. It also provides the cost per advertisement placed and the maximum number of ads than can be purchased per week.
The company arrangements require that at least five radio spots be placed each week. To ensure a board-scoped promotional campaign, management also insists that no more than $1800 be spent on radio advertising every week.


## Information Table
| Medium                             | Audience Reached per ad | Cost per ad | Maximum ads per week |
|:-----------------------------------|:------------------------|:------------|:---------------------|
| TV spot (1 minute)                 | 5000                    | 800         | 12                   |
| Daily newspaper  (full-page ad)    | 8500                    | 925         | 5                    |
| Radio spot (30 second, prime time) | 2400                    | 290         | 25                   |
| Radio spot  (1 minute, afternoon)  | 2800                    | 380         | 20                   |

