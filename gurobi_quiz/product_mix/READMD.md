# Product Mix Problem
아래 문제를 풀고, 이익(profit)의 최대값을 구하시요.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 다운받아야 합니다. Chrome 또는 익스플로러와 같은 웹 브라우저 주소창에 아래 주소를 입력합니다.

https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_8/product_mix_problem.zip

다운로드를 위해 View Raw 또는 Download 버튼을 클릭합니다. 또는 [Lab 8 - 다운로드 링크](https://github.com/TeamLab/Gachon_CS50_Python_KMOOC/blob/master/lab_assignment/lab_8/lab_8.zip) 를 클릭하면 자동으로 다운로드가 됩니다. 다운로드 된 lab_8.zip 파일을 작업 폴더로 이동한 후 압축해제 후 작업하길 바랍니다.


## Problem Description
Formulate a linear programming model for this problem, to determine how many containers of each product to produce tomorrow in order to maximize the profits. The company makes four types of juice using orange, grapefruit, and pineapple. The following table shows the price and cost per quart of juice (one container of juice) as well as the number of kilograms of fruits required to produce one quart of juice.
On hand there are 400 Kg of orange, 300 Kg. of grapefruit, and 200 Kg. of pineapples.The manager wants grapefruit juice to be used for no more than 30 percent of the number of containers produced. He wants the ratio of the number of containers of orange juice to the number of containers of pineapples juice to be at least 7 to 5. pineapples juice should not exceed one-third of the total product.

## Information Table
| Product          | Price/quart | Cost/quart | Fruit needed  |
|:-----------------|:------------|:-----------|:--------------|
| Orange juice     | 3           | 1          | 1 Kg.         |
| Grapefruit juice | 2           | 0.5        | 2 Kg.         |
| Pineapple juice  | 2.5         | 1.5        | 1.25 Kg.      |
| All –in - one    | 4           | 2          | 0.25 Kg. each |

