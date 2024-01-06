## UF_Rpf_RufO_RufW
RPF - riparian and miscella. ET fraction

RUFO - reuse fraction for all other crops

RUFW - reuse fraction for wetlands. -1 indicates nodata, -2 indicates a time series is used



RUFR{id} - timeseries ID of reuse fraction for rice



AW   = AWo +AWr +AWw

RUaw = AWo * RUFo +  AWr * RUFr + AWw*RUFw

RU   = Min(TW, RUaw)

GP   > GPmin * (1+ RPF)* AW -GPmin* RUaw

Div  = [AW*(1+ RPF) -RU -GP]/[1-(EVF+DPF+LFF+OSF)]

### First 10 Rows of the Table
|   DU |   RPF |   RUFO |   RUFRid |   RUFW |
|-----:|------:|-------:|---------:|-------:|
|    1 |  0.05 |  0.05  |        5 |  -1    |
|    2 |  0    |  0.025 |        5 |  -1    |
|    3 |  0    |  0.1   |        5 |  -1    |
|    4 |  0    |  0.05  |        5 |  -1    |
|    5 |  0.05 |  0.1   |        5 |  -1    |
|    6 |  0    |  0.025 |        5 |  -1    |
|    7 |  0    |  0.1   |        5 |  -1    |
|    8 |  0    |  0.05  |        5 |  -1    |
|    9 |  0    |  0.05  |        5 |  -1    |
|   10 |  0    |  0     |        5 |   0.15 |