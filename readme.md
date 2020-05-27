<!-- // This code Is written by Shivam Gupta(SXG190040) -->
<!-- Information Retieval (CS 6322.001) Assignment 3 (Relevance Model) -->

## Implementation of Index Building and Compression in Cranfield documents Collection

        
        ## Functions:
                - 'preprocess()': function for preprocessing the documents (Cranfield documents/queries)
                - 'preprocess_documents()': function for preprocessing the documents (Cranfield documents/queries)
                - 'extract_queries()' - Function for creating a dictionary for every Query
                - 'extract_tokens_queries()': Function for getting lemmatized tokens for the queries 
                - 'extract_cranfield_info()': Function for getting the information like tpkens, doc IDs and titles
                - 'create_doc_dict()': Function for generating dictionary for the documents
                - 'get_postings_dict()': Function for initializing ordered postings for the documents by removing stopwords
                - 'create_Postings()':  Function for generating ordered postings for the documents
                - 'get_postings_documents_dict()':  Function for getting the postings and documents dictionary by calling above functions
                - 'lemmatize_tokens()':  Function for lemmatizing the tokens in the documents
                - 'calculate_docfreq_query()':  Function for generating the dictionary of the queries for storing terms information
                - 'calculate_weights()':  Function for calculating the weights(both versions)
                 - 'calculate_document_vetor_representation': Function for calculating the Documents weights Vector representation
                

     


        ## Variables
                - 'docs_tokens' :The list containing tokens for all the documents
                - 'Document_IDs' : The list containing the document IDs
                - 'titles' : The dictionary containing the titles of the documents
                - 'lemma_result' :The lemmatized tokens for the documents
                - 'posting_dict' :The dictionary conataining ordered indexing of the documents
                - 'document_dict' : The dictionary with additional information of the documents
                - 'query_dict' : The dictionary conataining all the queries
                - 'tokenized_queries' : The dictionary conataining lemmatized tokens for the queries
                -  'queries_doc_freq' : The dictionary of the queries for storing terms information
                - 'rankings' : The dictionary containing the score for every query with documents
                - 'queries_vector' : The Query vector conataingn the weights(both types)


 

#### Compiling and Running the Code:
  ## Setup on UTD Linux Server(csgrads1.utdallas.edu):
  # Run command:-  ```pip install nltk==3 --user```  (For Installing NLTK verison 3)
  # ```pip install bs4 --user```

  # In this UTD Linux Server the python version is Python 2.7.5


  ## For Running the file: Run command:- ```python relevance_model.py``` on UTD CS Linux Servers / Anaconda Prompt


The results will be displayed as follows:

## Results

A Statistical Relevance model in retrieval system based on the vector relevance model:


Query No: 1

Query Vector for weight (Version 1) are:
[('aeroelastic', 0.05247433347812679),
 ('aircraft', 0.05247433347812679),
 ('constructing', 0.06827068185751761),
 ('heated', 0.06827068185751761),
 ('high', 0.05247433347812679),
 ('law', 0.06827068185751761),
 ('model', 0.06827068185751761),
 ('must', 0.06827068185751761),
 ('similarity', 0.06827068185751761),
 ('speed', 0.05247433347812679)]

Query Vector for weight (Version 2) are:
[('aeroelastic', 0.05052658164092087),
 ('aircraft', 0.05052658164092087),
 ('constructing', 0.05479005299633102),
 ('heated', 0.05479005299633102),
 ('high', 0.05052658164092087),
 ('law', 0.05479005299633102),
 ('model', 0.05479005299633102),
 ('must', 0.05479005299633102),
 ('similarity', 0.05479005299633102),
 ('speed', 0.05052658164092087)]

Ranks  Document Number   Scores Titles


1     238       0.052908002524909785   on a determination of the pitot-static tube factor at low reynolds numbers, with special reference to the measurement of low air speeds .


Vector Representation for the Rank 1 With Document ID 238


{'anemometer': 0.5354108567977349, 'calibration': 0.5354108567977349, 'enquiry': 0.7509775004326937, 'instrument': 0.5652336036984639, 'low': 0.24479870151537933, 'provide': 0.35407892984037437, 'reason': 0.5232008027208732, 'speed': 0.185448131504831, 'standard': 0.44042298928386026, 'to': 0.011748290985597008}
======================================================================
2     429       0.04822475792519278   a description of the r. a. e.  high speed supersonic tunnel .


Vector Representation for the Rank 2 With Document ID 429


{'account': 0.303402320792395, 'completion': 0.6370891515767835, 'described': 0.2685217101712429, 'design': 0.25730367938315063, 'development': 0.303402320792395, 'feature': 0.351849475256591, 'given': 0.13356179239887297, 'high': 0.19815778000687356, 'interesting': 0.4305425982496091, 'more': 0.22616033318930492, 'nearing': 0.7509775004326937, 'noted': 0.46355530891941527, 'now': 0.42593447771869397, 'philosophy': 0.6370891515767835, 'principal': 0.43536512556343715, 'problem': 0.15629204698258145, 'reviewed': 0.4305425982496091, 'speed': 0.185448131504831, 'supersonic': 0.19326698423974895, 'tunnel': 0.2167582158642367}
======================================================================
3     430       0.030811769765415446   calibration of the flow in the mach 4 working section of the 4ft . x 3ft . high supersonic speed wind tunnel at rae bedford .


Vector Representation for the Rank 3 With Document ID 430


{'angle': 0.163564324255595, 'distribution': 0.12607535993592625, 'flow': 0.06220061601834868, 'ft': 0.46965022359082137, 'high': 0.1639777441416276, 'humidity': 0.5271982855734489, 'mach': 0.16307374923830095, 'nozzle': 0.24553235789630273, 'number': 0.07845045600431105, 'presented': 0.12397011415191703, 'pressure': 0.0834887895608359, 'range': 0.13837168420922066, 'section': 0.20322597653563415, 'speed': 0.1534603701070292, 'supersonic': 0.15993055680978174, 'total': 0.23833663006222613, 'tunnel': 0.17936980955453063, 'wind': 0.21074975241888858, 'working': 0.37839647016748407, 'x': 0.23448049951385272}
======================================================================
4     879       0.02950570717667317   flutter model testing at transonic speeds .


Vector Representation for the Rank 4 With Document ID 879


{'construction': 0.3950520390840711, 'delta': 0.32685940877657377, 'developed': 0.17887537325596373, 'facility': 0.3950520390840711, 'flutter': 0.27924930419983346, 'foot': 0.32685940877657377, 'model': 0.26133963885470796, 'on': 0.047578484797422, 'plane': 0.23079027635009564, 'reflection': 0.36885503908586875, 'research': 0.2875844439235415, 'straight': 0.3387105610060959, 'swept': 0.3387105610060959, 'technique': 0.2393283689727511, 'test': 0.15875271962933116, 'testing': 0.33559078227780864, 'transonic': 0.2824868378681199, 'wing': 0.15953614480318243, 'x': 0.23448049951385272}
======================================================================
5     509       0.027613238082377662   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 5 With Document ID 509


{'acted': 0.5271982855734489, 'at': 0.055861380633815266, 'by': 0.06275576151877217, 'change': 0.22302558106185744, 'condition': 0.1242304617275272, 'conduction': 0.3093937822796063, 'considers': 0.36885503908586875, 'derived': 0.19103750478445003, 'entry': 0.3164485331545604, 'heat': 0.14608784514803438, 'heated': 0.3524654687089807, 'heating': 0.2545706528709851, 'material': 0.26203487688769017, 'method': 0.09736364101196376, 'most': 0.23261554649289723, 're': 0.32685940877657377, 'severe': 0.3891335228376759, 'space': 0.36885503908586875, 'state': 0.2731192355396403, 'sublimation': 0.5271982855734489, 'such': 0.17789496875257943, 'suitable': 0.3049936147025652, 'surface': 0.12634218584411033, 'under': 0.18036731451851562, 'upon': 0.2545706528709851, 'vehicle': 0.2716527987994464}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     238       0.020301920239958363   on a determination of the pitot-static tube factor at low reynolds numbers, with special reference to the measurement of low air speeds .


Vector Representation for the Rank 1 With Document ID 238


{'anemometer': 0.6587427378194435, 'calibration': 0.6587427378194435, 'enquiry': 0.7629175091161123, 'instrument': 0.6731548833417484, 'low': 0.5183014603468571, 'provide': 0.5711122412777057, 'reason': 0.6528421050984972, 'speed': 0.4896196942214549, 'standard': 0.6128388855009328, 'to': 0.40567748101428813}
======================================================================
2     429       0.018621973225484735   a description of the r. a. e.  high speed supersonic tunnel .


Vector Representation for the Rank 2 With Document ID 429


{'account': 0.5319438365869127, 'completion': 0.6770578243679968, 'described': 0.5167749295863688, 'design': 0.5118964236564693, 'development': 0.5319438365869127, 'feature': 0.5530125726962148, 'given': 0.45808345586977395, 'high': 0.4861750090617886, 'interesting': 0.5872346990582913, 'more': 0.4983527811087177, 'nearing': 0.7265856778509625, 'noted': 0.6015912922792392, 'now': 0.5852307160277201, 'philosophy': 0.6770578243679968, 'principal': 0.5893319234769109, 'problem': 0.46796840661286304, 'reviewed': 0.5872346990582913, 'speed': 0.4806478272635384, 'supersonic': 0.48404809600525, 'tunnel': 0.4942639810340518}
======================================================================
3     430       0.018074106688195875   calibration of the flow in the mach 4 working section of the 4ft . x 3ft . high supersonic speed wind tunnel at rae bedford .


Vector Representation for the Rank 3 With Document ID 430


{'angle': 0.48548231880139464, 'distribution': 0.4658897602523783, 'flow': 0.43250741206752935, 'ft': 0.6198152993936824, 'high': 0.4856983811405233, 'humidity': 0.675525437004926, 'mach': 0.4763251100744669, 'nozzle': 0.5283206187490602, 'number': 0.44099993639074936, 'presented': 0.4647895124319383, 'pressure': 0.44363308049027567, 'range': 0.47231609017731074, 'section': 0.5062103719378132, 'speed': 0.4802017697965108, 'supersonic': 0.4835832318906833, 'total': 0.5245599728776573, 'tunnel': 0.49374261357706395, 'wind': 0.5101424629458595, 'working': 0.5977583305124242, 'x': 0.522544674111401}
======================================================================
4     141       0.017455983842637336   free-flight techniques for high speed aerodynamic research .


Vector Representation for the Rank 4 With Document ID 141


{'aeroelastic': 0.5653168763789699, 'airborne': 0.6600540297733153, 'airplane': 0.5379574938416957, 'also': 0.4543543141920649, 'bang': 0.6600540297733153, 'beyond': 0.5430945427503009, 'borne': 0.6351713604835433, 'both': 0.47057972298462447, 'calibration': 0.5854060219039989, 'component': 0.5136781682262681, 'control': 0.5250340784033166, 'described': 0.49298567902689444, 'detail': 0.5070319059829517, 'development': 0.505064394231755, 'discussed': 0.46896806613993514, 'drag': 0.4834360448448163, 'effected': 0.6022782608736025, 'estimation': 0.5773955915838305, 'evaluation': 0.5474957336089541, 'extension': 0.522613064319182, 'free': 0.47131991629254794, 'high': 0.4686195381246846, 'higher': 0.4933292041707567, 'interference': 0.5242087982966382, 'involved': 0.526743835039648, 'launched': 0.6206159320311806, 'lift': 0.48587534474491056, 'limit': 0.5182118734605288, 'longitudinal': 0.5242087982966382, 'mach': 0.4470976775223156, 'measurement': 0.5292369278508107, 'model': 0.4754780588051052, 'much': 0.5096533698442756, 'number': 0.44580510323934325, 'obtained': 0.44443734186121253, 'on': 0.41991010224321423, 'pressure': 0.4349374374445928, 'recording': 0.6206159320311806, 'reynolds': 0.47131991629254794, 'rocket': 0.5892541798010607, 'sonic': 0.5168570672571391, 'speed': 0.4642183472660315, 'stability': 0.49734230364321486, 'telemetering': 0.6600540297733153, 'test': 0.4926914269529348, 'than': 0.4596171008950292, 'tracking': 0.6600540297733153, 'tunnel': 0.5206215244816765, 'unit': 0.5525129222940584, 'usual': 0.5314124957095017, 'wall': 0.47632775773021274, 'wind': 0.48819215526215143}
======================================================================
5     502       0.016170991444720964   on squire's test of the compressibility transformation .


Vector Representation for the Rank 5 With Document ID 502


{'air': 0.4904638414295134, 'application': 0.5052716488100103, 'author': 0.5218638904103183, 'boundary': 0.4491059460884536, 'by': 0.42214575039211555, 'compressibility': 0.6332039257851444, 'correlation': 0.5436028304942103, 'data': 0.48218022169316194, 'discussion': 0.5346507085149965, 'helium': 0.5581961193607206, 'high': 0.4838434521650712, 'incorrect': 0.656943289080779, 'invalid': 0.6695617290588387, 'layer': 0.4553900830476405, 'previous': 0.5452900557414009, 'shown': 0.4698175401547281, 'speed': 0.4784658141728666, 'squire': 0.7757187396607779, 'suggestion': 0.621373904542798, 'that': 0.4241639914229409, 'to': 0.4064996471777625, 'transformation': 0.6053589940621771}
======================================================================
========================================================================================================================================================================


Query No: 2

Query Vector for weight (Version 1) are:
[('aeroelastic', 0.07215220853242434),
 ('aircraft', 0.07215220853242434),
 ('associated', 0.09387218755408672),
 ('flight', 0.09387218755408672),
 ('high', 0.07215220853242434),
 ('problem', 0.04343995804332474),
 ('speed', 0.07215220853242434),
 ('structural', 0.09387218755408672)]

Query Vector for weight (Version 2) are:
[('aeroelastic', 0.07250110412252518),
 ('aircraft', 0.07250110412252518),
 ('associated', 0.07927461139896373),
 ('flight', 0.07927461139896373),
 ('high', 0.07250110412252518),
 ('problem', 0.06354701455287709),
 ('speed', 0.07250110412252518),
 ('structural', 0.07927461139896373)]

Ranks  Document Number   Scores Titles


1     429       0.06105668858242899   a description of the r. a. e.  high speed supersonic tunnel .


Vector Representation for the Rank 1 With Document ID 429


{'account': 0.303402320792395, 'completion': 0.6370891515767835, 'described': 0.2685217101712429, 'design': 0.25730367938315063, 'development': 0.303402320792395, 'feature': 0.351849475256591, 'given': 0.13356179239887297, 'high': 0.19815778000687356, 'interesting': 0.4305425982496091, 'more': 0.22616033318930492, 'nearing': 0.7509775004326937, 'noted': 0.46355530891941527, 'now': 0.42593447771869397, 'philosophy': 0.6370891515767835, 'principal': 0.43536512556343715, 'problem': 0.15629204698258145, 'reviewed': 0.4305425982496091, 'speed': 0.185448131504831, 'supersonic': 0.19326698423974895, 'tunnel': 0.2167582158642367}
======================================================================
2     238       0.052908002524909785   on a determination of the pitot-static tube factor at low reynolds numbers, with special reference to the measurement of low air speeds .


Vector Representation for the Rank 2 With Document ID 238


{'anemometer': 0.5354108567977349, 'calibration': 0.5354108567977349, 'enquiry': 0.7509775004326937, 'instrument': 0.5652336036984639, 'low': 0.24479870151537933, 'provide': 0.35407892984037437, 'reason': 0.5232008027208732, 'speed': 0.185448131504831, 'standard': 0.44042298928386026, 'to': 0.011748290985597008}
======================================================================
3     1158       0.033165630102438365   the tailored-interface hypersonic shock tunnel .


Vector Representation for the Rank 3 With Document ID 1158


{'application': 0.2983146820692516, 'associated': 0.26203487688769017, 'compared': 0.16998511017361387, 'condition': 0.1242304617275272, 'cylinder': 0.1834313709581794, 'discussed': 0.1648106095218505, 'encountered': 0.34194809467438225, 'evidence': 0.33559078227780864, 'experiment': 0.20257362008142774, 'experimental': 0.13329773304442719, 'flight': 0.2144007059732076, 'flow': 0.06220061601834868, 'gasdynamic': 0.4677370287671866, 'heattransfer': 0.4157399959776291, 'hemisphere': 0.3562787391713667, 'high': 0.23759229630146478, 'hypersonic': 0.2818397039595156, 'indication': 0.42391612831509007, 'interface': 0.44305837743833826, 'mach': 0.11254769596942187, 'mean': 0.19691545141064268, 'model': 0.18036731451851562, 'number': 0.07845045600431105, 'on': 0.047578484797422, 'phenomenon': 0.2731192355396403, 'presented': 0.17962403525120432, 'producing': 0.3950520390840711, 'provides': 0.3387105610060959, 'research': 0.2875844439235415, 'result': 0.066747412341137, 'shock': 0.22182330964418126, 'stagnation': 0.20793689516404892, 'successful': 0.4329544232897724, 'tailored': 0.5619808910508631, 'technique': 0.2393283689727511, 'temperature': 0.14343792139007638, 'theory': 0.10126360623697798, 'tunnel': 0.25989432384439404, 'various': 0.19047126866708147}
======================================================================
4     12       0.03239199196622085   some structural and aerelastic considerations of high speed flight .


Vector Representation for the Rank 4 With Document ID 12


{'acrothermoelasticity': 0.5754887502163468, 'aeroelastic': 0.5063865293673488, 'aeronautical': 0.38499752796799536, 'aircraft': 0.3409975204723399, 'alleviating': 0.5754887502163468, 'analytical': 0.24510287777053558, 'another': 0.32302094422766553, 'art': 0.4882138804505711, 'attacking': 0.5754887502163468, 'available': 0.2273761286881724, 'avenue': 0.5204244381420449, 'boundary': 0.08893771596118338, 'combined': 0.27669521436564537, 'concerned': 0.2953511086593236, 'demand': 0.4882138804505711, 'design': 0.19717684323293277, 'discussed': 0.1526234614487881, 'discussion': 0.24387120953351712, 'dominating': 0.5754887502163468, 'engineer': 0.4882138804505711, 'experimental': 0.12344084813192648, 'factor': 0.3189316829643157, 'failure': 0.3001671898448374, 'finally': 0.28445171299870836, 'flight': 0.2748236147404805, 'from': 0.0654778691891005, 'fundamental': 0.3166622706901821, 'heat': 0.13528517773688292, 'high': 0.24861669438432416, 'input': 0.4009390106847955, 'interrelation': 0.5204244381420449, 'into': 0.16843587669615823, 'largely': 0.35523150191913927, 'layer': 0.10031916428784036, 'load': 0.19924036210699853, 'matter': 0.4882138804505711, 'meet': 0.4653601260677431, 'method': 0.09016395214855977, 'mode': 0.2515650575245636, 'one': 0.13374258538491338, 'origin': 0.42090368268483946, 'presented': 0.11480297289695095, 'problem': 0.11976965319858021, 'research': 0.26631861515333216, 'respect': 0.2615979586158803, 'speed': 0.23267065987962346, 'state': 0.2529230565753127, 'structural': 0.41548459161682993, 'structure': 0.3120136511843358, 'subject': 0.2930483094538725, 'suggested': 0.2730836374538286, 'summarized': 0.3780852563019674, 'summary': 0.3603585072196042, 'thermal': 0.3133628759364394, 'these': 0.10276369593045806, 'to': 0.014739876826450955, 'tool': 0.39256906491107807, 'transfer': 0.16207720315867485, 'under': 0.16702980441552476, 'upon': 0.23574607446188983, 'well': 0.17083608978255838}
======================================================================
5     430       0.030811769765415446   calibration of the flow in the mach 4 working section of the 4ft . x 3ft . high supersonic speed wind tunnel at rae bedford .


Vector Representation for the Rank 5 With Document ID 430


{'angle': 0.163564324255595, 'distribution': 0.12607535993592625, 'flow': 0.06220061601834868, 'ft': 0.46965022359082137, 'high': 0.1639777441416276, 'humidity': 0.5271982855734489, 'mach': 0.16307374923830095, 'nozzle': 0.24553235789630273, 'number': 0.07845045600431105, 'presented': 0.12397011415191703, 'pressure': 0.0834887895608359, 'range': 0.13837168420922066, 'section': 0.20322597653563415, 'speed': 0.1534603701070292, 'supersonic': 0.15993055680978174, 'total': 0.23833663006222613, 'tunnel': 0.17936980955453063, 'wind': 0.21074975241888858, 'working': 0.37839647016748407, 'x': 0.23448049951385272}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     429       0.027516213737445568   a description of the r. a. e.  high speed supersonic tunnel .


Vector Representation for the Rank 1 With Document ID 429


{'account': 0.5319438365869127, 'completion': 0.6770578243679968, 'described': 0.5167749295863688, 'design': 0.5118964236564693, 'development': 0.5319438365869127, 'feature': 0.5530125726962148, 'given': 0.45808345586977395, 'high': 0.4861750090617886, 'interesting': 0.5872346990582913, 'more': 0.4983527811087177, 'nearing': 0.7265856778509625, 'noted': 0.6015912922792392, 'now': 0.5852307160277201, 'philosophy': 0.6770578243679968, 'principal': 0.5893319234769109, 'problem': 0.46796840661286304, 'reviewed': 0.5872346990582913, 'speed': 0.4806478272635384, 'supersonic': 0.48404809600525, 'tunnel': 0.4942639810340518}
======================================================================
2     320       0.024250961143392143   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 2 With Document ID 320


{'accurate': 0.5618011772797783, 'attention': 0.5880409419101723, 'drawn': 0.6330114612824701, 'previous': 0.5701493459299061, 'problem': 0.47744427105224063, 'solution': 0.4649972675032589, 'to': 0.4071860442032682}
======================================================================
3     12       0.02196194528197233   some structural and aerelastic considerations of high speed flight .


Vector Representation for the Rank 3 With Document ID 12


{'acrothermoelasticity': 0.6234408380037073, 'aeroelastic': 0.6069974515404812, 'aeronautical': 0.5494801944367897, 'aircraft': 0.5393907887075574, 'alleviating': 0.6234408380037073, 'analytical': 0.49516431448152587, 'another': 0.5254169963250277, 'art': 0.5895552580861185, 'attacking': 0.6234408380037073, 'available': 0.4882816783421476, 'avenue': 0.6020614174166771, 'boundary': 0.434531201134743, 'combined': 0.5074304415963526, 'concerned': 0.5146738301997285, 'demand': 0.5895552580861185, 'design': 0.4765564210774396, 'discussed': 0.45925800306665154, 'discussion': 0.4946861035991785, 'dominating': 0.6234408380037073, 'engineer': 0.5895552580861185, 'experimental': 0.44792748171031505, 'factor': 0.5303708565699987, 'failure': 0.5165437350685561, 'finally': 0.5104420009950285, 'flight': 0.5123406421286423, 'from': 0.4254226167875734, 'fundamental': 0.522948160325587, 'heat': 0.4525261935557311, 'high': 0.5013728510465819, 'input': 0.5556696781685296, 'interrelation': 0.6020614174166771, 'into': 0.46539737470928877, 'largely': 0.5379231556555863, 'layer': 0.4389501934275516, 'load': 0.47735760856596027, 'matter': 0.5895552580861185, 'meet': 0.5806819968296468, 'method': 0.43500730295462187, 'mode': 0.4976733380880304, 'one': 0.451927262425118, 'origin': 0.5634212163879683, 'presented': 0.4445737166187319, 'problem': 0.4465020935127639, 'research': 0.5034015947722292, 'respect': 0.5015687397385568, 'speed': 0.49487089435122894, 'state': 0.498200598518045, 'structural': 0.5698391379535123, 'structure': 0.5275429477195778, 'subject': 0.5137797390745296, 'suggested': 0.5060282008550909, 'summarized': 0.546796416912058, 'summary': 0.5399137807726797, 'thermal': 0.5280944751971939, 'these': 0.4398993139769068, 'to': 0.4060101488424705, 'tool': 0.5524199401032384, 'transfer': 0.462928538709848, 'under': 0.4648514492354017, 'upon': 0.4915314164074389, 'well': 0.4663292880146507}
======================================================================
4     238       0.021186495365798995   on a determination of the pitot-static tube factor at low reynolds numbers, with special reference to the measurement of low air speeds .


Vector Representation for the Rank 4 With Document ID 238


{'anemometer': 0.6587427378194435, 'calibration': 0.6587427378194435, 'enquiry': 0.7629175091161123, 'instrument': 0.6731548833417484, 'low': 0.5183014603468571, 'provide': 0.5711122412777057, 'reason': 0.6528421050984972, 'speed': 0.4896196942214549, 'standard': 0.6128388855009328, 'to': 0.40567748101428813}
======================================================================
5     578       0.01891523703225486   dissociation scaling for nonequilibrium blunt nose flows .


Vector Representation for the Rank 5 With Document ID 578


{'air': 0.4858199411207257, 'analysis': 0.4695763134953603, 'at': 0.42709624410055674, 'blade': 0.5572260547146666, 'characteristic': 0.4879789105721722, 'compressor': 0.6353350038875814, 'considered': 0.4775762674908278, 'efficiency': 0.5916248105934715, 'high': 0.47953940507568715, 'intermediate': 0.6300555295662313, 'lowspeed': 0.6725956865187944, 'more': 0.4907794705460089, 'multiple': 0.6016597564463906, 'one': 0.4700536892732316, 'operating': 0.5642956893711643, 'operation': 0.5674980997784189, 'part': 0.5102314863806159, 'performance': 0.5469133939337625, 'poor': 0.6934873330475382, 'pressure': 0.4404972558130974, 'principal': 0.574753083511616, 'problem': 0.483512873712725, 'ratio': 0.46536658080132304, 'row': 0.6016597564463906, 'speed': 0.511389755104936, 'stacking': 0.6437532785677624, 'stage': 0.5658660945699673, 'stall': 0.5947085025209993, 'stalled': 0.6557239594369391, 'study': 0.4910436669822318, 'surge': 0.6437532785677624, 'valued': 0.6557239594369391, 'were': 0.4649397996352611}
======================================================================
========================================================================================================================================================================


Query No: 3

Query Vector for weight (Version 1) are:
[('composite', 0.09387218755408672),
 ('conduction', 0.09387218755408672),
 ('far', 0.09387218755408672),
 ('heat', 0.07215220853242434),
 ('problem', 0.04343995804332474),
 ('slab', 0.09387218755408672),
 ('so', 0.09387218755408672),
 ('solved', 0.09387218755408672)]

Query Vector for weight (Version 2) are:
[('composite', 0.07927461139896373),
 ('conduction', 0.07927461139896373),
 ('far', 0.07927461139896373),
 ('heat', 0.07250110412252518),
 ('problem', 0.06354701455287709),
 ('slab', 0.07927461139896373),
 ('so', 0.07927461139896373),
 ('solved', 0.07927461139896373)]

Ranks  Document Number   Scores Titles


1     5       0.1025143597741058   one-dimensional transient heat conduction into a double-layer slab subjected to a linear heat input for a small time internal .


Vector Representation for the Rank 1 With Document ID 5


{'aerodynamic': 0.19814096454326377, 'analytic': 0.3488145151546617, 'at': 0.055861380633815266, 'composite': 0.44305837743833826, 'conduction': 0.3093937822796063, 'during': 0.2875844439235415, 'example': 0.2058861729589721, 'exposed': 0.42391612831509007, 'heat': 0.2116710823907653, 'heating': 0.36885509251999693, 'may': 0.15419672192711542, 'occur': 0.26739815197031136, 'one': 0.14442207513234676, 'presented': 0.12397011415191703, 'rate': 0.28269988518058486, 'slab': 0.4014093514806447, 'solution': 0.10854665920362061, 'surface': 0.12634218584411033, 'to': 0.009721840107770649, 'transient': 0.3296722660314134, 'triangular': 0.36885503908586875, 'type': 0.17789496875257943}
======================================================================
2     485       0.09143172628501331   linear heat flow in a composite slab .


Vector Representation for the Rank 2 With Document ID 485


{'case': 0.11555798590132785, 'composite': 0.44305837743833826, 'conduction': 0.3093937822796063, 'considered': 0.15993055680978174, 'determined': 0.19938423935311986, 'external': 0.25947395655495925, 'function': 0.2535906563998364, 'heat': 0.14608784514803438, 'linear': 0.2335429550964559, 'position': 0.26334458874487165, 'prescribed': 0.3488145151546617, 'slab': 0.4014093514806447, 'surface': 0.12634218584411033, 'temperature': 0.20783152798066645, 'throughout': 0.33559078227780864, 'time': 0.19103750478445003, 'to': 0.009721840107770649, 'ture': 0.5271982855734489, 'two': 0.1051403770694433}
======================================================================
3     181       0.06871425278141961   some problems on heat conduction in stratiform bodies .


Vector Representation for the Rank 3 With Document ID 181


{'applied': 0.19160750329564033, 'arising': 0.3453126223855793, 'body': 0.13961047050608286, 'calculation': 0.17361674072744135, 'case': 0.11555798590132785, 'class': 0.3387105610060959, 'complicated': 0.4082757719609241, 'composite': 0.44305837743833826, 'conduction': 0.3093937822796063, 'deduction': 0.5619808910508631, 'difficulty': 0.360269433606657, 'general': 0.1639777441416276, 'give': 0.20322597653563415, 'heat': 0.14608784514803438, 'idea': 0.37839647016748407, 'infinite': 0.26074486069362346, 'lead': 0.26203487688769017, 'multilayer': 0.6214421478571256, 'on': 0.047578484797422, 'paper': 0.16692885196679205, 'present': 0.1603267905873086, 'problem': 0.12933338923453824, 'question': 0.3835971206320758, 'solides': 0.6214421478571256, 'special': 0.25947395655495925, 'specific': 0.2761295254715463, 'to': 0.014086267179562515, 'usually': 0.3387105610060959}
======================================================================
4     509       0.040258151555959104   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 4 With Document ID 509


{'acted': 0.5271982855734489, 'at': 0.055861380633815266, 'by': 0.06275576151877217, 'change': 0.22302558106185744, 'condition': 0.1242304617275272, 'conduction': 0.3093937822796063, 'considers': 0.36885503908586875, 'derived': 0.19103750478445003, 'entry': 0.3164485331545604, 'heat': 0.14608784514803438, 'heated': 0.3524654687089807, 'heating': 0.2545706528709851, 'material': 0.26203487688769017, 'method': 0.09736364101196376, 'most': 0.23261554649289723, 're': 0.32685940877657377, 'severe': 0.3891335228376759, 'space': 0.36885503908586875, 'state': 0.2731192355396403, 'sublimation': 0.5271982855734489, 'such': 0.17789496875257943, 'suitable': 0.3049936147025652, 'surface': 0.12634218584411033, 'under': 0.18036731451851562, 'upon': 0.2545706528709851, 'vehicle': 0.2716527987994464}
======================================================================
5     281       0.030573866246648866   higher order approximations for relaxation oscillations .


Vector Representation for the Rank 5 With Document ID 281


{'asymptotic': 0.31403190967724753, 'by': 0.04331179236839078, 'can': 0.13535079247784257, 'carry': 0.4545132958903335, 'case': 0.11555798590132785, 'development': 0.36378109452860397, 'enough': 0.37349316648351, 'explicitly': 0.42391612831509007, 'ha': 0.11966097837637452, 'haag': 0.6214421478571256, 'indicates': 0.3028753722576236, 'involved': 0.3028753722576236, 'one': 0.14442207513234676, 'oscillation': 0.31893521336122166, 'out': 0.20793689516404892, 'paper': 0.16692885196679205, 'problem': 0.12933338923453824, 'quantity': 0.31168150346321444, 'relaxation': 0.3488145151546617, 'simple': 0.17549188555788003, 'solved': 0.2875844439235415, 'solving': 0.3524654687089807, 'such': 0.17789496875257943, 'to': 0.009721840107770649, 'treated': 0.2660255713229804}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     5       0.053021870683326956   one-dimensional transient heat conduction into a double-layer slab subjected to a linear heat input for a small time internal .


Vector Representation for the Rank 1 With Document ID 5


{'aerodynamic': 0.5041287615243675, 'analytic': 0.5833120351892043, 'at': 0.42935675818399677, 'composite': 0.63283988867217, 'conduction': 0.5625953090840068, 'during': 0.5511338760687907, 'example': 0.5081990907565628, 'exposed': 0.6227800875674897, 'heat': 0.49942742140135155, 'heating': 0.5732608455807672, 'may': 0.4810348012708999, 'occur': 0.5405254005034051, 'one': 0.47589794394599705, 'presented': 0.4651498516847835, 'rate': 0.5327915003622148, 'slab': 0.6109521306224008, 'solution': 0.45704438361110655, 'surface': 0.4663964434136795, 'to': 0.4051091058958636, 'transient': 0.5732522340845239, 'triangular': 0.5938439054769377, 'type': 0.4934889098794988}
======================================================================
2     485       0.04725029567217094   linear heat flow in a composite slab .


Vector Representation for the Rank 2 With Document ID 485


{'case': 0.459407414204706, 'composite': 0.6277726834718212, 'conduction': 0.5590568097296165, 'considered': 0.4822189895253167, 'determined': 0.5025018046200209, 'external': 0.533393436136526, 'function': 0.5174265330937424, 'heat': 0.4751025648231076, 'linear': 0.5200625206452891, 'position': 0.5353832964473187, 'prescribed': 0.5793226856696936, 'slab': 0.6063612603062777, 'surface': 0.4649514830794811, 'temperature': 0.4962375197289033, 'throughout': 0.5725244728917519, 'time': 0.49821081673277, 'to': 0.40499791838365384, 'ture': 0.6710283211911958, 'two': 0.45405180681789314}
======================================================================
3     181       0.039125421162851115   some problems on heat conduction in stratiform bodies .


Vector Representation for the Rank 3 With Document ID 181


{'applied': 0.49744353515700135, 'arising': 0.5756115083221334, 'body': 0.47100002639277916, 'calculation': 0.488294188316911, 'case': 0.45876794211171434, 'class': 0.5722539769672794, 'complicated': 0.6076319238784809, 'composite': 0.6253208973340816, 'conduction': 0.5573446936177807, 'deduction': 0.6857998970436128, 'difficulty': 0.5832179148301757, 'general': 0.4833921991644365, 'give': 0.5033522030648816, 'heat': 0.4742941473055401, 'idea': 0.592436564904029, 'infinite': 0.5326038937045354, 'lead': 0.5332599418038924, 'multilayer': 0.7160393968983785, 'on': 0.42419642068463786, 'paper': 0.4848930087578365, 'present': 0.48153547740298264, 'problem': 0.465773534147066, 'question': 0.595081397479316, 'solides': 0.7160393968983785, 'special': 0.5319575651944978, 'specific': 0.5404278885762452, 'to': 0.4064767343953059, 'usually': 0.5722539769672794}
======================================================================
4     320       0.024250961143392143   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 4 With Document ID 320


{'accurate': 0.5618011772797783, 'attention': 0.5880409419101723, 'drawn': 0.6330114612824701, 'previous': 0.5701493459299061, 'problem': 0.47744427105224063, 'solution': 0.4649972675032589, 'to': 0.4071860442032682}
======================================================================
5     509       0.02092280184673496   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 5 With Document ID 509


{'acted': 0.6725109590639371, 'at': 0.42887497707735966, 'by': 0.4291629329558567, 'change': 0.5152828388370986, 'condition': 0.4642152358926964, 'conduction': 0.5599269167685637, 'considers': 0.5906626846244781, 'derived': 0.4987480708313855, 'entry': 0.5635735464703271, 'heat': 0.4755134071530064, 'heated': 0.5821908483832174, 'heating': 0.5315886160136986, 'material': 0.5354469040641762, 'method': 0.45032766592036005, 'most': 0.5202399313552581, 're': 0.5689549708377533, 'severe': 0.6011447161613533, 'space': 0.5906626846244781, 'state': 0.5411764545758323, 'sublimation': 0.6725109590639371, 'such': 0.4919546399789279, 'suitable': 0.557652452076105, 'surface': 0.46530679476160014, 'under': 0.4932326056594879, 'upon': 0.5315886160136986, 'vehicle': 0.5404184474020378}
======================================================================
========================================================================================================================================================================


Query No: 4

Query Vector for weight (Version 1) are:
[('assumption', 0.035760833353937795),
 ('based', 0.035760833353937795),
 ('can', 0.019212277908861708),
 ('chemical', 0.027486555631399748),
 ('chemically', 0.035760833353937795),
 ('criterion', 0.035760833353937795),
 ('developed', 0.035760833353937795),
 ('empirically', 0.035760833353937795),
 ('equilibrium', 0.035760833353937795),
 ('flow', 0.012531999063099031),
 ('gas', 0.027486555631399748),
 ('instantaneous', 0.035760833353937795),
 ('local', 0.035760833353937795),
 ('mixture', 0.035760833353937795),
 ('on', 0.019212277908861708),
 ('reacting', 0.035760833353937795),
 ('show', 0.035760833353937795),
 ('simplifying', 0.035760833353937795),
 ('solution', 0.027486555631399748),
 ('to', 0.014372135720624499),
 ('validity', 0.035760833353937795)]

Query Vector for weight (Version 2) are:
[('assumption', 0.02571133716644553),
 ('based', 0.02571133716644553),
 ('can', 0.022627658783776764),
 ('chemical', 0.024169497975111143),
 ('chemically', 0.02571133716644553),
 ('criterion', 0.02571133716644553),
 ('developed', 0.02571133716644553),
 ('empirically', 0.02571133716644553),
 ('equilibrium', 0.02571133716644553),
 ('flow', 0.021382847323631632),
 ('gas', 0.024169497975111143),
 ('instantaneous', 0.02571133716644553),
 ('local', 0.02571133716644553),
 ('mixture', 0.02571133716644553),
 ('on', 0.022627658783776764),
 ('reacting', 0.02571133716644553),
 ('show', 0.02571133716644553),
 ('simplifying', 0.02571133716644553),
 ('solution', 0.024169497975111143),
 ('to', 0.021725740674703915),
 ('validity', 0.02571133716644553)]

Ranks  Document Number   Scores Titles


1     1085       0.04955435239159394   note on the convergence of numerical solutions of the navier-stokes equations .


Vector Representation for the Rank 1 With Document ID 1085


{'applies': 0.3299332158936935, 'based': 0.1578280080047599, 'case': 0.10701289108437298, 'certain': 0.19717684323293277, 'condition': 0.11504406871162397, 'converge': 0.42090368268483946, 'convergence': 0.3336288129190638, 'criterion': 0.41548459161682993, 'dimension': 0.4618014086047822, 'equation': 0.10052002661977971, 'exceeds': 0.39256906491107807, 'fixed': 0.28445171299870836, 'flow': 0.05760110558725104, 'given': 0.10235101443118594, 'if': 0.2020778426627266, 'local': 0.19994028742732853, 'mesh': 0.7965784284662087, 'navier': 0.35523150191913927, 'not': 0.13528517773688292, 'number': 0.07264932871949845, 'numerical': 0.23646742681441385, 'on': 0.044060228048051424, 'reynolds': 0.1578280080047599, 'show': 0.17638660772417045, 'size': 0.28445171299870836, 'solution': 0.16457423377136887, 'steady': 0.2958321322011587, 'stokes': 0.3336288129190638, 'that': 0.043764358022771316, 'to': 0.009002945218177212, 'two': 0.13477128421868342, 'under': 0.16702980441552476, 'used': 0.13404871682332475, 'value': 0.11951380431411825, 'viscous': 0.2020778426627266}
======================================================================
2     1221       0.043331142468823795   steady flow of conducting fluids in channels under transverse magnetic fields, with consideration of hall effect .


Vector Representation for the Rank 2 With Document ID 1221


{'account': 0.25106876010190277, 'approximate': 0.1882429755844433, 'arbitrary': 0.24341411545136124, 'assumption': 0.21978804739357102, 'based': 0.1704307447358744, 'both': 0.16866193031101664, 'by': 0.04331179236839078, 'calculation': 0.17361674072744135, 'carried': 0.270211009225151, 'case': 0.11555798590132785, 'channel': 0.5638272909708307, 'conducting': 0.4735964499663502, 'cross': 0.26739815197031136, 'effect': 0.09218542078944494, 'electrically': 0.360269433606657, 'field': 0.1834313709581794, 'flow': 0.06220061601834868, 'fluid': 0.1921813145342394, 'fully': 0.3296722660314134, 'gas': 0.19392614336958838, 'hall': 0.5025196342446008, 'incompressible': 0.21074975241888858, 'into': 0.1818856631878697, 'ionized': 0.4545132958903335, 'laminar': 0.16233588617078312, 'magnetic': 0.44828997726494435, 'making': 0.36885503908586875, 'method': 0.09736364101196376, 'minimum': 0.3028753722576236, 'nonconducting': 0.4677370287671866, 'number': 0.11366923045277778, 'numerical': 0.1844775358789806, 'on': 0.047578484797422, 'out': 0.20793689516404892, 'presence': 0.270211009225151, 'presented': 0.12397011415191703, 'principle': 0.33559078227780864, 'rectangular': 0.27924930419983346, 'reynolds': 0.24694224337658496, 'section': 0.20322597653563415, 'simplifying': 0.4014093514806447, 'small': 0.15419672192711542, 'solution': 0.10854665920362061, 'steady': 0.23079027635009564, 'straight': 0.3387105610060959, 'taken': 0.2716527987994464, 'that': 0.06847497403473064, 'through': 0.20257362008142774, 'transverse': 0.2858513655793169, 'uniform': 0.21219154199318402, 'wall': 0.18239781074082373}
======================================================================
3     1123       0.039486051007495346   an extension of donnell's equation for a circular cylindrical shell .


Vector Representation for the Rank 3 With Document ID 1123


{'agreement': 0.17549188555788003, 'approach': 0.25222024665695203, 'axial': 0.22725227141027599, 'between': 0.1415028515150645, 'buckling': 0.22639010877305443, 'can': 0.13535079247784257, 'circular': 0.30028767096120135, 'classical': 0.4450613362496161, 'compression': 0.2875844439235415, 'compressive': 0.3562787391713667, 'computation': 0.30080817680039457, 'critical': 0.3741450691762891, 'cylinder': 0.26577924259061636, 'cylindrical': 0.2393283689727511, 'donnell': 0.42391612831509007, 'donnells': 0.4157399959776291, 'easy': 0.4833773851213525, 'equation': 0.15727652646426243, 'equilibrium': 0.24553235789630273, 'from': 0.07070634769260985, 'furthermore': 0.3835971206320758, 'good': 0.2000126997486968, 'involved': 0.3028753722576236, 'known': 0.2373562255588418, 'obtained': 0.15386244767713833, 'physical': 0.2841526078838075, 'property': 0.2238544228750751, 'pure': 0.3488145151546617, 'readily': 0.3950520390840711, 'reduces': 0.37839647016748407, 'relation': 0.24237429107975692, 'shearing': 0.42391612831509007, 'shell': 0.2373562255588418, 'show': 0.19047126866708147, 'simple': 0.17549188555788003, 'simplifying': 0.4014093514806447, 'solution': 0.15727652646426243, 'still': 0.3524654687089807, 'stress': 0.27762588718919184, 'succeeded': 0.6214421478571256, 'tedious': 0.4833773851213525, 'that': 0.04725898923138793, 'thin': 0.21219154199318402, 'to': 0.009721840107770649, 'torsion': 0.36885503908586875, 'under': 0.26133963885470796, 'well': 0.1844775358789806}
======================================================================
4     320       0.039187386506061045   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 4 With Document ID 320


{'accurate': 0.270211009225151, 'attention': 0.31403190967724753, 'drawn': 0.3891335228376759, 'previous': 0.2841526078838075, 'problem': 0.12933338923453824, 'solution': 0.10854665920362061, 'to': 0.014086267179562515}
======================================================================
5     437       0.037990977835128496   hypervelocity stagnation point heat transfer .


Vector Representation for the Rank 5 With Document ID 437


{'air': 0.1638426315893216, 'analysis': 0.13283120624992406, 'approximated': 0.34157954394707607, 'atom': 0.38499752796799536, 'can': 0.1253420912509042, 'charge': 0.42090368268483946, 'contribution': 0.34587469861049364, 'diffusion': 0.3052941951453023, 'e': 0.31977800375441295, 'effect': 0.08536864256989969, 'electrical': 0.35523150191913927, 'equilibrium': 0.2273761286881724, 'field': 0.1698672849712528, 'fourcomponent': 0.5754887502163468, 'gas': 0.24857886298271317, 'ii': 0.4331495683762693, 'iii': 0.4653601260677431, 'includes': 0.326401922980584, 'including': 0.2335694722805302, 'ionized': 0.42090368268483946, 'iv': 0.4882138804505711, 'local': 0.19994028742732853, 'low': 0.18759403405361602, 'magnetic': 0.28651523187277417, 'molecule': 0.326401922980584, 'n': 0.487439965921816, 'neglected': 0.4189756923801347, 'no': 0.2571922667550831, 'partially': 0.39256906491107807, 're': 0.302689338503849, 'separation': 0.21044778843644407, 'specific': 0.25571074646193387, 'thermal': 0.2263892711532442, 'thermochemical': 0.4882138804505711, 'tions': 0.5754887502163468, 'v': 0.326401922980584}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     320       0.0402684943326255   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 1 With Document ID 320


{'accurate': 0.5618011772797783, 'attention': 0.5880409419101723, 'drawn': 0.6330114612824701, 'previous': 0.5701493459299061, 'problem': 0.47744427105224063, 'solution': 0.4649972675032589, 'to': 0.4071860442032682}
======================================================================
2     1085       0.033678812789023994   note on the convergence of numerical solutions of the navier-stokes equations .


Vector Representation for the Rank 2 With Document ID 1085


{'applies': 0.5589463612020397, 'based': 0.4760341376971451, 'case': 0.45155379579924376, 'certain': 0.4949905624393932, 'condition': 0.45542284080146045, 'converge': 0.6027716687999342, 'convergence': 0.5607267266558804, 'criterion': 0.5978102771494604, 'dimension': 0.6198614977962108, 'equation': 0.44842583798623703, 'exceeds': 0.589121377849413, 'fixed': 0.537035504583447, 'flow': 0.42774951321438937, 'given': 0.44930792210510934, 'if': 0.4973516342808837, 'local': 0.4963218603443172, 'mesh': 0.7792472762780542, 'navier': 0.5711338898129469, 'not': 0.46517405853667415, 'number': 0.43499904188930083, 'numerical': 0.512581039534955, 'on': 0.4212261530049351, 'reynolds': 0.4760341376971451, 'show': 0.48497480129906606, 'size': 0.537035504583447, 'solution': 0.47550237196430745, 'steady': 0.5408442990213085, 'stokes': 0.5607267266558804, 'that': 0.4210836166926101, 'to': 0.40433719708594495, 'two': 0.46416398013544674, 'under': 0.4804671319685806, 'used': 0.46457838961487047, 'value': 0.4575761499420005, 'viscous': 0.4973516342808837}
======================================================================
3     1011       0.025934714092990776   free-flight measurements of the static and dynamic


Vector Representation for the Rank 3 With Document ID 1011


{'air': 0.5119489767252806, 'also': 0.4611214864401361, 'atmosphere': 0.5321604552867548, 'based': 0.4801993247708569, 'bureau': 0.6364698658858337, 'by': 0.4203811613212375, 'calculated': 0.4878122707460959, 'chart': 0.6377520352424009, 'chemical': 0.5489106834747157, 'composition': 0.5858990103751137, 'data': 0.4756320434434098, 'equilibrium': 0.5155397715546973, 'exponent': 0.5994815389854357, 'from': 0.43327217369582455, 'included': 0.5103391161148044, 'isentropic': 0.5888905607691037, 'k': 0.5593864905510157, 'national': 0.5994815389854357, 'on': 0.4223889319986674, 'prepared': 0.6274621281290151, 'pressure': 0.4392871870570768, 'property': 0.5053388201135516, 'relating': 0.5735715297076205, 'showing': 0.5757540859480952, 'sound': 0.5500808366287394, 'speed': 0.4722136025442064, 'standard': 0.5715009498418562, 'temperature': 0.4674973547750857, 'thermodynamic': 0.6184951495975157, 'these': 0.4522187356272775, 'to': 0.4061514545690097}
======================================================================
4     1221       0.023674621433502522   steady flow of conducting fluids in channels under transverse magnetic fields, with consideration of hall effect .


Vector Representation for the Rank 4 With Document ID 1221


{'account': 0.5023448839626615, 'approximate': 0.476734777696582, 'arbitrary': 0.4992245685629395, 'assumption': 0.48959371208805563, 'based': 0.469473855634542, 'both': 0.4687528216556827, 'by': 0.4176554835510348, 'calculation': 0.47077258507395964, 'carried': 0.5101479705135652, 'case': 0.44710569587881055, 'channel': 0.6230694190397839, 'conducting': 0.5873710028675488, 'cross': 0.5090013461815166, 'effect': 0.43757817655177633, 'electrically': 0.5468591049033809, 'field': 0.474773390238623, 'flow': 0.425355264534784, 'fluid': 0.478340189865977, 'fully': 0.5343865712285285, 'gas': 0.4790514464341618, 'hall': 0.6048455316975654, 'incompressible': 0.4859093697986018, 'into': 0.47414330275849076, 'ionized': 0.5852763781065509, 'laminar': 0.4661740928117911, 'magnetic': 0.5773588940997582, 'making': 0.5503589142630259, 'method': 0.43968901004452826, 'minimum': 0.5234631692779028, 'nonconducting': 0.5906668592093588, 'number': 0.44497144711839115, 'numerical': 0.47519984563427536, 'on': 0.4193947447055342, 'out': 0.4847627454665533, 'presence': 0.5101479705135652, 'presented': 0.45053478952365966, 'principle': 0.536799176676624, 'rectangular': 0.513832312803019, 'reynolds': 0.49769882311221003, 'section': 0.48284240133378675, 'simplifying': 0.5636292523296786, 'small': 0.46285626936082447, 'solution': 0.444247620596924, 'steady': 0.49407862628219557, 'straight': 0.5380709135179823, 'taken': 0.5107356971053559, 'that': 0.42709104883942534, 'through': 0.48257647678952664, 'transverse': 0.5165235564508681, 'uniform': 0.4864970963903926, 'wall': 0.47435207298485255}
======================================================================
5     1189       0.022808032390861082   nonequilibrium flow past a wedge .


Vector Representation for the Rank 5 With Document ID 1189


{'amount': 0.5639812278496725, 'attached': 0.5286368618596662, 'both': 0.4640551075997079, 'by': 0.416449127051834, 'characterized': 0.5477866975081845, 'chemically': 0.5835790113282681, 'concave': 0.5726168911980698, 'contained': 0.5550566180233181, 'convex': 0.5726168911980698, 'depending': 0.5437089363748653, 'describing': 0.5550566180233181, 'dissociation': 0.5864080591890604, 'easily': 0.5456840603668864, 'either': 0.5394295651120912, 'energy': 0.5243580567601877, 'entropy': 0.5500344554598122, 'equilibrium': 0.5338484144710529, 'exact': 0.48470155396692705, 'example': 0.47819228048593976, 'field': 0.46966430528941155, 'flow': 0.43390776639181255, 'freestream': 0.6381693627228264, 'gas': 0.47365005224966283, 'identifiable': 0.6360138033199166, 'illustrating': 0.568266496105144, 'layer': 0.4590544009982829, 'nonreacting': 0.6360138033199166, 'numerical': 0.5176377537791284, 'obtained': 0.4403294118196675, 'on': 0.4180695486972668, 'out': 0.4789711120293774, 'parameter': 0.47170119151424383, 'past': 0.5026218260316695, 'presence': 0.5026218260316695, 'presentation': 0.5609965755900106, 'presented': 0.44708186955115403, 'reacting': 0.5835790113282681, 'regime': 0.5263087596797719, 'relative': 0.5158317041134954, 'relaxation': 0.5324741822850606, 'result': 0.425349601250439, 'shock': 0.4581428655328161, 'shown': 0.4518581474150687, 'solution': 0.4412242876744936, 'straight': 0.5286368618596662, 'these': 0.44214443933203046, 'to': 0.40529972055542984, 'value': 0.44901382954020097, 'wave': 0.462433899112719, 'wedge': 0.5158317041134954}
======================================================================
========================================================================================================================================================================


Query No: 5

Query Vector for weight (Version 1) are:
[('aerodynamic', 0.07215220853242434),
 ('applicable', 0.09387218755408672),
 ('chemical', 0.07215220853242434),
 ('hypersonic', 0.09387218755408672),
 ('kinetic', 0.09387218755408672),
 ('problem', 0.04343995804332474),
 ('system', 0.09387218755408672),
 ('to', 0.03772685626663931)]

Query Vector for weight (Version 2) are:
[('aerodynamic', 0.07250110412252518),
 ('applicable', 0.07927461139896373),
 ('chemical', 0.07250110412252518),
 ('hypersonic', 0.07927461139896373),
 ('kinetic', 0.07927461139896373),
 ('problem', 0.06354701455287709),
 ('system', 0.07927461139896373),
 ('to', 0.061765349091008205)]

Ranks  Document Number   Scores Titles


1     1305       0.027686501952076226   a proposed programme of wind tunnel tests at hypersonic speeds to investigate the lifting properties of geometrically slender shapes .


Vector Representation for the Rank 1 With Document ID 1305


{'aerodynamic': 0.19814096454326377, 'aim': 0.4545132958903335, 'at': 0.055861380633815266, 'based': 0.1704307447358744, 'body': 0.13961047050608286, 'built': 0.5619808910508631, 'by': 0.04331179236839078, 'compromise': 0.4677370287671866, 'configuration': 0.2488111440108371, 'described': 0.22220467087088383, 'enforced': 0.5619808910508631, 'from': 0.07070634769260985, 'generated': 0.3387105610060959, 'geometric': 0.4157399959776291, 'ha': 0.11966097837637452, 'heating': 0.2545706528709851, 'hypersonic': 0.19451572961012958, 'investigating': 0.4329544232897724, 'later': 0.4157399959776291, 'lift': 0.20521335021328854, 'lifting': 0.32685940877657377, 'may': 0.15419672192711542, 'model': 0.18036731451851562, 'on': 0.06893790079097756, 'programme': 0.6585580149026898, 'shape': 0.17549188555788003, 'simple': 0.17549188555788003, 'slender': 0.2413469199941321, 'speed': 0.1534603701070292, 'test': 0.15875271962933116, 'that': 0.04725898923138793, 'up': 0.2058861729589721}
======================================================================
2     320       0.02739724057939687   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 2 With Document ID 320


{'accurate': 0.270211009225151, 'attention': 0.31403190967724753, 'drawn': 0.3891335228376759, 'previous': 0.2841526078838075, 'problem': 0.12933338923453824, 'solution': 0.10854665920362061, 'to': 0.014086267179562515}
======================================================================
3     650       0.02711217358112592   some design problems of hovercraft .


Vector Representation for the Rank 3 With Document ID 650


{'aerodynamic': 0.19814096454326377, 'analysis': 0.14343792139007638, 'angle': 0.163564324255595, 'considered': 0.15993055680978174, 'cushion': 0.5271982855734489, 'drag': 0.19938423935311986, 'dynamic': 0.2660255713229804, 'each': 0.22900303544888745, 'economics': 0.6214421478571256, 'effect': 0.13357023494580939, 'examined': 0.29681748236510425, 'ground': 0.32685940877657377, 'influence': 0.23638689930953372, 'jet': 0.335714298746996, 'lift': 0.20521335021328854, 'machine': 0.37839647016748407, 'on': 0.047578484797422, 'operation': 0.3453126223855793, 'optimum': 0.3387105610060959, 'over': 0.14813042879608032, 'parameter': 0.18879464604080065, 'performance': 0.3028753722576236, 'peripheral': 0.5271982855734489, 'power': 0.24237429107975692, 'pressure': 0.0834887895608359, 'ratio': 0.195256628072377, 'related': 0.3071654891969682, 'requirement': 0.3296722660314134, 'simple': 0.17549188555788003, 'stability': 0.23261554649289723, 'structural': 0.3241358638258134, 'system': 0.24341411545136124, 'then': 0.2058861729589721, 'thickness': 0.1813765551041639, 'to': 0.009721840107770649, 'various': 0.19047126866708147, 'wave': 0.16439316606881269, 'weight': 0.3241358638258134}
======================================================================
4     925       0.026641728293507312   factors affecting loads at hypersonic speeds .


Vector Representation for the Rank 4 With Document ID 925


{'aerodynamic': 0.19814096454326377, 'aircraft': 0.2660255713229804, 'at': 0.055861380633815266, 'blunt': 0.22812318711727908, 'both': 0.16866193031101664, 'boundary': 0.09603948854195138, 'brief': 0.3296722660314134, 'can': 0.13535079247784257, 'characteristic': 0.1813765551041639, 'component': 0.2716527987994464, 'configuration': 0.2488111440108371, 'current': 0.360269433606657, 'deal': 0.3453126223855793, 'designer': 0.44305837743833826, 'discussed': 0.1648106095218505, 'effect': 0.09218542078944494, 'employ': 0.44305837743833826, 'estimating': 0.360269433606657, 'give': 0.20322597653563415, 'hypersonic': 0.19451572961012958, 'information': 0.29681748236510425, 'interference': 0.29681748236510425, 'layer': 0.10832975779775116, 'load': 0.31173720439012015, 'method': 0.09736364101196376, 'on': 0.047578484797422, 'paper': 0.24186824538519194, 'several': 0.21666826866528383, 'slender': 0.2413469199941321, 'speed': 0.1534603701070292, 'summary': 0.3891335228376759, 'touch': 0.5619808910508631, 'upon': 0.2545706528709851, 'various': 0.19047126866708147}
======================================================================
5     1032       0.025572069704237636   on the conservativeness of various distributed force systems .


Vector Representation for the Rank 5 With Document ID 1032


{'applicable': 0.23574607446188983, 'buckling': 0.2901918990988599, 'cantilever': 0.38499752796799536, 'cause': 0.2977226582022197, 'change': 0.285879172313337, 'character': 0.3375047528367761, 'column': 0.3166622706901821, 'conservative': 0.6427251885284571, 'conservativeness': 0.5754887502163468, 'constant': 0.1638426315893216, 'could': 0.24762502642954715, 'determination': 0.2679566321533636, 'determining': 0.2748689038193916, 'directional': 0.44763337698537986, 'discussed': 0.1526234614487881, 'eight': 0.4331495683762693, 'employed': 0.26631861515333216, 'end': 0.29081038653619173, 'example': 0.1906616356350296, 'force': 0.17331108777644477, 'generally': 0.27133761090628217, 'instability': 0.4121009265608575, 'kinetic': 0.3336288129190638, 'large': 0.15865985864180726, 'load': 0.32620196226288284, 'loading': 0.3540887685506807, 'magnitude': 0.2346503190209996, 'make': 0.2977226582022197, 'method': 0.12480289020385103, 'necessity': 0.42090368268483946, 'nonconservative': 0.4882138804505711, 'nongyroscopic': 0.5754887502163468, 'only': 0.15458506753150733, 'otherwise': 0.38499752796799536, 'problem': 0.11976965319858021, 'reference': 0.38299521744021364, 'shown': 0.12644930095033347, 'small': 0.14279443242670897, 'statical': 0.5754887502163468, 'system': 0.3690550389431708, 'tangential': 0.42090368268483946, 'that': 0.060577628187355376, 'time': 0.17691097273004497, 'usually': 0.3136641409190199, 'valid': 0.2679566321533636, 'whereas': 0.3375047528367761}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     320       0.04264064346845989   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 1 With Document ID 320


{'accurate': 0.5618011772797783, 'attention': 0.5880409419101723, 'drawn': 0.6330114612824701, 'previous': 0.5701493459299061, 'problem': 0.47744427105224063, 'solution': 0.4649972675032589, 'to': 0.4071860442032682}
======================================================================
2     533       0.01876121226943204   stagnation-point shock-detachment distance for flow around spheres and cylinders in air .


Vector Representation for the Rank 2 With Document ID 533


{'arbitrarily': 0.633153928549836, 'arc': 0.6109784688099826, 'author': 0.5310851791301352, 'bar': 0.657255429791618, 'cantilevered': 0.657255429791618, 'circular': 0.5139863511514744, 'deflection': 0.5393631047510348, 'discus': 0.5918480310403907, 'end': 0.5727175932707989, 'inclined': 0.633153928549836, 'initially': 0.5918480310403907, 'load': 0.518332485422561, 'problem': 0.47113338176716935, 'shape': 0.4965205610578357, 'subjected': 0.5518712767739752, 'to': 0.40534701338887325}
======================================================================
3     650       0.01689370874377457   some design problems of hovercraft .


Vector Representation for the Rank 3 With Document ID 650


{'aerodynamic': 0.4923193697861977, 'analysis': 0.4668317050777384, 'angle': 0.47620915427352095, 'considered': 0.4745160812569422, 'cushion': 0.6456363003415054, 'drag': 0.4928986459958475, 'dynamic': 0.5239486905101255, 'each': 0.5066988644195854, 'economics': 0.6895471291411022, 'effect': 0.4579419469798412, 'examined': 0.5382954957175909, 'ground': 0.5522928622887253, 'influence': 0.510139211345186, 'jet': 0.545630799453672, 'lift': 0.4956145903855658, 'machine': 0.5763054083021599, 'on': 0.4221681354080676, 'operation': 0.5608907262127273, 'optimum': 0.5578146427423119, 'over': 0.46901807440039683, 'parameter': 0.48796466082453793, 'performance': 0.5411180346024739, 'peripheral': 0.6456363003415054, 'power': 0.5129289031999936, 'pressure': 0.4388997421822175, 'ratio': 0.48470112518572905, 'related': 0.5431169190485163, 'requirement': 0.5536034504836699, 'simple': 0.4817665358329145, 'stability': 0.5083820334891286, 'structural': 0.5510238871728619, 'system': 0.5134133862088258, 'then': 0.495928077160007, 'thickness': 0.4845083665551241, 'to': 0.4045296748907044, 'various': 0.48874584579849983, 'wave': 0.4765953346579007, 'weight': 0.5510238871728619}
======================================================================
4     5       0.01650968507522481   one-dimensional transient heat conduction into a double-layer slab subjected to a linear heat input for a small time internal .


Vector Representation for the Rank 4 With Document ID 5


{'aerodynamic': 0.5041287615243675, 'analytic': 0.5833120351892043, 'at': 0.42935675818399677, 'composite': 0.63283988867217, 'conduction': 0.5625953090840068, 'during': 0.5511338760687907, 'example': 0.5081990907565628, 'exposed': 0.6227800875674897, 'heat': 0.49942742140135155, 'heating': 0.5732608455807672, 'may': 0.4810348012708999, 'occur': 0.5405254005034051, 'one': 0.47589794394599705, 'presented': 0.4651498516847835, 'rate': 0.5327915003622148, 'slab': 0.6109521306224008, 'solution': 0.45704438361110655, 'surface': 0.4663964434136795, 'to': 0.4051091058958636, 'transient': 0.5732522340845239, 'triangular': 0.5938439054769377, 'type': 0.4934889098794988}
======================================================================
5     1032       0.016165417077079886   on the conservativeness of various distributed force systems .


Vector Representation for the Rank 5 With Document ID 1032


{'applicable': 0.4994807480384074, 'buckling': 0.525956631757778, 'cantilever': 0.5624622686193882, 'cause': 0.5256337897186399, 'change': 0.5240847099664293, 'character': 0.5424211425592497, 'column': 0.5336259771693144, 'conservative': 0.6746479167590704, 'conservativeness': 0.6428462551916863, 'constant': 0.4691387442539231, 'could': 0.5044934594074185, 'determination': 0.513073043821895, 'determining': 0.5159899023848667, 'directional': 0.5888935087937711, 'discussed': 0.46440444935421793, 'eight': 0.5827815931736772, 'employed': 0.5123818291035387, 'end': 0.5227169311556682, 'example': 0.48045589806105216, 'force': 0.4731342682787194, 'generally': 0.5144997581212105, 'instability': 0.5788707569544589, 'kinetic': 0.5407855632468642, 'large': 0.46695170410528514, 'load': 0.5393919064901485, 'loading': 0.5513084353405939, 'magnitude': 0.4990183582778325, 'make': 0.5256337897186399, 'method': 0.4541701947315821, 'necessity': 0.5776140421476125, 'nonconservative': 0.6060177762909379, 'nongyroscopic': 0.6428462551916863, 'only': 0.46523221304407375, 'otherwise': 0.5624622686193882, 'problem': 0.45054071300950344, 'reference': 0.5662375404617097, 'shown': 0.45335940832179755, 'small': 0.4602567698569472, 'statical': 0.6428462551916863, 'system': 0.5577037891532575, 'tangential': 0.5776140421476125, 'that': 0.42629347693732467, 'time': 0.4746533571918807, 'usually': 0.5323608184894414, 'valid': 0.513073043821895, 'whereas': 0.5424211425592497}
======================================================================
========================================================================================================================================================================


Query No: 6

Query Vector for weight (Version 1) are:
[('behaviour', 0.07509775004326938),
 ('couette', 0.07509775004326938),
 ('do', 0.07509775004326938),
 ('experimental', 0.05772176682593947),
 ('flow', 0.026317198032507965),
 ('guide', 0.07509775004326938),
 ('theoretical', 0.07509775004326938),
 ('to', 0.03018148501331145),
 ('turbulent', 0.07509775004326938),
 ('we', 0.07509775004326938)]

Query Vector for weight (Version 2) are:
[('behaviour', 0.061220657276995306),
 ('couette', 0.061220657276995306),
 ('do', 0.061220657276995306),
 ('experimental', 0.05631065951416849),
 ('flow', 0.047436550890231625),
 ('guide', 0.061220657276995306),
 ('theoretical', 0.061220657276995306),
 ('to', 0.04852849718146322),
 ('turbulent', 0.061220657276995306),
 ('we', 0.061220657276995306)]

Ranks  Document Number   Scores Titles


1     271       0.06634169262556346   an experimental test of compressibility transformation for turbulent boundary layer .


Vector Representation for the Rank 1 With Document ID 271


{'application': 0.2488017333158573, 'boundary': 0.11605826108957569, 'by': 0.05233983836505397, 'co': 0.445740341606817, 'discussion': 0.3182369617027767, 'experimental': 0.16108273106391074, 'graphically': 0.5122785371621799, 'illustrated': 0.4215225079418247, 'insulated': 0.445740341606817, 'layer': 0.13091035265946915, 'light': 0.4132248292166513, 'mager': 0.6370891515767835, 'matting': 0.7509775004326937, 'measurement': 0.23224019116896719, 'theory': 0.12237131028024509, 'transformation': 0.3711920282390608, 'turbulent': 0.2512799144964561, 'various': 0.23017369797185824, 'wall': 0.22041738312547052, 'worker': 0.5652336036984639}
======================================================================
2     1146       0.04903248230452948   thermal buckling of cylinders .


Vector Representation for the Rank 2 With Document ID 1146


{'among': 0.5492534744193474, 'area': 0.3282769611482099, 'axial': 0.2746214484161083, 'both': 0.2038183526493618, 'buckling': 0.27357957389166593, 'circumferential': 0.4132248292166513, 'cylinder': 0.2216663818798242, 'difference': 0.31204612886278377, 'discussed': 0.19916425046207756, 'due': 0.24094451625367497, 'exist': 0.40190461444533776, 'experimental': 0.16108273106391074, 'future': 0.47024573618458926, 'indicated': 0.30479382682054995, 'investigation': 0.19815778000687356, 'on': 0.05749589356104888, 'result': 0.08066045255080079, 'reviewed': 0.4305425982496091, 'several': 0.26183128290606894, 'stress': 0.23154677291407538, 'that': 0.057109801336041384, 'theoretical': 0.20069251857152517, 'thermal': 0.2954241050090529, 'to': 0.011748290985597008, 'various': 0.23017369797185824, 'work': 0.28801626558942756}
======================================================================
3     1045       0.04033704738240432   the bending strength of pressurized cylinders .


Vector Representation for the Rank 3 With Document ID 1045


{'cylinder': 0.2216663818798242, 'data': 0.19422685815856466, 'discussion': 0.3182369617027767, 'experimental': 0.16108273106391074, 'loading': 0.2822233819620548, 'membrane': 0.5122785371621799, 'presented': 0.14981083400150466, 'pressurized': 0.47024573618458926, 'previously': 0.33368683078438854, 'term': 0.22616033318930492, 'theory': 0.12237131028024509}
======================================================================
4     137       0.03607041542947623   the generation of sound by aerodynamic means .


Vector Representation for the Rank 4 With Document ID 137


{'aerodynamic': 0.19814096454326377, 'cold': 0.4082757719609241, 'experimental': 0.13329773304442719, 'from': 0.07070634769260985, 'general': 0.1639777441416276, 'given': 0.11052385336735143, 'important': 0.25106876010190277, 'jet': 0.23169805688805684, 'lighthills': 0.4833773851213525, 'more': 0.1871501651331313, 'noise': 0.49545890178502827, 'prediction': 0.24770423239070574, 'radiated': 0.5619808910508631, 'related': 0.3071654891969682, 'relating': 0.36885503908586875, 'result': 0.066747412341137, 'subsonic': 0.22900303544888745, 'summary': 0.3891335228376759, 'then': 0.2058861729589721, 'theory': 0.10126360623697798, 'these': 0.11096948792961203, 'to': 0.014086267179562515, 'turbulent': 0.20793689516404892}
======================================================================
5     385       0.032149786160932316   on a generalised porous-wall ?couette type? flow .


Vector Representation for the Rank 5 With Document ID 385


{'above': 0.3135595227857385, 'below': 0.3231354623747757, 'by': 0.05233983836505397, 'can': 0.16356373665206167, 'considered': 0.19326698423974895, 'couette': 0.5122785371621799, 'different': 0.26753909008830196, 'fixed': 0.3711920282390608, 'flow': 0.0751659077259313, 'ha': 0.14460348843458312, 'interpretation': 0.47024573618458926, 'made': 0.14312040673633072, 'method': 0.11765842405816515, 'obtained': 0.1283250405536718, 'one': 0.1745258659461375, 'paper': 0.20172402601334635, 'parameter': 0.22814759486090103, 'porous': 0.40554237866270815, 'problem': 0.15629204698258145, 'quoted': 0.6370891515767835, 'recent': 0.33939463796662156, 'reference': 0.36107027355075894, 'result': 0.08066045255080079, 'rigorously': 0.6791219525543741, 'stated': 0.5122785371621799, 'to': 0.011748290985597008, 'type': 0.21497595461465033, 'wall': 0.22041738312547052}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     137       0.023339981345289654   the generation of sound by aerodynamic means .


Vector Representation for the Rank 1 With Document ID 137


{'aerodynamic': 0.501862647221912, 'cold': 0.6098912308435276, 'experimental': 0.4685272729336106, 'from': 0.4363495543082892, 'general': 0.4842996153887019, 'given': 0.45681940789536546, 'important': 0.5290723934732781, 'jet': 0.5191140735849062, 'lighthills': 0.6485003551343647, 'more': 0.4962123672528919, 'noise': 0.629424939991939, 'prediction': 0.5273427173303158, 'radiated': 0.6889097738194895, 'related': 0.5579112625041499, 'relating': 0.5896253549034505, 'result': 0.4343142980652856, 'subsonic': 0.5177285851335585, 'summary': 0.6000503573322369, 'then': 0.5058443954400459, 'theory': 0.4520587906812356, 'these': 0.45704850497435706, 'to': 0.40652272265315714, 'turbulent': 0.506898654931552}
======================================================================
2     1146       0.023303603039447045   thermal buckling of cylinders .


Vector Representation for the Rank 2 With Document ID 1146


{'among': 0.6349397893729108, 'area': 0.5404184474020378, 'axial': 0.5174676324375955, 'both': 0.48718204448756053, 'buckling': 0.5170219770294359, 'circumferential': 0.5767543745489275, 'cylinder': 0.49481642901750694, 'difference': 0.5334758089007223, 'discussed': 0.4851912809539179, 'due': 0.5030625322107244, 'exist': 0.5719122224317468, 'experimental': 0.46890214567650507, 'future': 0.6011447161613533, 'indicated': 0.530373681388334, 'investigation': 0.4847607694182272, 'on': 0.42459351420092595, 'result': 0.43450201157679064, 'reviewed': 0.5841619435466713, 'several': 0.5119967179492529, 'stress': 0.49904270540285517, 'that': 0.42442836563064573, 'theoretical': 0.4858449882210745, 'thermal': 0.5263658406164518, 'to': 0.40502525908018294, 'various': 0.49845538105673476, 'work': 0.5231971829492517}
======================================================================
3     271       0.022165310671638114   an experimental test of compressibility transformation for turbulent boundary layer .


Vector Representation for the Rank 3 With Document ID 271


{'application': 0.5100350333442017, 'boundary': 0.4513279166453765, 'by': 0.4231478124487881, 'co': 0.5971330854407515, 'discussion': 0.5407434515251854, 'experimental': 0.47124043489395906, 'graphically': 0.6265602621288759, 'illustrated': 0.5864225083907566, 'insulated': 0.5971330854407515, 'layer': 0.45789640139564014, 'light': 0.582752777705863, 'mager': 0.6817589938088772, 'matting': 0.7321272452549672, 'measurement': 0.5027105271276354, 'theory': 0.4541199252417034, 'transformation': 0.5641633547324798, 'turbulent': 0.511131033541652, 'various': 0.501796600022631, 'wall': 0.4974817730512452, 'worker': 0.6499801653361703}
======================================================================
4     418       0.02120979886816254   transition form laminar to turbulent shear flow .


Vector Representation for the Rank 4 With Document ID 418


{'also': 0.4620484992561947, 'behavior': 0.527737539327024, 'certain': 0.5017138095046755, 'character': 0.5741020576965439, 'common': 0.5807620345655666, 'dimensional': 0.47813555983145656, 'emphasized': 0.5986012382460496, 'examined': 0.5417913121208494, 'experimental': 0.4636770459762046, 'feature': 0.5390883744311994, 'flow': 0.4297135697321165, 'from': 0.4337768036259943, 'laminar': 0.4775487283331338, 'latter': 0.5446851987938972, 'layer': 0.45174970954366805, 'nonlinear': 0.542733415665831, 'process': 0.5233538540292597, 'random': 0.5807620345655666, 'recent': 0.5341648966536537, 'related': 0.5467346107932662, 'reviewed': 0.5701962751834495, 'shear': 0.5529705691778546, 'stability': 0.5111217011010334, 'stage': 0.5633504490192568, 'study': 0.4896628326630901, 'theory': 0.4483741708339421, 'three': 0.4970821450287198, 'to': 0.4062138701781363, 'transition': 0.553611869061374, 'turbulent': 0.4993325762644239, 'unsteadiness': 0.630911983821744, 'viscous': 0.5042419934141606}
======================================================================
5     286       0.019849492848678582   effect of roll on dynamic instability of symmetric missiles .


Vector Representation for the Rank 5 With Document ID 286


{'attempt': 0.575414410967581, 'by': 0.42382149172611616, 'certain': 0.5171069239223595, 'condition': 0.46832677094041564, 'describing': 0.6245517304160044, 'discussion': 0.5448395598257829, 'dynamic': 0.5463141006104051, 'experimental': 0.4733137714047885, 'extend': 0.6140234907802441, 'form': 0.48688703301081027, 'generalized': 0.5727175932707989, 'instability': 0.576822917500825, 'neater': 0.7417932663124371, 'note': 0.5374629231921529, 'on': 0.426168173145614, 'result': 0.43671108591627966, 'slightly': 0.5701666225677666, 'stability': 0.527938582384565, 'stating': 0.7090895669368236, 'to': 0.40534701338887325}
======================================================================
========================================================================================================================================================================


Query No: 7

Query Vector for weight (Version 1) are:
[('angle', 0.02591894215630066),
 ('at', 0.02591894215630066),
 ('attack', 0.02591894215630066),
 ('available', 0.015175718197747112),
 ('distribution', 0.02171154427744459),
 ('equivalent', 0.028247370357142074),
 ('forebody', 0.0409284663767219),
 ('lower', 0.028247370357142074),
 ('ogive', 0.0409284663767219),
 ('possible', 0.02171154427744459),
 ('pressure', 0.02591894215630066),
 ('relate', 0.028247370357142074),
 ('surface', 0.028247370357142074),
 ('to', 0.016448986738685466),
 ('zero', 0.028247370357142074)]

Query Vector for weight (Version 2) are:
[('angle', 0.024554507064490784),
 ('at', 0.024554507064490784),
 ('attack', 0.024554507064490784),
 ('available', 0.021496506897400736),
 ('distribution', 0.022924065624512546),
 ('equivalent', 0.024351624351624353),
 ('forebody', 0.02824489795918367),
 ('lower', 0.024351624351624353),
 ('ogive', 0.02824489795918367),
 ('possible', 0.022924065624512546),
 ('pressure', 0.024554507064490784),
 ('relate', 0.024351624351624353),
 ('surface', 0.024351624351624353),
 ('to', 0.022226129646719852),
 ('zero', 0.024351624351624353)]

Ranks  Document Number   Scores Titles


1     492       0.18071694073878994   prediction of ogive-forebody pressures at angles of attack .


Vector Representation for the Rank 1 With Document ID 492


{'angle': 0.24798988319115764, 'approximate': 0.17432308885010464, 'approximation': 0.1840627411405065, 'arbitrary': 0.22541452260545322, 'at': 0.07160436566891452, 'attack': 0.3308475657709923, 'being': 0.21980459174508976, 'body': 0.12928678150606152, 'by': 0.04010904208165435, 'calculated': 0.1728098810037261, 'distribution': 0.11675254337477482, 'forebody': 0.41029581399344117, 'lower': 0.23798399737957068, 'method': 0.09016395214855977, 'not': 0.13528517773688292, 'obtaining': 0.4426294338386114, 'ogive': 0.3780852563019674, 'on': 0.044060228048051424, 'over': 0.13717671971690412, 'present': 0.14847120469611422, 'pressure': 0.12658246390336925, 'suggested': 0.2730836374538286, 'surface': 0.16194823636556005, 'utilizing': 0.35041542073362547, 'various': 0.17638660772417045, 'zero': 0.18819815110911567}
======================================================================
2     3       0.07176536697595873   the boundary layer in simple shear flow past a flat plate .


Vector Representation for the Rank 2 With Document ID 3


{'boundary': 0.11605826108957569, 'equation': 0.13117246567543026, 'flow': 0.0751659077259313, 'gradient': 0.26464590763439305, 'incompressible': 0.2546790925496304, 'layer': 0.13091035265946915, 'no': 0.24246903847276882, 'presented': 0.14981083400150466, 'pressure': 0.10089145500469422, 'steady': 0.27889692621462275}
======================================================================
3     973       0.06948053485214382   interaction effects produced by jet exhausting laterally near base of ogive-cylinder model in supersonic main stream .


Vector Representation for the Rank 3 With Document ID 973


{'angle': 0.14101705678596077, 'appears': 0.2494660437074085, 'attack': 0.18813327934777807, 'base': 0.24498230053647563, 'boundary': 0.08280048886609036, 'condition': 0.10710534926064463, 'cylinder': 0.15814544016527124, 'determined': 0.17189921293073615, 'diameter': 0.21261614994569597, 'discussed': 0.14209154219690176, 'effect': 0.0794777025947831, 'exhausting': 0.3354916442632778, 'experimentally': 0.2559013278490896, 'force': 0.24679866755266158, 'forebody': 0.38198298226136923, 'found': 0.10915673501714981, 'free': 0.14693694433595458, 'independent': 0.2464468852587461, 'interaction': 0.3281122342074664, 'inversely': 0.4032596927645894, 'jet': 0.33692180843316166, 'laminar': 0.1399579583306445, 'layer': 0.09339655011262211, 'length': 0.19444641794294298, 'mach': 0.09703304743183391, 'mainstream': 0.39185884543125793, 'model': 0.15550376250778733, 'near': 0.1929961928191265, 'number': 0.06763609643846907, 'ogive': 0.35199514307886237, 'presented': 0.1068808904795443, 'pressure': 0.07197989801305217, 'product': 0.3220073038963556, 'proportional': 0.30073059339313546, 'ratio': 0.17770961812410752, 'root': 0.3071658775348166, 'side': 0.2818019884118769, 'square': 0.2464468852587461, 'stagnation': 0.17927288904042307, 'stream': 0.13520665720800554, 'to': 0.015188176552939726, 'tobody': 0.5357766313185501, 'turbulent': 0.17927288904042307}
======================================================================
4     430       0.06308232476783754   calibration of the flow in the mach 4 working section of the 4ft . x 3ft . high supersonic speed wind tunnel at rae bedford .


Vector Representation for the Rank 4 With Document ID 430


{'angle': 0.163564324255595, 'distribution': 0.12607535993592625, 'flow': 0.06220061601834868, 'ft': 0.46965022359082137, 'high': 0.1639777441416276, 'humidity': 0.5271982855734489, 'mach': 0.16307374923830095, 'nozzle': 0.24553235789630273, 'number': 0.07845045600431105, 'presented': 0.12397011415191703, 'pressure': 0.0834887895608359, 'range': 0.13837168420922066, 'section': 0.20322597653563415, 'speed': 0.1534603701070292, 'supersonic': 0.15993055680978174, 'total': 0.23833663006222613, 'tunnel': 0.17936980955453063, 'wind': 0.21074975241888858, 'working': 0.37839647016748407, 'x': 0.23448049951385272}
======================================================================
5     312       0.06007420948926314   chordwise pressure distributions over several naca 16 series airfoils at transonic mach numbers up to 1.25 .


Vector Representation for the Rank 5 With Document ID 312


{'airfoil': 0.3409975204723399, 'analysis': 0.13283120624992406, 'angle': 0.15146933446727653, 'apparatus': 0.3780852563019674, 'at': 0.0517306337157308, 'attack': 0.2020778426627266, 'coefficient': 0.14629460251475457, 'design': 0.19717684323293277, 'dimensional': 0.15146933446727653, 'distribution': 0.11675254337477482, 'flow': 0.05760110558725104, 'from': 0.10720222141940526, 'investigation': 0.15185218344903273, 'langley': 0.31977800375441295, 'lift': 0.19003856569623367, 'mach': 0.10422520119775185, 'naca': 0.3136641409190199, 'number': 0.10055954713058654, 'over': 0.13717671971690412, 'photograph': 0.34587469861049364, 'presented': 0.11480297289695095, 'pressure': 0.07731509574482126, 'schlieren': 0.326401922980584, 'series': 0.22350018877046007, 'several': 0.200646434387632, 'test': 0.14701353058842473, 'thickness': 0.16796441531262127, 'to': 0.014739876826450955, 'transonic': 0.2615979586158803, 'tunnel': 0.1661060613333444, 'two': 0.09736562672102574, 'wind': 0.1951655709966986, 'without': 0.2325031339886373, 'x': 0.3005623426939801}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     492       0.11103828877236416   prediction of ogive-forebody pressures at angles of attack .


Vector Representation for the Rank 1 With Document ID 492


{'angle': 0.5184205210342274, 'approximate': 0.49084321407129006, 'approximation': 0.49591873977378437, 'arbitrary': 0.5174679720678466, 'at': 0.43594786105313904, 'attack': 0.55798685259796, 'being': 0.5145445259917428, 'body': 0.467373902369538, 'by': 0.4209016161889557, 'calculated': 0.49005465149343713, 'distribution': 0.4608420626385423, 'forebody': 0.613813274586994, 'lower': 0.5240181743112837, 'method': 0.44698622116309666, 'not': 0.4704997854437502, 'obtaining': 0.6222152411660515, 'ogive': 0.5970277150433683, 'on': 0.4229606574493451, 'over': 0.47148550543155776, 'present': 0.47737128524167577, 'pressure': 0.4604458582597847, 'suggested': 0.5423092919029, 'surface': 0.4813035999171965, 'utilizing': 0.5826084157271793, 'various': 0.49191855462458933, 'zero': 0.4980737838102857}
======================================================================
2     312       0.05433188208462265   chordwise pressure distributions over several naca 16 series airfoils at transonic mach numbers up to 1.25 .


Vector Representation for the Rank 2 With Document ID 312


{'airfoil': 0.5683265922960555, 'analysis': 0.4674973547750857, 'angle': 0.4769682041947859, 'apparatus': 0.5921216813451747, 'at': 0.426286601132576, 'attack': 0.5026846041940374, 'coefficient': 0.4743386962024534, 'design': 0.5001941916877859, 'dimensional': 0.4769682041947859, 'distribution': 0.4593270818171559, 'flow': 0.42926964505573084, 'from': 0.45054589326601535, 'investigation': 0.4771627465337168, 'langley': 0.5624932120850377, 'lift': 0.4965669201679364, 'mach': 0.4529613904771219, 'naca': 0.5593864905510157, 'number': 0.44963920519973183, 'over': 0.46970550052969695, 'photograph': 0.5757540859480952, 'presented': 0.4583364196533785, 'pressure': 0.4392871870570768, 'schlieren': 0.5658591156150347, 'series': 0.5135702366908754, 'several': 0.5019572429443755, 'test': 0.474704015050458, 'thickness': 0.48535007736521485, 'to': 0.40694985823016855, 'transonic': 0.5329293824819448, 'tunnel': 0.48440576630023113, 'two': 0.44947574019106973, 'wind': 0.49917217615761783, 'without': 0.5181450275443787, 'x': 0.5483665771179728}
======================================================================
3     973       0.052259164359343864   interaction effects produced by jet exhausting laterally near base of ogive-cylinder model in supersonic main stream .


Vector Representation for the Rank 3 With Document ID 973


{'angle': 0.4684465348809846, 'appears': 0.5210852548720921, 'attack': 0.4913156986866975, 'base': 0.5189089459181162, 'boundary': 0.44018951096063197, 'condition': 0.45198654823179235, 'cylinder': 0.47676027023433487, 'determined': 0.4834360448448163, 'diameter': 0.5031991381411923, 'discussed': 0.46896806613993514, 'effect': 0.43857670459802084, 'exhausting': 0.5628401631314678, 'experimentally': 0.5242087982966382, 'force': 0.5258536109360863, 'forebody': 0.5854060219039989, 'found': 0.4529822451349698, 'free': 0.47131991629254794, 'independent': 0.5196198226841175, 'interaction': 0.5673190130108998, 'inversely': 0.5957332627414085, 'jet': 0.5686034365909036, 'laminar': 0.4679324721071867, 'layer': 0.4453326028123688, 'length': 0.49437995538663926, 'mach': 0.4470976775223156, 'mainstream': 0.590199545668742, 'model': 0.4754780588051052, 'near': 0.49367604844952845, 'number': 0.43282905302098323, 'ogive': 0.5708505934516364, 'presented': 0.45187760094456275, 'pressure': 0.4349374374445928, 'product': 0.5562951649992738, 'proportional': 0.5459679241618642, 'ratio': 0.4906220335821692, 'root': 0.5490914675864104, 'side': 0.5367804013853495, 'square': 0.5196198226841175, 'stagnation': 0.4870150628058053, 'stream': 0.46562629648962023, 'to': 0.4074410039701492, 'tobody': 0.6600540297733153, 'turbulent': 0.4870150628058053}
======================================================================
4     708       0.04482996448732572   aerodynamic characteristics of two winged reentry vehicles at supersonic  and hypersonic speeds .


Vector Representation for the Rank 4 With Document ID 708


{'angle': 0.5056163983354184, 'at': 0.4405471816879144, 'attack': 0.5409046524201863, 'center': 0.5500752282296417, 'conducted': 0.5283836467636346, 'configuration': 0.5206888805210677, 'control': 0.5449315527644021, 'data': 0.47796155541869834, 'degree': 0.5613858846512297, 'glider': 0.6344680971241227, 'hypersonic': 0.49435222744429297, 'langley': 0.5674980997784189, 'lifting': 0.5585471434161507, 'mach': 0.47267405250710354, 'number': 0.4506568571640286, 'on': 0.4230785244363468, 'performance': 0.5469133939337625, 'presented': 0.46013321611676755, 'reentry': 0.6149108706167306, 'research': 0.5394963426191804, 'stability': 0.5128330083832634, 'test': 0.47700494319862297, 'to': 0.40627756536792853, 'two': 0.4509996224506783, 'up': 0.532944370075529, 'were': 0.4649397996352611, 'winged': 0.6344680971241227}
======================================================================
5     430       0.04072525799486428   calibration of the flow in the mach 4 working section of the 4ft . x 3ft . high supersonic speed wind tunnel at rae bedford .


Vector Representation for the Rank 5 With Document ID 430


{'angle': 0.48548231880139464, 'distribution': 0.4658897602523783, 'flow': 0.43250741206752935, 'ft': 0.6198152993936824, 'high': 0.4856983811405233, 'humidity': 0.675525437004926, 'mach': 0.4763251100744669, 'nozzle': 0.5283206187490602, 'number': 0.44099993639074936, 'presented': 0.4647895124319383, 'pressure': 0.44363308049027567, 'range': 0.47231609017731074, 'section': 0.5062103719378132, 'speed': 0.4802017697965108, 'supersonic': 0.4835832318906833, 'total': 0.5245599728776573, 'tunnel': 0.49374261357706395, 'wind': 0.5101424629458595, 'working': 0.5977583305124242, 'x': 0.522544674111401}
======================================================================
========================================================================================================================================================================


Query No: 8

Query Vector for weight (Version 1) are:
[('angle', 0.030272560339299728),
 ('approximate', 0.04780324214285581),
 ('at', 0.030272560339299728),
 ('attack', 0.030272560339299728),
 ('available', 0.025681984642341265),
 ('body', 0.025681984642341265),
 ('dash', 0.06926355848368322),
 ('exact', 0.04780324214285581),
 ('method', 0.04780324214285581),
 ('predicting', 0.04780324214285581),
 ('presently', 0.04780324214285581),
 ('pressure', 0.030272560339299728)]

Query Vector for weight (Version 2) are:
[('angle', 0.03983032422644438),
 ('approximate', 0.0450775561886673),
 ('at', 0.03983032422644438),
 ('attack', 0.03983032422644438),
 ('available', 0.03845628665095213),
 ('body', 0.03845628665095213),
 ('dash', 0.052613773660894085),
 ('exact', 0.0450775561886673),
 ('method', 0.0450775561886673),
 ('predicting', 0.0450775561886673),
 ('presently', 0.0450775561886673),
 ('pressure', 0.03983032422644438)]

Ranks  Document Number   Scores Titles


1     492       0.042098608367251135   prediction of ogive-forebody pressures at angles of attack .


Vector Representation for the Rank 1 With Document ID 492


{'angle': 0.24798988319115764, 'approximate': 0.17432308885010464, 'approximation': 0.1840627411405065, 'arbitrary': 0.22541452260545322, 'at': 0.07160436566891452, 'attack': 0.3308475657709923, 'being': 0.21980459174508976, 'body': 0.12928678150606152, 'by': 0.04010904208165435, 'calculated': 0.1728098810037261, 'distribution': 0.11675254337477482, 'forebody': 0.41029581399344117, 'lower': 0.23798399737957068, 'method': 0.09016395214855977, 'not': 0.13528517773688292, 'obtaining': 0.4426294338386114, 'ogive': 0.3780852563019674, 'on': 0.044060228048051424, 'over': 0.13717671971690412, 'present': 0.14847120469611422, 'pressure': 0.12658246390336925, 'suggested': 0.2730836374538286, 'surface': 0.16194823636556005, 'utilizing': 0.35041542073362547, 'various': 0.17638660772417045, 'zero': 0.18819815110911567}
======================================================================
2     1083       0.032600738261441824   an investigation of fluid flow in two dimensions .


Vector Representation for the Rank 2 With Document ID 1083


{'bearing': 0.42090368268483946, 'boundary': 0.08893771596118338, 'condition': 0.11504406871162397, 'dash': 0.41029581399344117, 'described': 0.2057734396880969, 'dimensional': 0.15146933446727653, 'example': 0.1906616356350296, 'existence': 0.35041542073362547, 'experimental': 0.12344084813192648, 'flow': 0.09430616102264545, 'fluid': 0.24634230240117314, 'give': 0.18819815110911567, 'given': 0.10235101443118594, 'illustrating': 0.41029581399344117, 'inviscid': 0.2335694722805302, 'iv': 0.4882138804505711, 'method': 0.12480289020385103, 'numerical': 0.23646742681441385, 'obtaining': 0.4426294338386114, 'on': 0.044060228048051424, 'paper': 0.15458506753150733, 'part': 0.2912970384284152, 'perfect': 0.30798736864961457, 'present': 0.14847120469611422, 'problem': 0.11976965319858021, 'several': 0.200646434387632, 'simpler': 0.35041542073362547, 'solution': 0.16457423377136887, 'steady': 0.21372417071610914, 'to': 0.009002945218177212, 'two': 0.09736562672102574, 'viscous': 0.2020778426627266, 'work': 0.22071249888383895}
======================================================================
3     1306       0.027234352358252466   experiments on circular cones at yaw in supersonic flow .


Vector Representation for the Rank 3 With Document ID 1306


{'angle': 0.163564324255595, 'by': 0.04331179236839078, 'calculated': 0.1866089364588232, 'circular': 0.20724785964980616, 'coefficient': 0.1579763843732755, 'compared': 0.16998511017361387, 'cone': 0.21514991999592978, 'corresponding': 0.23079027635009564, 'discussed': 0.1648106095218505, 'fort': 0.6214421478571256, 'halstead': 0.6214421478571256, 'made': 0.118433711946317, 'measurement': 0.1921813145342394, 'merit': 0.42391612831509007, 'method': 0.14107311431436753, 'on': 0.047578484797422, 'pressure': 0.0834887895608359, 'relative': 0.3049936147025652, 'semiapex': 0.5271982855734489, 'supersonic': 0.15993055680978174, 'then': 0.2058861729589721, 'theoretical': 0.16607526820455334, 'these': 0.11096948792961203, 'tunnel': 0.17936980955453063, 'two': 0.1051403770694433, 'value': 0.12905711054059832}
======================================================================
4     248       0.027058597344852386   the application of lighthill formula for numerical calculation of pressure distributions on bodies of revolution at supersonic speed and zero angle of attack .


Vector Representation for the Rank 4 With Document ID 248


{'angle': 0.163564324255595, 'applied': 0.19160750329564033, 'applying': 0.3488145151546617, 'approximation': 0.19876034961904174, 'at': 0.055861380633815266, 'attack': 0.2182139764355936, 'based': 0.24694224337658496, 'body': 0.20228581902321388, 'by': 0.04331179236839078, 'computing': 0.5220052420278656, 'could': 0.26739815197031136, 'determining': 0.29681748236510425, 'developed': 0.17887537325596373, 'digital': 0.5482700517078164, 'distribution': 0.12607535993592625, 'drag': 0.19938423935311986, 'ducted': 0.5619808910508631, 'exact': 0.22302558106185744, 'expected': 0.31893521336122166, 'expression': 0.3439125898894312, 'external': 0.25947395655495925, 'flow': 0.09012434747486854, 'from': 0.10244855848771407, 'give': 0.20322597653563415, 'given': 0.16014134268705985, 'good': 0.2000126997486968, 'integral': 0.24237429107975692, 'lighthill': 0.4157399959776291, 'linearized': 0.4192526580554092, 'mach': 0.11254769596942187, 'method': 0.09736364101196376, 'much': 0.26203487688769017, 'number': 0.07845045600431105, 'numerical': 0.1844775358789806, 'on': 0.06893790079097756, 'over': 0.14813042879608032, 'pointed': 0.32685940877657377, 'pressure': 0.0834887895608359, 'procedure': 0.23833663006222613, 'range': 0.13837168420922066, 'result': 0.066747412341137, 'revolution': 0.372356611121051, 'shown': 0.13654641406641907, 'slender': 0.2413469199941321, 'supersonic': 0.15993055680978174, 'surface': 0.12634218584411033, 'than': 0.14246493031281426, 'theory': 0.14672389148633963, 'thickness': 0.1813765551041639, 'to': 0.009721840107770649, 'various': 0.19047126866708147, 'wave': 0.16439316606881269, 'wider': 0.4157399959776291, 'zero': 0.20322597653563415}
======================================================================
5     231       0.02679198081839391   practical calculation of second-order supersonic flow past non-lifting bodies of revolution .


Vector Representation for the Rank 5 With Document ID 231


{'accuracy': 0.25222024665695203, 'angle': 0.163564324255595, 'apply': 0.360269433606657, 'approximate': 0.1882429755844433, 'at': 0.055861380633815266, 'attack': 0.2182139764355936, 'basic': 0.31403190967724753, 'body': 0.20228581902321388, 'by': 0.04331179236839078, 'calculated': 0.1866089364588232, 'calculation': 0.2515585290048947, 'can': 0.13535079247784257, 'characteristic': 0.1813765551041639, 'compared': 0.16998511017361387, 'computation': 0.30080817680039457, 'computing': 0.360269433606657, 'condition': 0.1242304617275272, 'corner': 0.3891335228376759, 'described': 0.22220467087088383, 'detail': 0.3705935221220037, 'example': 0.2058861729589721, 'flow': 0.06220061601834868, 'form': 0.1579763843732755, 'function': 0.17501924270759028, 'given': 0.11052385336735143, 'increase': 0.20192618711907667, 'method': 0.09736364101196376, 'necessarily': 0.4014093514806447, 'one': 0.14442207513234676, 'order': 0.17223680008179437, 'past': 0.270211009225151, 'presented': 0.12397011415191703, 'procedure': 0.23833663006222613, 'reduced': 0.24237429107975692, 'revolution': 0.256987276348298, 'routine': 0.44305837743833826, 'sample': 0.4014093514806447, 'second': 0.2238544228750751, 'several': 0.21666826866528383, 'shown': 0.13654641406641907, 'so': 0.22989200154213685, 'solution': 0.10854665920362061, 'standard': 0.3644548715088276, 'summarized': 0.4082757719609241, 'supersonic': 0.15993055680978174, 'table': 0.3164485331545604, 'tangency': 0.5271982855734489, 'that': 0.04725898923138793, 'theory': 0.10126360623697798, 'to': 0.014086267179562515, 'understanding': 0.37839647016748407, 'use': 0.18395285864509878, 'without': 0.25106876010190277, 'zero': 0.20322597653563415}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     492       0.04051512125078767   prediction of ogive-forebody pressures at angles of attack .


Vector Representation for the Rank 1 With Document ID 492


{'angle': 0.5184205210342274, 'approximate': 0.49084321407129006, 'approximation': 0.49591873977378437, 'arbitrary': 0.5174679720678466, 'at': 0.43594786105313904, 'attack': 0.55798685259796, 'being': 0.5145445259917428, 'body': 0.467373902369538, 'by': 0.4209016161889557, 'calculated': 0.49005465149343713, 'distribution': 0.4608420626385423, 'forebody': 0.613813274586994, 'lower': 0.5240181743112837, 'method': 0.44698622116309666, 'not': 0.4704997854437502, 'obtaining': 0.6222152411660515, 'ogive': 0.5970277150433683, 'on': 0.4229606574493451, 'over': 0.47148550543155776, 'present': 0.47737128524167577, 'pressure': 0.4604458582597847, 'suggested': 0.5423092919029, 'surface': 0.4813035999171965, 'utilizing': 0.5826084157271793, 'various': 0.49191855462458933, 'zero': 0.4980737838102857}
======================================================================
2     1306       0.02235085140821223   experiments on circular cones at yaw in supersonic flow .


Vector Representation for the Rank 2 With Document ID 1306


{'angle': 0.4840870796109412, 'by': 0.4222662377602728, 'calculated': 0.49593412602375225, 'circular': 0.5065444274164468, 'coefficient': 0.48121436547915103, 'compared': 0.4873879530691996, 'cone': 0.5106068119274887, 'corresponding': 0.5186473910444916, 'discussed': 0.4847277846600313, 'fort': 0.7194783189933236, 'halstead': 0.7194783189933236, 'made': 0.4608858014140488, 'measurement': 0.49879883995805485, 'merit': 0.6179318099605305, 'method': 0.46532467308477726, 'on': 0.4244597093965124, 'pressure': 0.44292090299259124, 'relative': 0.5567947196128623, 'semiapex': 0.6710283211911958, 'supersonic': 0.4822189895253167, 'then': 0.5058443954400459, 'theoretical': 0.48537793533205026, 'these': 0.45704850497435706, 'tunnel': 0.4922125501661482, 'two': 0.45405180681789314, 'value': 0.4663472036324212}
======================================================================
3     1083       0.021176058074029842   an investigation of fluid flow in two dimensions .


Vector Representation for the Rank 3 With Document ID 1083


{'bearing': 0.6037335772185539, 'boundary': 0.4430492765158033, 'condition': 0.4556857557218054, 'dash': 0.5985989606208144, 'described': 0.49960226220119114, 'dimensional': 0.4733169858554991, 'example': 0.49228756759382053, 'existence': 0.569614546309546, 'experimental': 0.45975012003789123, 'flow': 0.443371634267286, 'fluid': 0.5176623834852551, 'give': 0.4910951462976096, 'given': 0.44954182906882995, 'illustrating': 0.5985989606208144, 'inviscid': 0.513056611463277, 'iv': 0.6363143027817678, 'method': 0.4596105718916256, 'numerical': 0.5129457701109663, 'obtaining': 0.6114165276468245, 'on': 0.42132684564800105, 'paper': 0.47482512054033904, 'part': 0.5391344625328145, 'perfect': 0.5490777366281656, 'present': 0.4718657756894391, 'problem': 0.45797312043630467, 'several': 0.4971205943677825, 'simpler': 0.569614546309546, 'solution': 0.47568809290452024, 'steady': 0.503450721933135, 'to': 0.4043577718852494, 'two': 0.44712870959804385, 'viscous': 0.49781345104816377, 'work': 0.5068333416510405}
======================================================================
4     248       0.020870522037726255   the application of lighthill formula for numerical calculation of pressure distributions on bodies of revolution at supersonic speed and zero angle of attack .


Vector Representation for the Rank 4 With Document ID 248


{'angle': 0.46365417801627024, 'applied': 0.47456771627640904, 'applying': 0.5357478248595173, 'approximation': 0.4773513829180498, 'at': 0.42173952225390543, 'attack': 0.4849221330194462, 'based': 0.4945441864883507, 'body': 0.4774470497075468, 'by': 0.41685561050167075, 'computing': 0.5998546715837391, 'could': 0.5040630934906188, 'determining': 0.5155121873110003, 'developed': 0.4696127649093529, 'digital': 0.6099104037683515, 'distribution': 0.4490646321644451, 'drag': 0.47759418151350314, 'ducted': 0.6187055878077284, 'exact': 0.48679466077767236, 'expected': 0.5241197243919031, 'expression': 0.531670205913749, 'external': 0.500979241630501, 'flow': 0.4345049635829656, 'from': 0.43922340498200707, 'give': 0.47908926684840386, 'given': 0.46131163611570186, 'good': 0.4778387588690988, 'integral': 0.4943245805047881, 'lighthill': 0.5617931528338047, 'linearized': 0.5605148675533811, 'mach': 0.44380008358891, 'method': 0.4378909188510023, 'much': 0.5019758726469957, 'number': 0.4305304919925726, 'numerical': 0.4717929533979157, 'on': 0.4263935309705525, 'over': 0.45764778307938137, 'pointed': 0.527203576252021, 'pressure': 0.4324912556405868, 'procedure': 0.492753247670755, 'range': 0.45384998140120747, 'result': 0.4259760292265738, 'revolution': 0.5425602699669042, 'shown': 0.45313964269424034, 'slender': 0.49392475944190806, 'supersonic': 0.4622400280730095, 'surface': 0.4491684725583464, 'than': 0.45544294623218984, 'theory': 0.45617463731317326, 'thickness': 0.4705861475546271, 'to': 0.4037834395959031, 'various': 0.474125528888397, 'wave': 0.4639767376243388, 'wider': 0.5617931528338047, 'zero': 0.47908926684840386}
======================================================================
5     291       0.020560099928645426   sweepback effects in the turbulent boundary-layer shock-wave interaction .


Vector Representation for the Rank 5 With Document ID 291


{'ahead': 0.5703799144917274, 'angle': 0.4773534276876563, 'at': 0.4354648029543454, 'available': 0.5161180445549496, 'boundary': 0.44541933985849125, 'by': 0.4204831684063067, 'can': 0.4640105829070708, 'configuration': 0.517668659860385, 'dimensional': 0.4773534276876563, 'experiment': 0.49580184397612903, 'extension': 0.5385686042524664, 'influence': 0.511792941433094, 'interaction': 0.517668659860385, 'layer': 0.4512316981369061, 'moderate': 0.550831986596494, 'on': 0.42250098791417684, 'peak': 0.5703799144917274, 'pressure': 0.45300465969649684, 'reattachment': 0.5898359522115957, 'reported': 0.5572851609425697, 'rise': 0.5922869659676546, 'separation': 0.5442760084883067, 'shock': 0.47240202489658145, 'show': 0.4900783564782236, 'simple': 0.48299425281798625, 'sweep': 0.5723593068169193, 'sweptback': 0.6004799379479042, 'that': 0.4223498909235817, 'theory': 0.4478899483618625, 'turbulent': 0.4983382632910418, 'two': 0.449723364747835, 'understood': 0.628600569078889, 'upstream': 0.5485130986074713, 'wave': 0.4777454065348471}
======================================================================
========================================================================================================================================================================


Query No: 9

Query Vector for weight (Version 1) are:
[('flow', 0.03289649754063496),
 ('heat', 0.07215220853242434),
 ('internal', 0.09387218755408672),
 ('on', 0.05043222951076198),
 ('paper', 0.07215220853242434),
 ('slip', 0.09387218755408672),
 ('study', 0.09387218755408672),
 ('transfer', 0.09387218755408672)]

Query Vector for weight (Version 2) are:
[('flow', 0.06025897240686098),
 ('heat', 0.07250110412252518),
 ('internal', 0.07927461139896373),
 ('on', 0.06572759684608664),
 ('paper', 0.07250110412252518),
 ('slip', 0.07927461139896373),
 ('study', 0.07927461139896373),
 ('transfer', 0.07927461139896373)]

Ranks  Document Number   Scores Titles


1     507       0.05897218595953786   energy equation approximations in fluid mechanics .


Vector Representation for the Rank 1 With Document ID 507


{'discussion': 0.3182369617027767, 'energy': 0.2756739005276814, 'equation': 0.13117246567543026, 'flow': 0.0751659077259313, 'fluid': 0.23224019116896719, 'form': 0.19090547796463975, 'incompressible': 0.2546790925496304, 'nearly': 0.3983901883062696, 'several': 0.26183128290606894, 'study': 0.22681852995652782, 'use': 0.22229657009763265}
======================================================================
2     21       0.046718998843695056   on heat transfer in slip flow .


Vector Representation for the Rank 2 With Document ID 21


{'analysis': 0.14343792139007638, 'author': 0.23833663006222613, 'boundary': 0.13915450988636802, 'by': 0.04331179236839078, 'considered': 0.15993055680978174, 'considers': 0.36885503908586875, 'effect': 0.09218542078944494, 'eg': 0.3950520390840711, 'flat': 0.17692564250327128, 'friction': 0.2488111440108371, 'heat': 0.14608784514803438, 'impulsive': 0.5271982855734489, 'infinite': 0.26074486069362346, 'laminar': 0.23521335879664781, 'layer': 0.15696225147919476, 'motion': 0.21590573510828764, 'number': 0.07845045600431105, 'on': 0.06893790079097756, 'other': 0.1682253672297902, 'over': 0.14813042879608032, 'perturbation': 0.3524654687089807, 'plate': 0.23002160078661651, 'reference': 0.4329252952679785, 'skin': 0.23638689930953372, 'slip': 0.3835971206320758, 'studiesdash': 0.6214421478571256, 'transfer': 0.17501924270759028, 'usual': 0.31403190967724753, 'while': 0.28935325834839926}
======================================================================
3     398       0.045006334037132126   heat transfer in turbulent shear flow .


Vector Representation for the Rank 3 With Document ID 398


{'along': 0.20064579827032275, 'analogy': 0.3325804923459027, 'analysis': 0.14343792139007638, 'between': 0.1415028515150645, 'discussed': 0.1648106095218505, 'extending': 0.37349316648351, 'flow': 0.06220061601834868, 'fluid': 0.1921813145342394, 'friction': 0.2488111440108371, 'from': 0.07070634769260985, 'heat': 0.2116710823907653, 'higher': 0.22302558106185744, 'karmans': 0.4545132958903335, 'known': 0.2373562255588418, 'method': 0.09736364101196376, 'number': 0.07845045600431105, 'on': 0.047578484797422, 'paper': 0.16692885196679205, 'point': 0.16998511017361387, 'prandtl': 0.2716527987994464, 'problem': 0.12933338923453824, 'shear': 0.2393283689727511, 'smooth': 0.3524654687089807, 'suggested': 0.29488966055399934, 'to': 0.009721840107770649, 'transfer': 0.2535906563998364, 'turbulent': 0.20793689516404892, 'view': 0.3488145151546617, 'von': 0.3325804923459027, 'wall': 0.18239781074082373, 'well': 0.1844775358789806}
======================================================================
4     1152       0.044690681812558974   on periodically oscillating wakes in the oseen approximation .


Vector Representation for the Rank 4 With Document ID 1152


{'approximation': 0.24019058098446416, 'at': 0.06750530221317826, 'behind': 0.3150953381735983, 'by': 0.05233983836505397, 'math': 0.6370891515767835, 'mean': 0.23796112640068073, 'mechs': 0.7509775004326937, 'number': 0.09480291538170249, 'obstacle': 0.5841340850404995, 'order': 0.20813837949995173, 'oscillating': 0.40554237866270815, 'oseen': 0.5354108567977349, 'reynolds': 0.20595586430686588, 'studied': 0.3198442131627761, 'study': 0.22681852995652782, 'vortex': 0.36856744140554065, 'wake': 0.35635738732867905}
======================================================================
5     326       0.03742944748273964   forst-order slip effects on the compressible laminar boundary layer over a slender body of revolution in axial flow .


Vector Representation for the Rank 5 With Document ID 326


{'analysis': 0.14343792139007638, 'boundary': 0.13915450988636802, 'case': 0.11555798590132785, 'compressible': 0.2354284037477369, 'considered': 0.15993055680978174, 'curvature': 0.29115931369431924, 'effect': 0.09218542078944494, 'examined': 0.29681748236510425, 'first': 0.1813765551041639, 'flow': 0.06220061601834868, 'gradient': 0.2189974016094449, 'interaction': 0.2488111440108371, 'layer': 0.15696225147919476, 'no': 0.20064579827032275, 'only': 0.16692885196679205, 'order': 0.17223680008179437, 'pressure': 0.0834887895608359, 'slip': 0.3835971206320758, 'transverse': 0.2858513655793169, 'zero': 0.20322597653563415}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     398       0.03164298326482257   heat transfer in turbulent shear flow .


Vector Representation for the Rank 1 With Document ID 398


{'along': 0.4983352871591335, 'analogy': 0.5629956794524992, 'analysis': 0.4702980541381645, 'between': 0.4693496881445945, 'discussed': 0.48077267878975616, 'extending': 0.5830467325742268, 'flow': 0.4304841441503737, 'fluid': 0.4941868950870495, 'friction': 0.5219408305861197, 'from': 0.4346527515864494, 'heat': 0.4949805892091891, 'higher': 0.5093034827871309, 'karmans': 0.6227542059405831, 'known': 0.5163268446214407, 'method': 0.4477173291457176, 'number': 0.43844809203806756, 'on': 0.42331792644293303, 'paper': 0.48181081654739494, 'point': 0.48330867013312206, 'prandtl': 0.5331353868748169, 'problem': 0.4633855085891595, 'shear': 0.5172933801312674, 'smooth': 0.5727411856015063, 'suggested': 0.5445236316973302, 'to': 0.40476461479360176, 'transfer': 0.5137906495812028, 'turbulent': 0.5019086094660561, 'view': 0.5709518754377074, 'von': 0.5629956794524992, 'wall': 0.48939205929561247, 'well': 0.4904113199551215}
======================================================================
2     507       0.026814902819351644   energy equation approximations in fluid mechanics .


Vector Representation for the Rank 2 With Document ID 507


{'discussion': 0.5474137008336801, 'energy': 0.527697642921805, 'equation': 0.46076169942432343, 'flow': 0.4348183459743789, 'fluid': 0.5075782834255236, 'form': 0.48843122076584533, 'incompressible': 0.517972429590905, 'nearly': 0.5845422722735273, 'several': 0.5212854666557016, 'study': 0.5050668619372222, 'use': 0.5029722000404572}
======================================================================
3     21       0.026690851513041007   on heat transfer in slip flow .


Vector Representation for the Rank 3 With Document ID 21


{'analysis': 0.46817639773026076, 'author': 0.5132819879662347, 'boundary': 0.4611782662285065, 'by': 0.4205862017122215, 'considered': 0.47601538801328513, 'considers': 0.5753177096114058, 'effect': 0.4438159578148172, 'eg': 0.5877692083079049, 'flat': 0.48409319415039614, 'friction': 0.5182605502743822, 'heat': 0.4694359130266802, 'impulsive': 0.6505786451145108, 'infinite': 0.5239326752402296, 'laminar': 0.5034098391544277, 'layer': 0.4690073100516929, 'motion': 0.5026205282838497, 'number': 0.4372876951843522, 'on': 0.4303080457203202, 'other': 0.47995793185950913, 'over': 0.47040675807126087, 'perturbation': 0.5675277063973734, 'plate': 0.501127320578558, 'reference': 0.5903324512628949, 'skin': 0.512355276131775, 'slip': 0.5823246573217878, 'studiesdash': 0.6953729852473034, 'transfer': 0.4831870776266508, 'usual': 0.5492601410189604, 'while': 0.5375303171889951}
======================================================================
4     326       0.02343285349109535   forst-order slip effects on the compressible laminar boundary layer over a slender body of revolution in axial flow .


Vector Representation for the Rank 4 With Document ID 326


{'analysis': 0.4766598175882614, 'boundary': 0.4660784246871832, 'case': 0.46175949870307836, 'compressible': 0.5258237592366958, 'considered': 0.48547423995698785, 'curvature': 0.555608918901094, 'effect': 0.4492681257057375, 'examined': 0.5586329042878203, 'first': 0.49693596710217247, 'flow': 0.4332428679364144, 'gradient': 0.5170422765262181, 'interaction': 0.5329761107031562, 'layer': 0.4745345466817294, 'no': 0.5072343362633125, 'only': 0.4892144505300779, 'order': 0.49205126195568033, 'pressure': 0.44462024628057123, 'slip': 0.6050119313641399, 'transverse': 0.5527721074754915, 'zero': 0.5086133021131177}
======================================================================
5     181       0.022392017954459893   some problems on heat conduction in stratiform bodies .


Vector Representation for the Rank 5 With Document ID 181


{'applied': 0.49744353515700135, 'arising': 0.5756115083221334, 'body': 0.47100002639277916, 'calculation': 0.488294188316911, 'case': 0.45876794211171434, 'class': 0.5722539769672794, 'complicated': 0.6076319238784809, 'composite': 0.6253208973340816, 'conduction': 0.5573446936177807, 'deduction': 0.6857998970436128, 'difficulty': 0.5832179148301757, 'general': 0.4833921991644365, 'give': 0.5033522030648816, 'heat': 0.4742941473055401, 'idea': 0.592436564904029, 'infinite': 0.5326038937045354, 'lead': 0.5332599418038924, 'multilayer': 0.7160393968983785, 'on': 0.42419642068463786, 'paper': 0.4848930087578365, 'present': 0.48153547740298264, 'problem': 0.465773534147066, 'question': 0.595081397479316, 'solides': 0.7160393968983785, 'special': 0.5319575651944978, 'specific': 0.5404278885762452, 'to': 0.4064767343953059, 'usually': 0.5722539769672794}
======================================================================
========================================================================================================================================================================


Query No: 10

Query Vector for weight (Version 1) are:
[('air', 0.06827068185751761),
 ('available', 0.03667798509873599),
 ('density', 0.06827068185751761),
 ('enthalpy', 0.06827068185751761),
 ('gas', 0.05247433347812679),
 ('over', 0.06827068185751761),
 ('property', 0.05247433347812679),
 ('range', 0.06827068185751761),
 ('real', 0.06827068185751761),
 ('transport', 0.06827068185751761),
 ('wide', 0.06827068185751761)]

Query Vector for weight (Version 2) are:
[('air', 0.05479005299633102),
 ('available', 0.04626311028551071),
 ('density', 0.05479005299633102),
 ('enthalpy', 0.05479005299633102),
 ('gas', 0.05052658164092087),
 ('over', 0.05479005299633102),
 ('property', 0.05052658164092087),
 ('range', 0.05479005299633102),
 ('real', 0.05479005299633102),
 ('transport', 0.05479005299633102),
 ('wide', 0.05479005299633102)]

Ranks  Document Number   Scores Titles


1     405       0.13086258711278625   tables of thermal properties of gases .


Vector Representation for the Rank 1 With Document ID 405


{'air': 0.17692564250327128, 'argon': 0.4329544232897724, 'carbon': 0.7003800638456551, 'dioxide': 0.5271982855734489, 'hydrogen': 0.4329544232897724, 'monoxide': 0.6214421478571256, 'nitrogen': 0.3835971206320758, 'oxygen': 0.4082757719609241, 'property': 0.2238544228750751, 'steam': 0.5619808910508631, 'table': 0.3164485331545604, 'thermodynamic': 0.3453126223855793, 'transport': 0.3562787391713667}
======================================================================
2     436       0.05212248631680083   heat transfer in planetary atmospheres at super-satellite speeds .


Vector Representation for the Rank 2 With Document ID 436


{'atmosphere': 0.28085279874249974, 'atom': 0.4157399959776291, 'by': 0.04331179236839078, 'concept': 0.28935325834839926, 'dependence': 0.3835971206320758, 'discussed': 0.1648106095218505, 'enthalpy': 0.3164485331545604, 'examine': 0.44305837743833826, 'feb': 0.6214421478571256, 'flight': 0.2144007059732076, 'ftsec': 0.5619808910508631, 'heat': 0.14608784514803438, 'hirshfelder': 0.6214421478571256, 'investigation': 0.1639777441416276, 'ionized': 0.4545132958903335, 'jchemphys': 0.6214421478571256, 'large': 0.1713290195438332, 'main': 0.27924930419983346, 'on': 0.047578484797422, 'planetary': 0.4677370287671866, 'property': 0.2238544228750751, 'proportion': 0.4157399959776291, 'purpose': 0.2499325254733439, 'thermodynamic': 0.3453126223855793, 'to': 0.014086267179562515, 'total': 0.3453331275269181, 'transfer': 0.17501924270759028, 'transport': 0.3562787391713667, 'up': 0.2058861729589721, 'used': 0.1447526514964224, 'velocity': 0.12988863039831225}
======================================================================
3     438       0.046051633277970315   stagnation point heat transfer measurements at super satellite speeds .


Vector Representation for the Rank 3 With Document ID 438


{'between': 0.1415028515150645, 'blunt': 0.22812318711727908, 'body': 0.13961047050608286, 'brief': 0.3296722660314134, 'by': 0.04331179236839078, 'comparison': 0.20322597653563415, 'corresponding': 0.23079027635009564, 'data': 0.1607248630432404, 'description': 0.3241358638258134, 'enthalpy': 0.3164485331545604, 'experiment': 0.20257362008142774, 'ft': 0.46965022359082137, 'heating': 0.2545706528709851, 'measurement': 0.1921813145342394, 'over': 0.14813042879608032, 'per': 0.35269004915891594, 'performed': 0.33559078227780864, 'point': 0.16998511017361387, 'provided': 0.29115931369431924, 'range': 0.13837168420922066, 'respectively': 0.3164485331545604, 'sec': 0.5344451846043565, 'shock': 0.15309455095854613, 'stagnation': 0.30128603528752607, 'technique': 0.2393283689727511, 'theory': 0.10126360623697798, 'thus': 0.2488111440108371, 'to': 0.014086267179562515, 'tube': 0.26074486069362346, 'used': 0.1447526514964224, 'using': 0.19392614336958838, 'velocity': 0.12988863039831225}
======================================================================
4     524       0.03581399441281179   stagnation point heat transfer in partially ionized air .


Vector Representation for the Rank 4 With Document ID 524


{'based': 0.2184619361145119, 'by': 0.05551802306592111, 'comparison': 0.18819815110911567, 'data': 0.14883984113467844, 'ft': 0.3001671898448374, 'hansens': 0.5754887502163468, 'heat': 0.18725866358969678, 'lower': 0.23798399737957068, 'obtained': 0.0983379890438054, 'on': 0.060987164741596066, 'peng': 0.7965784284662087, 'pindroh': 0.7965784284662087, 'property': 0.28694160026627946, 'range': 0.1281395989722977, 'rate': 0.295817297321991, 'recently': 0.28863378435483206, 'reported': 0.30798736864961457, 'sec': 0.34157954394707607, 'shown': 0.12644930095033347, 'that': 0.043764358022771316, 'thermodynamic': 0.31977800375441295, 'to': 0.012461671841138389, 'transfer': 0.22434357532410434, 'transport': 0.4566860473234241, 'using': 0.17958600694669774, 'velocity': 0.12028383628788435}
======================================================================
5     482       0.03168827409397153   a re-examination of the use of the simple concepts for prediction the shape and location of detached shock waves .


Vector Representation for the Rank 5 With Document ID 482


{'can': 0.13535079247784257, 'concept': 0.4192526580554092, 'detached': 0.37839647016748407, 'existing': 0.2987896257790135, 'good': 0.2000126997486968, 'ha': 0.11966097837637452, 'location': 0.270211009225151, 'mach': 0.11254769596942187, 'made': 0.118433711946317, 'method': 0.09736364101196376, 'modification': 0.3164485331545604, 'nose': 0.2393283689727511, 'number': 0.07845045600431105, 'predicting': 0.34194809467438225, 'prediction': 0.24770423239070574, 'range': 0.13837168420922066, 'reexamination': 0.5619808910508631, 'result': 0.066747412341137, 'shape': 0.2542754828725913, 'shock': 0.15309455095854613, 'show': 0.19047126866708147, 'simple': 0.2542754828725913, 'that': 0.04725898923138793, 'use': 0.18395285864509878, 'wave': 0.16439316606881269, 'wide': 0.2930042119027183, 'yield': 0.25947395655495925}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     405       0.06273503466128244   tables of thermal properties of gases .


Vector Representation for the Rank 1 With Document ID 405


{'air': 0.5014423677946904, 'argon': 0.6482394367729205, 'carbon': 0.7477739055150967, 'dioxide': 0.7022752475514293, 'hydrogen': 0.6482394367729205, 'monoxide': 0.7563110583299382, 'nitrogen': 0.6199398552158644, 'oxygen': 0.6340896459943924, 'property': 0.5283495279512219, 'steam': 0.7222182575514198, 'table': 0.5814394342965952, 'thermodynamic': 0.5979889944078587, 'transport': 0.6042765445703107}
======================================================================
2     436       0.024099036514665002   heat transfer in planetary atmospheres at super-satellite speeds .


Vector Representation for the Rank 2 With Document ID 436


{'atmosphere': 0.5348466239034382, 'atom': 0.5996103835540267, 'by': 0.4207954095605756, 'concept': 0.5389279728685024, 'dependence': 0.5841775367306953, 'discussed': 0.4791309695933122, 'enthalpy': 0.5519373014125153, 'examine': 0.6127268329074846, 'feb': 0.6983747214378525, 'flight': 0.5029407984981771, 'ftsec': 0.6698254252610631, 'heat': 0.47014155742703556, 'hirshfelder': 0.6983747214378525, 'investigation': 0.47873108365593875, 'ionized': 0.6182267142946627, 'jchemphys': 0.6983747214378525, 'large': 0.4822606716600828, 'main': 0.5340767336744845, 'on': 0.4228439882888821, 'planetary': 0.6245758613988703, 'property': 0.507479837501041, 'proportion': 0.5996103835540267, 'purpose': 0.520000788365441, 'thermodynamic': 0.5657958956735577, 'to': 0.4062349578024672, 'total': 0.5528536588492581, 'transfer': 0.4840324686203087, 'transport': 0.5710610873772375, 'up': 0.49885269242900204, 'used': 0.46950048724015003, 'velocity': 0.46236378405725836}
======================================================================
3     438       0.021846049010324844   stagnation point heat transfer measurements at super satellite speeds .


Vector Representation for the Rank 3 With Document ID 438


{'between': 0.46828713683456724, 'blunt': 0.5100888012292585, 'body': 0.467373902369538, 'brief': 0.5590948514465257, 'by': 0.4209016161889557, 'comparison': 0.4980737838102857, 'corresponding': 0.5113758981707075, 'data': 0.477563388990662, 'description': 0.5564230674440334, 'enthalpy': 0.552713277882764, 'experiment': 0.4977589664481171, 'ft': 0.6085875942009225, 'heating': 0.5228519483567818, 'measurement': 0.49274379690680276, 'over': 0.47148550543155776, 'per': 0.5566416136038248, 'performed': 0.5619510379081263, 'point': 0.4820322442550126, 'provided': 0.5405090829055552, 'range': 0.4667760828312257, 'respectively': 0.552713277882764, 'sec': 0.6373652341450078, 'shock': 0.4738811157372322, 'stagnation': 0.5338113474884918, 'technique': 0.5154962525875045, 'theory': 0.44886828541918167, 'thus': 0.5200724964558358, 'to': 0.4062561890416905, 'tube': 0.5258315277074119, 'used': 0.4698554411735673, 'using': 0.4935858249235999, 'velocity': 0.4626822893128751}
======================================================================
4     524       0.02165205276349171   stagnation point heat transfer in partially ionized air .


Vector Representation for the Rank 4 With Document ID 524


{'based': 0.5089335465726618, 'by': 0.4276834274145751, 'comparison': 0.4970821450287198, 'data': 0.47677913389654214, 'ft': 0.5548414502780324, 'hansens': 0.6968662655910329, 'heat': 0.49337439150310447, 'lower': 0.5227642078944891, 'obtained': 0.4507277189383661, 'on': 0.4304105523775587, 'peng': 0.7972047253605625, 'pindroh': 0.7972047253605625, 'property': 0.5430801481126508, 'range': 0.4661008998124426, 'rate': 0.5405412477182665, 'recently': 0.5488919351640048, 'reported': 0.5588754948656209, 'sec': 0.5762040414790652, 'shown': 0.4652289584211856, 'that': 0.42257587403285446, 'thermodynamic': 0.564957702052455, 'to': 0.4062138701781363, 'transfer': 0.5118663587144798, 'transport': 0.6277212757975111, 'using': 0.49263956456947106, 'velocity': 0.4620484992561947}
======================================================================
5     302       0.017649317142796224   approximations for the thermodynamic and transport properties of high temperature air .


Vector Representation for the Rank 5 With Document ID 302


{'air': 0.5319587781447008, 'approximate': 0.46568366786324766, 'atmosphere': 0.4979980362815218, 'become': 0.5193160329479973, 'can': 0.4472279853765586, 'closed': 0.5257089022569383, 'coefficient': 0.4551227387327196, 'compared': 0.4593129463857876, 'complete': 0.494787878034048, 'component': 0.5650590057557967, 'compressibility': 0.5788040846619315, 'conductivity': 0.5229858628619014, 'degree': 0.5281166766374139, 'energy': 0.4795990799018965, 'enthalpy': 0.5622131185917647, 'entropy': 0.5378456053583616, 'equilibrium': 0.4856736661523193, 'flux': 0.5320339735915242, 'form': 0.4551227387327196, 'found': 0.4649008465324699, 'fraction': 0.5357804560258858, 'from': 0.44734974683151435, 'fully': 0.5150326250342225, 'function': 0.4610695074915323, 'heat': 0.47488536828906436, 'high': 0.4572167946757285, 'ionized': 0.5585934363500247, 'k': 0.5181863595272305, 'major': 0.5648005441574264, 'minor': 0.5378456053583616, 'mol': 0.6168399618064897, 'neglecting': 0.5510708936203168, 'number': 0.4402141005254394, 'order': 0.4600986291003791, 'over': 0.4516871870266286, 'partition': 0.6168399618064897, 'prandtl': 0.5392505985986566, 'predicted': 0.48350890676824854, 'pressure': 0.42913176391731306, 'property': 0.47810957894282535, 'range': 0.44828206587288855, 'small': 0.4538039001838814, 'sound': 0.5112861425998609, 'specific': 0.4963499433750351, 'speed': 0.45354696476182443, 'starting': 0.5357804560258858, 'tabulated': 0.582630283644582, 'temperature': 0.450049829260981, 'that': 0.4164900907595078, 'thermal': 0.485301825434144, 'thermodynamic': 0.5204900184314547, 'to': 0.4065104008743407, 'transparent': 0.5960921308148266, 'transport': 0.524316428264124, 'unity': 0.5104184646625072, 'value': 0.4450319293871152, 'viscosity': 0.4928243681638519}
======================================================================
========================================================================================================================================================================


Query No: 11

Query Vector for weight (Version 1) are:
[('analytical', 0.06258145836939115),
 ('approximation', 0.06258145836939115),
 ('blast', 0.06258145836939115),
 ('find', 0.06258145836939115),
 ('newtonian', 0.06258145836939115),
 ('possible', 0.048101472354949555),
 ('problem', 0.02895997202888316),
 ('similar', 0.06258145836939115),
 ('solution', 0.048101472354949555),
 ('strong', 0.06258145836939115),
 ('to', 0.025151237511092873),
 ('wave', 0.048101472354949555)]

Query Vector for weight (Version 2) are:
[('analytical', 0.04949928469241774),
 ('approximation', 0.04949928469241774),
 ('blast', 0.04949928469241774),
 ('find', 0.04949928469241774),
 ('newtonian', 0.04949928469241774),
 ('possible', 0.04575883575292521),
 ('problem', 0.0408142312123184),
 ('similar', 0.04949928469241774),
 ('solution', 0.04575883575292521),
 ('strong', 0.04949928469241774),
 ('to', 0.03983036444796734),
 ('wave', 0.04575883575292521)]

Ranks  Document Number   Scores Titles


1     320       0.06444618379776781   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 1 With Document ID 320


{'accurate': 0.270211009225151, 'attention': 0.31403190967724753, 'drawn': 0.3891335228376759, 'previous': 0.2841526078838075, 'problem': 0.12933338923453824, 'solution': 0.10854665920362061, 'to': 0.014086267179562515}
======================================================================
2     495       0.0530542646470208   on similar solutions for strong blast waves and their application to steady hypersonic flow .


Vector Representation for the Rank 2 With Document ID 495


{'application': 0.2058861729589721, 'applied': 0.19160750329564033, 'approximation': 0.28798986183687697, 'blast': 0.5638272909708307, 'body': 0.13961047050608286, 'busemann': 0.4677370287671866, 'case': 0.11555798590132785, 'constitutes': 0.5271982855734489, 'density': 0.24237429107975692, 'equivalence': 0.44305837743833826, 'expression': 0.2373562255588418, 'flow': 0.06220061601834868, 'formula': 0.33053456217808586, 'found': 0.18344881980918248, 'general': 0.1639777441416276, 'higher': 0.22302558106185744, 'hypersonic': 0.19451572961012958, 'ie': 0.3488145151546617, 'improvement': 0.3835971206320758, 'investigated': 0.20863150997394708, 'law': 0.28085279874249974, 'layer': 0.10832975779775116, 'neglecting': 0.4329544232897724, 'newton': 0.5271982855734489, 'newtonian': 0.2987896257790135, 'obtained': 0.10619038357284823, 'order': 0.24955909140758387, 'power': 0.24237429107975692, 'pressure': 0.1209694238143449, 'principle': 0.33559078227780864, 'profile': 0.22139154193623733, 'result': 0.066747412341137, 'shock': 0.15309455095854613, 'shown': 0.13654641406641907, 'simple': 0.2542754828725913, 'solution': 0.10854665920362061, 'strong': 0.4450613362496161, 'temperature': 0.14343792139007638, 'term': 0.1871501651331313, 'thin': 0.21219154199318402, 'to': 0.009721840107770649, 'upon': 0.2545706528709851, 'using': 0.19392614336958838, 'velocity': 0.12988863039831225, 'wave': 0.2381942136539113}
======================================================================
3     1152       0.04741412439443163   on periodically oscillating wakes in the oseen approximation .


Vector Representation for the Rank 3 With Document ID 1152


{'approximation': 0.24019058098446416, 'at': 0.06750530221317826, 'behind': 0.3150953381735983, 'by': 0.05233983836505397, 'math': 0.6370891515767835, 'mean': 0.23796112640068073, 'mechs': 0.7509775004326937, 'number': 0.09480291538170249, 'obstacle': 0.5841340850404995, 'order': 0.20813837949995173, 'oscillating': 0.40554237866270815, 'oseen': 0.5354108567977349, 'reynolds': 0.20595586430686588, 'studied': 0.3198442131627761, 'study': 0.22681852995652782, 'vortex': 0.36856744140554065, 'wake': 0.35635738732867905}
======================================================================
4     670       0.046421906928877404   on blunt-body heat transfer at hypersonic speed and low reynolds number .


Vector Representation for the Rank 4 With Document ID 670


{'analytical': 0.3198442131627761, 'arising': 0.4172906696483052, 'between': 0.17099815019195158, 'comparison': 0.24558703719724512, 'data': 0.19422685815856466, 'difference': 0.31204612886278377, 'discussion': 0.3182369617027767, 'due': 0.24094451625367497, 'experimental': 0.16108273106391074, 'inconsistency': 0.7509775004326937, 'introduced': 0.3635095776851176, 'made': 0.14312040673633072, 'particular': 0.26753909008830196, 'presentation': 0.5122785371621799, 'result': 0.08066045255080079, 'those': 0.23796112640068073, 'to': 0.011748290985597008, 'way': 0.37948970696423406}
======================================================================
5     920       0.039511770328693026   supersonic flow over an inclined wing of zero aspect ratio .


Vector Representation for the Rank 5 With Document ID 920


{'approximation': 0.24019058098446416, 'asymptotic': 0.37948970696423406, 'at': 0.06750530221317826, 'distribution': 0.152354903827028, 'expression': 0.2868315024929699, 'found': 0.15300079777058181, 'incidence': 0.3355547307357344, 'laminar': 0.19617368800528992, 'lift': 0.24798866528445648, 'linearized': 0.3496669600635051, 'long': 0.3318519927509069, 'narrow': 0.5492534744193474, 'on': 0.05749589356104888, 'potential': 0.3318519927509069, 'stream': 0.18951397193648478, 'supersonic': 0.19326698423974895, 'theory': 0.12237131028024509, 'used': 0.17492534868552315, 'wing': 0.19279035975607345}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     320       0.06634672768267554   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 1 With Document ID 320


{'accurate': 0.5618011772797783, 'attention': 0.5880409419101723, 'drawn': 0.6330114612824701, 'previous': 0.5701493459299061, 'problem': 0.47744427105224063, 'solution': 0.4649972675032589, 'to': 0.4071860442032682}
======================================================================
2     495       0.02716630131323467   on similar solutions for strong blast waves and their application to steady hypersonic flow .


Vector Representation for the Rank 2 With Document ID 495


{'application': 0.4828544834949395, 'applied': 0.47710833851129375, 'approximation': 0.5129111734854573, 'blast': 0.621057785369898, 'body': 0.4561832456158776, 'busemann': 0.5882307557277564, 'case': 0.4465038380089661, 'constitutes': 0.6121596658135473, 'density': 0.4975383456365823, 'equivalence': 0.5782993607252815, 'expression': 0.4955189325749677, 'flow': 0.42503130656712107, 'formula': 0.5295915246980775, 'found': 0.47192413436730457, 'general': 0.46598933333044806, 'higher': 0.48975187143199406, 'hypersonic': 0.4782786919435343, 'ie': 0.5403729355561747, 'improvement': 0.5543704506394906, 'investigated': 0.48395928561509266, 'law': 0.513023197446849, 'layer': 0.443594992322545, 'neglecting': 0.5742332406444406, 'newton': 0.6121596658135473, 'newtonian': 0.5202414895656916, 'obtained': 0.44273404695715596, 'order': 0.4978437563220729, 'power': 0.4975383456365823, 'pressure': 0.4474280570559596, 'principle': 0.5350513273022536, 'profile': 0.48909428736105814, 'result': 0.4268610674270521, 'shock': 0.46160962517909226, 'shown': 0.45495018168516727, 'simple': 0.49969289535611433, 'solution': 0.4436822796507534, 'strong': 0.5744936347009806, 'temperature': 0.45772352130092187, 'term': 0.4753145781731939, 'thin': 0.4853919443018812, 'to': 0.4039123464639378, 'upon': 0.502446510387068, 'using': 0.47804142558060325, 'velocity': 0.4522708991519398, 'wave': 0.49338796862350176}
======================================================================
3     264       0.02657370342283728   asymptotic solution of the two dimensional oscillating aerofoil problem for high subsonic mach numbers .


Vector Representation for the Rank 3 With Document ID 264


{'asymptotic': 0.5597034505681145, 'boundary': 0.44884165346989835, 'burger': 0.7743942428825275, 'by': 0.422026559971663, 'equation': 0.4552022755912801, 'given': 0.473631497192996, 'ha': 0.46085455189794094, 'identical': 0.595081397479316, 'lead': 0.5332599418038924, 'method': 0.47233880801510275, 'new': 0.5276830350117669, 'obtaining': 0.5756115083221334, 'previously': 0.5404278885762452, 'problem': 0.465773534147066, 'result': 0.44446743173259623, 'simpler': 0.592436564904029, 'solution': 0.4552022755912801, 'than': 0.47245168485994427, 'to': 0.4049441198911225, 'value': 0.4656330303976668, 'wave': 0.4836034653229657}
======================================================================
4     670       0.020116353548652197   on blunt-body heat transfer at hypersonic speed and low reynolds number .


Vector Representation for the Rank 4 With Document ID 670


{'analytical': 0.5422588997028789, 'arising': 0.585600705210302, 'between': 0.47605580372077766, 'comparison': 0.509231120199101, 'data': 0.4863873660903871, 'difference': 0.538790502131019, 'discussion': 0.5415440334810254, 'due': 0.507166240191584, 'experimental': 0.47164566729436025, 'inconsistency': 0.7340164633799497, 'introduced': 0.561680188119037, 'made': 0.4636564638328384, 'particular': 0.5189948575499214, 'presentation': 0.6278489903489475, 'result': 0.43587580064665254, 'those': 0.5058393011993949, 'to': 0.40522535309447577, 'way': 0.5687877596016573}
======================================================================
5     570       0.020073519664242458   on the boundary layer equations in hypersonic flow and their approximate solutions .


Vector Representation for the Rank 5 With Document ID 570


{'also': 0.4550861898520269, 'analytical': 0.5122493601370598, 'at': 0.43292108857340844, 'begin': 0.5983687924684361, 'between': 0.46001181873470043, 'boundary': 0.44073065889516255, 'coefficient': 0.49310107418489363, 'conventional': 0.5321851375327376, 'downstream': 0.5100437473904474, 'equation': 0.44603499057891066, 'first': 0.4769223858819318, 'flat': 0.47503473939743446, 'friction': 0.5055216139722963, 'heat': 0.46195632942021303, 'hypersonic': 0.4824947524479276, 'increase': 0.5367634212814248, 'interaction': 0.546633212732902, 'layer': 0.46384256012170233, 'leadingedge': 0.6131202083775986, 'local': 0.5272408907255706, 'mach': 0.46632834036148885, 'number': 0.44623363012941364, 'obtained': 0.445035686433949, 'over': 0.5003278699364027, 'plate': 0.49355859602623164, 'practically': 0.5675428523626828, 'prandtl': 0.5152088339265083, 'problem': 0.4548507102718087, 'rapidly': 0.5331819524390042, 'region': 0.4762822262314636, 'remains': 0.5564326196115237, 'shock': 0.4649278961026204, 'skin': 0.5002524514575691, 'solution': 0.44603499057891066, 'spread': 0.5675428523626828, 'strong': 0.5302698812206028, 'then': 0.4873169943877748, 'to': 0.40412306395290676, 'transfer': 0.4742262290547146, 'unaffected': 0.5927605644228174, 'value': 0.45473353958073454, 'velocity': 0.4550861898520269, 'viscous': 0.49254525586600556}
======================================================================
========================================================================================================================================================================


Query No: 12

Query Vector for weight (Version 1) are:
[('aerodynamic', 0.06413529647326607),
 ('calculated', 0.06413529647326607),
 ('can', 0.044828648454010654),
 ('channel', 0.08344194449252153),
 ('effect', 0.06413529647326607),
 ('flow', 0.029241331147231073),
 ('ground', 0.08344194449252153),
 ('machine', 0.08344194449252153),
 ('performance', 0.08344194449252153)]

Query Vector for weight (Version 2) are:
[('aerodynamic', 0.06346015586490361),
 ('calculated', 0.06346015586490361),
 ('can', 0.05773585633845527),
 ('channel', 0.06918445539135194),
 ('effect', 0.06346015586490361),
 ('flow', 0.05311431494044519),
 ('ground', 0.06918445539135194),
 ('machine', 0.06918445539135194),
 ('performance', 0.06918445539135194)]

Ranks  Document Number   Scores Titles


1     650       0.0714873905475231   some design problems of hovercraft .


Vector Representation for the Rank 1 With Document ID 650


{'aerodynamic': 0.19814096454326377, 'analysis': 0.14343792139007638, 'angle': 0.163564324255595, 'considered': 0.15993055680978174, 'cushion': 0.5271982855734489, 'drag': 0.19938423935311986, 'dynamic': 0.2660255713229804, 'each': 0.22900303544888745, 'economics': 0.6214421478571256, 'effect': 0.13357023494580939, 'examined': 0.29681748236510425, 'ground': 0.32685940877657377, 'influence': 0.23638689930953372, 'jet': 0.335714298746996, 'lift': 0.20521335021328854, 'machine': 0.37839647016748407, 'on': 0.047578484797422, 'operation': 0.3453126223855793, 'optimum': 0.3387105610060959, 'over': 0.14813042879608032, 'parameter': 0.18879464604080065, 'performance': 0.3028753722576236, 'peripheral': 0.5271982855734489, 'power': 0.24237429107975692, 'pressure': 0.0834887895608359, 'ratio': 0.195256628072377, 'related': 0.3071654891969682, 'requirement': 0.3296722660314134, 'simple': 0.17549188555788003, 'stability': 0.23261554649289723, 'structural': 0.3241358638258134, 'system': 0.24341411545136124, 'then': 0.2058861729589721, 'thickness': 0.1813765551041639, 'to': 0.009721840107770649, 'various': 0.19047126866708147, 'wave': 0.16439316606881269, 'weight': 0.3241358638258134}
======================================================================
2     592       0.027892330193385172   design of axial compressors .


Vector Representation for the Rank 2 With Document ID 592


{'advocated': 0.5619808910508631, 'aerodynamic': 0.19814096454326377, 'air': 0.17692564250327128, 'also': 0.12988863039831225, 'axial': 0.22725227141027599, 'bending': 0.2731192355396403, 'blade': 0.46965022359082137, 'coefficient': 0.1579763843732755, 'compressor': 0.3644548715088276, 'considered': 0.15993055680978174, 'construction': 0.3950520390840711, 'curve': 0.23261554649289723, 'described': 0.22220467087088383, 'design': 0.21292162691329164, 'different': 0.3207808785619178, 'due': 0.19938423935311986, 'efficiency': 0.3950520390840711, 'estimate': 0.2841526078838075, 'flow': 0.09012434747486854, 'form': 0.1579763843732755, 'generalized': 0.31403190967724753, 'loading': 0.2335429550964559, 'main': 0.27924930419983346, 'make': 0.3214961336939525, 'mass': 0.2582216064253042, 'material': 0.26203487688769017, 'method': 0.09736364101196376, 'outlet': 0.4833773851213525, 'performance': 0.3028753722576236, 'power': 0.24237429107975692, 'pressure': 0.0834887895608359, 'ratio': 0.13475917316521085, 'rise': 0.3028753722576236, 'rotational': 0.37839647016748407, 'speed': 0.1534603701070292, 'stage': 0.34194809467438225, 'stress': 0.19160750329564033, 'temperature': 0.14343792139007638, 'to': 0.014086267179562515, 'type': 0.17789496875257943, 'use': 0.18395285864509878, 'variable': 0.24237429107975692, 'weight': 0.3241358638258134}
======================================================================
3     506       0.027305163651264504   a note on havelock's shallow-water wave-resistance curves .


Vector Representation for the Rank 3 With Document ID 506


{'acting': 0.35041542073362547, 'additional': 0.2930483094538725, 'analysis': 0.13283120624992406, 'attention': 0.29081038653619173, 'below': 0.24762502642954715, 'between': 0.13103922778854696, 'by': 0.04010904208165435, 'can': 0.1253420912509042, 'component': 0.2515650575245636, 'computer': 0.302689338503849, 'contact': 0.38499752796799536, 'continuous': 0.3107750585362357, 'currently': 0.3780852563019674, 'cushion': 0.4882138804505711, 'differ': 0.3658393706105376, 'digital': 0.35041542073362547, 'due': 0.1846404964868014, 'effect': 0.08536864256989969, 'equation': 0.10052002661977971, 'estimate': 0.26314055096784983, 'focused': 0.5754887502163468, 'from': 0.0654778691891005, 'generated': 0.3136641409190199, 'gravity': 0.3780852563019674, 'ground': 0.302689338503849, 'h': 0.34587469861049364, 'havelock': 0.7965784284662087, 'however': 0.2020778426627266, 'ibm': 0.41029581399344117, 'improved': 0.3603585072196042, 'land': 0.5754887502163468, 'machine': 0.35041542073362547, 'made': 0.10967596759648604, 'mean': 0.18235426647735564, 'motion': 0.19994028742732853, 'no': 0.1858087676880529, 'note': 0.23145091979847232, 'on': 0.060987164741596066, 'operates': 0.5754887502163468, 'original': 0.326401922980584, 'over': 0.22458960963145036, 'performance': 0.28047883467975504, 'physical': 0.26314055096784983, 'present': 0.14847120469611422, 'pressure': 0.07731509574482126, 'purpose': 0.23145091979847232, 'quest': 0.5754887502163468, 'resistance': 0.326401922980584, 'result': 0.08555832431100736, 'should': 0.258599828844718, 'shown': 0.12644930095033347, 'similar': 0.20502043869519987, 'solution': 0.10052002661977971, 'supporting': 0.4009390106847955, 'surface': 0.116999638472775, 'system': 0.22541452260545322, 't': 0.326401922980584, 'terrain': 0.5204244381420449, 'these': 0.10276369593045806, 'to': 0.014739876826450955, 'transportation': 0.5754887502163468, 'using': 0.17958600694669774, 'vehicle': 0.2515650575245636, 'water': 0.5989625761776486, 'wave': 0.15223688642824418}
======================================================================
4     339       0.02620065332060848   experimental evaluation of heat transfer with transpiration cooling in a turbulent boundary layer at m=3 .2.


Vector Representation for the Rank 4 With Document ID 339


{'accelerator': 0.5619808910508631, 'analytic': 0.3488145151546617, 'boundary': 0.09603948854195138, 'by': 0.04331179236839078, 'calculated': 0.1866089364588232, 'can': 0.13535079247784257, 'conductivity': 0.3524654687089807, 'current': 0.360269433606657, 'electrical': 0.3835971206320758, 'field': 0.26577924259061636, 'found': 0.12660984428377786, 'integration': 0.2875844439235415, 'investigation': 0.1639777441416276, 'layer': 0.10832975779775116, 'physically': 0.4014093514806447, 'prescribed': 0.3488145151546617, 'reasonable': 0.3164485331545604, 'related': 0.3071654891969682, 'that': 0.04725898923138793, 'to': 0.009721840107770649, 'velocity': 0.12988863039831225, 'work': 0.23833663006222613}
======================================================================
5     925       0.02421835342999025   factors affecting loads at hypersonic speeds .


Vector Representation for the Rank 5 With Document ID 925


{'aerodynamic': 0.19814096454326377, 'aircraft': 0.2660255713229804, 'at': 0.055861380633815266, 'blunt': 0.22812318711727908, 'both': 0.16866193031101664, 'boundary': 0.09603948854195138, 'brief': 0.3296722660314134, 'can': 0.13535079247784257, 'characteristic': 0.1813765551041639, 'component': 0.2716527987994464, 'configuration': 0.2488111440108371, 'current': 0.360269433606657, 'deal': 0.3453126223855793, 'designer': 0.44305837743833826, 'discussed': 0.1648106095218505, 'effect': 0.09218542078944494, 'employ': 0.44305837743833826, 'estimating': 0.360269433606657, 'give': 0.20322597653563415, 'hypersonic': 0.19451572961012958, 'information': 0.29681748236510425, 'interference': 0.29681748236510425, 'layer': 0.10832975779775116, 'load': 0.31173720439012015, 'method': 0.09736364101196376, 'on': 0.047578484797422, 'paper': 0.24186824538519194, 'several': 0.21666826866528383, 'slender': 0.2413469199941321, 'speed': 0.1534603701070292, 'summary': 0.3891335228376759, 'touch': 0.5619808910508631, 'upon': 0.2545706528709851, 'various': 0.19047126866708147}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     650       0.03490501223607921   some design problems of hovercraft .


Vector Representation for the Rank 1 With Document ID 650


{'aerodynamic': 0.4923193697861977, 'analysis': 0.4668317050777384, 'angle': 0.47620915427352095, 'considered': 0.4745160812569422, 'cushion': 0.6456363003415054, 'drag': 0.4928986459958475, 'dynamic': 0.5239486905101255, 'each': 0.5066988644195854, 'economics': 0.6895471291411022, 'effect': 0.4579419469798412, 'examined': 0.5382954957175909, 'ground': 0.5522928622887253, 'influence': 0.510139211345186, 'jet': 0.545630799453672, 'lift': 0.4956145903855658, 'machine': 0.5763054083021599, 'on': 0.4221681354080676, 'operation': 0.5608907262127273, 'optimum': 0.5578146427423119, 'over': 0.46901807440039683, 'parameter': 0.48796466082453793, 'performance': 0.5411180346024739, 'peripheral': 0.6456363003415054, 'power': 0.5129289031999936, 'pressure': 0.4388997421822175, 'ratio': 0.48470112518572905, 'related': 0.5431169190485163, 'requirement': 0.5536034504836699, 'simple': 0.4817665358329145, 'stability': 0.5083820334891286, 'structural': 0.5510238871728619, 'system': 0.5134133862088258, 'then': 0.495928077160007, 'thickness': 0.4845083665551241, 'to': 0.4045296748907044, 'various': 0.48874584579849983, 'wave': 0.4765953346579007, 'weight': 0.5510238871728619}
======================================================================
2     339       0.017838785384061973   experimental evaluation of heat transfer with transpiration cooling in a turbulent boundary layer at m=3 .2.


Vector Representation for the Rank 2 With Document ID 339


{'accelerator': 0.6937035928081268, 'analytic': 0.5822981492003731, 'boundary': 0.45019235224080445, 'by': 0.422635696750772, 'calculated': 0.49752594075854323, 'can': 0.470737305615204, 'conductivity': 0.5842062179499601, 'current': 0.5882847419088619, 'electrical': 0.600476305003574, 'field': 0.5243954348323326, 'found': 0.466169093546025, 'integration': 0.5502979652175162, 'investigation': 0.4856983811405233, 'layer': 0.4566155176802161, 'physically': 0.6097853692074651, 'prescribed': 0.5822981492003731, 'reasonable': 0.5653829740590666, 'related': 0.5605314508027468, 'that': 0.42469858877903194, 'to': 0.40508084779007186, 'velocity': 0.46788265939358864, 'work': 0.5245599728776573}
======================================================================
3     203       0.017075146578909736   calculated velocity distributions and force derivatives for a series of high-speed aerofoils .


Vector Representation for the Rank 3 With Document ID 203


{'aerodynamic': 0.4941768890293862, 'aerofoil': 0.5609899648489256, 'agreement': 0.4834117259388505, 'also': 0.46173638631162445, 'at': 0.44013609511357404, 'being': 0.5128159992882652, 'calculate': 0.5693401632510229, 'calculated': 0.48869568764482857, 'centre': 0.594054481151753, 'comparison': 0.49659380776813594, 'considered': 0.47601538801328513, 'distribution': 0.45992392945797494, 'experimental': 0.4633567412055911, 'flow': 0.42956410616967816, 'good': 0.49506652938790974, 'incidence': 0.5768823387362422, 'lift': 0.5307232802214298, 'low': 0.49628374113685136, 'made': 0.4562918353255073, 'method': 0.4462771786551921, 'number': 0.4372876951843522, 'only': 0.4793416949580196, 'over': 0.47040675807126087, 'polygon': 0.6388488212845457, 'result': 0.4317252096735271, 'show': 0.4905314636672691, 'slope': 0.5470556276300269, 'subcritical': 0.6388488212845457, 'these': 0.4527440712448585, 'to': 0.40462081457563026, 'twodimensional': 0.5823246573217878, 'used': 0.46880129219170824, 'velocity': 0.46173638631162445, 'wood': 0.6505786451145108, 'zero': 0.5294573001772529}
======================================================================
4     506       0.016833098415046696   a note on havelock's shallow-water wave-resistance curves .


Vector Representation for the Rank 4 With Document ID 506


{'acting': 0.5381560714943223, 'additional': 0.5155383033869846, 'analysis': 0.4523705195077352, 'attention': 0.5146559716734813, 'below': 0.4976295528991288, 'between': 0.4516640074943427, 'by': 0.4158135383248848, 'can': 0.4494178335070232, 'component': 0.4991829640375808, 'computer': 0.5193394109293377, 'contact': 0.5517905401757899, 'continuous': 0.522527316622925, 'currently': 0.5490652825473424, 'cushion': 0.5924849986077602, 'differ': 0.5442371746531338, 'digital': 0.5381560714943223, 'due': 0.4727970406666805, 'effect': 0.4336577547345608, 'equation': 0.4396313950887745, 'estimate': 0.5037467606204611, 'focused': 0.6268943094816213, 'from': 0.42581554532630533, 'generated': 0.5236663768600379, 'gravity': 0.5490652825473424, 'ground': 0.5193394109293377, 'h': 0.5363658297036902, 'havelock': 0.7292720342320813, 'however': 0.47967195284922304, 'ibm': 0.5617647353909947, 'improved': 0.5420762693114022, 'land': 0.6268943094816213, 'machine': 0.5381560714943223, 'made': 0.4432412500247455, 'mean': 0.47189566322165777, 'motion': 0.4788291924669703, 'no': 0.47325764756367994, 'note': 0.4912526901817251, 'on': 0.425209530008462, 'operates': 0.6268943094816213, 'original': 0.5286884216247696, 'over': 0.4923817490124351, 'performance': 0.5105826160719018, 'physical': 0.5037467606204611, 'present': 0.45853680276941133, 'pressure': 0.4304825337679179, 'purpose': 0.4912526901817251, 'quest': 0.6268943094816213, 'resistance': 0.5286884216247696, 'result': 0.4353662144047987, 'should': 0.5019565188298291, 'shown': 0.44985436607192375, 'similar': 0.4808321115745159, 'solution': 0.4396313950887745, 'supporting': 0.558075687733899, 'surface': 0.4461287074176512, 'system': 0.4888727580416929, 't': 0.5286884216247696, 'terrain': 0.6051844514514124, 'these': 0.4405159923962981, 'to': 0.40606303917483066, 'transportation': 0.6268943094816213, 'using': 0.47080423904622704, 'vehicle': 0.4991829640375808, 'water': 0.6463747564773205, 'wave': 0.46002147428734796}
======================================================================
5     925       0.016830164592192477   factors affecting loads at hypersonic speeds .


Vector Representation for the Rank 5 With Document ID 925


{'aerodynamic': 0.4937055365986116, 'aircraft': 0.5258097686525044, 'at': 0.42641816476212824, 'blunt': 0.5078848369830289, 'both': 0.47976420585204405, 'boundary': 0.44541933985849125, 'brief': 0.5559097921086812, 'can': 0.4640105829070708, 'characteristic': 0.4857772518753045, 'component': 0.5284710172815307, 'configuration': 0.517668659860385, 'current': 0.5703799144917274, 'deal': 0.563306485609891, 'designer': 0.6095327591549323, 'discussed': 0.4779428253919555, 'effect': 0.4435966602946338, 'employ': 0.6095327591549323, 'estimating': 0.5703799144917274, 'give': 0.496110358733468, 'hypersonic': 0.49199107747357185, 'information': 0.540371989815352, 'interference': 0.540371989815352, 'layer': 0.4512316981369061, 'load': 0.536592569530584, 'method': 0.4460455628004604, 'on': 0.42250098791417684, 'paper': 0.5059783839072121, 'several': 0.502467535807011, 'slender': 0.5141386522297577, 'speed': 0.472575029402165, 'summary': 0.584030423239666, 'touch': 0.665774021416902, 'upon': 0.5203924674764865, 'various': 0.4900783564782236}
======================================================================
========================================================================================================================================================================


Query No: 13

Query Vector for weight (Version 1) are:
[('aileron', 0.15019550008653876),
 ('basic', 0.11544353365187894),
 ('buzz', 0.15019550008653876),
 ('mechanism', 0.15019550008653876),
 ('transonic', 0.15019550008653876)]

Query Vector for weight (Version 2) are:
[('aileron', 0.1354601226993865),
 ('basic', 0.12262785860758145),
 ('buzz', 0.1354601226993865),
 ('mechanism', 0.1354601226993865),
 ('transonic', 0.1354601226993865)]

Ranks  Document Number   Scores Titles


1     879       0.03662881113571643   flutter model testing at transonic speeds .


Vector Representation for the Rank 1 With Document ID 879


{'construction': 0.3950520390840711, 'delta': 0.32685940877657377, 'developed': 0.17887537325596373, 'facility': 0.3950520390840711, 'flutter': 0.27924930419983346, 'foot': 0.32685940877657377, 'model': 0.26133963885470796, 'on': 0.047578484797422, 'plane': 0.23079027635009564, 'reflection': 0.36885503908586875, 'research': 0.2875844439235415, 'straight': 0.3387105610060959, 'swept': 0.3387105610060959, 'technique': 0.2393283689727511, 'test': 0.15875271962933116, 'testing': 0.33559078227780864, 'transonic': 0.2824868378681199, 'wing': 0.15953614480318243, 'x': 0.23448049951385272}
======================================================================
2     880       0.027607249406832558   the design and testing of supersonic flutter models .


Vector Representation for the Rank 2 With Document ID 880


{'airplane': 0.3296722660314134, 'basic': 0.31403190967724753, 'become': 0.34194809467438225, 'check': 0.37839647016748407, 'compared': 0.24629655002647194, 'edge': 0.17454918969413313, 'elsewhere': 0.4677370287671866, 'flutter': 0.27924930419983346, 'full': 0.3296722660314134, 'given': 0.11052385336735143, 'ii': 0.4677370287671866, 'included': 0.23448049951385272, 'leading': 0.2144007059732076, 'low': 0.20257362008142774, 'mach': 0.11254769596942187, 'number': 0.07845045600431105, 'on': 0.047578484797422, 'parameter': 0.18879464604080065, 'problem': 0.12933338923453824, 'range': 0.13837168420922066, 'result': 0.09671233772196752, 'reviewed': 0.3562787391713667, 'scale': 0.29488966055399934, 'scaled': 0.6214421478571256, 'serve': 0.4545132958903335, 'simulate': 0.4082757719609241, 'speed': 0.1534603701070292, 'supersonic': 0.15993055680978174, 'table': 0.3164485331545604, 'testing': 0.33559078227780864, 'these': 0.11096948792961203, 'those': 0.19691545141064268, 'transonic': 0.2824868378681199, 'velocity': 0.12988863039831225}
======================================================================
3     38       0.021748629596994237   on the prediction of mixed subsonic/supersonic pressure distributions .


Vector Representation for the Rank 3 With Document ID 38


{'also': 0.12028383628788435, 'analyzed': 0.26631861515333216, 'by': 0.05551802306592111, 'can': 0.1253420912509042, 'considered': 0.1481042709723417, 'derive': 0.3780852563019674, 'distribution': 0.11675254337477482, 'empirical': 0.5042456405079841, 'flow': 0.07973013920664691, 'high': 0.15185218344903273, 'improved': 0.3603585072196042, 'introducing': 0.38499752796799536, 'linked': 0.5204244381420449, 'mechanism': 0.30798736864961457, 'part': 0.21044778843644407, 'physical': 0.26314055096784983, 'prediction': 0.22938740092440651, 'pressure': 0.1070177956423496, 'relation': 0.36747849756945095, 'result': 0.08555832431100736, 'rise': 0.28047883467975504, 'scheme': 0.4009390106847955, 'semiempirical': 0.3780852563019674, 'separately': 0.37172658276448406, 'shock': 0.19624001563108695, 'shown': 0.12644930095033347, 'significance': 0.32302094422766553, 'solution': 0.10052002661977971, 'speed': 0.14211253115863087, 'subsonic': 0.21206908981096217, 'supersonic': 0.1481042709723417, 'that': 0.043764358022771316, 'then': 0.1906616356350296, 'theoretical': 0.1537946031990999, 'to': 0.012461671841138389, 'transonic': 0.3620979396832128, 'treated': 0.24635394315328818, 'tunnel': 0.1661060613333444, 'wind': 0.1951655709966986}
======================================================================
4     496       0.02097454701031569   a theory of transonic aileron buzz, neglecting viscous effects .


Vector Representation for the Rank 4 With Document ID 496


{'agreement': 0.1625148957808278, 'aileron': 0.554970652201324, 'airfoil': 0.3409975204723399, 'analysis': 0.18386193211606205, 'approximation': 0.1840627411405065, 'around': 0.2730836374538286, 'boundary': 0.08893771596118338, 'buzz': 0.5754887502163468, 'by': 0.04010904208165435, 'comparison': 0.18819815110911567, 'developed': 0.1656481868095371, 'distribution': 0.11675254337477482, 'due': 0.1846404964868014, 'effect': 0.08536864256989969, 'experimental': 0.12344084813192648, 'first': 0.16796441531262127, 'flow': 0.05760110558725104, 'flutter': 0.258599828844718, 'from': 0.0654778691891005, 'harmonic': 0.39256906491107807, 'hinge': 0.4331495683762693, 'linearized': 0.2679566321533636, 'local': 0.19994028742732853, 'moment': 0.21541446873807338, 'neglected': 0.302689338503849, 'nonsteady': 0.4331495683762693, 'numerical': 0.17083608978255838, 'observation': 0.302689338503849, 'obtained': 0.13611720601244287, 'oscillation': 0.2953511086593236, 'perturbation': 0.45179811205427917, 'present': 0.14847120469611422, 'presented': 0.11480297289695095, 'pressure': 0.07731509574482126, 'region': 0.16656659021704162, 'result': 0.10119983722076477, 'satisfactory': 0.26631861515333216, 'series': 0.22350018877046007, 'shock': 0.14177376301216435, 'show': 0.17638660772417045, 'solution': 0.13913753275639817, 'sponsored': 0.4882138804505711, 'stability': 0.21541446873807338, 'supersonic': 0.1481042709723417, 'terminated': 0.4653601260677431, 'theoretical': 0.1537946031990999, 'theory': 0.09377552906037659, 'to': 0.012461671841138389, 'transonic': 0.3620979396832128, 'twodimensional': 0.35523150191913927, 'unsteady': 0.2930483094538725, 'usaf': 0.4882138804505711, 'vicinity': 0.326401922980584, 'viscous': 0.2020778426627266, 'wave': 0.15223688642824418}
======================================================================
5     258       0.01836205231766431   the effect of turbulence on slider bearing lubrication .


Vector Representation for the Rank 5 With Document ID 258


{'also': 0.12988863039831225, 'analytical': 0.26467460701955103, 'based': 0.1704307447358744, 'bearing': 0.4545132958903335, 'capacity': 0.4082757719609241, 'carrying': 0.44305837743833826, 'compared': 0.16998511017361387, 'consequently': 0.42391612831509007, 'derived': 0.19103750478445003, 'effect': 0.09218542078944494, 'equation': 0.10854665920362061, 'flow': 0.09012434747486854, 'found': 0.12660984428377786, 'given': 0.11052385336735143, 'however': 0.2182139764355936, 'increase': 0.2925769392191645, 'laminar': 0.16233588617078312, 'length': 0.2255365250108158, 'load': 0.21514991999592978, 'loss': 0.3524654687089807, 'lubrication': 0.5619808910508631, 'mechanism': 0.3325804923459027, 'mixing': 0.3049936147025652, 'on': 0.047578484797422, 'one': 0.14442207513234676, 'power': 0.24237429107975692, 'prandtls': 0.5025196342446008, 'pressure': 0.1209694238143449, 'slider': 0.6214421478571256, 'solution': 0.10854665920362061, 'that': 0.04725898923138793, 'turbulent': 0.30128603528752607}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     879       0.017456692408326365   flutter model testing at transonic speeds .


Vector Representation for the Rank 1 With Document ID 879


{'construction': 0.6160212861776635, 'delta': 0.5787323767443203, 'developed': 0.4978121471942074, 'facility': 0.6160212861776635, 'flutter': 0.5526983482918516, 'foot': 0.5787323767443203, 'model': 0.5259327851035132, 'on': 0.42601673821037095, 'plane': 0.5262001139141983, 'reflection': 0.6016963135823351, 'research': 0.5572561468233073, 'straight': 0.5852127917125465, 'swept': 0.5852127917125465, 'technique': 0.5308688906002428, 'test': 0.48680873223193777, 'testing': 0.5835068427569687, 'transonic': 0.5544686876848294, 'wing': 0.4872371226639216, 'x': 0.5282179917511679}
======================================================================
2     880       0.014424189456131616   the design and testing of supersonic flutter models .


Vector Representation for the Rank 2 With Document ID 880


{'airplane': 0.5499075314628131, 'basic': 0.542795598025172, 'become': 0.5554895574872668, 'check': 0.5720632476607675, 'compared': 0.5050942562824993, 'edge': 0.47937045618325835, 'elsewhere': 0.6126879042641654, 'flutter': 0.5269793615314804, 'full': 0.5499075314628131, 'given': 0.4502570574877501, 'ii': 0.6126879042641654, 'included': 0.5066222320774161, 'leading': 0.49749161178534024, 'low': 0.4921136366472483, 'mach': 0.45117733280298317, 'number': 0.43567274355015867, 'on': 0.42163473831930676, 'parameter': 0.48584810509560794, 'problem': 0.45881007022295706, 'range': 0.4629199351642751, 'result': 0.44126696539248994, 'reviewed': 0.5620059428862417, 'scale': 0.5340912949691214, 'scaled': 0.6825802105031589, 'serve': 0.6066748502206574, 'simulate': 0.5856498693915145, 'speed': 0.46978101475458167, 'supersonic': 0.4727231176144587, 'table': 0.543894477419305, 'testing': 0.5525987804753556, 'these': 0.45045969502826017, 'those': 0.4895407720619186, 'transonic': 0.5284515226146159, 'velocity': 0.45906254773108923}
======================================================================
3     496       0.013913077306230537   a theory of transonic aileron buzz, neglecting viscous effects .


Vector Representation for the Rank 3 With Document ID 496


{'agreement': 0.46664901552802507, 'aileron': 0.6360188432680618, 'airfoil': 0.54501999343555, 'analysis': 0.47819310871112825, 'approximation': 0.4754860065808916, 'around': 0.5119943836881011, 'boundary': 0.4364742639968101, 'buzz': 0.6360138033199166, 'by': 0.416449127051834, 'comparison': 0.47718198036771475, 'developed': 0.4679340101214309, 'distribution': 0.44788140827912826, 'due': 0.4757229499383703, 'effect': 0.4350105506139019, 'experimental': 0.45062435024437886, 'first': 0.4688839190434826, 'flow': 0.4236228006194187, 'flutter': 0.5060544261214087, 'from': 0.4268531416726982, 'harmonic': 0.5609965755900106, 'hinge': 0.5776390537615756, 'linearized': 0.509891746546803, 'local': 0.4819975501777597, 'moment': 0.488343669685809, 'neglected': 0.5241359835058924, 'nonsteady': 0.5776390537615756, 'numerical': 0.4700616220190694, 'observation': 0.5241359835058924, 'obtained': 0.4578881520752614, 'oscillation': 0.5211265006366078, 'perturbation': 0.5921414535611559, 'present': 0.4608895546448937, 'presented': 0.44708186955115403, 'pressure': 0.4317077089585486, 'region': 0.4683106567215697, 'result': 0.4425635328495045, 'satisfactory': 0.509219979076223, 'series': 0.4916597059014713, 'shock': 0.4581428655328161, 'show': 0.47233794601202816, 'solution': 0.45917264166326455, 'sponsored': 0.6002214894998331, 'stability': 0.488343669685809, 'supersonic': 0.46073907138404563, 'terminated': 0.5908489318434016, 'theoretical': 0.4630727346406883, 'theory': 0.43845830046817863, 'to': 0.40529972055542984, 'transonic': 0.553993614860156, 'twodimensional': 0.5456840603668864, 'unsteady': 0.5201820992064212, 'usaf': 0.6002214894998331, 'vicinity': 0.5338607561392326, 'viscous': 0.4828741833712375, 'wave': 0.462433899112719}
======================================================================
4     38       0.012802939286364376   on the prediction of mixed subsonic/supersonic pressure distributions .


Vector Representation for the Rank 4 With Document ID 38


{'also': 0.45583804378960213, 'analyzed': 0.5236301647324147, 'by': 0.42576622645437634, 'can': 0.4581861819172229, 'considered': 0.4687528185265712, 'derive': 0.5755143645989503, 'distribution': 0.45419875047803704, 'empirical': 0.6268810603514431, 'flow': 0.437003205600425, 'high': 0.47049267075818935, 'improved': 0.567285270632083, 'introducing': 0.5787231725309615, 'linked': 0.6415909191373339, 'mechanism': 0.5429735923631638, 'part': 0.4976938646853144, 'physical': 0.5221548469122348, 'prediction': 0.5064859929055171, 'pressure': 0.44966756027848487, 'relation': 0.5653438413486732, 'result': 0.43970809905527053, 'rise': 0.5302036078681525, 'scheme': 0.5861235119072468, 'semiempirical': 0.5755143645989503, 'separately': 0.5725625474439006, 'shock': 0.4910760939048046, 'shown': 0.4587001697113354, 'significance': 0.5499524639833904, 'solution': 0.4466633075677234, 'speed': 0.4659713389826935, 'subsonic': 0.4984465036095487, 'supersonic': 0.4687528185265712, 'that': 0.4203162470961651, 'then': 0.488508756356138, 'theoretical': 0.47139437893785247, 'to': 0.40578353192219474, 'transonic': 0.5680516883942826, 'treated': 0.5143621843970072, 'tunnel': 0.47710959188440727, 'wind': 0.49059956878540323}
======================================================================
5     440       0.010584600151416945   compilation of information on the transonic attachment of flows at the leading edge of airfoils .


Vector Representation for the Rank 5 With Document ID 440


{'affecting': 0.586888869197301, 'airfoil': 0.5772136702243456, 'analyzed': 0.518250295446964, 'angle': 0.4672551317586196, 'at': 0.4372122132345645, 'attachment': 0.586888869197301, 'attack': 0.48972622730256615, 'basic': 0.5291250861572385, 'camber': 0.5624393159145868, 'change': 0.4917046850413337, 'compiled': 0.6167758178351523, 'data': 0.46608758902685626, 'determine': 0.49308812703305116, 'dimensional': 0.49433497285870587, 'edge': 0.47177193929462674, 'factor': 0.5023073115095226, 'fixed': 0.5263017197769903, 'flow': 0.4449166099811245, 'from': 0.4290733615162084, 'having': 0.4927371465325193, 'increased': 0.5088301232513536, 'information': 0.5220467786944314, 'involved': 0.5245376897458165, 'leading': 0.48815826920078437, 'mach': 0.44627787970269195, 'number': 0.43225761961910986, 'on': 0.41956354038993093, 'past': 0.5111066065951448, 'photograph': 0.5535746394399526, 'profile': 0.49103279331193317, 'provide': 0.5204788205926496, 'related': 0.5263017197769903, 'schlieren': 0.5449283738753637, 'separated': 0.5263017197769903, 'shaped': 0.5709458852598596, 'speed': 0.4631005413817905, 'subsonic': 0.4941625222513149, 'these': 0.4456289448561538, 'thickness': 0.4745792468313138, 'to': 0.40647623068062355, 'transition': 0.4988206977447946, 'transonic': 0.5629229864428653, 'two': 0.4606392296262659, 'unseparated': 0.6555274429476381, 'variously': 0.631077889664924, 'vary': 0.5272179595838778, 'were': 0.4550491170517642}
======================================================================
========================================================================================================================================================================


Query No: 14

Query Vector for weight (Version 1) are:
[('interaction', 0.1251629167387823),
 ('on', 0.06724297268101598),
 ('paper', 0.09620294470989911),
 ('shock', 0.1251629167387823),
 ('sound', 0.1251629167387823),
 ('wave', 0.09620294470989911)]

Query Vector for weight (Version 2) are:
[('interaction', 0.11021194605009633),
 ('on', 0.09006108817953544),
 ('paper', 0.10013651711481587),
 ('shock', 0.11021194605009633),
 ('sound', 0.11021194605009633),
 ('wave', 0.10013651711481587)]

Ranks  Document Number   Scores Titles


1     291       0.04427190881096882   sweepback effects in the turbulent boundary-layer shock-wave interaction .


Vector Representation for the Rank 1 With Document ID 291


{'ahead': 0.360269433606657, 'angle': 0.163564324255595, 'at': 0.08093923824135008, 'available': 0.24553235789630273, 'boundary': 0.09603948854195138, 'by': 0.04331179236839078, 'can': 0.13535079247784257, 'configuration': 0.2488111440108371, 'dimensional': 0.163564324255595, 'experiment': 0.20257362008142774, 'extension': 0.2930042119027183, 'influence': 0.23638689930953372, 'interaction': 0.2488111440108371, 'layer': 0.10832975779775116, 'moderate': 0.31893521336122166, 'on': 0.047578484797422, 'peak': 0.360269433606657, 'pressure': 0.1209694238143449, 'reattachment': 0.4014093514806447, 'reported': 0.3325804923459027, 'rise': 0.43884525649832795, 'separation': 0.3292726661580189, 'shock': 0.15309455095854613, 'show': 0.19047126866708147, 'simple': 0.17549188555788003, 'sweep': 0.3644548715088276, 'sweptback': 0.42391612831509007, 'that': 0.04725898923138793, 'theory': 0.10126360623697798, 'turbulent': 0.20793689516404892, 'two': 0.1051403770694433, 'understood': 0.4833773851213525, 'upstream': 0.31403190967724753, 'wave': 0.16439316606881269}
======================================================================
2     1317       0.03323795020750027   shock-tube testing time .


Vector Representation for the Rank 2 With Document ID 1317


{'attenuation': 0.4833773851213525, 'between': 0.1415028515150645, 'conservation': 0.42391612831509007, 'difference': 0.2582216064253042, 'effect': 0.09218542078944494, 'equation': 0.10854665920362061, 'example': 0.2058861729589721, 'experimentally': 0.29681748236510425, 'explanation': 0.4329544232897724, 'given': 0.11052385336735143, 'ideal': 0.3562787391713667, 'investigation': 0.1639777441416276, 'led': 0.4329544232897724, 'mass': 0.2582216064253042, 'numerical': 0.1844775358789806, 'obtained': 0.10619038357284823, 'shock': 0.15309455095854613, 'test': 0.15875271962933116, 'theoretical': 0.24063146214233447, 'time': 0.27679999916474657, 'to': 0.009721840107770649, 'wave': 0.16439316606881269}
======================================================================
3     326       0.030459616885223355   forst-order slip effects on the compressible laminar boundary layer over a slender body of revolution in axial flow .


Vector Representation for the Rank 3 With Document ID 326


{'analysis': 0.14343792139007638, 'boundary': 0.13915450988636802, 'case': 0.11555798590132785, 'compressible': 0.2354284037477369, 'considered': 0.15993055680978174, 'curvature': 0.29115931369431924, 'effect': 0.09218542078944494, 'examined': 0.29681748236510425, 'first': 0.1813765551041639, 'flow': 0.06220061601834868, 'gradient': 0.2189974016094449, 'interaction': 0.2488111440108371, 'layer': 0.15696225147919476, 'no': 0.20064579827032275, 'only': 0.16692885196679205, 'order': 0.17223680008179437, 'pressure': 0.0834887895608359, 'slip': 0.3835971206320758, 'transverse': 0.2858513655793169, 'zero': 0.20322597653563415}
======================================================================
4     1140       0.02856568708913625   shock-standoff distance for spherical bodies at high mach numbers .


Vector Representation for the Rank 4 With Document ID 1140


{'accurate': 0.32653464042795, 'almost': 0.4305425982496091, 'apropriate': 0.7509775004326937, 'behind': 0.3150953381735983, 'by': 0.05233983836505397, 'consideration': 0.2941521179759523, 'development': 0.303402320792395, 'distance': 0.25909106232649964, 'dyke': 0.5354108567977349, 'expression': 0.2868315024929699, 'give': 0.24558703719724512, 'hay': 0.7509775004326937, 'heat': 0.1765388542942732, 'method': 0.11765842405816515, 'prediction': 0.2993364803607412, 'ratio': 0.16284879835226998, 'shock': 0.18500605986439667, 'shockstandoff': 0.7509775004326937, 'simple': 0.2120719652133681, 'specific': 0.33368683078438854, 'sponsored': 0.6370891515767835, 'theory': 0.12237131028024509, 'those': 0.23796112640068073, 'usaf': 0.6370891515767835, 'van': 0.5023981461279287}
======================================================================
5     609       0.027550435777397055   on three dimensional bodies of delta planform which can support plane attached shock waves .


Vector Representation for the Rank 5 With Document ID 609


{'also': 0.12988863039831225, 'attached': 0.3387105610060959, 'available': 0.24553235789630273, 'body': 0.13961047050608286, 'calculation': 0.17361674072744135, 'can': 0.13535079247784257, 'collect': 0.5619808910508631, 'detail': 0.255770455090685, 'discus': 0.3488145151546617, 'from': 0.07070634769260985, 'future': 0.3891335228376759, 'given': 0.11052385336735143, 'illustrating': 0.44305837743833826, 'includes': 0.3524654687089807, 'merit': 0.42391612831509007, 'note': 0.2499325254733439, 'on': 0.047578484797422, 'one': 0.14442207513234676, 'plane': 0.23079027635009564, 'possible': 0.21590573510828764, 'preliminary': 0.32685940877657377, 'property': 0.2238544228750751, 'proposed': 0.31168150346321444, 'report': 0.24770423239070574, 'result': 0.066747412341137, 'shape': 0.17549188555788003, 'shock': 0.15309455095854613, 'such': 0.17789496875257943, 'support': 0.3524654687089807, 'test': 0.23002160078661651, 'theoretical': 0.16607526820455334, 'together': 0.4419144418274188, 'tunnel': 0.17936980955453063, 'wave': 0.16439316606881269, 'wind': 0.21074975241888858, 'work': 0.23833663006222613}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     291       0.02567094417775067   sweepback effects in the turbulent boundary-layer shock-wave interaction .


Vector Representation for the Rank 1 With Document ID 291


{'ahead': 0.5703799144917274, 'angle': 0.4773534276876563, 'at': 0.4354648029543454, 'available': 0.5161180445549496, 'boundary': 0.44541933985849125, 'by': 0.4204831684063067, 'can': 0.4640105829070708, 'configuration': 0.517668659860385, 'dimensional': 0.4773534276876563, 'experiment': 0.49580184397612903, 'extension': 0.5385686042524664, 'influence': 0.511792941433094, 'interaction': 0.517668659860385, 'layer': 0.4512316981369061, 'moderate': 0.550831986596494, 'on': 0.42250098791417684, 'peak': 0.5703799144917274, 'pressure': 0.45300465969649684, 'reattachment': 0.5898359522115957, 'reported': 0.5572851609425697, 'rise': 0.5922869659676546, 'separation': 0.5442760084883067, 'shock': 0.47240202489658145, 'show': 0.4900783564782236, 'simple': 0.48299425281798625, 'sweep': 0.5723593068169193, 'sweptback': 0.6004799379479042, 'that': 0.4223498909235817, 'theory': 0.4478899483618625, 'turbulent': 0.4983382632910418, 'two': 0.449723364747835, 'understood': 0.628600569078889, 'upstream': 0.5485130986074713, 'wave': 0.4777454065348471}
======================================================================
2     609       0.018048331432503246   on three dimensional bodies of delta planform which can support plane attached shock waves .


Vector Representation for the Rank 2 With Document ID 609


{'also': 0.46173638631162445, 'attached': 0.5609899648489256, 'available': 0.5167021351492143, 'body': 0.4663572008872547, 'calculation': 0.4825204649771543, 'can': 0.46433256541678936, 'collect': 0.6671109032659246, 'detail': 0.5215683279911134, 'discus': 0.5657923991703742, 'from': 0.4336069014081445, 'future': 0.5849561229419372, 'given': 0.4525322600385569, 'illustrating': 0.6105867393031668, 'includes': 0.5675277063973734, 'merit': 0.601488381093351, 'note': 0.518793545648648, 'on': 0.4226141711446791, 'one': 0.4686441684307179, 'plane': 0.5096951874388322, 'possible': 0.5026205282838497, 'preliminary': 0.5553570829713047, 'property': 0.506398559179518, 'proposed': 0.5481429871497279, 'report': 0.5177344324518777, 'result': 0.4317252096735271, 'shape': 0.4834117259388505, 'shock': 0.4727662175757632, 'such': 0.48455391730688624, 'support': 0.5675277063973734, 'test': 0.501127320578558, 'theoretical': 0.4789359844910349, 'together': 0.5942844640422835, 'tunnel': 0.4852549127767606, 'wave': 0.4781364771981392, 'wind': 0.5001698769978005, 'work': 0.5132819879662347}
======================================================================
3     1317       0.017887423810201815   shock-tube testing time .


Vector Representation for the Rank 3 With Document ID 1317


{'attenuation': 0.6458254526102559, 'between': 0.47196241195810135, 'conservation': 0.6155859527554903, 'difference': 0.5313206724748029, 'effect': 0.4468816363511566, 'equation': 0.4552022755912801, 'example': 0.5047050673277289, 'experimentally': 0.5509489152594931, 'explanation': 0.6201824502776457, 'given': 0.4562077935678306, 'ideal': 0.5811884151142588, 'investigation': 0.4833921991644365, 'led': 0.6201824502776457, 'mass': 0.5313206724748029, 'numerical': 0.49381753294579583, 'obtained': 0.4540039726891621, 'shock': 0.4778574638366673, 'test': 0.4807349709713705, 'theoretical': 0.5106401041229157, 'time': 0.5272700604324784, 'to': 0.4049441198911225, 'wave': 0.4836034653229657}
======================================================================
4     1276       0.017737746103513446   a three-dimensional linearized analysis of the forces exerted on a rigid wing by a shock wave .


Vector Representation for the Rank 4 With Document ID 1276


{'acoustic': 0.6133739118018908, 'author': 0.5245599728776573, 'by': 0.422635696750772, 'dimensional': 0.48548231880139464, 'distribution': 0.4658897602523783, 'edge': 0.4912232514508652, 'flat': 0.4924652380367039, 'found': 0.466169093546025, 'front': 0.5680209612879695, 'ha': 0.46253746315530136, 'induced': 0.5419717365382082, 'moving': 0.5628916193356822, 'obliquely': 0.7247793554096444, 'on': 0.424865564199593, 'plate': 0.5076594122692809, 'pressure': 0.44363308049027567, 'shock': 0.4800105846513601, 'solution': 0.45672887513276195, 'striking': 0.6444496744034084, 'term': 0.49780879878575807, 'two': 0.4549486770568892}
======================================================================
5     1314       0.016954902941889848   production of high temperature gases in shock tubes .


Vector Representation for the Rank 5 With Document ID 1314


{'aerodynamic': 0.490098033522514, 'briefly': 0.5396733209935751, 'calcualtions': 0.6825802105031589, 'calculation': 0.47894645593448254, 'comparison': 0.4924102741134845, 'discussed': 0.4749421597689022, 'experimental': 0.482412077764572, 'finally': 0.5396733209935751, 'forth': 0.6197998377018066, 'gas': 0.48818148335191924, 'high': 0.47456344185400745, 'intended': 0.5856498693915145, 'k': 0.5540173964041313, 'made': 0.4538538033956382, 'paper': 0.47590536028250163, 'preliminary': 0.5486284778969602, 'production': 0.6891810648819041, 'result': 0.4303511725024419, 'set': 0.5203520012672537, 'shock': 0.515404103378919, 'strength': 0.5262636049575402, 'strong': 0.5899068018947953, 'study': 0.4853480003118644, 'surveyed': 0.6825802105031589, 'temperature': 0.46522363853225823, 'theoretical': 0.4755172213703805, 'thermodynamic': 0.5570194649004543, 'to': 0.40601058266091666, 'tube': 0.5185650794309511, 'up': 0.4936199102282519, 'useful': 0.5396733209935751, 'wave': 0.5016370051958179}
======================================================================
========================================================================================================================================================================


Query No: 15

Query Vector for weight (Version 1) are:
[('material', 0.22510656507197047),
 ('photoelastic', 0.1553605369642814),
 ('property', 0.11941349352594524)]

Query Vector for weight (Version 2) are:
[('material', 0.19897810218978104),
 ('photoelastic', 0.1738562091503268),
 ('property', 0.15676749144637073)]

Ranks  Document Number   Scores Titles


1     509       0.06188354885861543   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 1 With Document ID 509


{'acted': 0.5271982855734489, 'at': 0.055861380633815266, 'by': 0.06275576151877217, 'change': 0.22302558106185744, 'condition': 0.1242304617275272, 'conduction': 0.3093937822796063, 'considers': 0.36885503908586875, 'derived': 0.19103750478445003, 'entry': 0.3164485331545604, 'heat': 0.14608784514803438, 'heated': 0.3524654687089807, 'heating': 0.2545706528709851, 'material': 0.26203487688769017, 'method': 0.09736364101196376, 'most': 0.23261554649289723, 're': 0.32685940877657377, 'severe': 0.3891335228376759, 'space': 0.36885503908586875, 'state': 0.2731192355396403, 'sublimation': 0.5271982855734489, 'such': 0.17789496875257943, 'suitable': 0.3049936147025652, 'surface': 0.12634218584411033, 'under': 0.18036731451851562, 'upon': 0.2545706528709851, 'vehicle': 0.2716527987994464}
======================================================================
2     1096       0.03652143867065829   qualitative measurements of the effective heats of ablation of several materials in supersonic air jets at stagnation temperature up to 11,000 f.


Vector Representation for the Rank 2 With Document ID 1096


{'ablation': 0.4014093514806447, 'air': 0.17692564250327128, 'ammonium': 0.5619808910508631, 'at': 0.055861380633815266, 'carbonate': 0.5619808910508631, 'chloride': 0.5619808910508631, 'content': 0.5025196342446008, 'derived': 0.19103750478445003, 'effective': 0.3093937822796063, 'f': 0.5054078653948213, 'fiber': 0.5025196342446008, 'from': 0.10244855848771407, 'glass': 0.4833773851213525, 'heat': 0.14608784514803438, 'included': 0.23448049951385272, 'inorganic': 0.5619808910508631, 'jet': 0.23169805688805684, 'laminate': 0.6214421478571256, 'lucite': 0.5619808910508631, 'material': 0.37967023169343117, 'melamine': 0.6214421478571256, 'number': 0.07845045600431105, 'nylon': 0.5271982855734489, 'phenolic': 0.5619808910508631, 'plastic': 0.33559078227780864, 'polystyrene': 0.6214421478571256, 'ranging': 0.360269433606657, 'reinforcement': 0.6214421478571256, 'resin': 0.7638734874130575, 'salt': 0.5619808910508631, 'several': 0.21666826866528383, 'sodium': 0.5025196342446008, 'stagnation': 0.20793689516404892, 'supersonic': 0.15993055680978174, 'teflon': 0.4545132958903335, 'temperature': 0.14343792139007638, 'test': 0.15875271962933116, 'to': 0.009721840107770649, 'type': 0.17789496875257943, 'varied': 0.29488966055399934, 'were': 0.1338793248336025}
======================================================================
3     592       0.03652143867065829   design of axial compressors .


Vector Representation for the Rank 3 With Document ID 592


{'advocated': 0.5619808910508631, 'aerodynamic': 0.19814096454326377, 'air': 0.17692564250327128, 'also': 0.12988863039831225, 'axial': 0.22725227141027599, 'bending': 0.2731192355396403, 'blade': 0.46965022359082137, 'coefficient': 0.1579763843732755, 'compressor': 0.3644548715088276, 'considered': 0.15993055680978174, 'construction': 0.3950520390840711, 'curve': 0.23261554649289723, 'described': 0.22220467087088383, 'design': 0.21292162691329164, 'different': 0.3207808785619178, 'due': 0.19938423935311986, 'efficiency': 0.3950520390840711, 'estimate': 0.2841526078838075, 'flow': 0.09012434747486854, 'form': 0.1579763843732755, 'generalized': 0.31403190967724753, 'loading': 0.2335429550964559, 'main': 0.27924930419983346, 'make': 0.3214961336939525, 'mass': 0.2582216064253042, 'material': 0.26203487688769017, 'method': 0.09736364101196376, 'outlet': 0.4833773851213525, 'performance': 0.3028753722576236, 'power': 0.24237429107975692, 'pressure': 0.0834887895608359, 'ratio': 0.13475917316521085, 'rise': 0.3028753722576236, 'rotational': 0.37839647016748407, 'speed': 0.1534603701070292, 'stage': 0.34194809467438225, 'stress': 0.19160750329564033, 'temperature': 0.14343792139007638, 'to': 0.014086267179562515, 'type': 0.17789496875257943, 'use': 0.18395285864509878, 'variable': 0.24237429107975692, 'weight': 0.3241358638258134}
======================================================================
4     119       0.035932383208228315   conduction of fluctuating heat flow in a wall consisting of many layers .


Vector Representation for the Rank 4 With Document ID 119


{'analogy': 0.3325804923459027, 'between': 0.1415028515150645, 'body': 0.13961047050608286, 'bounded': 0.4833773851213525, 'by': 0.04331179236839078, 'case': 0.11555798590132785, 'certain': 0.21292162691329164, 'conduction': 0.3093937822796063, 'consequence': 0.42391612831509007, 'consisting': 0.4014093514806447, 'different': 0.22139154193623733, 'draw': 0.5619808910508631, 'four': 0.2987896257790135, 'from': 0.07070634769260985, 'generalizes': 0.5619808910508631, 'gorcum': 0.6214421478571256, 'gorcums': 0.6214421478571256, 'ha': 0.11966097837637452, 'heat': 0.14608784514803438, 'idea': 0.37839647016748407, 'important': 0.25106876010190277, 'infinite': 0.26074486069362346, 'interesting': 0.3562787391713667, 'layer': 0.10832975779775116, 'made': 0.118433711946317, 'material': 0.26203487688769017, 'number': 0.07845045600431105, 'paper': 0.16692885196679205, 'parallel': 0.26739815197031136, 'passive': 0.5619808910508631, 'plane': 0.23079027635009564, 'pointed': 0.32685940877657377, 'pole': 0.6214421478571256, 'regard': 0.42391612831509007, 'solid': 0.31168150346321444, 'stratiform': 0.6214421478571256, 'theory': 0.10126360623697798, 'through': 0.20257362008142774, 'to': 0.009721840107770649, 'two': 0.1051403770694433, 'van': 0.6023782119076675, 'wave': 0.16439316606881269}
======================================================================
5     1099       0.035340754522434584   a theoretical study of stagnation point ablation .


Vector Representation for the Rank 5 With Document ID 1099


{'ablation': 0.6086012866104468, 'analysis': 0.18386193211606205, 'at': 0.0517306337157308, 'automatic': 0.41029581399344117, 'capacity': 0.3780852563019674, 'discussed': 0.1526234614487881, 'effective': 0.28651523187277417, 'enthalpy': 0.2930483094538725, 'given': 0.10235101443118594, 'good': 0.1852224845107199, 'heat': 0.18725866358969678, 'increase': 0.1869944764155687, 'linearly': 0.3336288129190638, 'made': 0.10967596759648604, 'material': 0.3358821591909818, 'mechanism': 0.42630910511130277, 'most': 0.21541446873807338, 'parameter': 0.17483396527288209, 'place': 0.3336288129190638, 'point': 0.1574153265054878, 'property': 0.20730119850254605, 'reduces': 0.35041542073362547, 'result': 0.061811682778245364, 'shielding': 0.7965784284662087, 'significant': 0.352002741382515, 'simplified': 0.2930483094538725, 'stagnation': 0.19256071435524527, 'stream': 0.14522826422286164, 'surface': 0.116999638472775, 'take': 0.27133761090628217, 'that': 0.043764358022771316, 'thermal': 0.2263892711532442, 'transfer': 0.16207720315867485}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     509       0.028780185362240664   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 1 With Document ID 509


{'acted': 0.6725109590639371, 'at': 0.42887497707735966, 'by': 0.4291629329558567, 'change': 0.5152828388370986, 'condition': 0.4642152358926964, 'conduction': 0.5599269167685637, 'considers': 0.5906626846244781, 'derived': 0.4987480708313855, 'entry': 0.5635735464703271, 'heat': 0.4755134071530064, 'heated': 0.5821908483832174, 'heating': 0.5315886160136986, 'material': 0.5354469040641762, 'method': 0.45032766592036005, 'most': 0.5202399313552581, 're': 0.5689549708377533, 'severe': 0.6011447161613533, 'space': 0.5906626846244781, 'state': 0.5411764545758323, 'sublimation': 0.6725109590639371, 'such': 0.4919546399789279, 'suitable': 0.557652452076105, 'surface': 0.46530679476160014, 'under': 0.4932326056594879, 'upon': 0.5315886160136986, 'vehicle': 0.5404184474020378}
======================================================================
2     1099       0.022190326409315755   a theoretical study of stagnation point ablation .


Vector Representation for the Rank 2 With Document ID 1099


{'ablation': 0.6798972212550309, 'analysis': 0.4878193998923873, 'at': 0.42503961711967264, 'automatic': 0.5985989606208144, 'capacity': 0.5830078113563821, 'discussed': 0.4738756277210393, 'effective': 0.5386843962606798, 'enthalpy': 0.5418466571783163, 'given': 0.44954182906882995, 'good': 0.4896548091714674, 'heat': 0.48944180707682766, 'increase': 0.49051252143303364, 'linearly': 0.5614891822414289, 'made': 0.45308738823763006, 'material': 0.5604299993763335, 'mechanism': 0.6036213225253315, 'most': 0.5042688912121102, 'parameter': 0.48462636614899757, 'place': 0.5614891822414289, 'point': 0.4761950747815228, 'property': 0.5003417562498284, 'reduces': 0.569614546309546, 'result': 0.429919232746984, 'shielding': 0.7804759296827393, 'significant': 0.5681297980115546, 'simplified': 0.5418466571783163, 'stagnation': 0.49320679476384954, 'stream': 0.47029606772416743, 'surface': 0.45663232672921106, 'take': 0.531337843734823, 'that': 0.42118363317179375, 'thermal': 0.5095811178503925, 'transfer': 0.47845160245323864}
======================================================================
3     405       0.021425756797613674   tables of thermal properties of gases .


Vector Representation for the Rank 3 With Document ID 405


{'air': 0.5014423677946904, 'argon': 0.6482394367729205, 'carbon': 0.7477739055150967, 'dioxide': 0.7022752475514293, 'hydrogen': 0.6482394367729205, 'monoxide': 0.7563110583299382, 'nitrogen': 0.6199398552158644, 'oxygen': 0.6340896459943924, 'property': 0.5283495279512219, 'steam': 0.7222182575514198, 'table': 0.5814394342965952, 'thermodynamic': 0.5979889944078587, 'transport': 0.6042765445703107}
======================================================================
4     817       0.01867881445825945   loading paths and the incremental stress law .


Vector Representation for the Rank 4 With Document ID 817


{'also': 0.4550861898520269, 'by': 0.4255251720715569, 'concerned': 0.5352614594505821, 'deformation': 0.526717650351733, 'differential': 0.5324185651441794, 'directly': 0.5352614594505821, 'expressed': 0.5293487821962573, 'flow': 0.42637948319566166, 'function': 0.503145033757715, 'given': 0.4468735250429634, 'hardening': 0.6235865045285709, 'incremental': 0.5731510804083014, 'introduced': 0.5275737243933856, 'law': 0.5902199520552377, 'material': 0.511129842017915, 'meant': 0.663555632497868, 'occasion': 0.6383379204377333, 'paper': 0.4707950680750506, 'plastic': 0.5977755247441795, 'prager': 0.663555632497868, 'property': 0.4949373875134227, 'refer': 0.6050019183766614, 'shall': 0.5836173765592737, 'strain': 0.6445390095512555, 'stress': 0.5402401067386821, 'that': 0.4200426907654033, 'to': 0.4057294244369372, 'total': 0.5010793385998371, 'w': 0.5702390091898999, 'we': 0.5510989699872122, 'work': 0.5010793385998371}
======================================================================
5     1096       0.01696896599391579   qualitative measurements of the effective heats of ablation of several materials in supersonic air jets at stagnation temperature up to 11,000 f.


Vector Representation for the Rank 5 With Document ID 1096


{'ablation': 0.5825275923599177, 'air': 0.48045106929804743, 'ammonium': 0.655542175630508, 'at': 0.42540111055056695, 'carbonate': 0.655542175630508, 'chloride': 0.655542175630508, 'content': 0.6285041407578571, 'derived': 0.486867970738926, 'effective': 0.5406865633855272, 'f': 0.6156565478780982, 'fiber': 0.6285041407578571, 'from': 0.4437145995764993, 'glass': 0.6197998377018066, 'heat': 0.4664286034930727, 'included': 0.5066222320774161, 'inorganic': 0.655542175630508, 'jet': 0.5053570085556103, 'laminate': 0.6825802105031589, 'lucite': 0.655542175630508, 'material': 0.5620045454479032, 'melamine': 0.6825802105031589, 'number': 0.43567274355015867, 'nylon': 0.6397259391368163, 'phenolic': 0.655542175630508, 'plastic': 0.5525987804753556, 'polystyrene': 0.6825802105031589, 'ranging': 0.5638205788543147, 'reinforcement': 0.6825802105031589, 'resin': 0.7259433233838071, 'salt': 0.655542175630508, 'several': 0.49852271073005383, 'sodium': 0.6285041407578571, 'stagnation': 0.49455240815165846, 'supersonic': 0.4727231176144587, 'teflon': 0.6066748502206574, 'temperature': 0.46522363853225823, 'test': 0.4721875352122385, 'to': 0.4044206844250987, 'type': 0.4808918382682891, 'varied': 0.5340912949691214, 'were': 0.46087718369916225}
======================================================================
========================================================================================================================================================================


Query No: 16

Query Vector for weight (Version 1) are:
[('about', 0.048101472354949555),
 ('body', 0.03362148634050799),
 ('by', 0.048101472354949555),
 ('calculated', 0.048101472354949555),
 ('can', 0.03362148634050799),
 ('computer', 0.06258145836939115),
 ('electronic', 0.06258145836939115),
 ('flow', 0.021930998360423306),
 ('potential', 0.048101472354949555),
 ('revolution', 0.03963122352553445),
 ('transverse', 0.048101472354949555)]

Query Vector for weight (Version 2) are:
[('about', 0.04575883575292521),
 ('body', 0.04201838681343268),
 ('by', 0.04575883575292521),
 ('calculated', 0.04575883575292521),
 ('can', 0.04201838681343268),
 ('computer', 0.04949928469241774),
 ('electronic', 0.04949928469241774),
 ('flow', 0.038998516951428246),
 ('potential', 0.04575883575292521),
 ('revolution', 0.04357081338745986),
 ('transverse', 0.04575883575292521)]

Ranks  Document Number   Scores Titles


1     1358       0.03646149067212035   compressive buckling of simply supported plates with transverse stiffeners .


Vector Representation for the Rank 1 With Document ID 1358


{'analysis': 0.17333657210766806, 'both': 0.2038183526493618, 'chart': 0.40190461444533776, 'compression': 0.347529448406001, 'equally': 0.5232008027208732, 'flexural': 0.5122785371621799, 'longitudinal': 0.3586870503712895, 'plate': 0.19184363497909526, 'presented': 0.14981083400150466, 'rectangular': 0.3374569059866435, 'rigidity': 0.5232008027208732, 'several': 0.26183128290606894, 'simply': 0.3738847937284974, 'spaced': 0.5354108567977349, 'stability': 0.2811026613971851, 'stiffener': 0.46355530891941527, 'supported': 0.36856744140554065, 'that': 0.057109801336041384, 'torsional': 0.485080377094971, 'transverse': 0.3454351217699856, 'under': 0.21796364389499664}
======================================================================
2     920       0.03578814875918636   supersonic flow over an inclined wing of zero aspect ratio .


Vector Representation for the Rank 2 With Document ID 920


{'approximation': 0.24019058098446416, 'asymptotic': 0.37948970696423406, 'at': 0.06750530221317826, 'distribution': 0.152354903827028, 'expression': 0.2868315024929699, 'found': 0.15300079777058181, 'incidence': 0.3355547307357344, 'laminar': 0.19617368800528992, 'lift': 0.24798866528445648, 'linearized': 0.3496669600635051, 'long': 0.3318519927509069, 'narrow': 0.5492534744193474, 'on': 0.05749589356104888, 'potential': 0.3318519927509069, 'stream': 0.18951397193648478, 'supersonic': 0.19326698423974895, 'theory': 0.12237131028024509, 'used': 0.17492534868552315, 'wing': 0.19279035975607345}
======================================================================
3     161       0.03405788586104044   supersonic flow past a family of blunt symmetric bodies .


Vector Representation for the Rank 3 With Document ID 161


{'assumed': 0.26183128290606894, 'body': 0.16871131534354014, 'bow': 0.4215225079418247, 'carried': 0.32653464042795, 'computation': 0.3635095776851176, 'detached': 0.45727061854237766, 'emphasis': 0.5122785371621799, 'free': 0.20595586430686588, 'gas': 0.23434871760537254, 'mach': 0.13600749110761504, 'number': 0.09480291538170249, 'numerical': 0.22293061270158732, 'on': 0.05749589356104888, 'out': 0.2512799144964561, 'paraboloid': 0.6370891515767835, 'perfect': 0.40190461444533776, 'result': 0.08066045255080079, 'revolution': 0.3105545111488335, 'sphere': 0.37948970696423406, 'stream': 0.18951397193648478, 'summarized': 0.49337805582014427, 'taken': 0.3282769611482099, 'unyawed': 0.5354108567977349, 'wave': 0.1986597937849511}
======================================================================
4     106       0.033372004263582125   the transverse potential flow past a body of revolution .


Vector Representation for the Rank 4 With Document ID 106


{'along': 0.20064579827032275, 'angle': 0.23699327976679202, 'at': 0.08093923824135008, 'axis': 0.28935325834839926, 'azimuthal': 0.5619808910508631, 'body': 0.20228581902321388, 'by': 0.04331179236839078, 'component': 0.2716527987994464, 'consideration': 0.24341411545136124, 'elementary': 0.42391612831509007, 'entirely': 0.4082757719609241, 'flow': 0.06220061601834868, 'fluid': 0.1921813145342394, 'incompressible': 0.21074975241888858, 'inviscid': 0.25222024665695203, 'manner': 0.2716527987994464, 'meridian': 0.4833773851213525, 'past': 0.270211009225151, 'perpendicular': 0.4014093514806447, 'potential': 0.2746111768021922, 'revolution': 0.256987276348298, 'right': 0.44305837743833826, 'round': 0.4329544232897724, 'set': 0.26467460701955103, 'shown': 0.1978462152873054, 'simple': 0.17549188555788003, 'stream': 0.1568248978182262, 'surface': 0.12634218584411033, 'that': 0.04725898923138793, 'to': 0.014086267179562515, 'vary': 0.3093937822796063, 'velocity': 0.12988863039831225}
======================================================================
5     339       0.03148202087611073   experimental evaluation of heat transfer with transpiration cooling in a turbulent boundary layer at m=3 .2.


Vector Representation for the Rank 5 With Document ID 339


{'accelerator': 0.5619808910508631, 'analytic': 0.3488145151546617, 'boundary': 0.09603948854195138, 'by': 0.04331179236839078, 'calculated': 0.1866089364588232, 'can': 0.13535079247784257, 'conductivity': 0.3524654687089807, 'current': 0.360269433606657, 'electrical': 0.3835971206320758, 'field': 0.26577924259061636, 'found': 0.12660984428377786, 'integration': 0.2875844439235415, 'investigation': 0.1639777441416276, 'layer': 0.10832975779775116, 'physically': 0.4014093514806447, 'prescribed': 0.3488145151546617, 'reasonable': 0.3164485331545604, 'related': 0.3071654891969682, 'that': 0.04725898923138793, 'to': 0.009721840107770649, 'velocity': 0.12988863039831225, 'work': 0.23833663006222613}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     106       0.02462083983567108   the transverse potential flow past a body of revolution .


Vector Representation for the Rank 1 With Document ID 106


{'along': 0.4925734941182317, 'angle': 0.5021268972065037, 'at': 0.4348789352676208, 'axis': 0.533501136782931, 'azimuthal': 0.6592854431078838, 'body': 0.4871705014844558, 'by': 0.41998309454087557, 'component': 0.525334539714512, 'consideration': 0.5123058413347502, 'elementary': 0.5955854423541397, 'entirely': 0.5883693309307211, 'flow': 0.42869797628838097, 'fluid': 0.48866817019861253, 'incompressible': 0.4972352331030819, 'inviscid': 0.5163687937732899, 'manner': 0.525334539714512, 'meridian': 0.6230195394280348, 'past': 0.5246693301769769, 'perpendicular': 0.5852013177381993, 'potential': 0.5266994693118302, 'revolution': 0.5185681949015343, 'right': 0.6044172489600936, 'round': 0.5997555099752435, 'set': 0.5221149577384085, 'shown': 0.48525735460189057, 'simple': 0.4809680400762856, 'stream': 0.4723555084677553, 'surface': 0.4582914653531233, 'that': 0.4218042430958424, 'to': 0.4060701584521137, 'vary': 0.5427473873412028, 'velocity': 0.4599277157351858}
======================================================================
2     339       0.024358108699563917   experimental evaluation of heat transfer with transpiration cooling in a turbulent boundary layer at m=3 .2.


Vector Representation for the Rank 2 With Document ID 339


{'accelerator': 0.6937035928081268, 'analytic': 0.5822981492003731, 'boundary': 0.45019235224080445, 'by': 0.422635696750772, 'calculated': 0.49752594075854323, 'can': 0.470737305615204, 'conductivity': 0.5842062179499601, 'current': 0.5882847419088619, 'electrical': 0.600476305003574, 'field': 0.5243954348323326, 'found': 0.466169093546025, 'integration': 0.5502979652175162, 'investigation': 0.4856983811405233, 'layer': 0.4566155176802161, 'physically': 0.6097853692074651, 'prescribed': 0.5822981492003731, 'reasonable': 0.5653829740590666, 'related': 0.5605314508027468, 'that': 0.42469858877903194, 'to': 0.40508084779007186, 'velocity': 0.46788265939358864, 'work': 0.5245599728776573}
======================================================================
3     498       0.02009810102862976   calculation of potential flow about bodies of revolution having axes perpendicular to the free-stream direction .


Vector Representation for the Rank 3 With Document ID 498


{'about': 0.48747450488114136, 'accuracy': 0.4816736755627976, 'after': 0.49807676115461, 'agreement': 0.4568275842837173, 'aid': 0.5166620413134543, 'also': 0.44206038967552286, 'analytic': 0.5129527225507975, 'angle': 0.45296521484680535, 'arbitrary': 0.4788220840962843, 'at': 0.42709164144270917, 'attack': 0.47066180352645925, 'ax': 0.5346244562044946, 'axisymmetric': 0.4948802931511851, 'basic': 0.5016894585081809, 'body': 0.5013281694009195, 'by': 0.41402517571379, 'calculate': 0.5727879931676497, 'calculated': 0.49050156546770696, 'calculating': 0.49549083700512275, 'case': 0.43741985655113647, 'certain': 0.46894804087822384, 'combined': 0.4967537193419529, 'compared': 0.4550443864949074, 'comparison': 0.46580840631751325, 'computer': 0.5058432447866688, 'data': 0.45204574372224327, 'derived': 0.46186154915355804, 'described': 0.4719540656937446, 'direction': 0.4798574322740758, 'distribution': 0.46114400337747846, 'electronic': 0.5401988126248324, 'ellipsoid': 0.5707167537257746, 'equation': 0.43514945665436616, 'exhibit': 0.5346244562044946, 'exhibited': 0.5401988126248324, 'experimental': 0.4431643214461462, 'flow': 0.44300913369925154, 'forward': 0.4948802931511851, 'free': 0.4551886913758203, 'general': 0.4530990880076264, 'make': 0.5041065151035524, 'method': 0.4566109373258536, 'off': 0.5041065151035524, 'on': 0.41540681123985823, 'other': 0.4544745485212603, 'perpendicular': 0.5299839230801082, 'point': 0.4550443864949074, 'possible': 0.46991435142542537, 'potential': 0.48892428128724175, 'presented': 0.44014386242551706, 'pressure': 0.44049037681497566, 'property': 0.47248828652547925, 'quite': 0.5067541010477392, 'region': 0.45824436522530143, 'revolution': 0.549422211861486, 'satisfactory': 0.4931252700020761, 'selected': 0.5279253053560707, 'separated': 0.49946598197916603, 'solution': 0.45264293752826257, 'stream': 0.4507828613854131, 'surface': 0.4409119840032562, 'then': 0.46666982812045255, 'these': 0.43593401431749457, 'to': 0.40627685557633464, 'type': 0.45760574797119175, 'variety': 0.5153697791461689, 'velocity': 0.44206038967552286, 'whose': 0.49807676115461}
======================================================================
4     93       0.0200063186803319   the supersonic blunt body problem - review and extensions .


Vector Representation for the Rank 4 With Document ID 93


{'adequate': 0.5621221775166629, 'analytical': 0.5102696660787975, 'approximation': 0.48280823623014885, 'blunt': 0.495041484906768, 'body': 0.48126371410597973, 'by': 0.41804471133637644, 'computer': 0.5361773169945373, 'conic': 0.6196432047718297, 'described': 0.49257569184289574, 'detached': 0.5576488688530742, 'detail': 0.5065599869714308, 'electronic': 0.5803789952542556, 'equation': 0.44522309109716796, 'existing': 0.5244827852338209, 'failure': 0.5350426241138986, 'field': 0.4764218232028597, 'flow': 0.4259142395089385, 'forth': 0.601386387034237, 'from': 0.4294579273679228, 'full': 0.537349219481562, 'given': 0.44604683668675316, 'hypersonic': 0.4810398277066234, 'indicates': 0.5261850033081286, 'inviscid': 0.505080886641761, 'medium': 0.5500967190980623, 'method': 0.4405639827088214, 'number': 0.43268430502169697, 'numerical': 0.47685768011327184, 'others': 0.5766134289991359, 'plausible': 0.6093614982192016, 'predicting': 0.5424636184053723, 'problem': 0.45388333170426964, 'proposed': 0.5298538446768619, 'reason': 0.5803789952542556, 'result': 0.42780854179160943, 'section': 0.4846687214292022, 'set': 0.5102696660787975, 'shock': 0.463782790509387, 'shown': 0.4568884474899741, 'simpler': 0.5576488688530742, 'sized': 0.6589074142894036, 'solution': 0.44522309109716796, 'solving': 0.5468454037828238, 'supersonic': 0.46663083132077005, 'support': 0.5468454037828238, 'survey': 0.5279723669228994, 'than': 0.45935424055384644, 'that': 0.4275082590576167, 'treatment': 0.5289007262276136, 'using': 0.48079419221253034, 'various': 0.4793548101574117, 'wave': 0.468490059292712}
======================================================================
5     326       0.01949390652440107   forst-order slip effects on the compressible laminar boundary layer over a slender body of revolution in axial flow .


Vector Representation for the Rank 5 With Document ID 326


{'analysis': 0.4766598175882614, 'boundary': 0.4660784246871832, 'case': 0.46175949870307836, 'compressible': 0.5258237592366958, 'considered': 0.48547423995698785, 'curvature': 0.555608918901094, 'effect': 0.4492681257057375, 'examined': 0.5586329042878203, 'first': 0.49693596710217247, 'flow': 0.4332428679364144, 'gradient': 0.5170422765262181, 'interaction': 0.5329761107031562, 'layer': 0.4745345466817294, 'no': 0.5072343362633125, 'only': 0.4892144505300779, 'order': 0.49205126195568033, 'pressure': 0.44462024628057123, 'slip': 0.6050119313641399, 'transverse': 0.5527721074754915, 'zero': 0.5086133021131177}
======================================================================
========================================================================================================================================================================


Query No: 17

Query Vector for weight (Version 1) are:
[('about', 0.0318435982735854),
 ('body', 0.022257720023362428),
 ('can', 0.022257720023362428),
 ('dimensional', 0.06002841735252546),
 ('flow', 0.014518514035799977),
 ('potential', 0.0318435982735854),
 ('problem', 0.027778535891671244),
 ('reduced', 0.04142947652380837),
 ('revolution', 0.02623621896072643),
 ('three', 0.04142947652380837),
 ('to', 0.01665034071050346),
 ('transverse', 0.0318435982735854),
 ('two', 0.04142947652380837)]

Query Vector for weight (Version 2) are:
[('about', 0.035473182449981974),
 ('body', 0.03282215704191579),
 ('can', 0.03282215704191579),
 ('dimensional', 0.04447947454844006),
 ('flow', 0.03068183863021378),
 ('potential', 0.035473182449981974),
 ('problem', 0.034909657984752276),
 ('reduced', 0.03812420785804817),
 ('revolution', 0.03392243199780425),
 ('three', 0.03812420785804817),
 ('to', 0.031271406589738066),
 ('transverse', 0.035473182449981974),
 ('two', 0.03812420785804817)]

Ranks  Document Number   Scores Titles


1     298       0.08461739722942448   incompressible wedge flows of an electrically conducting viscous fluid in the presence of a magnetic field .


Vector Representation for the Rank 1 With Document ID 298


{'analyzed': 0.347529448406001, 'boundary': 0.11605826108957569, 'condition': 0.15012544924324459, 'conducting': 0.39499101025309524, 'differential': 0.27152672180814785, 'dimensional': 0.19765818558169257, 'discus': 0.4215225079418247, 'electrically': 0.43536512556343715, 'equation': 0.13117246567543026, 'field': 0.2216663818798242, 'flow': 0.0751659077259313, 'fluid': 0.23224019116896719, 'given': 0.13356179239887297, 'governing': 0.39499101025309524, 'magnetic': 0.3738847937284974, 'note': 0.3020292458501778, 'past': 0.32653464042795, 'presence': 0.32653464042795, 'purpose': 0.3020292458501778, 'to': 0.011748290985597008, 'two': 0.1270561673977648, 'viscous': 0.26369918285741484, 'wedge': 0.36856744140554065}
======================================================================
2     320       0.06234046630196094   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 2 With Document ID 320


{'accurate': 0.270211009225151, 'attention': 0.31403190967724753, 'drawn': 0.3891335228376759, 'previous': 0.2841526078838075, 'problem': 0.12933338923453824, 'solution': 0.10854665920362061, 'to': 0.014086267179562515}
======================================================================
3     1276       0.06043185447234237   a three-dimensional linearized analysis of the forces exerted on a rigid wing by a shock wave .


Vector Representation for the Rank 3 With Document ID 1276


{'acoustic': 0.4082757719609241, 'author': 0.23833663006222613, 'by': 0.04331179236839078, 'dimensional': 0.163564324255595, 'distribution': 0.12607535993592625, 'edge': 0.17454918969413313, 'flat': 0.17692564250327128, 'found': 0.12660984428377786, 'front': 0.3214961336939525, 'ha': 0.11966097837637452, 'induced': 0.2716527987994464, 'moving': 0.31168150346321444, 'obliquely': 0.6214421478571256, 'on': 0.047578484797422, 'plate': 0.23002160078661651, 'pressure': 0.0834887895608359, 'shock': 0.15309455095854613, 'solution': 0.10854665920362061, 'striking': 0.4677370287671866, 'term': 0.1871501651331313, 'two': 0.1051403770694433}
======================================================================
4     963       0.055582135591354394   a variational principle for convection of heat .


Vector Representation for the Rank 4 With Document ID 963


{'agreement': 0.17549188555788003, 'author': 0.23833663006222613, 'between': 0.1415028515150645, 'biot': 0.5025196342446008, 'case': 0.11555798590132785, 'convection': 0.3488145151546617, 'dimensional': 0.163564324255595, 'due': 0.19938423935311986, 'exact': 0.22302558106185744, 'excellent': 0.3891335228376759, 'extend': 0.3891335228376759, 'flowing': 0.4677370287671866, 'fluid': 0.1921813145342394, 'forced': 0.4677370287671866, 'given': 0.11052385336735143, 'heat': 0.14608784514803438, 'numerical': 0.1844775358789806, 'one': 0.14442207513234676, 'parabolic': 0.360269433606657, 'parallel': 0.26739815197031136, 'principle': 0.33559078227780864, 'problem': 0.12933338923453824, 'profile': 0.22139154193623733, 'result': 0.066747412341137, 'solution': 0.10854665920362061, 'to': 0.014086267179562515, 'transfer': 0.17501924270759028, 'uniform': 0.21219154199318402, 'variational': 0.37349316648351, 'various': 0.19047126866708147, 'velocity': 0.12988863039831225, 'wall': 0.18239781074082373}
======================================================================
5     362       0.05390282586818881   three-dimensional effect of flutter in a real fluid .


Vector Representation for the Rank 5 With Document ID 362


{'account': 0.25106876010190277, 'accurate': 0.270211009225151, 'alternative': 0.42391612831509007, 'approximation': 0.19876034961904174, 'boundary': 0.09603948854195138, 'coefficient': 0.1579763843732755, 'determination': 0.28935325834839926, 'dimensional': 0.163564324255595, 'distribution': 0.12607535993592625, 'downwash': 0.37349316648351, 'effect': 0.09218542078944494, 'empirical': 0.48188590040174234, 'finite': 0.24661142193939375, 'fluid': 0.1921813145342394, 'flutter': 0.27924930419983346, 'following': 0.30080817680039457, 'formulation': 0.3325804923459027, 'given': 0.11052385336735143, 'governing': 0.32685940877657377, 'into': 0.1818856631878697, 'largeaspect': 0.6214421478571256, 'more': 0.1871501651331313, 'problem': 0.12933338923453824, 'ratio': 0.13475917316521085, 'real': 0.33559078227780864, 'rectangular': 0.27924930419983346, 'ref': 0.37839647016748407, 'reissners': 0.5271982855734489, 'semi': 0.3214961336939525, 'should': 0.27924930419983346, 'span': 0.3093937822796063, 'taken': 0.2716527987994464, 'three': 0.20322597653563415, 'value': 0.12905711054059832, 'vorticity': 0.32685940877657377, 'w': 0.4014093514806447, 'wing': 0.15953614480318243}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     320       0.06741598445358553   comment on improved numerical solution of the blasius problem with three-point boundary conditions .


Vector Representation for the Rank 1 With Document ID 320


{'accurate': 0.5618011772797783, 'attention': 0.5880409419101723, 'drawn': 0.6330114612824701, 'previous': 0.5701493459299061, 'problem': 0.47744427105224063, 'solution': 0.4649972675032589, 'to': 0.4071860442032682}
======================================================================
2     298       0.03677580881556507   incompressible wedge flows of an electrically conducting viscous fluid in the presence of a magnetic field .


Vector Representation for the Rank 2 With Document ID 298


{'analyzed': 0.5462533793827056, 'boundary': 0.44884165346989835, 'condition': 0.46317839936695343, 'conducting': 0.5662269782899543, 'differential': 0.514268591738897, 'dimensional': 0.48318195116001955, 'discus': 0.5773924240237153, 'electrically': 0.5832179148301757, 'equation': 0.4552022755912801, 'field': 0.4932854973705354, 'flow': 0.43163262298981697, 'fluid': 0.49773535147233444, 'given': 0.4562077935678306, 'governing': 0.5662269782899543, 'magnetic': 0.5573446936177807, 'note': 0.5271051937630151, 'past': 0.5374179795903583, 'presence': 0.5374179795903583, 'purpose': 0.5271051937630151, 'to': 0.4049441198911225, 'two': 0.4534699834462056, 'viscous': 0.5109744708261361, 'wedge': 0.555106953045959}
======================================================================
3     963       0.035363889940787645   a variational principle for convection of heat .


Vector Representation for the Rank 3 With Document ID 963


{'agreement': 0.487829686468598, 'author': 0.5192820478610876, 'between': 0.47081895008120866, 'biot': 0.6514996165190841, 'case': 0.4578341365379475, 'convection': 0.5745737098005345, 'dimensional': 0.48186021405576007, 'due': 0.4997872646561127, 'exact': 0.5116192170188935, 'excellent': 0.594752453633999, 'extend': 0.594752453633999, 'flowing': 0.6340917157268012, 'fluid': 0.4961823650535581, 'forced': 0.6340917157268012, 'given': 0.4553146680126937, 'heat': 0.4731136348295325, 'numerical': 0.4923267995283265, 'one': 0.47227995492609115, 'parabolic': 0.5803066352458552, 'parallel': 0.5338266768014699, 'principle': 0.5679555330750047, 'problem': 0.46472841174553425, 'profile': 0.5108014177022788, 'result': 0.43340555764089034, 'solution': 0.4543251274254696, 'to': 0.40640895517970066, 'transfer': 0.4875931395010809, 'uniform': 0.5061970275452023, 'variational': 0.586924811971385, 'various': 0.4953265260962072, 'velocity': 0.4650062972852201, 'wall': 0.4912859445267148}
======================================================================
4     577       0.033743556311717854   on hypersonic similitude .


Vector Representation for the Rank 4 With Document ID 577


{'about': 0.47514526522756684, 'around': 0.522857967999089, 'author': 0.4992966454442161, 'basic': 0.5308330791840536, 'body': 0.48126371410597973, 'by': 0.41804471133637644, 'certain': 0.48870815740532547, 'characterized': 0.5621221775166629, 'coordinate': 0.5308330791840536, 'dimension': 0.5500967190980623, 'dimensional': 0.4681447443000693, 'enlarges': 0.6589074142894036, 'essentially': 0.5289007262276136, 'fineness': 0.5576488688530742, 'flow': 0.4417293007066248, 'ha': 0.4498535778585301, 'hypersonic': 0.4810398277066234, 'indicating': 0.5948702467367286, 'inst': 0.6589074142894036, 'j': 0.5700972887016276, 'lengthwise': 0.6196432047718297, 'mach': 0.4468900171128598, 'mass': 0.5075811942652498, 'math': 0.6196432047718297, 'nonsteady': 0.5948702467367286, 'notion': 0.6589074142894036, 'number': 0.43268430502169697, 'on': 0.41982231574923745, 'out': 0.4866314009243353, 'paper': 0.4695464856737673, 'parameter': 0.5098925752845365, 'phys': 0.6341344562543025, 'pointed': 0.5361773169945373, 'problem': 0.45388333170426964, 'product': 0.5556060372191547, 'ratio': 0.4561438408970037, 'recent': 0.5170098812401128, 'replacing': 0.5845885401841006, 'same': 0.5108684947930934, 'similarity': 0.5663868301928643, 'slender': 0.5404819211314625, 'sonic': 0.5163418277015808, 'spatial': 0.601386387034237, 'tech': 0.6196432047718297, 'that': 0.4317052257512366, 'three': 0.4846687214292022, 'time': 0.4795907174410272, 'tsien': 0.5845885401841006, 'two': 0.44380395384884797}
======================================================================
5     4       0.032516140939512564   approximate solutions of the incompressible laminar boundary layer equations for a plate in shear flow .


Vector Representation for the Rank 5 With Document ID 4


{'also': 0.45906254773108923, 'boundary': 0.46746486556073386, 'boundarylayer': 0.5540173964041313, 'by': 0.4196946014153241, 'comparison': 0.4924102741134845, 'considered': 0.4727231176144587, 'dimensional': 0.47437545286931415, 'distribution': 0.4573285894315401, 'effect': 0.4419182633521547, 'flat': 0.48045106929804743, 'flow': 0.4384558828363566, 'fluid': 0.4873880802953595, 'friction': 0.513138617476391, 'ha': 0.45441186211010576, 'incompressible': 0.49583146171751136, 'karman': 0.5473900361399046, 'layer': 0.4760984117783979, 'made': 0.4538538033956382, 'obtained': 0.4482865557910719, 'plate': 0.4721875352122385, 'pohlhausen': 0.5638205788543147, 'problem': 0.45881007022295706, 'shear': 0.5088266399646363, 'show': 0.48661049364022546, 'skin': 0.5074891041706984, 'solution': 0.4493579940030488, 'steady': 0.5049442254568258, 'technique': 0.5088266399646363, 'thickness': 0.4824749742166764, 'to': 0.4044206844250987, 'two': 0.4478091001505349, 'uniform': 0.49648706771850526, 'velocity': 0.45906254773108923, 'vorticity': 0.5486284778969602}
======================================================================
========================================================================================================================================================================


Query No: 18

Query Vector for weight (Version 1) are:
[('angle', 0.047557468230641345),
 ('at', 0.047557468230641345),
 ('attack', 0.047557468230641345),
 ('available', 0.04034578360860959),
 ('body', 0.04034578360860959),
 ('distribution', 0.05772176682593947),
 ('experimental', 0.05772176682593947),
 ('on', 0.04034578360860959),
 ('pressure', 0.047557468230641345),
 ('revolution', 0.047557468230641345)]

Query Vector for weight (Version 2) are:
[('angle', 0.05343849494429004),
 ('at', 0.05343849494429004),
 ('attack', 0.05343849494429004),
 ('available', 0.051400661751341684),
 ('body', 0.051400661751341684),
 ('distribution', 0.05631065951416849),
 ('experimental', 0.05631065951416849),
 ('on', 0.051400661751341684),
 ('pressure', 0.05343849494429004),
 ('revolution', 0.05343849494429004)]

Ranks  Document Number   Scores Titles


1     492       0.04037831889810071   prediction of ogive-forebody pressures at angles of attack .


Vector Representation for the Rank 1 With Document ID 492


{'angle': 0.24798988319115764, 'approximate': 0.17432308885010464, 'approximation': 0.1840627411405065, 'arbitrary': 0.22541452260545322, 'at': 0.07160436566891452, 'attack': 0.3308475657709923, 'being': 0.21980459174508976, 'body': 0.12928678150606152, 'by': 0.04010904208165435, 'calculated': 0.1728098810037261, 'distribution': 0.11675254337477482, 'forebody': 0.41029581399344117, 'lower': 0.23798399737957068, 'method': 0.09016395214855977, 'not': 0.13528517773688292, 'obtaining': 0.4426294338386114, 'ogive': 0.3780852563019674, 'on': 0.044060228048051424, 'over': 0.13717671971690412, 'present': 0.14847120469611422, 'pressure': 0.12658246390336925, 'suggested': 0.2730836374538286, 'surface': 0.16194823636556005, 'utilizing': 0.35041542073362547, 'various': 0.17638660772417045, 'zero': 0.18819815110911567}
======================================================================
2     1045       0.04033704738240432   the bending strength of pressurized cylinders .


Vector Representation for the Rank 2 With Document ID 1045


{'cylinder': 0.2216663818798242, 'data': 0.19422685815856466, 'discussion': 0.3182369617027767, 'experimental': 0.16108273106391074, 'loading': 0.2822233819620548, 'membrane': 0.5122785371621799, 'presented': 0.14981083400150466, 'pressurized': 0.47024573618458926, 'previously': 0.33368683078438854, 'term': 0.22616033318930492, 'theory': 0.12237131028024509}
======================================================================
3     920       0.03946783384135691   supersonic flow over an inclined wing of zero aspect ratio .


Vector Representation for the Rank 3 With Document ID 920


{'approximation': 0.24019058098446416, 'asymptotic': 0.37948970696423406, 'at': 0.06750530221317826, 'distribution': 0.152354903827028, 'expression': 0.2868315024929699, 'found': 0.15300079777058181, 'incidence': 0.3355547307357344, 'laminar': 0.19617368800528992, 'lift': 0.24798866528445648, 'linearized': 0.3496669600635051, 'long': 0.3318519927509069, 'narrow': 0.5492534744193474, 'on': 0.05749589356104888, 'potential': 0.3318519927509069, 'stream': 0.18951397193648478, 'supersonic': 0.19326698423974895, 'theory': 0.12237131028024509, 'used': 0.17492534868552315, 'wing': 0.19279035975607345}
======================================================================
4     161       0.0391522829155487   supersonic flow past a family of blunt symmetric bodies .


Vector Representation for the Rank 4 With Document ID 161


{'assumed': 0.26183128290606894, 'body': 0.16871131534354014, 'bow': 0.4215225079418247, 'carried': 0.32653464042795, 'computation': 0.3635095776851176, 'detached': 0.45727061854237766, 'emphasis': 0.5122785371621799, 'free': 0.20595586430686588, 'gas': 0.23434871760537254, 'mach': 0.13600749110761504, 'number': 0.09480291538170249, 'numerical': 0.22293061270158732, 'on': 0.05749589356104888, 'out': 0.2512799144964561, 'paraboloid': 0.6370891515767835, 'perfect': 0.40190461444533776, 'result': 0.08066045255080079, 'revolution': 0.3105545111488335, 'sphere': 0.37948970696423406, 'stream': 0.18951397193648478, 'summarized': 0.49337805582014427, 'taken': 0.3282769611482099, 'unyawed': 0.5354108567977349, 'wave': 0.1986597937849511}
======================================================================
5     286       0.035784003389428484   effect of roll on dynamic instability of symmetric missiles .


Vector Representation for the Rank 5 With Document ID 286


{'attempt': 0.3854150706640581, 'by': 0.05233983836505397, 'certain': 0.25730367938315063, 'condition': 0.15012544924324459, 'describing': 0.49337805582014427, 'discussion': 0.3182369617027767, 'dynamic': 0.32147677670752695, 'experimental': 0.16108273106391074, 'extend': 0.47024573618458926, 'form': 0.19090547796463975, 'generalized': 0.37948970696423406, 'instability': 0.3885097972720185, 'neater': 0.7509775004326937, 'note': 0.3020292458501778, 'on': 0.05749589356104888, 'result': 0.08066045255080079, 'slightly': 0.3738847937284974, 'stability': 0.2811026613971851, 'stating': 0.6791219525543741, 'to': 0.011748290985597008}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     492       0.03919904755695737   prediction of ogive-forebody pressures at angles of attack .


Vector Representation for the Rank 1 With Document ID 492


{'angle': 0.5184205210342274, 'approximate': 0.49084321407129006, 'approximation': 0.49591873977378437, 'arbitrary': 0.5174679720678466, 'at': 0.43594786105313904, 'attack': 0.55798685259796, 'being': 0.5145445259917428, 'body': 0.467373902369538, 'by': 0.4209016161889557, 'calculated': 0.49005465149343713, 'distribution': 0.4608420626385423, 'forebody': 0.613813274586994, 'lower': 0.5240181743112837, 'method': 0.44698622116309666, 'not': 0.4704997854437502, 'obtaining': 0.6222152411660515, 'ogive': 0.5970277150433683, 'on': 0.4229606574493451, 'over': 0.47148550543155776, 'present': 0.47737128524167577, 'pressure': 0.4604458582597847, 'suggested': 0.5423092919029, 'surface': 0.4813035999171965, 'utilizing': 0.5826084157271793, 'various': 0.49191855462458933, 'zero': 0.4980737838102857}
======================================================================
2     1006       0.027047161161962038   free-flight measurements of the static and dynamic


Vector Representation for the Rank 2 With Document ID 1006


{'about': 0.4744884051223065, 'agreement': 0.4724749420481664, 'angle': 0.46754907717748584, 'at': 0.42306972947094496, 'attack': 0.4901183849383938, 'axisymmetric': 0.5210053855767273, 'blunt': 0.5523228468319531, 'body': 0.4932209679505402, 'calculated': 0.5079553115940145, 'characteristic': 0.474905203042763, 'computation': 0.524228280480996, 'computer': 0.5349869632642762, 'consisted': 0.5788022656299654, 'dimensional': 0.46754907717748584, 'distribution': 0.4520668199330752, 'experimental': 0.45504952805558946, 'field': 0.5061170551833518, 'flow': 0.44153271320790877, 'fuller': 0.5996260275094591, 'gas': 0.48008795368319085, 'good': 0.48260159025075333, 'ha': 0.44941779755619715, 'ibm': 0.5829750140681439, 'inviscid': 0.5041623531579635, 'method': 0.4402094046542866, 'nosed': 0.5455617981279144, 'number': 0.4323986048385664, 'numerically': 0.5361486219124023, 'on': 0.41964904484028376, 'over': 0.4611751603695952, 'perfect': 0.5373496662395262, 'pressure': 0.4344793445341236, 'region': 0.5040550924726668, 'result': 0.42756546165032505, 'shape': 0.4724749420481664, 'shock': 0.46322525211543875, 'showed': 0.525956789855898, 'solution': 0.44482778682499163, 'studied': 0.5093057764145827, 'subsonic': 0.4945740691670804, 'supersonic': 0.46604839762062406, 'surface': 0.4521770141575609, 'survey': 0.5268537343363642, 'transonic': 0.51666190227986, 'two': 0.44342105454509495, 'wave': 0.46789137370127715, 'were': 0.45528971483734393, 'zero': 0.48392861484894306}
======================================================================
3     312       0.02623548526984735   chordwise pressure distributions over several naca 16 series airfoils at transonic mach numbers up to 1.25 .


Vector Representation for the Rank 3 With Document ID 312


{'airfoil': 0.5683265922960555, 'analysis': 0.4674973547750857, 'angle': 0.4769682041947859, 'apparatus': 0.5921216813451747, 'at': 0.426286601132576, 'attack': 0.5026846041940374, 'coefficient': 0.4743386962024534, 'design': 0.5001941916877859, 'dimensional': 0.4769682041947859, 'distribution': 0.4593270818171559, 'flow': 0.42926964505573084, 'from': 0.45054589326601535, 'investigation': 0.4771627465337168, 'langley': 0.5624932120850377, 'lift': 0.4965669201679364, 'mach': 0.4529613904771219, 'naca': 0.5593864905510157, 'number': 0.44963920519973183, 'over': 0.46970550052969695, 'photograph': 0.5757540859480952, 'presented': 0.4583364196533785, 'pressure': 0.4392871870570768, 'schlieren': 0.5658591156150347, 'series': 0.5135702366908754, 'several': 0.5019572429443755, 'test': 0.474704015050458, 'thickness': 0.48535007736521485, 'to': 0.40694985823016855, 'transonic': 0.5329293824819448, 'tunnel': 0.48440576630023113, 'two': 0.44947574019106973, 'wind': 0.49917217615761783, 'without': 0.5181450275443787, 'x': 0.5483665771179728}
======================================================================
4     291       0.02552011051731639   sweepback effects in the turbulent boundary-layer shock-wave interaction .


Vector Representation for the Rank 4 With Document ID 291


{'ahead': 0.5703799144917274, 'angle': 0.4773534276876563, 'at': 0.4354648029543454, 'available': 0.5161180445549496, 'boundary': 0.44541933985849125, 'by': 0.4204831684063067, 'can': 0.4640105829070708, 'configuration': 0.517668659860385, 'dimensional': 0.4773534276876563, 'experiment': 0.49580184397612903, 'extension': 0.5385686042524664, 'influence': 0.511792941433094, 'interaction': 0.517668659860385, 'layer': 0.4512316981369061, 'moderate': 0.550831986596494, 'on': 0.42250098791417684, 'peak': 0.5703799144917274, 'pressure': 0.45300465969649684, 'reattachment': 0.5898359522115957, 'reported': 0.5572851609425697, 'rise': 0.5922869659676546, 'separation': 0.5442760084883067, 'shock': 0.47240202489658145, 'show': 0.4900783564782236, 'simple': 0.48299425281798625, 'sweep': 0.5723593068169193, 'sweptback': 0.6004799379479042, 'that': 0.4223498909235817, 'theory': 0.4478899483618625, 'turbulent': 0.4983382632910418, 'two': 0.449723364747835, 'understood': 0.628600569078889, 'upstream': 0.5485130986074713, 'wave': 0.4777454065348471}
======================================================================
5     920       0.025514946578968235   supersonic flow over an inclined wing of zero aspect ratio .


Vector Representation for the Rank 5 With Document ID 920


{'approximation': 0.5062266658489722, 'asymptotic': 0.5678330854173734, 'at': 0.42985488919607967, 'distribution': 0.46738046676498457, 'expression': 0.5268540758151136, 'found': 0.46766611976534184, 'incidence': 0.5484024065798496, 'laminar': 0.4867597585162857, 'lift': 0.5096754459460194, 'linearized': 0.5546436799180499, 'long': 0.5467648339946614, 'narrow': 0.6429127947248894, 'on': 0.4254281289797649, 'potential': 0.5467648339946614, 'stream': 0.4838144330560182, 'supersonic': 0.48547423995698785, 'theory': 0.4541199252417034, 'used': 0.4773624697820017, 'wing': 0.48526344805351135}
======================================================================
========================================================================================================================================================================


Query No: 19

Query Vector for weight (Version 1) are:
[('basic', 0.03848117788395965),
 ('combining', 0.05006516669551291),
 ('consideration', 0.05006516669551291),
 ('doe', 0.05006516669551291),
 ('dynamic', 0.05006516669551291),
 ('effect', 0.03848117788395965),
 ('entry', 0.05006516669551291),
 ('exist', 0.05006516669551291),
 ('good', 0.05006516669551291),
 ('re', 0.05006516669551291),
 ('realistic', 0.05006516669551291),
 ('relative', 0.05006516669551291),
 ('result', 0.05006516669551291),
 ('simplicity', 0.05006516669551291),
 ('treatment', 0.05006516669551291)]

Query Vector for weight (Version 2) are:
[('basic', 0.035473182449981974),
 ('combining', 0.03812420785804817),
 ('consideration', 0.03812420785804817),
 ('doe', 0.03812420785804817),
 ('dynamic', 0.03812420785804817),
 ('effect', 0.035473182449981974),
 ('entry', 0.03812420785804817),
 ('exist', 0.03812420785804817),
 ('good', 0.03812420785804817),
 ('re', 0.03812420785804817),
 ('realistic', 0.03812420785804817),
 ('relative', 0.03812420785804817),
 ('result', 0.03812420785804817),
 ('simplicity', 0.03812420785804817),
 ('treatment', 0.03812420785804817)]

Ranks  Document Number   Scores Titles


1     286       0.07515076560860234   effect of roll on dynamic instability of symmetric missiles .


Vector Representation for the Rank 1 With Document ID 286


{'attempt': 0.3854150706640581, 'by': 0.05233983836505397, 'certain': 0.25730367938315063, 'condition': 0.15012544924324459, 'describing': 0.49337805582014427, 'discussion': 0.3182369617027767, 'dynamic': 0.32147677670752695, 'experimental': 0.16108273106391074, 'extend': 0.47024573618458926, 'form': 0.19090547796463975, 'generalized': 0.37948970696423406, 'instability': 0.3885097972720185, 'neater': 0.7509775004326937, 'note': 0.3020292458501778, 'on': 0.05749589356104888, 'result': 0.08066045255080079, 'slightly': 0.3738847937284974, 'stability': 0.2811026613971851, 'stating': 0.6791219525543741, 'to': 0.011748290985597008}
======================================================================
2     509       0.05510346445158705   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 2 With Document ID 509


{'acted': 0.5271982855734489, 'at': 0.055861380633815266, 'by': 0.06275576151877217, 'change': 0.22302558106185744, 'condition': 0.1242304617275272, 'conduction': 0.3093937822796063, 'considers': 0.36885503908586875, 'derived': 0.19103750478445003, 'entry': 0.3164485331545604, 'heat': 0.14608784514803438, 'heated': 0.3524654687089807, 'heating': 0.2545706528709851, 'material': 0.26203487688769017, 'method': 0.09736364101196376, 'most': 0.23261554649289723, 're': 0.32685940877657377, 'severe': 0.3891335228376759, 'space': 0.36885503908586875, 'state': 0.2731192355396403, 'sublimation': 0.5271982855734489, 'such': 0.17789496875257943, 'suitable': 0.3049936147025652, 'surface': 0.12634218584411033, 'under': 0.18036731451851562, 'upon': 0.2545706528709851, 'vehicle': 0.2716527987994464}
======================================================================
3     1146       0.05140111152014116   thermal buckling of cylinders .


Vector Representation for the Rank 3 With Document ID 1146


{'among': 0.5492534744193474, 'area': 0.3282769611482099, 'axial': 0.2746214484161083, 'both': 0.2038183526493618, 'buckling': 0.27357957389166593, 'circumferential': 0.4132248292166513, 'cylinder': 0.2216663818798242, 'difference': 0.31204612886278377, 'discussed': 0.19916425046207756, 'due': 0.24094451625367497, 'exist': 0.40190461444533776, 'experimental': 0.16108273106391074, 'future': 0.47024573618458926, 'indicated': 0.30479382682054995, 'investigation': 0.19815778000687356, 'on': 0.05749589356104888, 'result': 0.08066045255080079, 'reviewed': 0.4305425982496091, 'several': 0.26183128290606894, 'stress': 0.23154677291407538, 'that': 0.057109801336041384, 'theoretical': 0.20069251857152517, 'thermal': 0.2954241050090529, 'to': 0.011748290985597008, 'various': 0.23017369797185824, 'work': 0.28801626558942756}
======================================================================
4     716       0.03237233521266626   study of the oscillatory motion of manned vehicles entering the earth's atmosphere .


Vector Representation for the Rank 4 With Document ID 716


{'aerodynamic': 0.18348915734933427, 'analysis': 0.13283120624992406, 'applied': 0.17743882191433544, 'arbitrarily': 0.39256906491107807, 'atmosphere': 0.26008475076950177, 'ballistic': 0.3336288129190638, 'behavior': 0.24762502642954715, 'comparable': 0.3299332158936935, 'consequence': 0.39256906491107807, 'continuous': 0.3107750585362357, 'damping': 0.28445171299870836, 'deceleration': 0.3658393706105376, 'deficiency': 0.44763337698537986, 'derived': 0.17691097273004497, 'doe': 0.27133761090628217, 'entry': 0.2930483094538725, 'expression': 0.21980459174508976, 'found': 0.11724750453956863, 'function': 0.16207720315867485, 'human': 0.44763337698537986, 'limit': 0.2615979586158803, 'made': 0.10967596759648604, 'may': 0.14279443242670897, 'missile': 0.3107750585362357, 'more': 0.17331108777644477, 'motion': 0.27675279470896497, 'oscillatory': 0.5592437010557056, 'prescribed': 0.32302094422766553, 'property': 0.20730119850254605, 're': 0.302689338503849, 'remain': 0.35041542073362547, 'result': 0.061811682778245364, 'serious': 0.41029581399344117, 'study': 0.17381547683570062, 'such': 0.16474027967078791, 'than': 0.13193016434126684, 'that': 0.060577628187355376, 'through': 0.18759403405361602, 'to': 0.009002945218177212, 'tolerance': 0.4331495683762693, 'trajectory': 0.5063865293673488, 'traverse': 0.42090368268483946, 'vehicle': 0.41186943515600627, 'within': 0.2042745082385507}
======================================================================
5     1140       0.032358916237417615   shock-standoff distance for spherical bodies at high mach numbers .


Vector Representation for the Rank 5 With Document ID 1140


{'accurate': 0.32653464042795, 'almost': 0.4305425982496091, 'apropriate': 0.7509775004326937, 'behind': 0.3150953381735983, 'by': 0.05233983836505397, 'consideration': 0.2941521179759523, 'development': 0.303402320792395, 'distance': 0.25909106232649964, 'dyke': 0.5354108567977349, 'expression': 0.2868315024929699, 'give': 0.24558703719724512, 'hay': 0.7509775004326937, 'heat': 0.1765388542942732, 'method': 0.11765842405816515, 'prediction': 0.2993364803607412, 'ratio': 0.16284879835226998, 'shock': 0.18500605986439667, 'shockstandoff': 0.7509775004326937, 'simple': 0.2120719652133681, 'specific': 0.33368683078438854, 'sponsored': 0.6370891515767835, 'theory': 0.12237131028024509, 'those': 0.23796112640068073, 'usaf': 0.6370891515767835, 'van': 0.5023981461279287}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     286       0.025596091820387117   effect of roll on dynamic instability of symmetric missiles .


Vector Representation for the Rank 1 With Document ID 286


{'attempt': 0.575414410967581, 'by': 0.42382149172611616, 'certain': 0.5171069239223595, 'condition': 0.46832677094041564, 'describing': 0.6245517304160044, 'discussion': 0.5448395598257829, 'dynamic': 0.5463141006104051, 'experimental': 0.4733137714047885, 'extend': 0.6140234907802441, 'form': 0.48688703301081027, 'generalized': 0.5727175932707989, 'instability': 0.576822917500825, 'neater': 0.7417932663124371, 'note': 0.5374629231921529, 'on': 0.426168173145614, 'result': 0.43671108591627966, 'slightly': 0.5701666225677666, 'stability': 0.527938582384565, 'stating': 0.7090895669368236, 'to': 0.40534701338887325}
======================================================================
2     509       0.02240329151186158   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 2 With Document ID 509


{'acted': 0.6725109590639371, 'at': 0.42887497707735966, 'by': 0.4291629329558567, 'change': 0.5152828388370986, 'condition': 0.4642152358926964, 'conduction': 0.5599269167685637, 'considers': 0.5906626846244781, 'derived': 0.4987480708313855, 'entry': 0.5635735464703271, 'heat': 0.4755134071530064, 'heated': 0.5821908483832174, 'heating': 0.5315886160136986, 'material': 0.5354469040641762, 'method': 0.45032766592036005, 'most': 0.5202399313552581, 're': 0.5689549708377533, 'severe': 0.6011447161613533, 'space': 0.5906626846244781, 'state': 0.5411764545758323, 'sublimation': 0.6725109590639371, 'such': 0.4919546399789279, 'suitable': 0.557652452076105, 'surface': 0.46530679476160014, 'under': 0.4932326056594879, 'upon': 0.5315886160136986, 'vehicle': 0.5404184474020378}
======================================================================
3     1146       0.01868343041701715   thermal buckling of cylinders .


Vector Representation for the Rank 3 With Document ID 1146


{'among': 0.6349397893729108, 'area': 0.5404184474020378, 'axial': 0.5174676324375955, 'both': 0.48718204448756053, 'buckling': 0.5170219770294359, 'circumferential': 0.5767543745489275, 'cylinder': 0.49481642901750694, 'difference': 0.5334758089007223, 'discussed': 0.4851912809539179, 'due': 0.5030625322107244, 'exist': 0.5719122224317468, 'experimental': 0.46890214567650507, 'future': 0.6011447161613533, 'indicated': 0.530373681388334, 'investigation': 0.4847607694182272, 'on': 0.42459351420092595, 'result': 0.43450201157679064, 'reviewed': 0.5841619435466713, 'several': 0.5119967179492529, 'stress': 0.49904270540285517, 'that': 0.42442836563064573, 'theoretical': 0.4858449882210745, 'thermal': 0.5263658406164518, 'to': 0.40502525908018294, 'various': 0.49845538105673476, 'work': 0.5231971829492517}
======================================================================
4     716       0.017746457707164844   study of the oscillatory motion of manned vehicles entering the earth's atmosphere .


Vector Representation for the Rank 4 With Document ID 716


{'aerodynamic': 0.48182859781231646, 'analysis': 0.4592372405550716, 'applied': 0.4791303977001564, 'arbitrarily': 0.5750696149582721, 'atmosphere': 0.5159870739790682, 'ballistic': 0.5487846930321831, 'behavior': 0.5104305507130891, 'comparable': 0.5471366091506398, 'consequence': 0.5750696149582721, 'continuous': 0.5385928609756788, 'damping': 0.5268537343363642, 'deceleration': 0.5631492735268658, 'deficiency': 0.5996260275094591, 'derived': 0.4788949987303708, 'doe': 0.5210053855767273, 'entry': 0.5306874618658071, 'expression': 0.4980237840482656, 'found': 0.45228755220233685, 'function': 0.4722797491873949, 'human': 0.5996260275094591, 'limit': 0.51666190227986, 'made': 0.4489109589458915, 'may': 0.463680428585965, 'missile': 0.5385928609756788, 'more': 0.47728959848605046, 'motion': 0.5249038301747843, 'oscillatory': 0.6462925857378359, 'prescribed': 0.5440540210222741, 'property': 0.4924477862524642, 're': 0.5349869632642762, 'remain': 0.5562708279043145, 'result': 0.42756546165032505, 'serious': 0.5829750140681439, 'study': 0.47751453520747317, 'such': 0.4734673714970785, 'than': 0.458835413019207, 'that': 0.4273398423725459, 'through': 0.48365920355358283, 'to': 0.4040149423215345, 'tolerance': 0.5931668461246482, 'trajectory': 0.6285419272221313, 'traverse': 0.587705686078053, 'vehicle': 0.581388521639961, 'within': 0.4910980072034307}
======================================================================
5     1331       0.017698235263711944   calculated responses of a large sweptwing airplane to continuous turbulence with flight-test comparisons .


Vector Representation for the Rank 5 With Document ID 1331


{'aerodynamics': 0.5605616112916868, 'aeroelasticity': 0.6266381658300703, 'airplane': 0.5417233700165232, 'available': 0.5055523220926668, 'based': 0.4732667621367106, 'calculated': 0.5110138336994205, 'compare': 0.5626695008350584, 'connection': 0.5566761233237867, 'contribute': 0.6077999245549066, 'deformation': 0.528447179379483, 'degree': 0.5486850970028242, 'determined': 0.48571362908220084, 'dimensional': 0.47031494498166077, 'due': 0.48571362908220084, 'dynamic': 0.5143621843970072, 'effect': 0.4396297470149536, 'examined': 0.5275993712998417, 'extent': 0.5470006468283406, 'favorably': 0.590467117906214, 'five': 0.5531612719154015, 'flight': 0.4921690834058493, 'freedom': 0.6194322134047819, 'gust': 0.5755143645989503, 'lifting': 0.5405141460368108, 'load': 0.4924911642937627, 'motion': 0.492816082935304, 'on': 0.4204535955873463, 'one': 0.46208585101479344, 'process': 0.511007324681013, 'random': 0.5626695008350584, 'relative': 0.5311142227082268, 'response': 0.6516269724465271, 'result': 0.4286941583856709, 'shown': 0.4587001697113354, 'static': 0.5064859929055171, 'surface': 0.4543134567206057, 'symmetrical': 0.5484470293569195, 'test': 0.46824647610185444, 'theory': 0.44353238356593583, 'these': 0.44770486152115063, 'to': 0.4071571240393595, 'turbulence': 0.539343316675094, 'various': 0.48188201698546634, 'vertical': 0.528447179379483, 'wing': 0.4949082042066897}
======================================================================
========================================================================================================================================================================


Query No: 20

Query Vector for weight (Version 1) are:
[('by', 0.03206764823663304),
 ('condition', 0.041720972246260764),
 ('convection', 0.041720972246260764),
 ('current', 0.041720972246260764),
 ('determined', 0.041720972246260764),
 ('flow', 0.014620665573615537),
 ('formally', 0.041720972246260764),
 ('free', 0.041720972246260764),
 ('general', 0.041720972246260764),
 ('ha', 0.041720972246260764),
 ('heating', 0.041720972246260764),
 ('induced', 0.041720972246260764),
 ('influence', 0.041720972246260764),
 ('joule', 0.041720972246260764),
 ('magnetohydrodynamic', 0.041720972246260764),
 ('produced', 0.041720972246260764),
 ('under', 0.041720972246260764)]

Query Vector for weight (Version 2) are:
[('by', 0.02880957617845637),
 ('condition', 0.030792567311338646),
 ('convection', 0.030792567311338646),
 ('current', 0.030792567311338646),
 ('determined', 0.030792567311338646),
 ('flow', 0.025225607394045006),
 ('formally', 0.030792567311338646),
 ('free', 0.030792567311338646),
 ('general', 0.030792567311338646),
 ('ha', 0.030792567311338646),
 ('heating', 0.030792567311338646),
 ('induced', 0.030792567311338646),
 ('influence', 0.030792567311338646),
 ('joule', 0.030792567311338646),
 ('magnetohydrodynamic', 0.030792567311338646),
 ('produced', 0.030792567311338646),
 ('under', 0.030792567311338646)]

Ranks  Document Number   Scores Titles


1     509       0.06670380244777907   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 1 With Document ID 509


{'acted': 0.5271982855734489, 'at': 0.055861380633815266, 'by': 0.06275576151877217, 'change': 0.22302558106185744, 'condition': 0.1242304617275272, 'conduction': 0.3093937822796063, 'considers': 0.36885503908586875, 'derived': 0.19103750478445003, 'entry': 0.3164485331545604, 'heat': 0.14608784514803438, 'heated': 0.3524654687089807, 'heating': 0.2545706528709851, 'material': 0.26203487688769017, 'method': 0.09736364101196376, 'most': 0.23261554649289723, 're': 0.32685940877657377, 'severe': 0.3891335228376759, 'space': 0.36885503908586875, 'state': 0.2731192355396403, 'sublimation': 0.5271982855734489, 'such': 0.17789496875257943, 'suitable': 0.3049936147025652, 'surface': 0.12634218584411033, 'under': 0.18036731451851562, 'upon': 0.2545706528709851, 'vehicle': 0.2716527987994464}
======================================================================
2     1276       0.04804878445943171   a three-dimensional linearized analysis of the forces exerted on a rigid wing by a shock wave .


Vector Representation for the Rank 2 With Document ID 1276


{'acoustic': 0.4082757719609241, 'author': 0.23833663006222613, 'by': 0.04331179236839078, 'dimensional': 0.163564324255595, 'distribution': 0.12607535993592625, 'edge': 0.17454918969413313, 'flat': 0.17692564250327128, 'found': 0.12660984428377786, 'front': 0.3214961336939525, 'ha': 0.11966097837637452, 'induced': 0.2716527987994464, 'moving': 0.31168150346321444, 'obliquely': 0.6214421478571256, 'on': 0.047578484797422, 'plate': 0.23002160078661651, 'pressure': 0.0834887895608359, 'shock': 0.15309455095854613, 'solution': 0.10854665920362061, 'striking': 0.4677370287671866, 'term': 0.1871501651331313, 'two': 0.1051403770694433}
======================================================================
3     286       0.04573947230242199   effect of roll on dynamic instability of symmetric missiles .


Vector Representation for the Rank 3 With Document ID 286


{'attempt': 0.3854150706640581, 'by': 0.05233983836505397, 'certain': 0.25730367938315063, 'condition': 0.15012544924324459, 'describing': 0.49337805582014427, 'discussion': 0.3182369617027767, 'dynamic': 0.32147677670752695, 'experimental': 0.16108273106391074, 'extend': 0.47024573618458926, 'form': 0.19090547796463975, 'generalized': 0.37948970696423406, 'instability': 0.3885097972720185, 'neater': 0.7509775004326937, 'note': 0.3020292458501778, 'on': 0.05749589356104888, 'result': 0.08066045255080079, 'slightly': 0.3738847937284974, 'stability': 0.2811026613971851, 'stating': 0.6791219525543741, 'to': 0.011748290985597008}
======================================================================
4     26       0.04531672344480748   inviscid leading-edge effect in hypersonic flow .


Vector Representation for the Rank 4 With Document ID 26


{'account': 0.25106876010190277, 'basis': 0.26074486069362346, 'blunt': 0.22812318711727908, 'current': 0.360269433606657, 'downstream': 0.25947395655495925, 'edge': 0.25290958241973427, 'effect': 0.09218542078944494, 'flow': 0.06220061601834868, 'give': 0.20322597653563415, 'ha': 0.11966097837637452, 'hypersonic': 0.2818397039595156, 'influence': 0.23638689930953372, 'interaction': 0.2488111440108371, 'interest': 0.29681748236510425, 'inviscid': 0.25222024665695203, 'leading': 0.31065164560888653, 'led': 0.4329544232897724, 'note': 0.2499325254733439, 'on': 0.047578484797422, 'perturbation': 0.3524654687089807, 'problem': 0.12933338923453824, 'purpose': 0.2499325254733439, 'realization': 0.6214421478571256, 'significant': 0.2746111768021922, 'small': 0.15419672192711542, 'theory': 0.10126360623697798, 'thickness': 0.1813765551041639, 'to': 0.014086267179562515, 'viscous': 0.2182139764355936}
======================================================================
5     407       0.04227990014931493   stationary convection flow of an electrically conducting liquid between parallel plates in a magnetic field .


Vector Representation for the Rank 5 With Document ID 407


{'between': 0.1415028515150645, 'calculated': 0.1866089364588232, 'conducting': 0.32685940877657377, 'convection': 0.3488145151546617, 'convective': 0.360269433606657, 'different': 0.22139154193623733, 'distribution': 0.12607535993592625, 'electrically': 0.360269433606657, 'field': 0.26577924259061636, 'flow': 0.06220061601834868, 'found': 0.12660984428377786, 'heat': 0.14608784514803438, 'heated': 0.3524654687089807, 'induced': 0.2716527987994464, 'liquid': 0.3644548715088276, 'made': 0.118433711946317, 'magnetic': 0.3093937822796063, 'parallel': 0.26739815197031136, 'plate': 0.15875271962933116, 'presence': 0.270211009225151, 'space': 0.36885503908586875, 'stationary': 0.34194809467438225, 'study': 0.1876948302029902, 'temperature': 0.20783152798066645, 'to': 0.009721840107770649, 'two': 0.1051403770694433, 'velocity': 0.12988863039831225}
======================================================================


Rankings  Doc No   Score Titles
========================================================================================================================================================================
1     509       0.03311025836707379   a graphical approximation for temperatures and sublimation rates at surfaces subjected to small net and large gross heat transfer rates .


Vector Representation for the Rank 1 With Document ID 509


{'acted': 0.6725109590639371, 'at': 0.42887497707735966, 'by': 0.4291629329558567, 'change': 0.5152828388370986, 'condition': 0.4642152358926964, 'conduction': 0.5599269167685637, 'considers': 0.5906626846244781, 'derived': 0.4987480708313855, 'entry': 0.5635735464703271, 'heat': 0.4755134071530064, 'heated': 0.5821908483832174, 'heating': 0.5315886160136986, 'material': 0.5354469040641762, 'method': 0.45032766592036005, 'most': 0.5202399313552581, 're': 0.5689549708377533, 'severe': 0.6011447161613533, 'space': 0.5906626846244781, 'state': 0.5411764545758323, 'sublimation': 0.6725109590639371, 'such': 0.4919546399789279, 'suitable': 0.557652452076105, 'surface': 0.46530679476160014, 'under': 0.4932326056594879, 'upon': 0.5315886160136986, 'vehicle': 0.5404184474020378}
======================================================================
2     1276       0.02588848497651098   a three-dimensional linearized analysis of the forces exerted on a rigid wing by a shock wave .


Vector Representation for the Rank 2 With Document ID 1276


{'acoustic': 0.6133739118018908, 'author': 0.5245599728776573, 'by': 0.422635696750772, 'dimensional': 0.48548231880139464, 'distribution': 0.4658897602523783, 'edge': 0.4912232514508652, 'flat': 0.4924652380367039, 'found': 0.466169093546025, 'front': 0.5680209612879695, 'ha': 0.46253746315530136, 'induced': 0.5419717365382082, 'moving': 0.5628916193356822, 'obliquely': 0.7247793554096444, 'on': 0.424865564199593, 'plate': 0.5076594122692809, 'pressure': 0.44363308049027567, 'shock': 0.4800105846513601, 'solution': 0.45672887513276195, 'striking': 0.6444496744034084, 'term': 0.49780879878575807, 'two': 0.4549486770568892}
======================================================================
3     953       0.024551877582220365   vibrations of infinitely long cylindrical shells under initial stress .


Vector Representation for the Rank 3 With Document ID 953


{'applied': 0.4924668842782028, 'armenakas': 0.6712034817299548, 'bending': 0.5757574234421132, 'by': 0.4209016161889557, 'circumferential': 0.5650189807578765, 'cylindrical': 0.5154962525875045, 'dynamic': 0.5283799188208748, 'effect': 0.44448729037047574, 'general': 0.47913318023015866, 'herrmann': 0.6998985853014351, 'infinitely': 0.5738605819359809, 'influence': 0.5140767437985565, 'initial': 0.5546580254085055, 'investigation': 0.47913318023015866, 'long': 0.5325232022239244, 'moment': 0.5122567459463317, 'on': 0.4229606574493451, 'presented': 0.4598261028512745, 'radial': 0.5551491735910778, 'recently': 0.5504127814239155, 'response': 0.5780038653390304, 'shear': 0.5154962525875045, 'shell': 0.5527432462226276, 'stress': 0.5233030731976042, 'study': 0.49057868739732025, 'theory': 0.44886828541918167, 'to': 0.404691613056663, 'under': 0.48704253910881823, 'uniform': 0.5536266118925959}
======================================================================
4     500       0.024021422373330947   joule heating in magnetohydrodynamic free-convection flows .


Vector Representation for the Rank 4 With Document ID 500


{'actual': 0.5251130773451756, 'alters': 0.5939673602440383, 'analytic': 0.5923708372866928, 'analyzed': 0.5110046088427009, 'between': 0.4546186312036147, 'conducting': 0.5261643374126537, 'confirms': 0.5939673602440383, 'constant': 0.4975743052743931, 'convection': 0.5346387804748364, 'description': 0.5251130773451756, 'developed': 0.4690440364888074, 'distributed': 0.5283726162580094, 'electrically': 0.539060260040076, 'energy': 0.48805318120974667, 'equation': 0.4418978832154194, 'estimating': 0.539060260040076, 'field': 0.5011622076570552, 'flow': 0.4343035741442479, 'fluid': 0.4741799916424583, 'free': 0.4657844975759737, 'fully': 0.5818139070805144, 'ha': 0.44618789499593314, 'heating': 0.5638087506294377, 'influence': 0.5303671257017999, 'joule': 0.7998798002868794, 'laminar': 0.4626599662334723, 'located': 0.5332870862324857, 'magnetic': 0.5194227869621569, 'magnitude': 0.4978049050861293, 'manner': 0.5048551592720173, 'negligibly': 0.5865786508712163, 'obtained': 0.4409883852914322, 'openended': 0.6398702155099468, 'plate': 0.46127690115900016, 'practice': 0.5480645049781299, 'present': 0.4618844762023408, 'qualitative': 0.5360480106323194, 'result': 0.4429500026811447, 'retained': 0.5939673602440383, 'small': 0.4595183333591467, 'steady': 0.4890826499563806, 'submerged': 0.603493063373699, 'such': 0.46866561053182226, 'temperature': 0.4791058623929029, 'term': 0.47223802022119576, 'that': 0.4182414790673669, 'transverse': 0.5103356585995314, 'two': 0.4405830936852431, 'uniformly': 0.5283726162580094, 'useful': 0.5185626889726742, 'usual': 0.5212130559715428, 'vertical': 0.5153296926751515, 'well': 0.4712064130838589}
======================================================================
5     26       0.023109342468133016   inviscid leading-edge effect in hypersonic flow .


Vector Representation for the Rank 5 With Document ID 26


{'account': 0.5181450275443787, 'basis': 0.5226982948264851, 'blunt': 0.5073475657208144, 'current': 0.5695314149780343, 'downstream': 0.52210024748516, 'edge': 0.510445285929222, 'effect': 0.44337954699715976, 'flow': 0.42926964505573084, 'give': 0.4956317248939718, 'ha': 0.4563086764778146, 'hypersonic': 0.5230790324043773, 'influence': 0.5112362076377797, 'interaction': 0.517082664727295, 'interest': 0.5396729310944354, 'inviscid': 0.5186868807431123, 'leading': 0.5356611698749918, 'led': 0.6037346750916747, 'note': 0.5176103514204616, 'on': 0.4223889319986674, 'perturbation': 0.5658591156150347, 'problem': 0.4608602074878633, 'purpose': 0.5176103514204616, 'realization': 0.6924310441729925, 'significant': 0.5292233451669617, 'small': 0.47256010645027235, 'theory': 0.44765145429983033, 'thickness': 0.48535007736521485, 'to': 0.4061514545690097, 'viscous': 0.5026846041940374}
======================================================================
========================================================================================================================================================================


Time (in sec) to build Relevance Model is:  05.081913 seconds
