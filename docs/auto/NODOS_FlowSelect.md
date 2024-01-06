## NODOS_FlowSelect
This file contains a variety of flow actions selected to accompany NODOS



AprCotton and MayCotton - Modify spring flows into a snowmelt pattern in years with peak storm events in late-winter and early-spring - Red Bluff to Colusa

The snowmelt pattern would be designed to increase the success of cottonwood cohorts specifically

(fixed flows shown here are taken from table 6 of Environmental Flow Recommendations plus baseline flow values)

(also see dynamic Cottonwood option)



MarKesSup               - Supplement flows from Shasta and Keswick Dams in March during years when no flow event has occurred (provided only when

sufficient inflow to Lake Shasta is available; add 8,000  10,000 cfs in dry years and add 15,000  20,000 cfs in below normal years)

(see code for triggering criteria)



MarDelta                - Provide a March Delta outflow that occurs from the natural late-winter and early-spring peak inflow from the Sacramento River

(10 days at 20,000 CFS in dry, 30,000 cfs in below-normal, and 40,000 cfs in above-normal water years)

(code applies target flow = selected flow x 10/days in month + base flow x (days in month - 10)/days in month)



MayFreeport             - Provide a minimum flow of 13,000 cfs on the Sacramento River below Sacramento in May of all but critical years



### First 10 Rows of the Table
|   Year |   AprCotton |   MayCotton |   MarKesSup |   MarDelta |   MayFreeport |
|-------:|------------:|------------:|------------:|-----------:|--------------:|
|   1922 |           0 |           0 |           0 |      40000 |         13000 |
|   1923 |           0 |           0 |       20000 |      30000 |         13000 |
|   1924 |           0 |           0 |           0 |          0 |             0 |
|   1925 |           0 |           0 |       10000 |      20000 |         13000 |
|   1926 |           0 |           0 |       10000 |      20000 |         13000 |
|   1927 |           0 |           0 |           0 |          0 |         13000 |
|   1928 |           0 |           0 |           0 |      40000 |         13000 |
|   1929 |           0 |           0 |           0 |          0 |             0 |
|   1930 |           0 |           0 |       10000 |      20000 |         13000 |
|   1931 |           0 |           0 |           0 |          0 |             0 |