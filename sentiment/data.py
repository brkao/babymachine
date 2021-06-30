'''includes US stock symbols with market cap > 100 Million, and price above $3.
Download the csv file  https://www.nasdaq.com/market-activity/stocks/screener?exchange=nasdaq&letter=0&render=download
of all the NYSE, NASDAQ and NYSEAMERICAN public traded companies.
'''
us = {'AA','AACG','AACQ','AAIC','AAL','AAME','AAN','AAOI','AAON','AAP','AAPL','AAT','AAU','AAWW','AB','ABB','ABBV','ABC','ABCB','ABCL','ABCM','ABEO','ABEV','ABG','ABGI','ABIO','ABM','ABMD','ABNB','ABR','ABST','ABT','ABTX','ABUS','AC','ACA','ACAC','ACAD','ACB','ACBI','ACC','ACCD','ACCO','ACEL','ACET','ACEV','ACGL','ACH','ACHC','ACHV','ACI','ACIC','ACII','ACIU','ACIW','ACLS','ACM','ACMR','ACN','ACNB','ACND','ACP','ACR','ACRE','ACRS','ACRX','ACST','ACTC','ACTG','ACU','ACV','ACVA','ADAG','ADAP','ADBE','ADC','ADCT','ADER','ADES','ADI','ADM','ADMA','ADMP','ADMS','ADN','ADNT','ADOC','ADP','ADPT','ADRA','ADS','ADSK','ADT','ADTN','ADUS','ADV','ADVM','ADX','ADXN','ADXS','AE','AEE','AEF','AEG','AEGN','AEHR','AEI','AEIS','AEL','AEM','AENZ','AEO','AEP','AER','AERI','AES','AESE','AEVA','AEYE','AEZS','AFB','AFCG','AFG','AFI','AFIB','AFIN','AFL','AFMD','AFRM','AFT','AFYA','AG','AGAC','AGBA','AGC','AGCB','AGCO','AGD','AGE','AGEN','AGFS','AGFY','AGI','AGIO','AGLE','AGM','AGMH','AGNC','AGO','AGR','AGRO','AGRX','AGS','AGTC','AGX','AGYS','AHAC','AHCO','AHH','AHT','AI','AIF','AIG','AIH','AIHS','AIKI','AIM','AIMC','AIN','AINV','AIO','AIR','AIRC','AIRG','AIRT','AIT','AIV','AIZ','AJAX','AJG','AJRD','AJX','AKAM','AKBA','AKER','AKIC','AKR','AKRO','AKTS','AKTX','AKU','AKUS','AL','ALAC','ALB','ALBO','ALC','ALCO','ALDX','ALE','ALEC','ALEX','ALG','ALGM','ALGN','ALGS','ALGT','ALHC','ALIM','ALJJ','ALK','ALKS','ALL','ALLE','ALLK','ALLO','ALLT','ALLY','ALNA','ALNY','ALOT','ALPN','ALRM','ALRN','ALRS','ALSK','ALSN','ALT','ALTA','ALTG','ALTM','ALTO','ALTR','ALTU','ALUS','ALV','ALVR','ALX','ALXN','ALXO','ALYA','AM','AMAL','AMAT','AMBA','AMBC','AMBO','AMC','AMCR','AMCX','AMD','AME','AMED','AMEH','AMG','AMGN','AMH','AMHC','AMK','AMKR','AMN','AMNB','AMOT','AMOV','AMP','AMPE','AMPG','AMPH','AMPY','AMR','AMRB','AMRC','AMRK','AMRN','AMRS','AMRX','AMSC','AMSF','AMST','AMSWA','AMT','AMTB','AMTBB','AMTI','AMTX','AMWD','AMWL','AMX','AMYT','AMZN','AN','ANAB','ANAT','ANDE','ANET','ANF','ANGI','ANGN','ANGO','ANIK','ANIP','ANIX','ANNX','ANPC','ANSS','ANTE','ANTM','ANVS','AOD','AON','AONE','AOS','AOSL','AOUT','AP','APA','APAM','APD','APDN','APEI','APEN','APG','APH','APHA','API','APLE','APLS','APLT','APM','APO','APOG','APPF','APPH','APPN','APPS','APR','APRE','APRN','APSG','APT','APTO','APTS','APTV','APTX','APVO','APWC','APXT','APYX','AQB','AQMS','AQN','AQST','AQUA','AR','ARAV','ARAY','ARBG','ARC','ARCB','ARCC','ARCE','ARCH','ARCO','ARCT','ARD','ARDC','ARDS','ARDX','ARE','AREC','ARES','ARGO','ARGX','ARI','ARKO','ARKR','ARL','ARLO','ARLP','ARMK','ARMP','ARNA','ARNC','AROC','AROW','ARPO','ARQT','ARR','ARRY','ARTNA','ARVN','ARW','ARWR','ARYA','ARYD','ASA','ASAN','ASAQ','ASB','ASC','ASG','ASGI','ASGN','ASH','ASIX','ASLE','ASLN','ASM','ASMB','ASML','ASND','ASO','ASPL','ASPN','ASPS','ASPU','ASR','ASRT','ASRV','ASTE','ASUR','ASX','ASXC','ASYS','AT','ATAC','ATAX','ATC','ATCO','ATCX','ATEC','ATEN','ATEX','ATGE','ATH','ATHA','ATHE','ATHM','ATHX','ATI','ATIF','ATKR','ATLC','ATLO','ATNF','ATNI','ATNM','ATNX','ATO','ATOM','ATOS','ATR','ATRA','ATRC','ATRI','ATRO','ATRS','ATSG','ATTO','ATUS','ATVI','ATXI','AU','AUB','AUBN','AUDC','AUMN','AUPH','AUTL','AUVI','AUY','AVA','AVAL','AVAN','AVAV','AVB','AVCO','AVCT','AVD','AVDL','AVEO','AVGO','AVGR','AVID','AVIR','AVK','AVLR','AVNS','AVNT','AVNW','AVO','AVRO','AVT','AVTR','AVXL','AVY','AVYA','AWF','AWH','AWI','AWK','AWP','AWR','AWRE','AX','AXDX','AXGN','AXL','AXLA','AXNX','AXON','AXP','AXR','AXS','AXSM','AXTA','AXTI','AXU','AY','AYI','AYLA','AYRO','AYTU','AYX','AZEK','AZN','AZO','AZPN','AZRE','AZRX','AZUL','AZYO','AZZ','BA','BABA','BAC','BAH','BAK','BALY','BAM','BANC','BAND','BANF','BANR','BANX','BAOS','BAP','BATL','BATRA','BATRK','BAX','BB','BBAR','BBBY','BBCP','BBD','BBDC','BBDO','BBF','BBGI','BBI','BBIO','BBL','BBN','BBQ','BBSI','BBU','BBVA','BBW','BBY','BC','BCAB','BCAC','BCAT','BCBP','BCC','BCDA','BCE','BCEI','BCEL','BCH','BCLI','BCML','BCO','BCOR','BCOV','BCOW','BCPC','BCRX','BCS','BCSF','BCTG','BCV','BCX','BCYC','BDC','BDJ','BDN','BDSI','BDSX','BDTX','BDX','BE','BEAM','BECN','BEDU','BEEM','BEKE','BELFA','BELFB','BEN','BENE','BEP','BEPC','BERY','BEST','BFAM','BFC','BFI','BFIN','BFK','BFLY','BFRA','BFS','BFST','BFY','BFZ','BG','BGB','BGCP','BGFV','BGH','BGI','BGIO','BGNE','BGR','BGS','BGSF','BGT','BGX','BGY','BH','BHB','BHC','BHE','BHF','BHK','BHLB','BHP','BHR','BHSE','BHVN','BIDU','BIF','BIG','BIGC','BIIB','BILI','BILL','BIO','BIOC','BIOL','BIOT','BIOX','BIP','BIPC','BIT','BIVI','BJ','BJRI','BK','BKCC','BKD','BKE','BKEP','BKH','BKI','BKN','BKNG','BKR','BKSC','BKT','BKTI','BKU','BL','BLBD','BLCT','BLD','BLDP','BLDR','BLE','BLFS','BLI','BLK','BLKB','BLL','BLMN','BLNK','BLRX','BLSA','BLTS','BLU','BLUA','BLUE','BLUW','BLW','BLX','BMA','BMBL','BME','BMEZ','BMI','BMO','BMRA','BMRC','BMRN','BMTC','BMTX','BMY','BNED','BNFT','BNGO','BNL','BNR','BNS','BNTX','BNY','BOAC','BOCH','BOE','BOH','BOKF','BOLT','BOMN','BOOM','BOOT','BORR','BOTJ','BOWX','BOX','BOXL','BP','BPFH','BPMC','BPMP','BPOP','BPRN','BPT','BPTS','BPY','BPYU','BQ','BR','BRBR','BRBS','BRC','BREZ','BRFS','BRG','BRID','BRKL','BRKR','BRKS','BRLI','BRMK','BRO','BROG','BRP','BRPA','BRQS','BRT','BRX','BRY','BSAC','BSBK','BSBR','BSD','BSE','BSET','BSGM','BSIG','BSL','BSM','BSMX','BSPE','BSRR','BST','BSTZ','BSVN','BSX','BSY','BTA','BTAI','BTAQ','BTAQU','BTBT','BTG','BTI','BTNB','BTO','BTRS','BTT','BTU','BTWN','BTZ','BUD','BUI','BUR','BURL','BUSE','BV','BVH','BVN','BVS','BVXV','BW','BWA','BWAC','BWAY','BWB','BWEN','BWFG','BWG','BWMX','BWXT','BX','BXC','BXG','BXMT','BXMX','BXP','BXRX','BXS','BY','BYD','BYFC','BYM','BYND','BYSI','BZH','BZUN','CAAP','CAAS','CABA','CABO','CAC','CACC','CACI','CADE','CAE','CAF','CAG','CAH','CAI','CAJ','CAKE','CAL','CALA','CALB','CALM','CALT','CALX','CAMP','CAMT','CAN','CANG','CAP','CAPA','CAPL','CAPR','CAR','CARA','CARE','CARG','CARR','CARS','CAS','CASA','CASH','CASI','CASS','CASY','CAT','CATB','CATC','CATM','CATO','CATY','CB','CBAH','CBAN','CBAT','CBAY','CBB','CBD','CBFV','CBH','CBIO','CBLI','CBNK','CBPO','CBRE','CBRL','CBSH','CBT','CBTX','CBU','CBZ','CC','CCAC','CCAP','CCB','CCBG','CCCC','CCD','CCEP','CCF','CCI','CCIV','CCJ','CCK','CCL','CCLP','CCM','CCMP','CCNC','CCNE','CCO','CCOI','CCRC','CCRN','CCS','CCU','CCV','CCX','CCXI','CD','CDAK','CDAY','CDE','CDEV','CDK','CDLX','CDMO','CDNA','CDNS','CDR','CDTX','CDW','CDXC','CDXS','CDZI','CE','CEA','CECE','CEE','CEIX','CELC','CELH','CEM','CEMI','CEN','CENT','CENTA','CENX','CEPU','CEQP','CERC','CERE','CERN','CERS','CERT','CET','CEV','CEVA','CF','CFAC','CFB','CFBK','CFFI','CFFN','CFG','CFIV','CFMS','CFR','CFRX','CFV','CFX','CG','CGBD','CGC','CGEM','CGEN','CGNT','CGNX','CGO','CGRO','CHAQ','CHCO','CHCT','CHD','CHDN','CHE','CHEF','CHEK','CHFW','CHGG','CHH','CHI','CHK','CHKP','CHMA','CHMG','CHMI','CHN','CHNG','CHNR','CHPM','CHPT','CHRA','CHRS','CHRW','CHS','CHT','CHTR','CHUY','CHW','CHWY','CHX','CHY','CI','CIA','CIB','CIDM','CIEN','CIG','CIGI','CIH','CII','CIK','CIM','CINF','CINR','CIO','CIR','CIT','CIVB','CIX','CIXX','CIZN','CKH','CKPT','CL','CLAR','CLB','CLBK','CLBS','CLDB','CLDR','CLDT','CLDX','CLF','CLFD','CLGN','CLGX','CLH','CLI','CLII','CLIR','CLLS','CLM','CLMT','CLNC','CLNE','CLNN','CLNY','CLOV','CLPR','CLPS','CLPT','CLR','CLRB','CLRM','CLRO','CLS','CLSD','CLSK','CLSN','CLVR','CLVS','CLVT','CLW','CLX','CLXT','CM','CMA','CMBM','CMC','CMCL','CMCM','CMCO','CMCSA','CMCT','CMD','CME','CMG','CMI','CMLF','CMLS','CMMB','CMO','CMP','CMPI','CMPR','CMPS','CMRE','CMRX','CMS','CMT','CMTL','CMU','CNA','CNBKA','CNC','CNCE','CNDT','CNET','CNEY','CNF','CNHI','CNI','CNK','CNMD','CNNE','CNO','CNOB','CNP','CNQ','CNR','CNS','CNSL','CNSP','CNST','CNTB','CNTG','CNTY','CNX','CNXC','CNXN','CO','COCP','CODA','CODI','CODX','COE','COF','COFS','COG','COGT','COHR','COHU','COKE','COLB','COLD','COLL','COLM','COMM','COMS','CONE','CONN','COO','COOL','COOP','COP','COR','CORE','CORR','CORT','COST','COTY','COUP','COUR','COWN','CP','CPA','CPAC','CPB','CPE','CPF','CPG','CPHC','CPK','CPLG','CPLP','CPNG','CPRI','CPRT','CPRX','CPS','CPSH','CPSI','CPSR','CPSS','CPST','CPT','CPUH','CQP','CR','CRAI','CRBP','CRC','CRCT','CRDF','CREE','CRESY','CRF','CRH','CRHC','CRHM','CRI','CRIS','CRK','CRKN','CRL','CRM','CRMD','CRMT','CRNC','CRNT','CRNX','CRON','CROX','CRS','CRSA','CRSP','CRSR','CRT','CRTO','CRTX','CRU','CRUS','CRVL','CRVS','CRWD','CRWS','CRY','CS','CSAN','CSBR','CSCO','CSCW','CSGP','CSGS','CSII','CSIQ','CSL','CSLT','CSOD','CSPR','CSQ','CSR','CSSE','CSTA','CSTE','CSTL','CSTM','CSTR','CSU','CSV','CSWC','CSWI','CSX','CTAC','CTAQ','CTAS','CTB','CTBI','CTG','CTHR','CTIC','CTK','CTLT','CTMX','CTO','CTR','CTRE','CTRM','CTRN','CTS','CTSH','CTSO','CTT','CTVA','CTXR','CTXS','CUB','CUBE','CUBI','CUE','CUK','CULP','CURI','CURO','CUTR','CUZ','CVA','CVAC','CVBF','CVCO','CVCY','CVE','CVEO','CVET','CVGI','CVGW','CVI','CVLG','CVLT','CVLY','CVM','CVNA','CVS','CVU','CVX','CW','CWBC','CWBR','CWCO','CWEN','CWH','CWK','CWST','CWT','CX','CXDC','CXDO','CXE','CXH','CXP','CXW','CYAD','CYBE','CYBR','CYCC','CYCN','CYD','CYH','CYRN','CYRX','CYTH','CYTK','CZNC','CZR','CZWI','DAC','DADA','DAKT','DAL','DAN','DAO','DAR','DARE','DASH','DAVA','DB','DBD','DBDR','DBI','DBL','DBTX','DBVT','DBX','DCBO','DCF','DCI','DCO','DCOM','DCP','DCPH','DCRB','DCT','DCTH','DD','DDD','DDF','DDMX','DDOG','DDS','DE','DEA','DECK','DEH','DEI','DELL','DEN','DENN','DEO','DESP','DEX','DFFN','DFH','DFHT','DFIN','DFNS','DFP','DFPH','DFS','DG','DGICA','DGICB','DGII','DGLY','DGNR','DGNS','DGNU','DGX','DHC','DHF','DHI','DHIL','DHR','DHT','DHX','DHY','DIAX','DIN','DIOD','DIS','DISCA','DISCB','DISCK','DISH','DIT','DJCO','DK','DKL','DKNG','DKS','DLA','DLB','DLCA','DLHC','DLNG','DLPN','DLR','DLTH','DLTR','DLX','DM','DMAC','DMB','DMF','DMLP','DMO','DMRC','DMS','DMTK','DMYD','DMYI','DNB','DNLI','DNMR','DNN','DNOW','DNP','DNZ','DOC','DOCN','DOCU','DOGZ','DOMO','DOOO','DOOR','DORM','DOV','DOW','DOX','DOYU','DPG','DPW','DPZ','DQ','DRD','DRE','DRH','DRI','DRIO','DRNA','DRQ','DRRX','DRTT','DRVN','DS','DSAC','DSEY','DSGN','DSGX','DSKE','DSL','DSM','DSP','DSPG','DSS','DSSI','DSU','DSWL','DSX','DT','DTE','DTEA','DTF','DTIL','DTSS','DUK','DUO','DVA','DVAX','DVD','DVN','DWIN','DWSN','DX','DXC','DXCM','DXPE','DY','DYAI','DYN','DZSI','EA','EAC','EAD','EAF','EAR','EARN','EAT','EB','EBAY','EBC','EBF','EBIX','EBMT','EBON','EBR','EBS','EBSB','EBTC','EC','ECC','ECF','ECHO','ECL','ECOL','ECOM','ECOR','ECPG','ED','EDAP','EDD','EDF','EDI','EDIT','EDN','EDSA','EDTX','EDTXU','EDU','EDUC','EEA','EEFT','EEX','EFC','EFF','EFL','EFR','EFSC','EFT','EFX','EGAN','EGBN','EGF','EGHT','EGLE','EGO','EGOV','EGP','EGRX','EGY','EH','EHC','EHI','EHT','EHTH','EIG','EIGR','EIM','EIX','EKSO','EL','ELA','ELAN','ELDN','ELF','ELLO','ELMD','ELOX','ELP','ELS','ELVT','ELY','ELYS','EMAN','EMCF','EMD','EME','EMF','EMKR','EML','EMN','EMO','EMPW','EMR','EMX','ENB','ENBL','ENDP','ENFA','ENG','ENIA','ENIC','ENLC','ENLV','ENOB','ENPC','ENPH','ENR','ENS','ENSG','ENTA','ENTG','ENTX','ENV','ENVA','ENVB','ENX','ENZ','EOD','EOG','EOI','EOLS','EOS','EOSE','EOT','EPAC','EPAM','EPAY','EPC','EPD','EPHY','EPIX','EPM','EPR','EPRT','EPSN','EPWR','EPZM','EQ','EQBK','EQC','EQD','EQH','EQHA','EQIX','EQNR','EQOS','EQR','EQT','EQX','ERC','ERES','ERF','ERH','ERIC','ERIE','ERII','ERJ','ERYP','ES','ESCA','ESE','ESEA','ESGC','ESGR','ESI','ESLT','ESNT','ESPR','ESQ','ESRT','ESS','ESSA','ESSC','ESTA','ESTC','ESTE','ESXB','ET','ETAC','ETB','ETG','ETH','ETJ','ETM','ETN','ETNB','ETO','ETON','ETR','ETRN','ETSY','ETTX','ETV','ETW','ETWO','ETX','ETY','EURN','EUSG','EVA','EVAX','EVBG','EVBN','EVC','EVER','EVF','EVFM','EVG','EVGN','EVH','EVI','EVLO','EVM','EVN','EVOK','EVOP','EVR','EVRG','EVRI','EVT','EVTC','EVV','EVY','EW','EWBC','EWTX','EXAS','EXC','EXD','EXEL','EXFO','EXG','EXK','EXLS','EXN','EXP','EXPC','EXPD','EXPE','EXPI','EXPO','EXPR','EXR','EXTN','EXTR','EYE','EYEN','EYES','EYPT','EZGO','EZPW','FAF','FAII','FAM','FANG','FANH','FARM','FARO','FAST','FAT','FATE','FAX','FB','FBC','FBHS','FBIO','FBIZ','FBK','FBMS','FBNC','FBP','FBRX','FBSS','FC','FCAC','FCAP','FCBC','FCBP','FCCO','FCCY','FCEL','FCF','FCFS','FCN','FCNCA','FCO','FCPT','FCRD','FCT','FCX','FDBC','FDEU','FDMT','FDP','FDUS','FDX','FE','FEDU','FEI','FEIM','FELE','FEN','FENC','FENG','FEO','FERG','FET','FEYE','FF','FFA','FFBC','FFBW','FFC','FFG','FFIC','FFIN','FFIV','FFNW','FFWM','FGB','FGBI','FGEN','FGNA','FHB','FHI','FHN','FHS','FHTX','FI','FIBK','FICO','FIF','FIII','FINM','FINS','FINV','FIS','FISI','FISV','FITB','FIV','FIVE','FIVN','FIX','FIXX','FIZZ','FL','FLAC','FLC','FLDM','FLEX','FLGT','FLIC','FLIR','FLL','FLMN','FLNG','FLNT','FLO','FLOW','FLR','FLS','FLT','FLUX','FLWS','FLXN','FLXS','FLY','FMAC','FMAO','FMBH','FMBI','FMC','FMN','FMNB','FMO','FMS','FMTX','FMX','FMY','FN','FNB','FNCB','FNCH','FND','FNF','FNHC','FNKO','FNLC','FNV','FNWB','FOCS','FOE','FOF','FOLD','FONR','FOR','FORM','FORR','FORTY','FOSL','FOUR','FOX','FOXA','FOXF','FOXW','FPAC','FPAY','FPF','FPH','FPI','FPL','FPRX','FR','FRA','FRAF','FRBA','FRBK','FRC','FRD','FREE','FREQ','FRG','FRGI','FRHC','FRLN','FRME','FRO','FROG','FRPH','FRPT','FRSX','FRT','FRTA','FRX','FSBW','FSD','FSEA','FSFG','FSII','FSK','FSKR','FSLF','FSLR','FSLY','FSM','FSP','FSR','FSRV','FSS','FSSI','FST','FSTR','FSTX','FSV','FT','FTAI','FTCH','FTCV','FTDR','FTEK','FTF','FTFT','FTHM','FTI','FTIV','FTK','FTNT','FTOC','FTS','FTSI','FTV','FUBO','FUL','FULC','FULT','FUN','FUNC','FUND','FURY','FUSB','FUSE','FUSN','FUTU','FUV','FVAM','FVCB','FVE','FVRR','FVT','FWAA','FWONA','FWONK','FWRD','FXNC','GAB','GABC','GAIA','GAIN','GALT','GAM','GAN','GANX','GASS','GATO','GATX','GAU','GB','GBAB','GBCI','GBDC','GBIO','GBL','GBLI','GBNH','GBOX','GBS','GBT','GBX','GCAC','GCBC','GCI','GCMG','GCO','GCP','GCV','GD','GDDY','GDEN','GDL','GDO','GDOT','GDP','GDRX','GDS','GDV','GDYN','GE','GECC','GEF','GEG','GEL','GENC','GENE','GEO','GEOS','GER','GERN','GES','GEVO','GF','GFED','GFF','GFI','GFL','GFN','GGAL','GGB','GGG','GGM','GGN','GGT','GGZ','GH','GHAC','GHC','GHG','GHL','GHLD','GHM','GHSI','GHVI','GHY','GIB','GIFI','GIII','GIK','GIL','GILD','GILT','GIM','GIS','GIX','GKOS','GL','GLAD','GLDD','GLDG','GLEO','GLG','GLMD','GLNG','GLO','GLOB','GLOG','GLOP','GLP','GLPG','GLPI','GLQ','GLRE','GLSI','GLT','GLTO','GLU','GLUU','GLV','GLW','GLYC','GM','GMAB','GMBL','GMBT','GMDA','GME','GMED','GMII','GMLP','GMRE','GMS','GMTX','GNCA','GNE','GNFT','GNK','GNL','GNLN','GNMK','GNOG','GNPK','GNPX','GNRC','GNRS','GNSS','GNT','GNTX','GNTY','GNUS','GNW','GO','GOAC','GOCO','GOED','GOEV','GOF','GOGL','GOGO','GOL','GOLD','GOLF','GOOD','GOOG','GOOGL','GOOS','GORO','GOSS','GP','GPAC','GPC','GPI','GPK','GPL','GPM','GPMT','GPN','GPP','GPRE','GPRK','GPRO','GPS','GPX','GRA','GRAY','GRBK','GRC','GRCL','GRCY','GRFS','GRIN','GRMN','GRNQ','GRNV','GROW','GROY','GRPN','GRSV','GRTS','GRTX','GRUB','GRVY','GRWG','GRX','GS','GSAH','GSAQ','GSAT','GSBC','GSBD','GSHD','GSIT','GSK','GSKY','GSL','GSM','GSMG','GSS','GSV','GSX','GT','GTBP','GTE','GTEC','GTES','GTH','GTHX','GTIM','GTLS','GTN','GTS','GTT','GTY','GTYH','GUT','GVA','GWAC','GWB','GWGH','GWPH','GWRE','GWRS','GWW','GXGX','HA','HAAC','HAE','HAFC','HAIN','HAL','HALL','HALO','HAPP','HARP','HAS','HASI','HAYN','HAYW','HBAN','HBB','HBCP','HBI','HBIO','HBM','HBMD','HBNC','HBP','HBT','HCA','HCAP','HCAQ','HCAT','HCC','HCCI','HCHC','HCI','HCKT','HCM','HCSG','HD','HDB','HDSN','HE','HEAR','HEC','HEES','HEI','HELE','HEP','HEPA','HEQ','HES','HESM','HEXO','HFBL','HFC','HFFG','HFRO','HFWA','HGBL','HGEN','HGLB','HGV','HHC','HHR','HI','HIBB','HIE','HIFS','HIG','HII','HIL','HIMS','HIMX','HIO','HIW','HIX','HJLI','HKIB','HL','HLAH','HLF','HLG','HLI','HLIO','HLIT','HLNE','HLT','HLX','HLXA','HMC','HMCO','HMHC','HMLP','HMN','HMNF','HMPT','HMST','HMSY','HMTV','HMY','HNGR','HNI','HNNA','HNP','HNRG','HNW','HOFT','HOFV','HOG','HOL','HOLI','HOLX','HOMB','HOME','HON','HONE','HOOK','HOPE','HOV','HP','HPE','HPF','HPI','HPK','HPP','HPQ','HPS','HPX','HQH','HQI','HQL','HQY','HR','HRB','HRC','HRI','HRL','HRMY','HROW','HRTG','HRTX','HRZN','HSAQ','HSBC','HSC','HSIC','HSII','HSKA','HST','HSTM','HSY','HT','HTA','HTBI','HTBK','HTBX','HTD','HTGC','HTH','HTHT','HTLD','HTLF','HTOO','HTPA','HTY','HUBB','HUBG','HUBS','HUDI','HUGE','HUIZ','HUM','HUN','HURC','HURN','HUYA','HVT','HWBK','HWC','HWCC','HWKN','HWM','HXL','HY','HYB','HYFM','HYI','HYLN','HYMC','HYRE','HYT','HYW','HZAC','HZN','HZNP','HZO','HZON','IAA','IAC','IACA','IAE','IAF','IAG','IART','IBA','IBCP','IBEX','IBIO','IBKR','IBM','IBN','IBOC','IBP','IBRX','IBTX','ICAD','ICBK','ICCC','ICE','ICFI','ICHR','ICL','ICLK','ICLR','ICMB','ICPT','ICUI','ID','IDA','IDBA','IDCC','IDE','IDEX','IDN','IDRA','IDT','IDXX','IDYA','IEA','IEC','IEP','IESC','IEX','IFF','IFN','IFRX','IFS','IGA','IGAC','IGC','IGD','IGI','IGIC','IGMS','IGR','IGT','IH','IHC','IHD','IHG','IHIT','IHRT','IHTA','IIAC','IIF','III','IIIN','IIIV','IIM','IIN','IIPR','IIVI','IKNA','IKT','ILMN','ILPT','IMAB','IMAX','IMBI','IMCC','IMCR','IMGN','IMKTA','IMMP','IMMR','IMNM','IMO','IMOS','IMPX','IMRA','IMTX','IMUX','IMV','IMVT','IMXI','INBK','INBX','INCY','INDB','INDT','INFI','INFN','INFO','INFU','INFY','ING','INGN','INGR','INKA','INMB','INMD','INN','INNV','INO','INOD','INOV','INPX','INS','INSE','INSG','INSI','INSM','INSP','INSW','INT','INTC','INTG','INTT','INTU','INTZ','INUV','INVA','INVE','INVH','INZY','IONS','IOSP','IOVA','IP','IPA','IPAR','IPG','IPGP','IPHA','IPHI','IPI','IPOD','IPOE','IPOF','IPWR','IQ','IQI','IQV','IR','IRBT','IRCP','IRDM','IRIX','IRL','IRM','IRMD','IROQ','IRR','IRS','IRT','IRTC','IRWD','ISBC','ISD','ISDR','ISEE','ISR','ISRG','ISSC','ISTR','ISUN','IT','ITAC','ITCB','ITCI','ITGR','ITI','ITIC','ITMR','ITOS','ITP','ITRG','ITRI','ITRM','ITRN','ITT','ITUB','ITW','IVA','IVAC','IVAN','IVC','IVH','IVR','IVZ','IX','IZEA','JACK','JAGX','JAMF','JAX','JAZZ','JBGS','JBHT','JBL','JBLU','JBSS','JBT','JCE','JCI','JCIC','JCO','JCOM','JCS','JD','JDD','JEF','JELD','JEMD','JEQ','JFIN','JFR','JFU','JG','JGH','JHAA','JHB','JHG','JHI','JHS','JHX','JIH','JILL','JJSF','JKHY','JKS','JLL','JLS','JMIA','JMM','JMP','JNCE','JNJ','JNPR','JOAN','JOBS','JOE','JOF','JOUT','JP','JPC','JPI','JPM','JPS','JPT','JQC','JRI','JRO','JRS','JRSH','JRVR','JSD','JT','JTA','JTD','JWEL','JWN','JWS','JYAC','JYNT','KAI','KALA','KALU','KALV','KAMN','KAR','KB','KBAL','KBH','KBNT','KBR','KC','KDMN','KDNY','KDP','KE','KELYA','KELYB','KEN','KEP','KERN','KEX','KEY','KEYS','KF','KFFB','KFRC','KFS','KFY','KGC','KHC','KIDS','KIM','KIN','KINS','KINZ','KIO','KIQ','KIRK','KKR','KL','KLAC','KLAQ','KLDO','KLIC','KLR','KLXE','KMB','KMDA','KMF','KMI','KMPH','KMPR','KMT','KMX','KN','KNDI','KNL','KNOP','KNSA','KNSL','KNTE','KNX','KO','KOD','KODK','KOF','KOP','KOPN','KOR','KOS','KOSS','KPTI','KR','KRA','KRBP','KRC','KREF','KRG','KRKR','KRMD','KRNT','KRNY','KRO','KRON','KROS','KRP','KRTX','KRUS','KRYS','KSM','KSMT','KSPN','KSS','KSU','KT','KTB','KTCC','KTF','KTOS','KTRA','KUKE','KURA','KVHI','KVSA','KVSB','KVSC','KW','KWAC','KWR','KXIN','KYMR','KYN','KZIA','KZR','LABP','LAC','LACQ','LAD','LADR','LAIX','LAKE','LAMR','LANC','LAND','LANDM','LARK','LASR','LATN','LAUR','LAWS','LAZ','LAZR','LAZY','LB','LBAI','LBC','LBPH','LBPS','LBRDA','LBRDK','LBRT','LBTYA','LBTYB','LBTYK','LC','LCAP','LCI','LCII','LCNB','LCTX','LCUT','LCY','LDI','LDL','LDOS','LDP','LE','LEA','LEAF','LEAP','LECO','LEE','LEG','LEGH','LEGN','LEGO','LEJU','LEN','LEO','LESL','LEU','LEVI','LEVL','LFC','LFMD','LFT','LFTR','LFUS','LFVN','LGHL','LGI','LGIH','LGL','LGND','LGVN','LH','LHAA','LHC','LHCG','LHDX','LHX','LI','LIFE','LII','LILA','LILAK','LIN','LINC','LIND','LINK','LINX','LIQT','LITB','LITE','LIVK','LIVN','LIVX','LIZI','LJPC','LKCO','LKFN','LKQ','LL','LLNW','LLY','LMAO','LMAT','LMB','LMND','LMNL','LMNR','LMNX','LMPX','LMRK','LMST','LMT','LNC','LND','LNDC','LNG','LNN','LNSR','LNT','LNTH','LOAN','LOB','LOCO','LODE','LOGC','LOGI','LOKB','LOMA','LOOP','LOPE','LORL','LOTZ','LOV','LOVE','LOW','LPCN','LPG','LPI','LPL','LPLA','LPRO','LPSN','LPTH','LPTX','LPX','LQDA','LQDT','LRCX','LRMR','LRN','LSAQ','LSBK','LSCC','LSEA','LSF','LSI','LSPD','LSTR','LSXMA','LSXMB','LSXMK','LTC','LTHM','LTRN','LTRPA','LTRPB','LTRX','LU','LUB','LULU','LUMN','LUMO','LUNA','LUNG','LUV','LUXA','LVS','LVTX','LW','LWAC','LWAY','LX','LXEH','LXFR','LXP','LXRX','LXU','LYB','LYFT','LYG','LYRA','LYTS','LYV','LZB','MA','MAA','MAAC','MAC','MACK','MACU','MAG','MAGS','MAIN','MAN','MANH','MANT','MANU','MAR','MARA','MARK','MAS','MASI','MASS','MAT','MATW','MATX','MAV','MAX','MAXN','MAXR','MAYS','MBCN','MBI','MBII','MBIN','MBIO','MBOT','MBRX','MBT','MBUU','MBWM','MC','MCA','MCB','MCBC','MCBS','MCD','MCF','MCFE','MCFT','MCHP','MCHX','MCI','MCK','MCMJ','MCN','MCO','MCR','MCRB','MCRI','MCS','MCY','MD','MDB','MDC','MDCA','MDGL','MDGS','MDH','MDJH','MDLA','MDLZ','MDNA','MDP','MDRX','MDT','MDU','MDVL','MDWD','MDWT','MDXG','MEC','MED','MEDP','MEG','MEI','MEIP','MELI','MEN','MEOH','MERC','MESA','MESO','MET','METC','METX','MFA','MFC','MFD','MFG','MFGP','MFH','MFIN','MFL','MFM','MFNC','MFT','MG','MGA','MGEE','MGF','MGI','MGIC','MGLN','MGM','MGNI','MGNX','MGP','MGPI','MGRC','MGTA','MGTX','MGU','MGY','MGYR','MHD','MHF','MHH','MHI','MHK','MHLD','MHN','MHO','MIC','MICT','MIDD','MIE','MIK','MILE','MIME','MIN','MIRM','MIST','MIT','MITC','MITK','MITO','MITT','MIXT','MIY','MKC','MKD','MKGI','MKL','MKSI','MKTX','MKTY','MLAB','MLAC','MLCO','MLHR','MLI','MLM','MLP','MLR','MLSS','MLVF','MMAC','MMC','MMD','MMI','MMLP','MMM','MMP','MMS','MMSI','MMT','MMU','MMX','MMYT','MN','MNDO','MNKD','MNOV','MNP','MNPR','MNR','MNRL','MNRO','MNSB','MNSO','MNST','MNTK','MNTX','MO','MOD','MODN','MODV','MOFG','MOGO','MOGU','MOH','MOHO','MOMO','MOR','MORF','MORN','MOS','MOTN','MOTS','MOTV','MOV','MOVE','MOXC','MP','MPA','MPAA','MPB','MPC','MPLN','MPLX','MPV','MPW','MPWR','MPX','MQT','MQY','MRAC','MRAM','MRBK','MRC','MRCC','MRCY','MREO','MRK','MRKR','MRLN','MRM','MRNA','MRNS','MRO','MRSN','MRTN','MRTX','MRUS','MRVI','MRVL','MS','MSA','MSB','MSBI','MSC','MSCI','MSD','MSEX','MSFT','MSGE','MSGM','MSGN','MSGS','MSI','MSM','MSON','MSP','MSTR','MT','MTA','MTAC','MTB','MTBC','MTC','MTCH','MTCR','MTD','MTDR','MTEM','MTG','MTH','MTL','MTLS','MTN','MTNB','MTOR','MTRN','MTRX','MTSC','MTSI','MTT','MTW','MTX','MTZ','MU','MUA','MUC','MUDS','MUE','MUFG','MUI','MUJ','MUR','MUSA','MUX','MVBF','MVF','MVIS','MVT','MWA','MWK','MX','MXF','MXIM','MXL','MYC','MYD','MYE','MYF','MYFW','MYGN','MYI','MYJ','MYN','MYO','MYOV','MYRG','MYTE','MZA','NAC','NAD','NAII','NAK','NAKD','NAN','NAPA','NARI','NAT','NATH','NATI','NATR','NAV','NAVB','NAVI','NAZ','NBA','NBB','NBEV','NBH','NBHC','NBIX','NBLX','NBN','NBO','NBR','NBRV','NBSE','NBTB','NBTX','NBW','NC','NCA','NCBS','NCLH','NCMI','NCNA','NCNO','NCR','NCSM','NCTY','NCV','NCZ','NDAQ','NDLS','NDRA','NDSN','NEA','NEBC','NEE','NEM','NEN','NEO','NEOG','NEON','NEP','NEPH','NEPT','NERV','NESR','NET','NETE','NETI','NEU','NEV','NEW','NEWR','NEWT','NEX','NEXA','NEXI','NEXT','NFBK','NFE','NFG','NFH','NFJ','NFLX','NG','NGA','NGAC','NGD','NGG','NGL','NGM','NGMS','NGS','NGVC','NGVT','NH','NHC','NHF','NHI','NHIC','NHS','NHTC','NI','NICE','NICK','NID','NIE','NIM','NINE','NIO','NIQ','NISN','NIU','NJR','NKE','NKG','NKLA','NKSH','NKTR','NKTX','NKX','NL','NLOK','NLS','NLSN','NLTX','NLY','NM','NMCI','NMCO','NMFC','NMI','NMIH','NML','NMM','NMMC','NMR','NMRD','NMRK','NMS','NMT','NMTR','NMY','NMZ','NNA','NNBR','NNDM','NNI','NNN','NNOX','NNVC','NNY','NOA','NOAH','NOC','NODK','NOG','NOK','NOMD','NOTV','NOV','NOVA','NOVN','NOVT','NOW','NP','NPA','NPK','NPO','NPTN','NPV','NQP','NR','NRBO','NRC','NREF','NRG','NRGX','NRIM','NRIX','NRK','NRO','NRP','NRZ','NS','NSA','NSC','NSCO','NSH','NSIT','NSL','NSP','NSPR','NSSC','NSTB','NSTG','NTAP','NTB','NTCO','NTCT','NTES','NTG','NTGR','NTIC','NTIP','NTLA','NTNX','NTP','NTR','NTRA','NTRS','NTST','NTUS','NTZ','NUAN','NUE','NUO','NUS','NUV','NUVA','NUVB','NUW','NUZE','NVAX','NVCN','NVCR','NVDA','NVEC','NVEE','NVG','NVGS','NVMI','NVO','NVOS','NVR','NVRO','NVS','NVST','NVT','NVTA','NVVE','NWBI','NWE','NWFL','NWG','NWHM','NWL','NWLI','NWN','NWPX','NWS','NWSA','NX','NXC','NXE','NXGN','NXJ','NXN','NXP','NXPI','NXQ','NXR','NXRT','NXST','NXTC','NXTD','NYC','NYCB','NYMT','NYMX','NYT','NZF','OACB','OAS','OBAS','OBCI','OBLG','OBNK','OBSV','OC','OCA','OCAX','OCDX','OCFC','OCFT','OCG','OCGN','OCN','OCSL','OCUL','OCUP','OCX','ODC','ODFL','ODP','ODT','OEC','OEG','OEPW','OESX','OFC','OFED','OFG','OFIX','OFLX','OFS','OGE','OGEN','OGI','OGS','OHI','OI','OIA','OII','OIIM','OIS','OKE','OKTA','OLED','OLK','OLLI','OLMA','OLN','OLO','OLP','OM','OMAB','OMC','OMCL','OMEG','OMER','OMEX','OMF','OMI','OMP','ON','ONB','ONCR','ONCS','ONCT','ONCY','ONDS','ONE','ONEM','ONEW','ONTF','ONTO','ONTX','ONVO','OOMA','OPBK','OPCH','OPEN','OPGN','OPI','OPK','OPOF','OPP','OPRA','OPRT','OPRX','OPT','OPTN','OPTT','OPY','OR','ORA','ORAN','ORBC','ORC','ORCC','ORCL','ORGO','ORGS','ORI','ORIC','ORLA','ORLY','ORMP','ORN','ORPH','ORRF','ORTX','OSBC','OSCR','OSG','OSH','OSIS','OSK','OSMT','OSPN','OSS','OSTK','OSTR','OSUR','OSW','OTEX','OTIC','OTIS','OTLK','OTRA','OTRK','OTTR','OUST','OUT','OVBC','OVID','OVLY','OVV','OXLC','OXM','OXSQ','OXY','OYST','OZK','OZON','PAA','PAAS','PAC','PACB','PACE','PACK','PACW','PACX','PAE','PAG','PAGP','PAGS','PAHC','PAI','PAIC','PAM','PAND','PANL','PANW','PAQC','PAR','PARR','PASG','PATK','PAVM','PAX','PAYA','PAYC','PAYS','PAYX','PB','PBA','PBCT','PBF','PBFS','PBFX','PBH','PBHC','PBI','PBIP','PBPB','PBR','PBT','PBY','PBYI','PCAR','PCB','PCG','PCH','PCI','PCK','PCM','PCN','PCOM','PCQ','PCRX','PCSA','PCSB','PCT','PCTI','PCTY','PCVX','PCYG','PCYO','PD','PDAC','PDCE','PDCO','PDD','PDEX','PDFS','PDI','PDLB','PDM','PDO','PDS','PDSB','PDT','PEAK','PEB','PEBK','PEBO','PED','PEG','PEGA','PEI','PEN','PENN','PEO','PEP','PERI','PESI','PETQ','PETS','PETZ','PFBC','PFBI','PFC','PFD','PFE','PFG','PFGC','PFHD','PFIE','PFIS','PFL','PFLT','PFMT','PFN','PFO','PFPT','PFS','PFSI','PFSW','PFX','PG','PGC','PGEN','PGNY','PGP','PGR','PGRE','PGTI','PGZ','PH','PHAR','PHAS','PHAT','PHCF','PHD','PHG','PHGE','PHI','PHK','PHM','PHR','PHT','PHUN','PHVS','PHX','PI','PIAI','PII','PIM','PINC','PINE','PING','PINS','PIPR','PIRS','PJT','PK','PKBK','PKE','PKG','PKI','PKO','PKOH','PKX','PLAB','PLAG','PLAN','PLAY','PLBC','PLBY','PLCE','PLD','PLG','PLL','PLM','PLMR','PLNT','PLOW','PLPC','PLRX','PLSE','PLT','PLTK','PLTR','PLUG','PLUS','PLX','PLXP','PLXS','PLYA','PLYM','PM','PMBC','PME','PMF','PML','PMM','PMO','PMT','PMVC','PMVP','PMX','PNC','PNF','PNFP','PNI','PNM','PNNT','PNR','PNRG','PNTG','PNTM','PNW','PODD','POLA','POOL','POR','POSH','POST','POW','POWI','POWL','POWW','PPBI','PPBT','PPC','PPD','PPG','PPGH','PPL','PPR','PPT','PPTA','PQG','PRA','PRAA','PRAH','PRAX','PRCH','PRDO','PRFT','PRG','PRGO','PRGS','PRI','PRIM','PRK','PRLB','PRLD','PRMW','PRO','PROF','PROG','PROS','PROV','PRPB','PRPH','PRPL','PRQR','PRS','PRSP','PRSR','PRT','PRTA','PRTC','PRTG','PRTH','PRTK','PRTS','PRTY','PRU','PRVB','PS','PSA','PSAC','PSB','PSEC','PSF','PSMT','PSN','PSNL','PSO','PSTG','PSTH','PSTI','PSTL','PSTX','PSX','PSXP','PTA','PTC','PTCT','PTE','PTEN','PTGX','PTIC','PTK','PTMN','PTN','PTNR','PTON','PTR','PTRS','PTSI','PTVCA','PTVCB','PTVE','PTY','PUBM','PUK','PULM','PUMP','PUYI','PV','PVAC','PVBC','PVG','PVH','PW','PWFL','PWOD','PWR','PXD','PXLW','PYN','PYPD','PYPL','PYR','PZC','PZN','PZZA','QADA','QADB','QCOM','QCRH','QD','QDEL','QELL','QFIN','QGEN','QH','QIWI','QK','QLGN','QLI','QLYS','QMCO','QNST','QQQX','QRHC','QRTEA','QRTEB','QRVO','QS','QSR','QTNT','QTRX','QTS','QTT','QTWO','QUAD','QUIK','QUMU','QUOT','QURE','RA','RAAC','RAAS','RACA','RACB','RACE','RAD','RADA','RADI','RAIL','RAMP','RAPT','RARE','RAVN','RBA','RBAC','RBB','RBBN','RBC','RBCAA','RBKB','RBLX','RBNC','RC','RCEL','RCHG','RCI','RCII','RCKT','RCKY','RCL','RCM','RCS','RCUS','RDCM','RDFN','RDHL','RDI','RDIB','RDN','RDNT','RDUS','RDVT','RDWR','RDY','RE','REAL','REDU','REED','REFR','REG','REGI','REGN','REI','REKR','RELL','RELX','RENN','REPH','REPL','REPX','RES','RESN','RETA','REV','REVG','REX','REXR','REYN','REZI','RF','RFI','RFIL','RFL','RFM','RFP','RGA','RGCO','RGEN','RGLD','RGLS','RGNX','RGP','RGR','RGS','RGT','RH','RHI','RHP','RICE','RICK','RIDE','RIG','RIGL','RILY','RIO','RIOT','RIV','RIVE','RJF','RKDA','RKT','RL','RLAY','RLGT','RLGY','RLI','RLJ','RLMD','RLX','RM','RMAX','RMBI','RMBL','RMBS','RMD','RMGB','RMGC','RMI','RMM','RMNI','RMO','RMR','RMRM','RMT','RMTI','RNA','RNDB','RNET','RNG','RNGR','RNLX','RNP','RNR','RNST','RNWK','ROAD','ROCC','ROCK','ROCR','ROG','ROIC','ROK','ROKU','ROL','ROLL','ROOT','ROP','ROST','RP','RPAI','RPAY','RPD','RPLA','RPM','RPRX','RPT','RPTX','RQI','RRBI','RRC','RRD','RRGB','RRR','RS','RSF','RSG','RSI','RSSS','RSVA','RTLR','RTP','RTPZ','RTX','RUBY','RUHN','RUN','RUSHA','RUSHB','RUTH','RVI','RVLV','RVMD','RVNC','RVP','RVSB','RVT','RWLK','RWT','RXDX','RXN','RXT','RY','RYAAY','RYAM','RYB','RYI','RYN','RYTM','RZLT','SA','SABR','SACH','SAFE','SAFM','SAFT','SAGE','SAH','SAIA','SAIC','SAII','SAIL','SAL','SALM','SAM','SAMG','SAN','SANA','SAND','SANM','SANW','SAP','SAR','SASR','SATS','SAVA','SAVE','SB','SBAC','SBBP','SBCF','SBFG','SBG','SBGI','SBH','SBI','SBLK','SBNY','SBOW','SBR','SBRA','SBS','SBSI','SBSW','SBT','SBTX','SBUX','SC','SCCO','SCD','SCHL','SCHN','SCHW','SCI','SCKT','SCL','SCM','SCOR','SCPE','SCPH','SCPL','SCPS','SCR','SCS','SCSC','SCU','SCVL','SCVX','SCWX','SCYX','SD','SDC','SDGR','SDH','SE','SEAC','SEAH','SEAS','SEB','SECO','SEDG','SEE','SEED','SEEL','SEER','SEIC','SELB','SEM','SEMR','SENEA','SENEB','SENS','SESN','SF','SFBC','SFBS','SFE','SFIX','SFL','SFM','SFNC','SFST','SFT','SFTW','SFUN','SGA','SGAM','SGC','SGEN','SGFY','SGH','SGMO','SGMS','SGOC','SGRY','SGTX','SGU','SHAC','SHAK','SHBI','SHC','SHEN','SHG','SHI','SHIP','SHLS','SHLX','SHO','SHOO','SHOP','SHSP','SHW','SHYF','SI','SIBN','SIC','SID','SIEB','SIEN','SIF','SIFY','SIG','SIGA','SIGI','SII','SILC','SILK','SILV','SIM','SIMO','SINO','SIOX','SIRI','SITC','SITE','SITM','SIVB','SIX','SJ','SJI','SJM','SJR','SJT','SJW','SKLZ','SKM','SKT','SKX','SKY','SKYW','SLAB','SLB','SLCA','SLCR','SLCT','SLDB','SLF','SLG','SLGG','SLGL','SLGN','SLM','SLN','SLNO','SLP','SLQT','SLRC','SLRX','SLS','SM','SMAR','SMBC','SMBK','SMCI','SMED','SMFG','SMG','SMHI','SMID','SMLP','SMM','SMMF','SMMT','SMP','SMPL','SMSI','SMTC','SMTI','SMTS','SMTX','SNA','SNAP','SNBR','SNCR','SNCY','SND','SNDL','SNDR','SNDX','SNE','SNEX','SNFCA','SNMP','SNN','SNOW','SNP','SNPR','SNPS','SNR','SNRH','SNSE','SNV','SNX','SNY','SO','SOAC','SOFI','SOGO','SOHO','SOHU','SOI','SOL','SOLO','SOLY','SON','SONM','SONO','SOR','SOS','SP','SPB','SPCE','SPE','SPFI','SPFR','SPG','SPGI','SPH','SPI','SPKE','SPLK','SPLP','SPNE','SPNS','SPNT','SPNV','SPOK','SPOT','SPPI','SPR','SPRB','SPRO','SPRQ','SPRT','SPSC','SPT','SPTN','SPWH','SPWR','SPXC','SPXX','SQ','SQM','SQNS','SQZ','SR','SRAC','SRAX','SRC','SRCE','SRCL','SRDX','SRE','SREV','SRG','SRGA','SRI','SRL','SRLP','SRNE','SRPT','SRRA','SRRK','SRSA','SRT','SRTS','SRV','SSB','SSBI','SSD','SSKN','SSL','SSNC','SSP','SSPK','SSRM','SSSS','SSTI','SSTK','SSYS','ST','STAA','STAG','STAR','STAY','STBA','STC','STCN','STE','STEP','STFC','STG','STIC','STIM','STK','STKL','STKS','STL','STLA','STLD','STM','STMP','STN','STND','STNE','STNG','STOK','STON','STOR','STPC','STPK','STRA','STRL','STRM','STRO','STRS','STRT','STSA','STT','STTK','STWD','STWO','STX','STXB','STXS','STZ','SU','SUI','SUM','SUMO','SUN','SUNS','SUNW','SUP','SUPN','SUPV','SURF','SUZ','SV','SVAC','SVBI','SVC','SVFA','SVFB','SVFC','SVM','SVMK','SVOK','SVOKU','SVRA','SWAV','SWBI','SWBK','SWCH','SWET','SWI','SWIR','SWK','SWKH','SWKS','SWM','SWN','SWTX','SWX','SWZ','SXC','SXI','SXT','SY','SYBT','SYBX','SYF','SYK','SYKE','SYN','SYNA','SYNC','SYNH','SYNL','SYPR','SYRS','SYX','SYY','SZC','TA','TAC','TACO','TACT','TAK','TAL','TALO','TAOP','TAP','TARA','TARO','TARS','TAST','TBA','TBBK','TBI','TBIO','TBK','TBLT','TBNK','TBPH','TC','TCBI','TCBK','TCDA','TCF','TCFC','TCI','TCMD','TCOM','TCON','TCPC','TCRR','TCS','TCX','TD','TDAC','TDC','TDF','TDG','TDOC','TDS','TDUP','TDW','TDY','TEAF','TEAM','TECH','TECK','TEDU','TEF','TEI','TEKK','TEL','TELA','TELL','TEN','TENB','TEO','TER','TERN','TESS','TEVA','TEX','TFC','TFFP','TFII','TFSL','TFX','TG','TGA','TGB','TGH','TGI','TGLS','TGNA','TGP','TGS','TGT','TGTX','TH','THBR','THC','THCA','THCB','THFF','THG','THM','THO','THQ','THR','THRM','THRY','THS','THTX','THW','TIG','TIGO','TIGR','TIL','TILE','TIMB','TINV','TIPT','TIRX','TISI','TITN','TIXT','TJX','TK','TKAT','TKC','TKR','TLC','TLGA','TLIS','TLK','TLMD','TLND','TLRY','TLS','TLSA','TLYS','TM','TMBR','TMDI','TMDX','TME','TMHC','TMKR','TMO','TMP','TMPM','TMQ','TMST','TMTS','TMUS','TMX','TNC','TNDM','TNET','TNK','TNL','TNP','TNXP','TOL','TOMZ','TOPS','TOT','TOUR','TOWN','TPB','TPC','TPCO','TPGY','TPH','TPHS','TPIC','TPL','TPR','TPTX','TPVG','TPX','TPZ','TR','TRC','TRCH','TREB','TREC','TREE','TREX','TRGP','TRHC','TRI','TRIB','TRIL','TRIN','TRIP','TRIT','TRMB','TRMD','TRMK','TRN','TRNO','TRNS','TROW','TROX','TRP','TRQ','TRS','TRST','TRTN','TRTX','TRU','TRUP','TRV','TRVG','TRVI','TRVN','TRX','TS','TSBK','TSC','TSCAP','TSCO','TSE','TSEM','TSHA','TSI','TSIA','TSLA','TSLX','TSM','TSN','TSQ','TT','TTC','TTCF','TTD','TTEC','TTEK','TTGT','TTI','TTM','TTMI','TTOO','TTWO','TU','TUFN','TUP','TURN','TUSK','TUYA','TV','TVAC','TVTX','TVTY','TW','TWCT','TWI','TWIN','TWLO','TWN','TWND','TWNK','TWO','TWOU','TWST','TWTR','TX','TXG','TXMD','TXN','TXRH','TXT','TY','TYG','TYL','TYME','TZOO','TZPS','UA','UAA','UAL','UAMY','UAN','UAVS','UBA','UBCP','UBER','UBFO','UBOH','UBP','UBS','UBSI','UBX','UCBI','UCL','UCTT','UDR','UE','UEC','UEIC','UEPS','UFAB','UFCS','UFI','UFPI','UFPT','UFS','UG','UGI','UGP','UGRO','UHAL','UHS','UHT','UI','UIHC','UIS','UK','UL','ULBI','ULH','ULTA','UMBF','UMC','UMH','UMPQ','UNB','UNF','UNFI','UNH','UNIT','UNM','UNP','UNTY','UNVR','UONE','UONEK','UPC','UPLD','UPS','UPST','UPWK','URBN','URG','URGN','URI','USA','USAC','USAK','USAP','USAS','USAT','USAU','USB','USCR','USDP','USFD','USIO','USLM','USM','USNA','USPH','USWS','USX','UTF','UTG','UTHR','UTI','UTL','UTMD','UTSI','UTZ','UUUU','UVE','UVSP','UVV','UWMC','UXIN','VAC','VACQ','VALE','VALU','VAPO','VAQC','VAR','VBF','VBFC','VBIV','VBLT','VBTX','VC','VCEL','VCF','VCIF','VCNX','VCRA','VCTR','VCV','VCVC','VCYT','VEC','VECO','VEDL','VEEV','VEI','VEL','VEON','VER','VERB','VERI','VERO','VERU','VERX','VERY','VET','VFC','VFF','VFL','VG','VGAC','VGI','VGM','VGR','VGZ','VHAQ','VHC','VHI','VIAC','VIACA','VIAO','VIAV','VICI','VICR','VIEW','VIH','VII','VINC','VINP','VIOT','VIPS','VIR','VIRT','VIRX','VISL','VIST','VITL','VIV','VIVO','VJET','VKI','VKQ','VKTX','VLDR','VLGEA','VLO','VLRS','VLT','VLY','VMAC','VMAR','VMC','VMD','VMI','VMM','VMO','VMW','VNCE','VNDA','VNE','VNET','VNO','VNOM','VNRX','VNT','VNTR','VOC','VOD','VOLT','VOR','VOXX','VOYA','VPG','VPV','VRA','VRAY','VRCA','VRDN','VREX','VRM','VRNA','VRNS','VRNT','VRRM','VRS','VRSK','VRSN','VRT','VRTS','VRTV','VRTX','VS','VSAT','VSEC','VSH','VSPR','VST','VSTA','VSTM','VSTO','VTA','VTGN','VTN','VTNR','VTOL','VTR','VTRS','VTRU','VTVT','VUZI','VVI','VVNT','VVOS','VVPR','VVR','VVV','VWTR','VXRT','VYGG','VYGR','VYNE','VZIO','WAB','WABC','WAFD','WAFU','WAL','WASH','WAT','WATT','WB','WBA','WBAI','WBK','WBS','WBT','WCC','WCN','WD','WDAY','WDC','WDFC','WDR','WEA','WEC','WEI','WELL','WEN','WERN','WES','WETF','WEX','WEYS','WF','WFC','WFG','WGO','WH','WHD','WHF','WHG','WHR','WIA','WIFI','WILC','WIMI','WINA','WING','WIRE','WISH','WIT','WIW','WIX','WK','WKEY','WKHS','WLDN','WLFC','WLK','WLKP','WLL','WLMS','WLTW','WM','WMB','WMC','WMG','WMK','WMS','WMT','WNC','WNEB','WNS','WNW','WOOF','WOR','WORK','WOW','WPC','WPF','WPG','WPM','WPP','WPRT','WRAP','WRB','WRE','WRI','WRK','WRLD','WRN','WSBC','WSBF','WSC','WSFS','WSM','WSO','WSR','WST','WSTG','WTBA','WTER','WTFC','WTI','WTM','WTRE','WTRG','WTRH','WTS','WTTR','WU','WVE','WW','WWD','WWE','WWR','WWW','WY','WYNN','WYY','XAIR','XBIT','XCUR','XEC','XEL','XELA','XENE','XENT','XERS','XFLT','XFOR','XGN','XHR','XIN','XL','XLNX','XLRN','XM','XNCR','XNET','XOG','XOM','XOMA','XONE','XP','XPEL','XPER','XPEV','XPO','XPOA','XRAY','XRX','XSPA','XTNT','XXII','XYF','XYL','YAC','YALA','YCBD','YELL','YELP','YETI','YEXT','YGMZ','YI','YJ','YMAB','YMTX','YNDX','YORW','YPF','YQ','YRD','YSAC','YSG','YTEN','YTRA','YUM','YUMC','YY','ZBH','ZBRA','ZDGE','ZEAL','ZEN','ZEPP','ZEUS','ZG','ZGNX','ZGYH','ZH','ZI','ZIM','ZION','ZIOP','ZIXI','ZKIN','ZLAB','ZM','ZNGA','ZNH','ZNTL','ZOM','ZS','ZSAN','ZTO','ZTR','ZTS','ZUMZ','ZUO','ZVO','ZYME','ZYNE','ZYXI','TRUE'}

# includes common words and words used on wsb that are also stock names
blacklist = {'I', 'ARE',  'ON', 'GO', 'NOW', 'CAN', 'UK', 'SO', 'OR', 'OUT', 'SEE', 'ONE', 'LOVE', 'U', 'STAY', 'HAS', 'BY', 'BIG', 'GOOD', 'RIDE', 'EOD', 'ELON', 'WSB', 'THE', 'A', 'ROPE', 'YOLO', 'TOS', 'CEO', 'DD', 'IT', 'OPEN', 'ATH', 'PM', 'IRS', 'FOR','DEC', 'BE', 'IMO', 'ALL', 'RH', 'EV', 'TOS', 'CFO', 'CTO', 'DD', 'BTFD', 'WSB', 'OK', 'PDT', 'RH', 'KYS', 'FD', 'TYS', 'US', 'USA', 'IT', 'ATH', 'RIP', 'BMW', 'GDP', 'OTM', 'ATM', 'ITM', 'IMO', 'LOL', 'AM', 'BE', 'PR', 'PRAY', 'PT', 'FBI', 'SEC', 'GOD', 'NOT', 'POS', 'FOMO', 'TL;DR', 'EDIT', 'STILL', 'WTF', 'RAW', 'PM', 'LMAO', 'LMFAO', 'ROFL', 'EZ', 'RED', 'BEZOS', 'TICK', 'IS', 'PM', 'LPT', 'GOAT', 'FL', 'CA', 'IL', 'MACD', 'HQ', 'OP', 'PS', 'AH', 'TL', 'JAN', 'FEB', 'JUL', 'AUG', 'SEP', 'SEPT', 'OCT', 'NOV', 'FDA', 'IV', 'ER', 'IPO', 'MILF', 'BUT', 'SSN', 'FIFA', 'USD', 'CPU', 'AT', 'GG', 'Mar'}


# adding wsb/reddit flavour to vader to improve sentiment analysis, score: 4.0 to -4.0
new_words = {
    'citron': -4.0,
    'hidenburg': -4.0,
    'moon': 4.0,
    'highs': 2.0,
    'mooning': 4.0,
    'long': 2.0,
    'short': -2.0,
    'call': 4.0,
    'calls': 4.0,
    'put': -4.0,
    'puts': -4.0,
    'break': 2.0,
    'tendie': 2.0,
     'tendies': 2.0,
     'town': 2.0,
     'overvalued': -3.0,
     'undervalued': 3.0,
     'buy': 4.0,
     'sell': -4.0,
     'gone': -1.0,
     'gtfo': -1.7,
     'paper': -1.7,
     'bullish': 3.7,
     'bearish': -3.7,
     'bagholder': -1.7,
     'stonk': 1.9,
     'green': 1.9,
     'money': 1.2,
     'print': 2.2,
     'rocket': 2.2,
     'bull': 2.9,
     'bear': -2.9,
     'pumping': -1.0,
     'sus': -3.0,
     'offering': -2.3,
     'rip': -4.0,
     'downgrade': -3.0,
     'upgrade': 3.0,
     'maintain': 1.0,
     'pump': 1.9,
     'hot': 1.5,
     'drop': -2.5,
     'rebound': 1.5,
     'crack': 2.5,}
