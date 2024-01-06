## NODOS_Div_X2Trigger
NODOS_Div_X2Trigger table file

This a compound rule to control NODOS Diversions to avoid unnecessary WQ impacts in the Delta

For each month,

if the year type that month is greater than or equal to the YrType value,

then the max NODOS diversion rate for excess fills is set to the YrDivLimit

in addition, if the year type is triggered and if the previous month ending X2 is greater than the X2Limit value,

then the max NODOS diversion rate for excess fills is additionally limited to X2DivLimit



### First 10 Rows of the Table
|   Month |   YrType |   YrDivLimit |   X2Limit |   X2DivLimit |
|--------:|---------:|-------------:|----------:|-------------:|
|       1 |        9 |         9999 |        99 |         9999 |
|       2 |        4 |         6000 |        85 |         4000 |
|       3 |        4 |         6000 |        84 |         4000 |
|       4 |        4 |         6000 |        82 |         4000 |
|       5 |        4 |         4000 |        80 |         4000 |
|       6 |        4 |         4000 |        78 |         4000 |
|       7 |        4 |         3000 |        76 |         2000 |
|       8 |        4 |         3000 |        76 |         2000 |
|       9 |        9 |         9999 |        99 |         9999 |
|      10 |        9 |         9999 |        99 |         9999 |