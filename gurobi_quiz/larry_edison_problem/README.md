# Larry Edision Computer Center

## Problem Description
Larry Edison is the director of the Computer Center for Buckly College. He now needs to schedule the staffing of the center. It is open from 8 A.M. until midnight. Larry has monitored the usage of the center at various times of the day, and determined that the following number of computer consultants are required:

| Time of Day | Minimum Number of Consultants Required to Be on Duty |
|:------------|:-----------------------------------------------------|
| 8 A.M.–noon	 |                4                                       |
| Noon–4 P.M.	 |                 8                                     |
| 4 P.M.–8 P.M.	|                   10                                   |
| 8 P.M.–midnight	|                 6                                     |

Two types of computer consultants can be hired: full-time and part-time. The full-time consultants work for 8 consecutive hours in any of the following shifts: morning (8 A.M.–4 P.M.), afternoon (noon–8 P.M.), and evening (4 P.M.–midnight). Full-time consultants are paid 14 dollor per hour.

Part-time consultants can be hired to work any of the four shifts listed in the above table. Part-time consultants are paid 12 dollor per hour.

An additional requirement is that during every time period, there must be at least 2 full-time consultants on duty for every parttime consultant on duty.

Larry would like to determine how many full-time and how many part-time workers should work each shift to meet the above requirements at the minimum possible cost.

(a) Formulate a linear programming model for this problem.
(b) Solve this model by the gurobi.