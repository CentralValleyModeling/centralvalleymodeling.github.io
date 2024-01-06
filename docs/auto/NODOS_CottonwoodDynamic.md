## NODOS_CottonwoodDynamic
This lookup table is used for implementing Cottonwood Establishment Flows

The trigger value is the maximum of the Red Bluff flow in March or the Average Red Bluff Flow for March and April

If the trigger flow exceeds 20,000 cfs then 2 months of flow augmentation are targeted for Apr and May

If the trigger flow exceeds 14,000 cfs then 1 month of flow augmentation is targeted for Apr

Calculations are then made to determine the volume of water associated with April and May flow augmentations

This is the table of values upon which those calculations rest (see NODOS_ERP1 code for more information)

### First 10 Rows of the Table
|   Trigger |   Week2 |   Week4 |   Week6 |   Week8 |   Week10 |
|----------:|--------:|--------:|--------:|--------:|---------:|
|         0 |    6500 |    6500 |    6500 |    6500 |     6500 |
|      7500 |    6500 |    6500 |    6500 |    6500 |     6500 |
|      8100 |    6500 |    6500 |    6500 |    6500 |     6500 |
|      8800 |    6500 |    6500 |    6500 |    6500 |     6500 |
|      9500 |    6500 |    6500 |    6500 |    6500 |     6500 |
|     10300 |    6500 |    6500 |    6500 |    6500 |     6500 |
|     11100 |    7000 |    6500 |    6500 |    6500 |     6500 |
|     12000 |    7500 |    6500 |    6500 |    6500 |     6500 |
|     12900 |    8100 |    6500 |    6500 |    6500 |     6500 |
|     13900 |    8800 |    6500 |    6500 |    6500 |     6500 |