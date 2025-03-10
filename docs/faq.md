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

There are flood zones for channels and reservoirs and limitations for CalSim 3 on real-time operations.  Flood zones have large negative weights which make flood events less likely to occur. In addition, CS3 uses channel flow limits, bypass channels and weir operations to deal with flood conditions.

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

### How are rim inflows derived when no gauge data exists and does it account for residence time in larger watersheds?	
A simple method is employed which assumes that runoff is proportional to the product of drainage area and average annual precipitation depth over the watershed. Residence time is not taken into account.

*Keywords: Rim inflows*

### Why is it necessary to calculate unimpaired flows?	
It's part of the philosphy of CalSim, since we are taking into account historical hydrology (e.g. precipitation and temperature) for the modeling scenarios.

*Keywords: Unimpaired flows, Historical hydrology*

### What are the units used in the Rim Inflow spreadsheets?	
It is TAF/year. CalSim can convert this into CFS.

*Keywords: Units, Rim inflows, Hydrology spreadsheets*

### For the Rim Inflow spreadsheets, how do you get pop-up (menu) to see (hidden) tabs in Excel?	
Right click on arrows at the on bottom left of workbook and select the tab to unhide it.

*Keywords: Rim inflows, Hydrology spreadsheets*

### Are there schematics available that show the same variables as the ones in CalSim 3 hydrology spreadsheets? 
Sometimes there are schematic tabs within the Excel workbooks. They are typically USGS schematics.

*Keywords: Schematics, Hydrology spreadsheets, USGS* 

### Would a process-based hydrologic model (e.g., SWAT) produce more realistic and coherent flow simulations for watersheds with limited or no data records compared to statistical linear regression based on another watershed selected with some degree of randomness? 
The former accounts for hydrological processes, dynamic hydroclimatic forcing, and static watershed characteristics. Model parameters can be calibrated using the particle data record, or a regional model can be calibrated and applied to the ungauged watershed. The choice to use model or gauge data is subjective.

*Keywords: Hydrologic Model, SWAT, Linear Regression, Dynamic hydroclimatic forcing*

### There are some negative flow values in the data. What is the physical meaning of these values?
There are two possibilities.  First of all, if the value is '-902' it means that data was not available. Secondly, it could be due to gauge error. When that happens, further preprocessing is needec to distribute the error to other months. 

*Keywords: Flow data, Preprocessing*

### For evapotranspiration, assuming the existence of a reservoir versus unimpaired flows, is surface area based on bathymetry of the reservoir accounted for?	
Yes. These factors are considered in the ET calculation for the reservoirs. There are separate workbooks used for the calculation of reservoir ET. Stream ET is assumed negligible on a monthly time scale.

*Keywords: Evapotranspiration, Unimpaired flows, Bathymetry*

### What is the most common reason to update the 200 or so hydrology spreadsheets used for CalSim 3 modeling?	
The last big update was due to simulation period extension. If we get new data from the source agencies, updating the spreadsheets could improve watershed representation in the model.

*Keywords: Hydrology spreadsheets, Simulation period*

### If rim inflows are assumed to be unimpaired, why do the rim inflow spreadsheets state '2020 Level of Development?'	
Prior to the last few years, we did not change or adjust the historical record for climate change. The workbook should have stated 'Existing Conditions.'

*Keywords: Rim inflows, Unimpaired flows, Historical record, Hydrology spreadsheets*

### Do the modules for the interconnected upper watersheds need to be run together (e.g. the Yuba and American upper watersheds)?  If so, why were two separate modules developed instead of one?  	
We develop standalone modules that can be run and debugged. The interconnections have to be preprocessed.

*Keywords: Upper watershed module, Yuba module, Upper american module, Preprocessed*

### Are the switches declared in statements within the CalSim 3 main wresl file (e.g. `svar simulateUpperFeather {value 1.}`) used to change from unimpaired flow ('0') to real conditions ('1')? 	
The switches activate a cycle for the upper watershed module. When it is set to "0", the Valley floor module will take its values from SV file. When set to "1", values are derived dynamically from the upper watershed module. Typically, timeseries values from the SV file should be similar to corresponding watershed results derived from dynamic runs.

*Keywords: Cycles, Upper watershed module, Dynamic runs*

### What are rules used to decide whether to use dynamically generated data or data from the SV file? Are there lists of considerations for when to run one versus the other?	
The only advantage of running modules and storing those results in SV file would be runtime. It's easier to run everything dynamically.

*Keywords: Dynamic runs, Upper watershed module*

### Is temporal and spatial variation represented in the Upper watersheds?	
These are represented by the GCMs. Climate change is not uniform across watersheds.

*Keywords: Temporal variation, Spatial variation, Upper watershed module*

### For Delta precipitation, why not use PRISM data (instead of Thiesen polygons) since we are now using it for CalSim 3?	
We use PRISM data for the station. But then use the Thiesen polygons to account for the spatial extent. Comparisons have shown that PRISM precip and station precip data seem comparable.

*Keywords: Delta precipitaton, PRISM, Thiesen polygons, Upper watershed module*

### What is spatial resolution of PRISM?	
It is 4 km by 4 km.

*Keywords: PRISM, Spatial resolution*

### Is double-counted water eliminated from the point-of-view of the water balance used inside CalSim 3?	
The DCD model accounts for double counting.

*Keywords: DCD model, Water balance*

### Are the rim watershed's simulated in CalSimHydro? 
No, they are calculated using Excels and also upper watershed modules. CalSimHydro deals with valley floor hydrology.

### How often is input data revised? 
It is constantly being revised as new GIS data becomes available.  We are working on revising land use, for example

*Keywords: GIS, land use*

### Will all the applied water demands calculated by CalSimHydro be met? Is applied water part of from CalSimHydro output?
CalSim 3 will meet all the applied water demands. If it does not get enough from stream diversion, it will take it from groundwater pumping. Applied water is output from the CalSimHydro model and used as input to CalSim 3.

*Keywords: CalSimHydro, applied water*

### Are return flow and deep percolation data pre-processed, assuming that the Ag and urban applied demand is fully met in CalSim 3? 
Yes. The exception is refuge demand which is handled in CalSim 3, not CalSimHydro. There can be shortages (not fully met) in CalSim 3.

*Keywords: Return flow, Refuge demand*

### How often does the Level-of-Development (LOD) get updated? 
Roughly about every 5-10 years.  The current update went from 2015 to 2020 LOD. LOD means more than just land use.  It also considers facilities, water supply contracts, and regulatory requirements. These are all represented at the 2020 level.

*Keywords: LOD*

### Does the growing season for rice ever change with time in CalSim 3? 
It does not change with time.

*Keywords: Rice*

### Is the pumping distributed across different aquifer layers according to C2VSim-CG (Coarse Grid) assumptions? 
Yes. In C2VSim-CG, the fraction of pumping from each layer is defined. 

*Keywords: C2VSim-CG, aquifer*

### Please explain how the GW DLL feeds back into CalSim 3 for tile drains. Why are tile drains not simulated in CalSimHydro? 
Tile drains are used by farmers to drain the water table below the root zone to prevent oversaturation.  Tile drain outflow is retrieved from the GW DLL to CalSim 3 using a function that is invoked from the model using the WRESL language.  CalSimHydro has nothing to do with GW and only calculates recharge back into groundwater. 

*Keywords: GW DLL, tile drains*

### What is the calibration period for the GW DLL (C2VSim-CG ver374) to provide aquifer parameters?
It was 1922-2009.

*Keywords: Calibration*

### Subsidence can impact hydraulic conductivity and aquifer storage over time. Does the GW DLL dynamically account for reductions in storage capacity and changes in hydraulic conductivity, or are these as static parameters? 
The change in storage capacity is represented in the model. Hydraulic conductivity is assumed to be static.

*Keywords: Subsidence, hydraulic conductivity, aquifer, GW DLL*

### How do you define the three water year types (i.e. Wet Years, Average Years and Dry Years)? 
We take 30 years of annual precipitation data, rank this and divide it into the three portions.

*Keywords: water year, precipitation*

### Do you envision that we'll need to redo the stress testing (seeing how the system responds to high temperatures or lower precipitation, higher sea levels, etc.) in the future? Or is the Eight River Index a sufficiently robust proxy (for SWP deliveries)?
We might want to sometime in the future.  For major infrastructure or operational changes maybe, but for now the Eight River Index seems pretty robust.

*Keywords: Stress testing*

### How about potentially adding dimensions to the risk analysis? Like subsidence? 
Yes. The San Francisco Public Utility District did something similar where they had financial risk built into their stress tests, Regulatory risk is another one.  So you could make that two or three dimensional stress test twenty dimensional if you wanted to.  However it becomes harder to interpret things.

*Keywords: Risk analysis, Stress testing*

### Are the Weather Generator graded data (precipitation and temperature) publically available?
Yes. All of the data are on a Box site. The output for the DWR's Delivery Capability Report (DCR) are available, as are the VIC inputs for the CalSim watersheds and the meterological outputs for the statewide grid.  There are also 23 different stress test scenarios using different combinations of temperature and precipitation.

[Weather Generator Data](https://cadwr.app.box.com/s/64ghda1cqfy4vtdwkbsr8s6o8i3lbem5)

*Keywords: Weather Generator, VIC*

### What is your experience conveying risk information to contractors and how are they receiving this information?
Contractors have just made comments on the DCR, but we need to get them to take greater ownership of this.  They need to understand the uncertainty involved and figure out how to deal with it because we can answer those question for them.

*Keywords: Risk information, contractors*

### How do you calculate how much land use reductions you need to impose to control groundwater decline?  Do all crops get reduced in landuse reduction? 
This was determined by conducting a sensitivity analysis.  Just annual crops are reduced, not permanent crops.

*Keywords: Land use, groundwater*

### Do the assumptions for climate change scenarios, take into account regulatory changes?
We don’t make assumptions about how regulations will change as a result of climate change.

*Keywords Assumptions, climate change*

### To determine if settlement contractors must take a deficiency (in allocation), do we use perfect foresight in CalSim 3? 
CalSim 3 used to rely on perfect foresight but currently has the ability to dynamically make forecasts. Ultimately we try to replicate the level of accuracy of Bulletin 120. 

Keywords: Perfect foresight, forecast*

### In CalSim 3, are contract limits applicable to surface water deliveries only or are they ever applied to the total applied water amounts? 
Contract limits only apply to surface water. No agreements to limit groundwater pumping. 

*Keywords: Contract limits, applied water*