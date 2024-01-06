## CVP_SOD_Contracts
The code in the contractor column enables all contract info to be in the same table

The contractor code can be parsed as AABC.d where:

AA = WBA #

B = 1 for Ag, 2 for RF, 3 for MI, and 4 for EX

C = the count of the particular contract type in the WBA

d = used if one contractor has more than one contract

Example: 7214 would be 72_PA4

values are in TAF

### First 10 Rows of the Table
|   contractor |   contract |
|-------------:|-----------:|
|       5011   |     25     |
|       5031   |     10     |
|       5031.1 |     10     |
|       5031.2 |     10     |
|       6331   |     13.5   |
|       6332   |      8.863 |
|       6431   |     14     |
|       6441   |     59     |
|       7111   |     34.105 |
|       7112   |     50     |