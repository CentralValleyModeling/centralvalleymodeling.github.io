# Lookup Table Documentation

!!! Warning
    Under Construction

## AgMinMaxGW
**Author:** None  
**Date:**  None

**Description:**
Presents minimum GW pumping (as a fraction of applied water demand) for CalSim 3 demand units in the Sacramento River/San Joaquin River/Tulare Lake hydrologic regions. Maximum GW pumping is expressed a “1“ or having a 100 percent non-surface water source.


**Source:** [CS3_VolI_11_AgriculturalWaterUse_clean (PDF)](https://cadwr.box.com/s/ojp1bsy92q4evhl404v77uzx3zriepl5)


## AgReuse
**Author:** None  
**Date:**  None

**Description:**
Reuse of tailwater from irrigation to meet applied water demands is expressed as a fraction of the applied water demand. For the majority of crops, reuse is a constant fraction, defined in the file arcs-WUfactors.wresl. The exception is rice, for which the volume of tailwater and its relation to applied water varies significantly from month to month depending on cultural practices, including flood-up and drawdown. For rice cultivation, the agreuse.table defines the ratio of tailwater to applied water for each month and the fraction of the tailwater that is reused.


**Source:** [CS3L2015V0_ComparisionDiversions (Excel)](https://cadwr.box.com/s/t60uwj6db0hzzfoks4xdgfq9nz4hxdkt)

## American_ResInfo
Area-capacity curves for reservoirs in the Lower, Middle Fork and Upper American River (French Meadows, Hell Hole, Gerle, Loon Lake, Union Valley, Ice House, Folsom, Lake Valley, Stumpy Meadows, Silver, Caples, Lake Aloha, Echo Lake, Jenkinson Lake, etc.).


**Source:** [ER_AmericanRiv (Excel)](https://cadwr.box.com/s/gk0kkflsssolca7edjcex4bu6gqftlk3)

## American_ResLevel
**Author:** None  
**Date:**  None

**Description:**
These are minimum storage levels for Upper American River Project (UARP) reservoirs that must be maintained by SMUD (Sacramento Municipal Utility District) for July, August and September.


**Source:** [FERC 2101 Streamflow and Reservoir Elevation Gaging Plan (PDF)](https://cadwr.box.com/s/5frzfi45x1azlnij5uy8n4f772tsmhy1)

## American_SilverLakeLeakage
SILVERLAKELEAKAGE_ANALYSIS_ECORP (SPREADSHEET, SEE 'FERC TABLE')

## American_UARP_StorObj
**Author:** None  
**Date:**  None

**Description:**
Upper American River Project (UARP) reservoirs at Loon Lake, Ice House and Union Valley reservoirs are operated to build storage during the winter and spring and make releases for power generation
during the Summer and Fall months.  These operations rely on target storages for each facility which are base on April-July unimpaired runoff
at the Fair Oaks gage.  A five-level "wetness index" is defined by the following:

   
|Wetness Index|April - July Runoff (TAF) |	      
|:-------------|:-------------:|
|      A      | 0           |      
|      B      | 500	    |
|     C       | 1,000       |
|      D      | 1,500	    |
|     E       | 2,000	    |




**Source:** [hydro-rel-rpt-WBM_Technical_Report (PDF)](https://cadwr.box.com/s/su7cbydl4oe0sj17eld16qp7cnzuea3s)


## AmerSteelhead

## ANNlimit

## AnnualReqDel_swp
**Author:** None  
**Date:**  None

**Description:**
Annual SWP South-of-Delta contract demands by contract type (Agricultural, MWD Municipal&Industrial, Other (non-MWD) M&I, conveyance losses).


**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (XLSM)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## Apr_snowmelt_release_pattern (!!)
Nancy Parker, Reclamation 

## AR_90ExcFall
**Author:** Jonathan Byers  
**Date:**  2/26/2024

**Description:**
This table provides the 90% exceedance inflow forecast into Folsom for October, November and December. This is used in the American River Flow Management Standard to help determine the minimum storage needed at a the end of a given month, ensuring that end of December Folsom storage target is met and minimum release requirements are made.  In CalSim, total Folsom
inflow is calculated as the sum of flows from North Fork, South Fork and local inflows into Folsom Reservoir.  

**Source:** [AR_90EXCFall_yc_TF_LTO_3.12.13_9.0.0_Danube_hist (XLSX)](https://cadwr.box.com/s/l7a704cnvbwre23jnuql3hzavdkwkddg)


## BanksLimits
**Author:** Idy Lui (last update)  
**Date:**  5/17/2019

**Description:**
Monthly permitted capacity of Banks Pumping Plant (6680 cfs),  Permitted capacity may increase up to 10,300 cfs depending on Vernalis flow between December 15 - March 15.  For July to September, capacity may increased by 500 cfs (to 7180 cfs) to mitigate impact of reducing impact of NMFS BO (Jun 2009) Action IV.2.1.


**Source:** [Final DCR 2019 Technical Addendum (PDF)](https://cadwr.box.com/s/ct4rn6p1qg0l3djytseejn67imeq8pdk)

## black_butte_min
**Author:** None  
**Date:**  None

**Description:**
Black Butte Reservoir (capacity 136,000 acre-feet) has a minimum release requirement of 30 cfs to maintain 20,000 acre-feet of space for flood protection.


**Source:** [StonyCreek2003ReportandAppendicies (PDF)](https://cadwr.box.com/s/u8k0vf940y0amvnoinsa34c3ycd2szy8)

## calaveras_dist
**Author:** R. Field  
**Date:** 12/03/2003


**Description:**
Calaveras River ag and mi distributions percentage given month.  The following list identifies the water demand types used in this table:

- SEWD_MI = Stockton East Water District Municipal and Industrial (M&I)
- SEWD_AG = Stockton East Water District Agricultural (Ag)
- CACWD_MI = Calaveras County Water District M&I
- CACWD_AG = Calaveras County Water District Ag


**Source:** [Calaveras_dem (Excel)](https://cadwr.box.com/s/k7wu4wijguw35e0fys5r16mfax6wvcw0)

## CCWD_ann_demand
**Author:** None  
**Date:**  None

**Description:**
Contra Costa Water District annual demand depending on water year type.


**Source:** [CCWD_2015UWMP_Final_June2016_201610111231300825 (PDF)](https://cadwr.box.com/s/aecdhmsxispmz2yutbv4668adi3pf2h6)

## CCWD_demand_pattern
## CCWD_INTAKE_PREF
**Author:** None  
**Date:**  None

**Description:**
This table establishes intake preference months as long as service area water quality objectives are met and Los Vaqueros storage is not reduced(1= preference, 0 = no preference).
**Source:** [5626_p020749 (PDF)](https://cadwr.box.com/s/6ldaaqelmp81vg7su0jrnqxug5spprwo)


Set months that intakes should take preference
!as long as service area water quality objective
!met and LV storage is not reduced.  1= preference, 0 = no preference
## ChiliBarYrType_hist
## cho_gcid_min
**Author:** None  
**Date:**  None

**Description:**
The Constant-head Orifice (CHO) brings in water released from Black Butte Reservoir into Stony Creek for flood reservation requirements or for summer recreation purposes.

**Source:** [StonyCreek2003ReportandAppendicies (PDF)](https://cadwr.box.com/s/u8k0vf940y0amvnoinsa34c3ycd2szy8)


## chow_max_surf
## chowchilla_agdist
## chowchilla_seep
## clear_ck_min_PA
**Author:** None  
**Date:**  None

**Description:**
Reclamation proposes a minimum base flow in Clear Creek of 200 cfs from October through May and 150 cfs from June to September in all year types except critical year
types (minimum is 150 cfs each month during critical years).

**Source:** [Re-managed-Instream-Flows-in-the-Sac-River-Basin (PDF)](https://cadwr.box.com/s/883byvizigjzr27p968nl3jfg2j09tqy)

## Contracts_CVPService
**Author:** None  
**Date:**  None

**Description:**
These are Central Valley Project (CVP) service contract amounts for service contractors situated in the Sacramento River hydrologic region. Service contracts are agreements between Reclamation and various water districts and agencies for purchasing CVP water.  Most contracts are meant to last 40-years.


**Source:** [CS3_VolI_14_ContractsAndWaterRights_clean_updated (DOC)](https://cadwr.box.com/s/huos58q5afsr4gb6qucucxia9fsjr2u2)

## Contracts_CVPSettlement
## Contracts_FRSA
**Author:** None  
**Date:**  10/14/2008

**Description:**
These are DWR agricultural settlement contracts with Feather River Service Area (FRSA) districts, including Western Canal WD, Joint WD Board, Plumas MWC, Garden Highway MWC (Mutual Water Comparny), Oswald WD, and Tudor MWC. City of Yuba City is contracted with SWP for 9.6 AF/year of Table A water.


**Source:** [CS3_VolI_14_ContractsAndWaterRights_clean_updated  (DOC)](https://cadwr.box.com/s/huos58q5afsr4gb6qucucxia9fsjr2u2)

## COSMA_WWTP_PerMonth
**Author:** None  
**Date:**  None

**Description:**
Not used in CalSim 3.

**Source:** 
## Consumnes_demands_OASISVal
## CVP_SOD_Contracts
**Author:** None  
**Date:**  None

**Description:**
This table presents CVP water service contracts for servce areas South of Delta (located in San Joaquin River and Tulare Lake hydrologic regions).


**Source:** [CS3_VolI_14_ContractsAndWaterRights_clean_updated  (DOC)](https://cadwr.box.com/s/huos58q5afsr4gb6qucucxia9fsjr2u2)

## CVPSL_fill_targets
## Daguerre_del_pattern
## demand
## dltidx_expidx_swp_s
**Author:** None  
**Date:**  None

**Description:**
This table was originally derived to split the responsibility for export restrictions and supply reductions brought about by the Wanger decisions to the SWP and CVP (the Delta index was based on January to May Eight River Index - please see the entry for EiRatio for a description of this).  The values are currently set to 9999, so as not to constrain operations on top of existing restrictions used in the model.


**Source:** [CA_Main_Document_and_Appendices_032509  (PDF)](https://cadwr.box.com/s/ujs3ia9m719nv1qaqk4nrv6ck7yzp76i)

## DO
**Author:** None  
**Date:**  None

**Description:**
These are monthly required minimum "surrogate" flows below Goodwin (in TAF) needed to meet Stanislaus dissolved oxygen objectives.


**Source:** [feirch04  (PDF)](https://cadwr.box.com/s/d4jeoqn4hj8pkv33uvwz85elg1whefex)

## east_park_min
**Author:** None  
**Date:**  None

**Description:**
This table presents minimum flow requirements (5 cfs) below East Park Reservoir. The minimum flow is meant to help maintain flood capacity and provide for recreation (during Summer).  East Park was built by Reclamation and is intended to provide water supply, not hydropower. ce areas South of Delta (located in San Joaquin River and Tulare Lake hydrologic regions)..


**Source:** [AppendixC-Reservoir_Operations_ModelingTechnical  (PDF)](https://cadwr.box.com/s/bb3eeoloy7zwkvlsk4sc9b17j0k7cd3z)

## ECCID_Transfer
**Author:** None  
**Date:**  None

**Description:**
This table outlines an ECCID transfer schedule to CCWD for Normal Years (CVP allocations of 100%) and specifies an additional dry year supply.

**Source:** [CCWD USBR WMP Final Draft wAppdx no reso_201705311512085186  (PDF)](https://cadwr.box.com/s/a8ejs471o60avu7xx9n21aytyl9sejd0)

**Author:** None  
**Date:**  None

**Description:**
This table outlines an ECCID (East Contra Costa Irrigation District) transfer schedule to CCWD for Normal years (CVP allocations of 100%) and Dry years (allocations less than 100%).

**Source:** [ARWA 602 - Technical Memorandum 1- Lower American River Flow Management Standard - Project Description-Modified  (PDF)](https://cadwr.box.com/s/c10w9un41sgbz7za5ndqv5vek2lrukor)



## EiRatio
**Author:** None  
**Date:**  None

**Description:**
This is the Export/Inflow ratio imposed monthly by D-1641 to protect migrating fish species by limiting the proportion of Delta inflow that is exported. The E:I ratio is 0.35 from March to June and 0.65 for the remaining months.  The February E:I ratio (0.0 in the table) can vary from 0.35 to 0.45 depending on the amount of January runoff (February E:I is determined by another table: "FebEIratio").


**Source:** [Delta_Standards (modified)  (PDF)](https://cadwr.box.com/s/sp1gpydb5d9q8aw6l5nf445h6r6tqtvt)

## ElDoradoForebay_monthlypattern
## EOMay_Target
**Author:** None  
**Date:**  None

**Description:**
This helps determine the End-of-May storage target for the American River Flow Management Standards. The American River Index (ARI) is an indicator of unimpaired Folsom inflow and is based on DWR's Bulletin 120.  The End-of-May storage target is derived from linear interpolation of the ARI.


**Source:** [ARWA 602 - Technical Memorandum 1- Lower American River Flow Management Standard - Project Description-Modified  (PDF)](https://cadwr.box.com/s/c10w9un41sgbz7za5ndqv5vek2lrukor)

## EstExpCVP
## ESTMN_Gross_Res
## EstmnCarryover
## evap_est
## ExchContractLimits
## ExportEstimate_CVP
## ExportEstimate_SWP
## featherfish_058
**Author:** None  
**Date:**  None

**Description:**
Flow below Thermalito must not exceed 2500 cfs between October 15 and November 30 (except in the case of flood release).  Otherwise this will trigger a 500 cfs increase in required flows to the end of March (to prevent dewatering of spawning sites). To avoid this, CalSim uses a 4000 cfs constraint on flows for October.and a 2500 cfs limit in November.  See example for an explanation for the October constraint.

Example:  A 4000 cfs requirement for all of October provides for a partial month requirement of less than 2500 cfs from Oct 15 to Oct 31 (17 days) and from Oct 1 to Oct 14 (14 days).


**Source:** [ch07_otherassumptions  (PDF)](https://cadwr.box.com/s/yf5fhw1c33u3lhp4irt5tfjmk7dr83t4)

## Feb_snowmelt_release_pattern
## FebEiRatio
**Author:** None  
**Date:**  None

**Description:**
February Export/Inflow ratio (E:I) depends on January Eight River Index (8RI),  The January 8RI is the sum of unimpaired flow from the Sacramento River at Bend Bridge, Feather River at Oroville, Yuba River at Smartville, American River at Folsom, plus the Stanislaus River inflow to New Melones Lake, Tuolumne River inflow to New Don Pedro Reservoir, Merced River inflow to Lake McClure, and San Joaquin River inflow to Millerton Lake. If January 8RI greater than (or equal to) 1.5 MAF, the February E:I ratio is 0.35, If it is less than (or equal to) 1.0 MAF, February E:I ratio is 0.45. All ratios in between are derived through interpolation.


**Source:** [Delta_Standards (modified)  (PDF)](https://cadwr.box.com/s/sp1gpydb5d9q8aw6l5nf445h6r6tqtvt4)

## FK_delivery_class1
## FK_delivery_dist
## FK_delivery_total
## FlowLossFactors
**Author:** Idy Lui  
**Date:**  03/2018

**Description:**
These loss fractions determine what fraction of the surface water delivery is lost to evaporation, horizontal seepage to canal toe drains, vertical percolation to the underlying aquifer, or spills from the end of the canal distribution system back to the stream or river.

Then naming conventions for these loss factors are as follows:

- EVF - Evaporative loss fraction 
- LFF - Lateral flow loss fraction			
- DPF - Deep percolation loss fraction  					
- OSF - Canal operating spill fraction  					
 

**Source:** [CS3L2015V0_ComparisionDiversions  (Excel)](https://cadwr.box.com/s/t60uwj6db0hzzfoks4xdgfq9nz4hxdkt)

## FolEvapCoef
## FRE_No_Notch
**Author:** None  
**Date:**  None

**Description:** Need flow curves

**Source:** Need flow curves

## FRE_Notch
**Author:** None  
**Date:**  None

**Description:** Need flow curves

**Source:** Need flow curves
## FRENotch_OnOff
**Author:** None  
**Date:**  None

**Description:** Need flow curves

**Source:** Need flow curves
## Freq_Exceedence
## fresno_agdist
## fresno_seep
## Friant_Allocation
## Friant_canal_losses
## Friant_Evap
## Friant_max_del
## HistoricFlow
## HistoricUnimp_Precip
## HNSLY_Gross_Res
## HnslyCarryover
## HSt_base
**Author:** None  
**Date:**  None 

**Description:**
Based on State Water Resources Control Board Decision 893 (D-893) which was enacted in 1958 as a pre-CVPIA measure to provide fish protection by applying minimum flow requirements along the Lower American River.  D-893 requires a minimum of 500 cfs between September 15 and December 31 and 250 cfs from January through mid-September. During critically dry periods (when unimpaired inflows to Folsom Reservoir from April and September fall below 600 TAF) minimum flows can decrease by as much as 50%.  In the table, for each month, the D-893 year type can be either Not Critically Dry ("1") or Critically Dry ("2"). 

Example:  For September (Month = "12"), if conditions are not critically dry (D-893 index is “1”), D-893 calls for a 250 cfs minimum for the first part of the month, then a 500 cfs minimum for the latter half (averaging out to 375 cfs for the entire month). 


**Source:** [Decision on Major Applications to Appropriate Water from American River Systems (PDF)](https://cadwr.box.com/s/rzwiei5rhs9mtg8tlymfgb7wtxuogvt3)

## IsolatedFacility
## IsolatedFacilityControl
## JUBSFU_Dist
## Kellogg_Creek_Inflow
## Kern_GW_RechLim
## KernGW_NODStor
## KeswickWinterFlow
## LCPSIM_JobControl
## LCPSIM_SB_Output
## LCPSIM_SC_Output
## LV_evaporation
## LV_Precipitation
## lyons_target
## Madera_delivery_class1
## Madera_delivery_total
## Mar_snowmelt_release_pattern
## MaxPermissible
## May_snowmelt_release_pattern
## Merced_MinFlows
**Author:** None  
**Date:**  None  

**Description:**
Minimum flow requirements for the Merced River Hydropower Project (FERC 2179-043). The following describe the minimum flow agreements applied by this table:

Davis-Grunsky Agreement: Provides a miniumum flow of 180 to 220 cfs in the Merced River between Crocker-Huffman diversion dam and Shaffer Bridge from November through March every year for fall-run Chinook salmon.
Davis-Grunsky Act requirements are assumed to be 220 cfs in non-dry years, per the FERC definition. In FERC dry years, the Davis-Grunsky Act requirement is modeled as 180 cfs.

The existing FERC license defines a “normal” or "non-dry" year as when the May 1 DWR Bulletin 120 forecasted April through July inflow to Lake McClure is greater than 450,000 AF,
and a “dry” year when inflow is forecasted to be less than 450,000 AF.

The Cowell Agreement, calls for —Merced ID to provide releases from Crocker-Huffman diversion dam up to the following flows for use by the Cowell Agreement diverters at 11 locations: 100 cfs in March; 175 cfs
in April; 225 cfs in May; 250 cfs in June until the flow of the Merced River falls below 1,200 cfs; 225 cfs flow for the next 31 days; 175 cfs flow for the next 31 days; 150 cfs for the next 30 days; and 50 cfs thereafter or the natural inflow into Lake McClure, whichever is
less, through the last day of February.

The FERC license requires a specific flow at Shaffer Bridge, approximately 20 miles downstream from Crocker-Huffman.
Flows vary by month and water year type between 15-100 cfs.  The following schedule for these flows (dependent on year type) are as follows:

|				|Normal Year (cfs)  |Dry Years (cfs)|
|:------------------------------|:-----------------:|:-------------:|
|June 1 through October 15	|25		    |15		    |
|October 16 through October 31	|75		    |60             |
|November 1 through December 31	|100		    |75             |
|January 1 through May 31	|75		    |60             |

Example:  For the month of October, the flow requirement is calculated using monthly averaging, combining flow (cfs) with the corresponding number of days (d):

Normal Year
(25 cfs(15d)+75 cfs (16d))/31d = 50.81 cfs

Dry Year
(15 cfs(15d)+60 cfs(16d))/31d = 38.23 cfs

**Source:** [feis_master_sent2ferc (PDF)](https://cadwr.box.com/s/o1bz87rwmi8ejwovse2hta36zhlkg4z2)
applied below dams located on the South Fork of the American River as part of the El Dorado Hydroelectric Project (FERC No.184).  Values are determined by month and water year type.  Year type definitions: Critically dry: <50% of forecast average pre-project inflow to Folsom reservoir; Dry: 50–70% of forecast average pre-project inflow to Folsom reservoir; Below Normal: 75–100% of forecast average pre-project inflow to Folsom reservoir; Above Normal: 100–125% of forecast average pre-project inflow to Folsom reservoir; Wet: >125% of forecast average pre-project inflow to Folsom reservoir.


**Source:** [Merced EIS_Master_with Cover (PDF)](https://cadwr.box.com/s/8dtz6mo5g35kr0f8jkvguh3qoleplejw)

## MFP_DemandFractions
## MFPpow_forecast
## MIF_EID
**Author:** None  
**Date:**  None  

**Description:**
Minimum flow requirements applied below dams located on the South Fork of the American River as part of the El Dorado Hydroelectric Project (FERC No.184).  Values are determined by month and water year type.  Year type definitions: Critically dry: <50% of forecast average pre-project inflow to Folsom reservoir; Dry: 50–70% of forecast average pre-project inflow to Folsom reservoir; Below Normal: 75–100% of forecast average pre-project inflow to Folsom reservoir; Above Normal: 100–125% of forecast average pre-project inflow to Folsom reservoir; Wet: >125% of forecast average pre-project inflow to Folsom reservoir.


**Source:** [feis_master_sent2ferc (PDF)](https://cadwr.box.com/s/o1bz87rwmi8ejwovse2hta36zhlkg4z2)

## MIF_MFP
**Author:** None  
**Date:**  None 

**Description:**
Minimum flow requirements applied below dams located in the Middle Fork of the American River as part of the Middle Fork Hydroelectric Project (FERC No.2079).  Values are determined by month and water year type.  There are six water year types which are based on forecasted American River unimpaired flow below Folsom Reservoir (based on DWR Bulletin 120 and abbreviated here as “UBFR“).  Year type definitions: Extreme Critical: UBFR < 600,000 AF; Critical:  900,000 AF <= UBFR < 1,000,000 AF; Dry: 1,000,000 AF <= UBFR < 1,500,000 AF; Below Normal: 1,500,000 AF <= UBFR < 2,400,000 AF;  Above Normal: 2,600,000 AF <= UBFR < 3,400,000 AF; Wet: UBFR >= 3,400,000 AF.  March is split into two periods: March 1-14 and March 15-31 (represented in the table as 6.1 and 6.2 respectively) for forecasting purposes.


**Source:** [Middle Fork American River Hydroelectric Project (FERC 2079) (PDF)](https://cadwr.box.com/s/i32seu3ji0jbhurr65q1e90d1uz7oir7)

## MIF_PGECh
**Author:** None  
**Date:**  None 

**Description:**
Minimum instream flow requirements for the South Fork of the American River below Chili Bar Dam as mandated by FERC Project No. 2155.  Water year type definitions mostly similar to those used in Middle Fork Project.  A “Super Dry“ year is defined as a critically dry (CD) year that is preceded by a dry or CD year, or any dry year type which is preceded by any combination of two CD or dry water year types.

**Source:** [Appendix C_CalSim3_UAR_Module_Doc  (PDF)](https://cadwr.box.com/s/rstoxh0y8zcga7wpptyx793vfe1blkal)

## MIF_PGECh_req
**Author:** None  
**Date:**  None 

**Description:**
These values represent total flow requirements for South Fork American River below Chili Bar Dam.  These are monthly averages over calculated over 94 years (from 1922 to 2015) for each month.  Year type definitions are from FERC Project No. 2155. A “Super Dry“ year is defined as a critically dry (CD) year that is preceded by a dry or CD year, or any dry year type which is preceded by any combination of two CD or dry water year types.

**Source:** [Appendix C_CalSim3_UAR_Module_Doc  (PDF)](https://cadwr.box.com/s/rstoxh0y8zcga7wpptyx793vfe1blkal)

## MIF_PGELV
**Author:** None  
**Date:**  None 

**Description:**
These are minimum streamflow requirements (in cfs) proposed by Pg&E for the Upper Drum-Spaulding Project at North Fork American River, below Lake Valley Reservoir (FERC Project No. 2310).   total flow requirements for South Fork American River below Chili Bar Dam.  These are monthly averages over calculated over 94 years (from 1922 to 2015) for each month.  Year type definitions are from FERC Project No. 2155. A “Super Dry“ year is defined as a critically dry (CD) year that is preceded by a dry or CD year, or any dry year type which is preceded by any combination of two CD or dry water year types.

**Source:** [20141219-4003(30000282) (PDF)](https://cadwr.box.com/s/nzhv3n9lyl4bavnksw6vlq6tgrzfg0ej)

## minflow
**Author:** None  
**Date:**  None 

**Description:**
Monthly minimum instream requirements for various flow arcs (CalSim 3 only uses C_arc = 200 values, tied to the Feather Low Flow Channel).  The minimum flow requirement is 800 cfs from September 9 to March 31 (Chinook salmon spawing season), and 700 cfs for the rest of the year.

Example:  The September minimum flow is 773.333 cfs in the table.  This is a monthly average of 700 cfs minimum from Sep 1 to Sep 8 (8 days) and 800 cfs from Sep 9 to 30 (22 days) or 700*(8d/30d)+800*(22d/30d) = 773.333 cfs.

**Source:** [FERC 2100-121410_15 (PDF)](https://cadwr.box.com/s/xnptd6i1qkeo89glphjtbbbmejmi4t2u)

## Mok_Demands
## Mok_GWSeepage
## Mok_JSAFlow
**Author:** None  
**Date:**  None 

**Description:**
Minimum requirements (applied by EBMUD) as stated in the Mokelumne Joint Seetlement Agreement for flows below Camanche and Woodbridge Dams. "WBAAprSepTAF" is the sum of April to September requirements for Woodbridge (in TAF).

**Source:** [LOWER MOKELUMNE RIVER PROJECT - FERC Project No. 2916-004 JOINT SETTLEMENT AGREEMENT 1996 (PDF)](https://cadwr.box.com/s/v2538agwjp98a7rpmxl5xv6w89df5ycv)

## Mok_LodiPrecip
**Author:** None  
**Date:**  None 

**Description:**
The Lodi Decree is a series of court orders, stipulations and agreements establishing daily and monthly average flows for the North Fork of the Mokelumne River below Electra Diversion Dam and Powerhouse.  It may be triggered when when precipitation at Salt Springs Reservoir exceeds the limits in the lookup table. 

**Source:** [Appendix D (PDF)](https://cadwr.box.com/s/goutshk1vp9tijmeeygrqmkll5hfzz94)

## Mok_P137Flow
**Author:** None  
**Date:**  None 

**Description:**
Minimum flow requirements from the 2000 Joint Settlement Agreement for Relicensing of FERC Project 137 for several location at North Fork Mokelumne River including: Tiger's Creek Dam, Electra Dam and Salt Springs Dam. The minimum streamflow schedules have been separated into five water year types:Wet, Above Normal (AN), Below Normal (BN), Dry, and Critically Dry (CD). Water Year Types are based on unimpaired inflow into Pardee Reaervoir where: 

Wet: 	Pardee Inflow >= 958,700 AF
AN: 	Pardee Inflow < 958,700 AF but >= 724,400 AF
BN: 	Pardee Inflow < 724,400 AF but >= 518,100 AF
Dry: 	Pardee Inflow < 518,100 AF but >= 376,100 AF
CD:	Pardee Inflow < 376,100 AF

**Source:** [WS-Final-Rprt_Appendices_033018  (PDF)](https://cadwr.box.com/s/ukkioltabel12z1vwvlcveb53jljgqaq)

## Mok_PardeeTargets
## Mok_percut
**Author:** None  
**Date:**  None 

**Description:**
This table sets the amount of delivery cuts to be made to the Mokelumne Aqueduct.  The cuts (in percentage) are tied to the supply storage projected for April to the end of September for the Mokelumne River.  This is determined by
summing end of March storage at Pardee, Comanche and EBMUD Terminal reservoirs with available inflows from April to September.  Generally, a supply index of below 500 TAF calls for a 15 percent cut in deliveries. An SI above 500 TAF would
not require delivery cuts (0 percent, etc.).

**Source:** [Water_Supply_Board_Briefing_-_February_23_2021_FINAL_BOARD  (PDF)](https://cadwr.box.com/s/61heharw78yad0c527wwruj7d4k5nprq)


## Mok_RainfloodReservation
## Mok_ResInfo
**Author:** None  
**Date:**  None


**Description:** Area-Capacity relationships for Lower Mokelumne reservoirs.  Based on updated bathymetric data received from EBMUD.

**Source:** [Mok_ResInfo (Excel)](https://cadwr.box.com/s/doqbik3beqxremj9z6f1wsfv689b0zow)

## Mok_ResLevel
## Mok_SnowmeltReservation
**Author:** None  
**Date:**  None 


**Description:** can't find numbers in camanche flood control diag.

**Source:**
**Author:** None  
**Date:**  None 


**Description:** can't find numbers in camanche flood control diag.

**Source:**


## MRR_Schedule
## ncp_with_relax
**Author:** None  
**Date:**  None 

**Description:** Navigational Control Point minimum flow requirement based on Ag allocation and Shasta storage (Low - Shasta below 5.5 maf, Med - Shasta between 3.5 - 4.0 maf, high - Shasta > 4.0 maf).  Values in between Ag allocation levels use maximum flow levels.

Example:  For an Ag allocation of 30%, flow is at 3250 cfs at Shasta low levels and 4000 cfs at Shasta high levels.

**Source:** [app_5A_CalSim (PDF)](https://cadwr.box.com/s/9s291wa9phu01b5tz2b71rzuyebhusju)

## ndd_cho_min
**Author:** None  
**Date:**  None 

**Description:** Northern Diversion Dam (NDD) contains a 36-foot sluiceway with a 12-foot by 6-foot wide electrically operated drum gate that permits 30 cfs or additional water flows to be bypassed downstream during diversions.  Chinook salmon, steelhead trout, and other at-risk species may benefit from these actions to improve upstream fish passage in Stony Creek.

**Source:** [Northside Diversion Dam Fish Passage Feasibility Study (PDF)](https://cadwr.box.com/s/r3emzbqemkbkyoeclxsqt0phd6y9a4ah)

## ndo_flow_std
**Author:** None  
**Date:**  None 

**Description:** Miniumum average Delta outflow requirement based on month and water year type (40-30-30 index).

**Source:** [Delta_Standards (modified) (PDF)](https://cadwr.box.com/s/sp1gpydb5d9q8aw6l5nf445h6r6tqtvt)

## NewFacSwitch
## newspicer_target
## NODOS
## NODOS_jobcontrol
## OMRiverFlowEq2
**Author:** Paul Hutton  
**Date:**  April 2008

**Description:** Model to estimate combined Old and Middle River flow (OMR) using OMR Flow Model coefficients, where: QOMR (cfs) = A * QVernalis + B * QSouth Delta Diversions + C based on HOR, GLC barrier conditions and Vernalis flow.

**Source:** [Hutton_2008_OMR_Report (PDF)](https://cadwr.box.com/s/d944efnit6oi0wen5i3lednvcx8w0v79)

## Putah_minflow
**Author:** None
**Date:**  None

**Description:** Minimum flow requirements along Putah Creek at various locations (e.g. Putah Diversion Dam and I-80 Road Bridge).

**Source:** [Putah Creek (PDF)](https://cadwr.box.com/s/n0l3tr6yqpuefsndym16n9jpg4e4rbte)

## qwest
## redbluff_base
## refuge
**Author:** None  
**Date:**  None 

**Description:** Annual refuge demands (without losses) and percent conveyance losses.  Note: value for Butte Sink Annual Demand is not used.

**Source:** [CS3_VolI_13_WetlandWaterUse_clean (PDF)](https://cadwr.box.com/s/yq0ks4qom85k8sb1eja9yr86061ik5h5)

## res_info
**Author:** None  
**Date:**  None 

**Description:** Reservoir area-capacity curves.

**Source:** [ER_spreadsheets_2020_2021 (Excel)](https://cadwr.box.com/s/5bqlv2f1daasntvtqvtu859krzso10e6)

## res_level
## riovista
**Author:** None  
**Date:**  None 

**Description:** Rio Vista minimum monthly average flow requirements based on month and water year type (40-30-30 index).

**Source:** [Delta_Standards (modified) (PDF)](https://cadwr.box.com/s/sp1gpydb5d9q8aw6l5nf445h6r6tqtvt)

## Rpf_RufO_RufW
**Author:** Idy Lui  
**Date:**  03/2018 

**Description:** The reuse of irrigation water is expressed as a fraction of applied water demand and is associated with reuse variables (prefix 'RU_') within the model.  The table also.
The table also defines one state variable for miscellaneous evaporative and riparian losses (RPF), and is expressed as a fraction of the applied water demand or urban demand and an associated reuse variable (with prefix 'RP_') in the model.

The naming conventions used in the table (and model) riparian loss factor and reuse factor for other crops (than rice) and wetlands are as follows::

- RPF - Evaporative/Riparian loss factor (Evapotranspiration fraction)
- RUFO - Reuse fraction of applied water for other crops
- RUFW - Reuse fraction of applied water for wetlands. 

Note: In the table, (-1) indicates no data and (-2) indicates a time series is used.

**Source:** [CS3L2015V0_ComparisionDiversions (Excel)](https://cadwr.box.com/s/t60uwj6db0hzzfoks4xdgfq9nz4hxdkt)


## S92carryover
## SAC_weir
**Author:** None  
**Date:**  None 

**Description:** Spill curve for Sacrmento Weir.  Used to estimate daily spill over the weir.  This was developed by using monthly to daily flow mapping process which involves using historical daily flow patterns taken from DAYFLOW.

**Source:** [app_5A_CalSim (PDF)](https://cadwr.box.com/s/9s291wa9phu01b5tz2b71rzuyebhusju)

## salinity_std_col
**Author:** None  
**Date:**  None 

**Description:** Salinity standard (EC levels) for Collinsville.  Currently, only "EC Standard 1" is being used.

**Source:** [D1641rev (PDF)](https://cadwr.box.com/s/1gd2229l39ca7xj60be3ocvzo0jg7mit)

## salinity_std_emt_new
**Author:** None  
**Date:**  None 

**Description:** Salinity standard (EC, mmhos/cm) standard at Emmaton based on month and water year type (Sacramento Vally 40-30-30 index). for Collinsville.  Currently, only "EC Standard 1" is being used.

**Source:** [D1641rev (PDF)](https://cadwr.box.com/s/1gd2229l39ca7xj60be3ocvzo0jg7mit)

## salinity_std_jpt_new
## salinity_std_rsl
## seep_rates
**Author:** None  
**Date:**  None 

**Description:** Apparently not used in model.

## ShastaNCPlevel
## ShrngRatios
**Author:** None  
**Date:**  None 

**Description:** Project (CVP and SWP) sharing ratios under the Coordinated Operations Agreement (COA) Addendum from 2018 for balanced conditions - when releases from upstream reservoirs plus unregulated flow approximately equal the water supply needed to meet Sacramento Valley inbasin uses, plus exports; and surplus (excess) conditions - when releases from upstream reservoirs plus unregulated flow are greater than the water supply needed to meet Sacramento Valley inbasin uses, plus exports.

**Source:** [20181200_COAAddendum (PDF)](https://cadwr.box.com/s/5tnluk18kjxzd7wyh6dayqrel8jxoub5)
## shsta_floodCurve
## SMSCG_TriggerMTZ
**Author:** Idy Lui  
**Date:**  9/22/2020 

**Description:** The Suisun Marsh Habitat Management, Preservation, and Restoration Plan (SMPP) was collaborative development by Federal, State, and local agencies working with
develop a long-term, comprehensive plan to restore and enhance wetlands in the Suisun Marsh (Marsh) while also providing for flood management and public recreation. The Suisun Marsh Preservation Agreement (SMPA) was signed by
Reclamation, DWR, DFG, and SRCD in 1987, contains provisions to mitigate the effects of the SWP and CVP operations on Suisun Marsh channel water salinity. It required Reclamation and DWR
to meet salinity standards specified in the then-current State Water Board D-1485 (the SMPA was amended in 2005).  As part of the SMPA, the EC threshold at Martinez (MTZ) for triggering SMSCG operation for D-1641 and SMPA ( Suisun Marsh Preservation Agreement) 
is the last 7-day average MTZ EC value of previous month in mmhos/cm. 

**Source:** [SMSCG_MTZ_EC_Trig (Excel)](https://cadwr.box.com/s/2i8nwi0k99dvsmeuk75ri3tyyrwtofg0)
## SRRP_Recapture_Pot
**Author:** None
**Date:**  None 

**Description:** SJR Restoration program potential recapture amounts at Patterson ID, Banta Carbona ID, and West Stanislaus ID.

**Source:** [Combined_LTRRRF_PDTM_20170907-1-1 (PDF)](https://cadwr.box.com/s/na9yko60gx977zctzhjht844bsw77w26)

## stan_mon
## stan_pulse_rpa
**Author:** Tom Fitzhugh (updated) 
**Date:**  06/10/14 

**Description:** Pulse period (April 15 to May 15) flows for fishery purposes.

**Source:** [app_5A_CalSim (PDF)](https://cadwr.box.com/s/9s291wa9phu01b5tz2b71rzuyebhusju)

## stan_rpa
**Author:** None
**Date:**  None 

**Description:** Monthly base flows for fishery purposes (TAF).

**Source:** [app_5A_CalSim (PDF)](https://cadwr.box.com/s/9s291wa9phu01b5tz2b71rzuyebhusju)

## stan_yr
**Author:** None
**Date:**  None 

**Description:** New Melones Operations Plan annual flows for fishery purposes.  Summarized in Appendix 5.A. CalSim II Modeling Results Report Table 5.A-3

**Source:** [app_5A_CalSim (PDF)](https://cadwr.box.com/s/9s291wa9phu01b5tz2b71rzuyebhusju)

## stanf_yr
## Stanislaus_beardsley_reslevel
## Stanislaus_BeaverCk_Div
## Stanislaus_donnell_reslevel
## Stanislaus_donnell_supplflow
## Stanislaus_lyons_reslevel
## Stanislaus_lyons_targetflow
## Stanislaus_newspicer_trigmon
## Stanislaus_NF_Div
## Stanislaus_philadel_div
## Stanislaus_pinecrest_target
## Stanislaus_relief_rel1
## Stanislaus_relief_rel2
## Stanislaus_relief_reslevel
## Stanislaus_res_info
**Author:** Idy Lui 
**Date:**  1/28/19 

**Description:** Area-capacity curves for Upper Stanislaus reservoirs.  Area-Capacity Relationships spreadsheets provided by Andy Draper/Stantec.

**Source:** [ER_UpperStanislaus (Excel)](https://cadwr.box.com/s/ipze2dkr9otxgvn1u146bgvrmd6gxv14)

## Stanislaus_upa_diversion
## stony_gorge_min
**Author:** None
**Date:**  None 

**Description:** Minimum flow requirement below Stony Gorge Reservoir which maintains flood space during winter and provides recreational flow for the rest of the year.

**Source:** [AppendixC-Reservoir_Operations_ModelingTechnical (PDF)](https://cadwr.box.com/s/bb3eeoloy7zwkvlsk4sc9b17j0k7cd3z)

## Stony_Gross_Res
## swp_3_tablea
**Author:** None
**Date:**  None 

**Description:** Table A contract amounts based on demand profile (30, 50, 60 and 100 percent).

**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (Excel)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## swp_3pattern_demands
**Author:** None
**Date:**  None 

**Description:** SWP contractor demand based on month, demand profile, and remaining demand for each contractor.  

**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (Excel)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## swp_3pattern_SLRule_new
**Author:** None
**Date:**  None 

**Description:** This table contains a distribution of deliveries for use with SWP Rule Curve determination  

**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (Excel)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## swp_art21_ann_max
**Author:** None
**Date:**  None 

**Description:** Annual Article 21 demands were calculated by using the maximum of these data sources: 
1) Article 21 historical deliveries 2005-2018 - take annual maximum delivery for each contractor
2) Article 21 historical requests 2011,2017,2019 - take annual maximum request for each contractor
3) Contractor stated annual maximums

Then, scale up the annual demand from historical delivery or request by 20% to act as a buffer in future studies where more article 21 opportunities (Not done to contractor specified values)		

**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (Excel)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## SWP_Butt_Alloc
**Author:** None
**Date:**  None 

**Description:** Determine Butte County allocation which is based on SWP South-of-Delta allocation.  This provided in Section 1.a of the Settlement Agreement in Principle for Butte allocations.  Allocations are linearly interpolated.

Example: Assume the SOD Allocation is 39%. To interpolate between 35% and 40% to get an allocation of 39%:
39% = 0.65 + (4/5)(0.70 - 0.65) = 0.65 or 65% allocation: (27,500)(0.69) = 18,975 AF

**Source:** [SWP Supply Allocation Settlement Agreements (PDF)](https://cadwr.box.com/s/py1ct1tufhhppiaeguwskonomk0dstiz)

## swp_carryover
**Author:** None
**Date:**  None 

**Description:** SWP carryover amounts based on demand profile (30, 50, 60 and 100 percent)  

**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (Excel)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## swp_limits
**Author:** None
**Date:**  2/6/2024 

**Description:** Represents monthly operational availability limits applied to SWP pumping facilities. Previous limits were based on SWP outages (planned and unplanned from 2001 - 2006). Updated to reflect more recent SWP outage occurances. Limits are taken from Table 1 ("Recommmended") under the tab
"Hunt Review." Monthly limits in the spreadsheet table are ordered by calendar year (January - December) and when transfering to the lookup, were reordered by wateryear (October - September).

**Source:** [Plant OA Summary for CalSIM scenarios (Excel)](https://cadwr.box.com/s/qjsx7jn32vltu8cjtzdwzoyjd34ibtl1)

## SWP_NOD_Alloc
**Author:** None
**Date:**  None 

**Description:** North-of-Delta SWP allocations for SCWA, Napa, and Yuba City based on water year types (Sacramento Valley 40-30-30 index). Allocations are proposed under the settlement agreement.

**Source:** [SWP Supply Allocation Settlement Agreements (PDF)](https://cadwr.box.com/s/py1ct1tufhhppiaeguwskonomk0dstiz)

## swp_table_a
**Author:** None
**Date:**  None 

**Description:** Table A entitlement for SWP contractors.

**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (Excel)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## swprule_cap_oroville
## swprule_deltar
## swprulecv_params
**Author:** None
**Date:**  None 

**Description:** Evaporation and loss amount (from timeseres for SWP delivery losses and San Luis evaporation) taken from timeseries (Oct 1921 - Mar 1923) and converted to TAF.

**Source:** [SWP Demands table (Excel)](https://cadwr.box.com/s/9bckxln3scvogee2xcegmdyc6krp4hl1)

## TableA
**Author:** None
**Date:**  None 

**Description:** Total SWP entitlements for Agricultural, Municipal & Industrial (MI) for MWD, MI (non-MWD) and losses (from conveyance) in TAF.

**Source:** [FIXED_BST_SWP_SOD_2021DCR_Oct2021_Public (Excel)](https://cadwr.box.com/s/xcbfnnvqr0hz9kxfxb3vgf0q9ij9pv0k)

## tcca_per
## TCGCIntertie
## TracyLimits
**Author:** None
**Date:**  None 

**Description:** Tracy (Jones) pumping plant permitted capacity and physical capacity. Permit capacity set by D-1641; Physical capacity source: Jones Pumping Plant Reclamation Fact Sheet; Discussed in Appendix 5.A. CalSim II Modeling Results Report Section 5.A.5.1.2.2 (Page 5.A-16).

**Source:** [app_5A_CalSim (PDF)](https://cadwr.box.com/s/9s291wa9phu01b5tz2b71rzuyebhusju)

## TrinFactor
**Author:** None
**Date:**  None 

**Description:** This is the 369-815 taf/yr Trinity minimum required flow based on the Trinity River index.

**Source:** [app_5A_CalSim (PDF)](https://cadwr.box.com/s/9s291wa9phu01b5tz2b71rzuyebhusju)

## TrinImportMonthly
## trinity_import
## Trinitymin
## TrinMinFlow_Forecast
## TrinOffSeason
## TuolAllocNormal
## Tuolumne_LaGrangeFERC
## Tuolumne_ResInfo
## UARPmif_BSH002
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for Brush Creek below Brush Creek Reservoir (FERC Project No. 2101-084).  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_GRL001
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for Gerle Creek below Gerle Creek Reservoir Dam under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_GRL010
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for Gerle Creek below Loon Lake Reservoir under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_LRB003
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for Little Rubicon River below Buck Island Reservoir under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_RUB044
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for Rubicon River below Rubicon Reservoir Dam under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_SFA039
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for South Fork American River below Slab Creek Reservoir under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_SFR006
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for South Fork Rubicon below Robbs Peak Reservoir under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_SLV005
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for Silver Creek below Junction Reservoir under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_SLV014
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for Silver Creek below Junction Reservoir under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UARPmif_SSV013
**Author:** None
**Date:**  None 

**Description:** Minimum streamflow requirements for South Fork Silver Creek below Ice House Reservoir under the provisions of FERC Project No. 2101-084.  Flow requirements are based on month and water year type. The minimum streamflow schedules have been separated into five water year types: Wet, AN, BN, Dry, and CD. They are based on the amount of unimpaired flow below Folsom Reservoir (abbreviated here as "UBFR"), where:

- Wet: UBFR greater than or equal to 3.500 Million Acre-Feet (MAF)
- AN: UBFR greater than or equal to 2.600 MAF but less than 3.500 MAF
- BN: UBFR greater than or equal to 1.700 MAF but less than 2.600 MAF
- Dry: UBFR greater than or equal to 0.900 MAF but less than 1.700 MAF
- Critical: UBFR less than 0.900 MAF

EOM terms are summation of minimum flows from January to May (each of the five year types has this term) to develop forecast amounts to determine future water availability.

**Source:** [ferc_p2101_upper_american (PDF)](https://cadwr.box.com/s/o48vdacl0xu6r9cnouylxwb8vgt8spqg)

## UF_DavisMinFlow
## UF_FERC_GZL008
**Author:** None
**Date:**  None 

**Description:** Grizzly Creek Minimum Instream Flow Requirements Below Grizzly Forebay by Water Year Type (in cfs) under provisions of FERC Project No. 619. Water years are categorized into four water year types based on inflow to Lake Oroville: Wet, Normal, Dry, and Critically Dry. The year types are defined as:

- Wet: Inflow greater than or equal to 5,679 thousand acre-feet (TAF) at Oroville;
- Normal: Inflow less than 5,679 TAF but greater than or equal to 3,228 TAF at Oroville;
- Dry: Inflow less than 3,228 TAF but greater than or equal to 2,505 TAF at Oroville; and
- Critical Dry: Inflow less than 2,505 TAF at Oroville.

**Source:** [bucks_wqc (PDF)](https://cadwr.box.com/s/psfschbx4k08p3d02giusctj7ki6mo3a)

## UF_FERC_LBUCK
**Author:** None
**Date:**  None 

**Description:** Grizzly Creek minimum instream flow requirements below Lower Buck Dam by Water Year Type (in cfs) under provisions of FERC Project No. 619. Water years are categorized into four water year types based on inflow to Lake Oroville: Wet, Normal, Dry, and Critically Dry. The year types are defined as:

- Wet: Inflow greater than or equal to 5,679 thousand acre-feet (TAF) at Oroville;
- Normal: Inflow less than 5,679 TAF but greater than or equal to 3,228 TAF at Oroville;
- Dry: Inflow less than 3,228 TAF but greater than or equal to 2,505 TAF at Oroville; and
- Critical Dry: Inflow less than 2,505 TAF at Oroville.

**Source:** [bucks_wqc (PDF)](https://cadwr.box.com/s/psfschbx4k08p3d02giusctj7ki6mo3a)

## UF_FERC_NFF035
## UF_FERC_NFF046
## UF_FERC2105
**Author:** Puneet Khatavkar, Stantec
**Date:**  01/08/21 

**Description:** Minimum Instream Flow Requirements (from FERC Project No. 2105) for: 

- 1. North Fork Feather River Flows below Canyon Dam (Almanor Reervoir)
- 2. North Fork Feather River Flows below Belden Dam 

Water years are categorized into four water year types based on inflow to Lake Oroville: Wet, Normal, Dry, and Critically Dry. The year types are defined as:

- Wet: Inflow greater than or equal to 5,679 thousand acre-feet (TAF) at Oroville;
- Normal: Inflow less than 5,679 TAF but greater than or equal to 3,228 TAF at Oroville;
- Dry: Inflow less than 3,228 TAF but greater than or equal to 2,505 TAF at Oroville; and
- Critical Dry: Inflow less than 2,505 TAF at Oroville.

**Source:** [unffr_appx_a (PDF)](https://cadwr.box.com/s/chfd2mihjh31j2mn6ovdgvnvi00ylw9z)

## UF_MFFDelivery
## UF_P2088minflow
**Author:** None
**Date:**  None 

**Description:** Minimum instream flow requirements for the South Fork Feather River below Little Grass Valley Dam based on the month and water year type.  based on the forecast of unimpaired runoff in the Feather River at Oroville.
The water year type definitions are:

- Wet: Flow greater than or equal to 7.1 million acre-feet (MAF)
- AN: Flow greater than or equal to 4.0 MAF but less than 7.1 MAF
- BN: Flow greater than 2.4 MAF but less than 4.0 MAF
- Dry: Flow less than or equal to 2.4 MAF

**Source:** [final_south_feather_wqc_2018_11_30 (PDF)](https://cadwr.box.com/s/xw16gm38hq8aticr65nqdfi4z2g3w5pg)

## UF_res_info
**Author:** None
**Date:**  None 

**Description:** Area-capacity curves for Upper Feather reservoirs.  

**Source:** [ER_UpperFeather (Excel)](https://cadwr.box.com/s/t160c7juv4614nv8jp43q6yae77kpxks)

## UF_res_level
## UF_SFFres_level
## UrbanMinMaxGW
**Author:** None
**Date:**  None 

**Description:** Minimum and maximum amounts of groundwater pumping for demand unit. Values are expressed as fraction of urban water demand.  

**Source:** [CS3_VolI_12_UrbanWaterUse_clean. (DOC)](https://cadwr.box.com/s/o7khhzv8zk1cq20pwwf4sdzyxwawe820)

## USJRS_FP_REQ
## Vern_WQ_std
## VernMin
**Author:** None
**Date:**  None 

**Description:** Vernalis Minimum flows for Feb thru Jun. East and West dependant on X2 position in relation to Chipps Is.  The larger flow objective is taken if X2 must be west of Chipps Is. 

**Source:** [Delta_Standards (modified) (PDF)](https://cadwr.box.com/s/sp1gpydb5d9q8aw6l5nf445h6r6tqtvt)

## WaterRightAmounts
**Author:** None
**Date:**  None 

**Description:** Annual water rights amounts for North-of-Delta (in TAF).  Some amounts include CVP contract amounts (see notes in table). The table includes non-project agricultural diversions from the Sacramento River (Table 14-13 in source document).


**Source:** [CS3_VolI_14_ContractsAndWaterRights_clean_updated (DOC)](https://cadwr.box.com/s/huos58q5afsr4gb6qucucxia9fsjr2u2)

## WatershedAreaPpt
## WetlandMinMaxGW
**Author:** None
**Date:**  None 

**Description:** Minimum and maximum amounts of groundwater pumping for demand unit. Values are expressed as fraction of applied water demand.

**Source:** [CS3_VolI_13_WetlandWaterUse_clean (PDF)](https://cadwr.box.com/s/yq0ks4qom85k8sb1eja9yr86061ik5h5)

## WheelCap
**Author:** None
**Date:**  None 

**Description:** SWP can use available Banks capacity to wheel water for CVP through the Joint Point of Diversion which has no limit.  Table represents this as a large number, "99999" under "cap."

**Source:** [Final DCR 2019 Technical Addendum (PDF)](https://cadwr.box.com/s/ct4rn6p1qg0l3djytseejn67imeq8pdk)

## WIIN_wetness
**Author:** None
**Date:**  None 

**Description:** Table may no longer be used by the model.

**Source:** 
## WSI_CVP_NODAG
## wsi_di_CVP_SYS
**Author:** None
**Date:**  None 

**Description:** Generated by model
**Source:** 

## wsi_di_SWP_SYS
## WTS_JobControl

 Sacramento Valley Water Management Agreement (SVWMA)

## WTS_Patterns
## WTS_Stage1_Targets
## wwtp_factors
## wytype_SJRR
## x2days_chs
**Author:** None
**Date:**  None 

**Description:** Number of days when maximumu daily average electrical conductivity (EC) of 2.64 mmhos/cm Must Be Maintained at Chipps Is.

**Source:** [D1641rev (PDF)](https://cadwr.box.com/s/1gd2229l39ca7xj60be3ocvzo0jg7mit)

## x2days_roe
**Author:** None
**Date:**  None 

**Description:** Number of days when maximumu daily average electrical conductivity (EC) of 2.64 mmhos/cm Must Be Maintained at Roe Is.

**Source:** [D1641rev (PDF)](https://cadwr.box.com/s/1gd2229l39ca7xj60be3ocvzo0jg7mit)

## xchanneldays
**Author:** None
**Date:**  None 

**Description:** Number of days the Delta Cross Channel gates are open to help augment flow through the interior of the Delta (and to the pumps).

**Source:** [D1641rev (PDF)](https://cadwr.box.com/s/1gd2229l39ca7xj60be3ocvzo0jg7mit)

## Yuba_carryover
## Yuba_contracts
**Author:** None
**Date:**  None 

**Description:** Yuba Water Agency contracts and water rights amounts for member districts.  Diversion points include:  Brophy ID, South Yuba ID, Dry Creek MWC, Cordua ID, and City of Marysville.

**Source:** [CS3_VolI_14_ContractsAndWaterRights_clean_updated (DOC)](https://cadwr.box.com/s/huos58q5afsr4gb6qucucxia9fsjr2u2)

## Yuba_LowerYubaMinflow
**Author:** None
**Date:**  None 

**Description:** Minimum flow requirements at Smartville and Marysville according to water year types based on the Yuba River Index.

Yuba River Index = 0.5X + 0.3Y + 0.2Z

Where:

- X = Current year’s April-July Yuba River unimpaired runoff
- Y = Current year’s October-March Yuba River unimpaired runoff
- 5Z = Previous year’s index
	
Classification Index Thousand Acre-Feet (TAF)
- Wet: Equal to or greater than 1,230
- Above Normal:  Greater than 990 and less than 1,230
- Below Normal: Equal to or less than 990 and greater than 790
- Dry: Equal to or less than 790 and greater than 630
- Critical: Equal to or less than 630

**Source:** [Appendix D-Modeling Technical Memorandum (PDF)](https://cadwr.box.com/s/xwyhz0j8b58cecf1qkli1afurjeyotsb)

## Yuba_min_FERC2246
**Author:** Megan Lionberger, HDR
**Date:**  04/20/16 

**Description:** Minimum streamflow (or natural flow, whichever is less) on Middle Yuba below Our House Diversion Dam, Oregon Creek below Log Cabin Diversion Dam, and North Yuba River below New Bullards Bar Dam. As specified in the Yuba River Development Project (FERC No. 2246-06) Flows are dependent on water year type

Water year type refers to the Existing FERC Year Type, flow values are in units of CFS
! 
Existing FERC Year Type is based on the April 1 forecast of % of average unimpaired runoff in the Yuba River at Smartsville

- 1 (A) = 50-100% of April-1 average
- 2 (B) = 45-50% of April-1 average 
- 3 (C) = 40-45% of April-1 average 
- 4 (D) < 40% of April-1 average   

**Source:** [01-02-19-FEIS (PDF)](https://cadwr.box.com/s/dqbcqpc2mian07mm4tyytm4wkhv5ymcm)

## Yuba_min_FERC2246_WQC
**Author:** Puneet Khatavkar, Stantec
**Date:**  01/14/21 

**Description:** Minimum streamflow (or natural flow, whichever is less) on Middle Yuba below Our House Diversion Dam, Oregon Creek below Log Cabin Diversion Dam, and North Yuba River below New Bullards Bar Dam. Based on the YCWA Yuba River Development Project (FERC 2246).

Water year types is based on unimpaired inflows at Smartville (cfs).

Where: 	

- Critically Dry: Inflows are Equal to or Less than 900			
- Dry:  Inflows are between 901 to 1,460	              	
- Below Normal:  Inflows are between 1,461 to 2,190    			
- Above Normal:  Inflows are between 2,191 to 3,240    			
- Wet:  Inflows are greater than 3,240                 


**Source:** [01-02-19-FEIS (PDF)](https://cadwr.box.com/s/dqbcqpc2mian07mm4tyytm4wkhv5ymcm)

## Yuba_min_FERC2266
**Author:** Megan Lionberger, HDR
**Date:**  04/20/16 

**Description:** Minimum streamflow on Middle Yuba River below Jackson Meadows Dam, Middle Yuba River below Milton Diversion Dam, and Canyon Creek below Bowman-Spaulding Diversion Dam. Based on the FERC license for the NID Yuba-Bear Project (FERC 2266).

**Source:** [yb_wqc (PDF)](https://cadwr.box.com/s/unf7ipc8l4hb5gaavlupu3k0bgogo9qp)

## yuba_min_FERC2266_WQC
**Author:** Puneet Khatavkar, Stantec
**Date:**  01/12/20 

**Description:** Minimum streamflow on Middle Yuba River below Jackson Meadows Dam, Middle Yuba River below Milton Diversion Dam, and Canyon Creek below Bowman-Spaulding Diversion Dam.  Based on new Water Quality Certification for the NID Yuba-Bear Project (FERC 2266) issued in August 2020.

**Source:** [yb_wqc (PDF)](https://cadwr.box.com/s/unf7ipc8l4hb5gaavlupu3k0bgogo9qp)

## Yuba_min_FERC2310
**Author:** Megan Lionberger, HDR
**Date:**  04/20/16 

**Description:**  Minimum streamflow on Fordyce Creek below Fordyce Dam, and South Yuba River below Spaulding Dam. Based on the old FERC license for the PG&E Drum-Spaulding Project (FERC 2310).

**Source:** [pge_annotated0507 (PDF)](https://cadwr.box.com/s/qepfqezzaoqqysxbp7ad37t0m54ybs4m)
## YubaBear_Res_info
**Author:** None
**Date:**  None

**Description:**  Area-capacity curves for reservoirs in the Yuba-Bear region.

**Source:** [ER_YubaBear (Excel)](https://cadwr.box.com/s/fr4alx0zhw00wj9qwpn7nvio8v7m8tds)

## YubaCityContractAmounts
**Author:** None
**Date:**  None

**Description:**  Yuba City’s existing surface water sources include two appropriative water rights, State Water Resources Control Board Permits 14045 and 18558 and two water supply contracts with 
Yuba City Water District (YCWD) for 4.5 TAF per annum and with the Departent of Water Resources, State Water Project for 9.6 TAF per annum.


**Source:** [urban-water-management-plan (PDF)](https://cadwr.box.com/s/08pk32creoqsyajxbdycelu0kyeweh79)


