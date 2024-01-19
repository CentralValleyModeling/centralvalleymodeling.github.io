# Common CalSim 3 Output Variables

## Sacramento River Basin boundary conditions

|CalSim 3 Variable|Kind|Description|
|---|---|---|
|S_TRNTY|STORAGE|Trinity storage
|C_LWSTN           |     CHANNEL            | Trinity River
|D_LWSTN_CCT011    |            DIVERSION   | Clear Creek Tunnel Diversion
|C_LWSTN_MIF       |     FLOW-MIN-INSTREAM  | Trinity River minimum instream flow
|D_WKYTN_SPT003    |              DIVERSION | Spring Creek Tunnel Diversion
|S_SHSTA           |       STORAGE          | Shasta Storage
|C_SHSTA           |       CHANNEL          | Sacramento River below Shasta
|C_KSWCK           |       CHANNEL          | Sacramento River below Keswick
|C_KSWCK_MIF       |       FLOW-MIN-INSTREAM| Sacramento River minimum instream flow below Keswick
|C_SAC240          |      CHANNEL           | Sacramento River downstream of Red Bluff Diversion Dam
|C_SAC240_MIF      |      FLOW-MIN-INSTREAM | Sacramento River minimum instream flow downstream of Red Bluff Diversion Dam
|C_SAC097          |      CHANNEL           | Sacramento River at NCP
|C_SAC097_MIF      |      FLOW-MIN-INSTREAM | Sacramento River minimum instream flow at NCP
|S_OROVL           |       STORAGE          | Oroville Storage
|C_FTR068          |     CHANNEL            |Feather River downstream of Thermalito Diversion Dam
|C_FTR068_MIF      |     FLOW-MIN-INSTREAM  | Feather River minimum instream flow downstream of Thermalito Diversion Dam
|C_FTR059          |      CHANNEL           | Feather River Below Thermalito Return
|C_FTR059_MIF      |      FLOW-MIN-INSTREAM | Feather River minimum instream flow Below Thermalito Return
|C_FTR003          |      CHANNEL           | Feather River near mouth
|C_FTR003_MIF      |      FLOW-MIN-INSTREAM | Feather River minimum instream flow near mouth
|S_FOLSM           |       STORAGE          | Folsom Storage
|C_NTOMA           |       CHANNEL          | American River below Nimbus
|C_NTOMA_MIF       |       FLOW-MIN-INSTREAM| American River minimum instream flow below Nimbus
|C_AMR004          |      CHANNEL           | American River below H Street
|C_AMR004_MIF      |      FLOW-MIN-INSTREAM | American River minimum instream flow below H Street
|C_SAC049          |      CHANNEL           | Sacramento River Downstream of American River (YC: this is actually Freeport)
|DEL_CVP_PAG_N     |  DELIVERY-CVP          | CVP NOD AG delivery
|DEL_CVP_PMI_N     |  DELIVERY-CVP          | CVP NOD M&I delivery
|DEL_CVP_PSC_N     |  DELIVERY-CVP          | CVP NOD Settlement delivery
|DEL_CVP_PRF_N     |  DELIVERY-CVP          | CVP NOD refuge delivery
|PERDV_CVPAG_SYS   |  PERCENT-DELIVERY      | CVP NOD AG percent delivery
|PERDV_CVPMI_SYS   |  PERCENT-DELIVERY      | CVP NOD M&I percent delivery
|PERDV_CVPRF_SYS   |  PERCENT-DELIVERY      | CVP NOD Refuge percent delivery
|PERDV_CVPSC_SYS   |  PERCENT-DELIVERY      | CVP NOD Settlement percent delivery


## San Joaquin River Basin boundary conditions
|CalSim 3 Variable|Kind|Description|
|---|---|---|
|C_SJR070              |  CHANNEL           | San Joaquin river at Vernalis
|S_MLRTN               |  STORAGE           | Millerton Storage
|D_MLRTN_FRK000        |  DIVERSION         | Friant-Kern Canal diversion at Friant
|D_MLRTN_MDC006        |  DIVERSION         | Madera Canal diversion at Friant
|C_MLRTN               |  CHANNEL           | Friant Release
|C_SJR205              | CHANNEL            | San Joaquin River flow below Bifurcation


## South of Delta (export area) boundary conditions
|CalSim 3 Variable|Kind|Description|
|---|---|---|
|DEL_CVP_PAG_S     |  DELIVERY-CVP          | CVP SOD AG delivery
|DEL_CVP_PMI_S     |  DELIVERY-CVP          | CVP SOD M&I delivery
|DEL_CVP_PEX_S     |  DELIVERY-CVP          | CVP SOD Exchange delivery
|DEL_CVP_PRF_S     |  DELIVERY-CVP          | CVP SOD refuge delivery
|DEL_CVP_PLS_S     |  DELIVERY-CVP          | CVP SOD losses
|DEL_CVP_TOTAL_S   |  DELIVERY-CVP          | Total CVP SOD delivery
|PERDV_CVPAG_S     |  PERCENT-DELIVERY      | CVP SOD AG percent delivery
|PERDV_CVPEX_S     |  PERCENT-DELIVERY      | CVP SOD Exchange percent delivery
|PERDV_CVPMI_S     |  PERCENT-DELIVERY      | CVP SOD M&I percent delivery
|PERDV_CVPRF_S     |  PERCENT-DELIVERY      | CVP SOD Refuge percent delivery
|DEL_SWP_MWD       |  DELIVERY-SWP          | SWP MWD delivery
|DEL_SWP_PAG_S     |  DELIVERY-SWP          | SWP SOD AG delivery
|DEL_SWP_OTH       |  DELIVERY-SWP          | SWP SOD M&I delivery
|DEL_SWP_PIN       |  DELIVERY-SWP          | SWP Article 21 delivery
|SWP_PERCENT_ACT   |  ALIAS                 | SWP percent delivery
|SWP_LOSS          |  SWP_DELIVERY          | SWP SOD Losses
|S_SLUIS_CVP       |  STORAGE               | CVP San Luis storage
|S_SLUIS_SWP       |  STORAGE               |SWP San Luis storage
|D_SLUIS_PCH000    |  DIVERSION             | CVP Santa Clara diversion
|C_SLUIS_CVP       |  CHANNEL               | CVP San Luis release
|C_SLUIS_SWP       |  CHANNEL               | SWP San Luis release
|S_DELVE           |  AGE                   | Del Valle storage
|S_CSTIC           |  STORAGE               | Castaic storage
|S_PYRMD           |  STORAGE               | Pyramid storage
|S_SVRWD           |  STORAGE               | Silverwood storage
|S_PRRIS           |  STORAGE               | Lake Perris storage
|E_SLUIS_CVP       |  EVAPORATION           | CVP San Luis evaporation
|E_SLUIS_SWP       |  EVAPORATION           | SWP San Luis evaporation
|E_DELVE           |  EVAPORATION           | Del Valle
|E_CSTIC           |  EVAPORATION           | Castaic
|E_PYRMD           |  EVAPORATION           | Pyramid
|E_SVRWD           |  EVAPORATION           | Silverwood
|E_PRRIS           |  EVAPORATION           | Lake Perris
|D607A             |  DIVERSION             | Mendota Pool diversion
|D607B             |  DIVERSION             | Mendota Pool diversion
|D_MDOTA_91_PR     |  DIVERSION             | Mendota Pool diversion
|D607D             |  DIVERSION             | Mendota Pool diversion
|R_91_PR_FSL005    |  RETURN-FLOW           | Mendota Pool return flow
|C_SJR205          |  CHANNEL               | SJR to Mendota Pool
|D_MLRTN_FRK000    |  DIVERSION             | FKC
|D_MLRTN_MDC006    |  DIVERSION             | MC
|D_SBA009_ACFC     |  FLOW-DELIVERY         | Alameda Co. FC&WCD, Zone 7
|D_SBA020_ACFC     |  FLOW-DELIVERY         | Alameda Co. FC&WCD, Zone 7
|D_SBA029_ACWD     |  FLOW-DELIVERY         | Alameda County WD
|D_SBA036_SCVWD    |  FLOW-DELIVERY         | SWP Santa Clara Valley WD
|D_ESB324_AVEK     |  FLOW-DELIVERY         | Antelope Valley-East Kern WA
|D_PCH000_SCVWD    |  DIVERSION             | CVP SCVWD

!!! Note 
    Derived Timeseries (South of Delta)
    CVP Exchange contract diversion from Mendota Pool:  
    D_MDOTA_64_XA + D_MDOTA_73_XA  

    Upper DMC diversion:  
    D_DMC011_71_PA8 + D_DMC016_WTPJJO + D_DMC021_50_PA1  

    Upper DMC diversion:   
    D_DMC064_71_PA6 + D_DMC054_NMW004 + D_DMC044_71_PA4 + D_DMC044_71_PA5 +D_DMC034_71_PA3 + D_DMC034_WWW001 + D_DMC034_71_PA2 + D_DMC030_71_PA1

## Delta boundary conditions
|CalSim 3 Variable|Kind|Description|
|---|---|---|
|C_SAC041               |CHANNEL                   | Sacramento River at Hood
|C_MOK019               |CHANNEL                   | Mokelumne River inflow to Delta
|C_SJR056               |CHANNEL                   | San Joaquin River inflow to Delta (include Calaveras) (YC: Does NOT include Calaveras)
|C_YBP020               |CHANNEL                   | Yolo Bypass inflow to Delta
|C_CLV004               |CHANNEL                   | CALAVERAS
|D_SAC030_MOK014        |DIVERSION                 | DXC
|C_SAC029B              |CHANNEL                   | Georgiana Sl
|C_CSL004B              |CHANNEL                   | NBA diversion from Delta
|C_DMC000               |CHANNEL                   | Total Tracy export from Delta
|C_CAA003               |CHANNEL                   | Total Banks export from Delta
|C_CAA003_SWP           |FLOW-DELIVERY             | Banks Export for SWP
|C_CAA003_CVC           |FLOW-DELIVERY             | Banks Export for CVC
|NDOI_MIN               |FLOW                      | MRDO
|BANKSALLOWOUT          |FLOW-ALLOW-BANKS          | Allowable Banks pumping
|TRACYALLOWOUT          |FLOW-ALLOW-TRACY              | Allowable Tracy pumping
|EXPRATIO_              |EI-RATIO-STD                  | Export/Inflow Ratio standard
|EXPORTACTUALTD         |EXPORT-PRJ                    | Total project exports, was EXPORTACTUAL
|EIEXPCTRL              |EXPORT-CTRL-EI                | Allowable export under E/I
|DXC                    |GATE-DAYS-OPEN                | Days per month DXC is open
|C_SAC017_ADD           |FLOW-ADDITIONAL-INSTREAM  | Flow at Rio Vista
|C_SAC017_MIF           |FLOW-MIN-INSTREAM         | Minimum instream flow at Rio Vista
|DeltaInflowforNDOI     |FLOW              | Delta inflow
|D_BKR004_NBA009        |DIVERSION           | NBA
|VERNWQFINAL            |SALINITY-EC                   | SJR at Vernalis
|DD_SAC017_SACS         |DIVERSION           | Delta CU
|DD_SJR026_SJRE         |DIVERSION           | Delta CU
|DD_MOK004_MOK          |DIVERSION            | Delta CU
|DD_SJR013_SJRW         |DIVERSION           | Delta CU
|UNUSED_FS              |UNUSED-FS                     | COA - Unused Federal Share
|UNUSED_SS              |UNUSED-SS                     | COA - Unused state Share
|UWFE                   |UWFE                          | COA - Unstored water for export
|IBU                    |IBU                           | COA - Inbasin use
|SWPDS                  |STORAGE-CHANGE                | COA - storage withdrawal
|SHADS                  |STORAGE-CHANGE                | COA - storage withdrawal
|FOLDS                  |STORAGE-CHANGE                | COA - storage withdrawal
|WHSSW                  |STORAGE-WDL                   | COA - storage withdrawal
|CVP_SHARE              |PERCENT-COA                   | COA - CVP share
|SWP_SHARE              |PERCENT-COA                   | COA - SWP share
|NDOI_ADD_CVP           |FLOW-CHANNEL              | COA - CVP share of outflow
|NDOI_ADD_SWP           |FLOW-CHANNEL              | COA - SWP share of outflow
|D_SAC050_FPT013        |DIVERSION          | COA - Freeport diversion project
|NDOI_ADD               |FLOW                      | surplus delta outflow (flow above flow standard)
|D_DMC007_CAA009        |DIVERSION             | DMC intertie
|JP_MRDO                |FLOW                  | ANN MRDO
|EM_MRDO                |FLOW                  | ANN MRDO
|RS_MRDO_1              |FLOW                  | ANN MRDO
|RS_MRDO_2              |FLOW                  | ANN MRDO
|RS_MRDO_3              |FLOW                  | ANN MRDO
|CO_MRDO                |FLOW                  | ANN MRDO
|!B2ACTION2ON__Z3       |TRIGGER               | b2 -  Exp. Red. (D-J)
|!B2ACTION3ON__Z3       |TRIGGER               | b2 -  VAMP Exp.R.
|!B2ACTION4ON__Z3       |TRIGGER               | b2 -  Post VAMP
|!B2ACTION5ON__Z3       |TRIGGER               | b2 -  Exp. Ramping
|!B2ACTION6ON__Z3       |TRIGGER               | b2 -  Pre Vamp
|!B2ACTION7ON__Z3       |TRIGGER               | b2 -  Exp. Red.

!!! Note 
Derived Timeseries (Delta)
CCWD diversion from Delta:  
D_OMR021_ORP000 + D_VCT002_ORP000

Upper DMC diversion:  
D_DMC011_71_PA8 + D_DMC016_WTPJJO + D_DMC021_50_PA1

Upper DMC diversion:  
D_DMC064_71_PA6 + D_DMC054_NMW004 + D_DMC044_71_PA4 + D_DMC044_71_PA5 +D_DMC034_71_PA3 + D_DMC034_WWW001 + D_DMC034_71_PA2 + D_DMC030_71_PA1  

Upper DMC diversion - loss:  
D_DMC064_DMCLOS + D_DMC058_DMCLOS + D_DMC054_DMCLOS + D_DMC049_DMCLOS + D_DMC044_DMCLOS +  D_DMC039_DMCLOS + D_DMC034_DMCLOS + D_DMC030_DMCLOS + D_DMC024_DMCLOS + D_DMC021_DMCLOS + D_DMC016_DMCLOS + D_DMC011_DMCLOS

## CalSim input
|CalSim 3 Variable|Kind|Description|
|---|---|---|
|I_SHSTA                 |INFLOW            | Shasta inflow
|I_OROVL                 |INFLOW            | Oroville inflow
|I_FOLSM                 |INFLOW            | Folsom inflow
|S_SHSTALEVEL5DV         |STORAGE-LEVEL     | Shasta flood control limits (YC: no longer in SV, calculated dynamically)
|S_OROVLLEVEL5           |STORAGE-LEVEL     | Oroville flood control limits
|S_FOLSMLEVEL5           |STORAGE-LEVEL     | Folsom flood control limits
|I_MSH015                |INFLOW            | marsh creek
|DRN_SAC_SOUTH           |DRN               | delta precip
|DRN_SJR_WEST            |DRN               | delta precip
|DRN_SJR_East            |DRN               | delta precip
|DRN_MOK                 |DRN               | delta precip
|I_JBP006                |INFLOW            | JBP to Mendota Pool
|I_MLRTN                 |INFLOW            | Millerton Inflow
|I_CAA245                |FLOW-INFLOW       | Kern River intertie