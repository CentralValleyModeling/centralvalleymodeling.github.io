# Freqently Asked Questions

### Why are the historical results different from CalSim 3 results for the year 2018?
The Oroville spillway was being repaired in 2018 - DWR maintained Lake Oroville at a lower-than-normal level to reduce the possibility that the spillway would have to be used the following winter. 

CalSim does not model real-time emergency measures, such as Temporary Urgency Change Petitions (TUCP) from the SWRCB. Additionally, CalSim is not a transient model; The regulatory environment isn’t changing with time. We are using 2020 BiOps throughout the simulation period. These factors can lead to differences between historical operations.

*Keywords: corroboration; historical operations*

### How does CalSim handle timesteps other than monthly (i.e. seasonal regulations, regulations averaged weekly, daily values, etc.)?
Behind scenes, CalSim has routines for disaggregation for daily calculations for things like delta salinity and weir spills. Seasonal regulatory requirements are averaged over the month.

*Keywords: Input, timestep, daily, monthly*

### How frequently are the physical parameters (such as downstream channel capacity) updated based upon field observations? And that data's stored in the "Table" data on the workflow?
As soon as we get the information from agencies and contractors. Last time we updated in DCR 2021. We also recently updated Oroville storage based on recent bathymetry.

*Keywords: physical parameters, data, input updates*

### How does CalSim estimate Delta water quality using an Artificial Neural Network (ANN)?
	
CalSim uses an ANN to emulate a one-dimensional Delta hydrodynamic and water quality model called DSM2. This allows CalSim to approximate Delta water quality quickly, without the need to run the full DSM2 model during its runtime. 

The ANN takes inputs from CalSim like flows, delta cross channel gate operation, exports, etc. and determines what the Delta salinity would be. This helps ensure operations and flows are meeting salinity standards in the Delta and can adjust these flows in CalSim if needed. It provides an inflow-export-salinity relationship that allows compliance with salinity standards.

*Keywords: Delta Water Quality; Artificial Neural Network (ANN); Salinity Standards*

### Where does ANN come in for sequence of cycles?
The ANN is called throughout Sac/Delta cycles and starts at GW_Initial.

*Keywords: Delta Water Quality; Artificial Neural Network (ANN); Salinity Standards*

###  Is hydrology the only type of input can be changed in CalSim?

While hydrology is one of the major inputs we can change, planning studies will often vary other inputs such as demands, regulatory assumptions (minimum required outflows), operational assumptions (reservoir rule curves, etc.), and even infrastructure assumptions (channel capacity, pumping plant outages).

*Keywords: Hydrology, Inputs/Outputs, Operations, Infrastructure*

### What happens if you have flooding events where physical limits are exceeded?

There are flood zones for channels and reservoirs and limitations for CS3 on real-time operations.  Flood zones have large negative weights which make flood events less likely to occur. In addition, CS3 uses channel flow limits, bypass channels and weir operations to deal with flood conditions.

*Keywords: Linear Programming, Solver; physical capacity*

### What are weights and hare are their values determined in CalSim?
Weights are coefficients in the objective function and influence how the solver prioritizes allocations, ensuring that higher-priority diversions are favored while still complying with constraints like environmental flows, contractual deliveries, and reservoir operations. For example, meeting regulatory requirements like D1641 have some of the highest weights of around 5000.

Weights and penalties are relative to each other, determined with consulation from expert opinions, engineering judgement and trial-and-error.

*Keywords: Linear Programming, Solver; operations, objective function*

### In the WRESL Syntax, what do brackets indicate?
Consider the variable `foo`. The any instance of `foo[BAR]` pulls the value of `foo` from a prior cycle with the name `BAR`. This allows CalSim to retrieve, from memory, the value of a variable from a previous cycle to use in the current cycle as a state variable. A state variable is a variable that represents the system's condition at a specific point in time. It captures essential system properties that determine its future evolution.

*Keywords: WRESL, syntax, cycles*

### Is a statement with a “<” or a “>” without any penalties listed considered a hard constraint?
Consider the following goal statement: `Goal constrain_foo {foo < bar}`. The goal `constrain_foo` is a "hard" constraint. 
Note: in the WRESL syntax, `<` is `<=` and `>` is `>=` 

*Keywords: WRESL, syntax, goals, constraints*

### Could it be possible that, during a given cycle, the solver might struggle to find the optimal solution or identify multiple equally optimal ones?
It is possible for the model to experience instability (e.g., if many localized diversion arcs share a same weight) and arrive at non-unique solutions. The CalSim development teams work diligently to ensure model stability and the avoidance of non-unique solutions. However, careful inspection of the outcomes the model—like all modeling tools—remains essential.

*Keywords: cycles, debugging, QA/QC*

### Is the sequence for the upper watersheds need to be run in that order? They seem to be independent of each other.
The upper watershed modules are separate solutions and are largely independent, but not completely. For example there are inter-basins transfers from the Yuba to the Upper American, so a result from Yuba could affect the Upper American.

*Keywords: cycles, upper watersheds, American, Yuba, transfers*

### Why do the upper watershed cycles need to be part of the CalSim 3 run? Can't they be run separately and generate timeseries input to CalSim 3?
They can be run separately. In some previous versions of the model, the upper watersheds were run and the timeseries were stored for the valley floor run. However, whenever operations in the upper watersheds changed/revised/bug-fixed, we would have to re-pre-process and compile SV file. It can be simpler just to run all the upper watersheds together,

*Keywords: cycles, upper watersheds, inputs, timeseries*

### Since the outputs from the earlier cycles are used as inputs for later cycles, do earlier cycles generally have higher priority over later cycles?

They follow a sequence where earlier cycles have a precedence over later ones and are executed before them.

*Keywords: cycles, priorities*

### Why don't we specify weights for C_** terms (channel flows) even though they are also DVs?
They are mainly used to convey water, and weights are set to diversions.  However, minimum flow arcs, which are specialized Channel arcs are weighted since they are required to carry a certain amount of flow to meet regulations.

*Keywords: weights, WRESL syntax*

### Is there a particular file names that give you topology of schematic?
The protocol for file structure, system folders provides the convention. Anything with “arcs” defines the grid. “Constraints-connectivity” defines the mass balances. Motivation of model comes from the weight table. Each upper watershed module has separate system.

*Keywords: folder structure, WRESL syntax*

### Where can I find more information for the naming convention for hydrologic inputs?
the latest CalSim 3 Hydrology Report on DWR's website has detailed documentation on the different "arcs" and how they are named in the [CalSim Hydrology Report](https://data.cnra.ca.gov/dataset/a3bb1ddd-624b-4c3d-95e7-2aa6b3bf2b5b/resource/6ba59600-d562-44da-a267-a6a50dff3f0d/download/final_cs3_hydrologyreport_v2.pdf)

*Keywords: naming convention, hydrology*

### The San Joaquin Cycles come before the Sacramento Valley Cycles, so does this mean that Delta Outflow doesn't impact SJR reservoir operations requirement?
There is no delta outflow requirement that drives releases from the San Joaquin

*Keywords: cycles, delta outflow hydrology*