## flowlossfactors
LFF - lateral flow loss fraction lateral flow

DPF - deep percolation loss fraction

OSF - canal operating spill fraction

EVF - evaporative loss fraction

Diversions = AW*(1+ RPF) + Div*(EVF+DPF+LFF+OSF) -GP -RU

AW = ET+SR - PR +DP+TW

RU = min(TW, RUFR*AWR + RUFO*AWO + RUFW*AWW)

GPminCFS = GPmin * (1+ RPF)* (AWo + AWr + Aww) -GPmin* (AWo * RUFo +  AWr * RUFr + AWW*RUFw)

For the canals with "*", flow loss factors have been calibrated by Idy Lui 03/2018

### First 10 Rows of the Table
|   ID |   lff |   dpf |   osf |   evf |
|-----:|------:|------:|------:|------:|
|    1 |  0.11 | 0.14  |  0.04 |  0.01 |
|    2 |  0.11 | 0.14  |  0.04 |  0.01 |
|    3 |  0.11 | 0.14  |  0.04 |  0.01 |
|    4 |  0.2  | 0.21  |  0.2  |  0.01 |
|    5 |  0.11 | 0.14  |  0.04 |  0.01 |
|    6 |  0.11 | 0.14  |  0.04 |  0.01 |
|    7 |  0.11 | 0.14  |  0.04 |  0.01 |
|    8 |  0.11 | 0.14  |  0.04 |  0.01 |
|    9 |  0    | 0.025 |  0    |  0    |
|   10 |  0.22 | 0.26  |  0.2  |  0.01 |