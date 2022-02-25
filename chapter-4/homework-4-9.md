# Homework 4-9: Explore BlueLeaks With the Terminal

## Change to the `BlueLeaks-extracted` folder

```sh
cd /media/micah/datasets/BlueLeaks-extracted/
```

Example:

```
micah@rogue:~$ cd /media/micah/datasets/BlueLeaks-extracted/
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ 
```

## Measure disk space of all of `BlueLeaks-extracted`

```sh
du -sh .
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ du -sh .
271G	.
```

## Measure disk space of the `ncric` folder

```sh
du -sh ncric
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ du -sh ncric
19G	ncric
```

## Measure disk space of each BlueLeaks folder

```sh
for FOLDER in $(ls); do du -sh $FOLDER; done
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ for FOLDER in $(ls); do du -sh $FOLDER; done
2.8G	211sfbay
225M	acprlea
71M	acticaz
771M	akorca
587M	alabamafusioncenter
27M	alabamalecc
776M	alertmidsouth
129M	aorca
9.4G	arictexas
1.4G	atlantahidta
212M	attackwa
5.6G	azhidta
1.7G	azorca
1016M	bostonbric
1.2G	burlingamepolice
492M	calema
2.0G	cal-orca
2.7G	calstas
212M	cbaghidta
386M	ccroc
833M	chicagoheat
126M	chicagolandfsg
2.9G	ciacco
821M	cnoa3
105M	cnoatraining
349M	cnyorca
3.3G	coorca
1.3G	corca
5.1G	counterdrugtraining
27M	crimestopperslea
214M	cvchidta
13G	dediac
76M	dvicphila
12M	energysecuritycouncil
34M	eousa
5.3G	fbicahouston
76M	fbinaakansaswmissouri
357M	fbinaamichigan
135M	fbinaatexas
8.1M	fcpddoc
815M	flinttownshippolice
602M	fwintex
42M	gatlinburglec
1.6G	graorca
832M	hcsovcp
7.1M	hennepincountyshield
62M	hidtatraining
1.6G	hiorca
791M	houstonhidta
459M	houstonhidtatraining
4.6G	hpdlineup
13M	hpdretired
2.2G	icefishx
1.7G	ilcrime
477M	ileatraining
1.1G	iowaintex
4.2G	jerseyvillagepd
14G	jric
7.0M	kcpers
5.4M	kyorca
13G	lacleartraining
31M	lapdtraining
2.5M	leapsla
1.6G	losaltospdbc
55M	lupd
2.3G	mactf
1.6G	maorca
546M	membersfaithbased-isao
4.8G	memiac
187M	metrohoustonpolice
462M	mhidta
36G	miacx
12K	miacxold
1.9M	millvalleypolice
308M	miorca
495M	mlrin
2.7M	mnorca
1.3G	morciu
3.7M	mtorca
12G	mvpddoc
45M	mvpdtx
19G	ncric
12K	ncric-history-good
12K	ncricSteveBackup
297M	nctccounterdrug
2.1M	ndslic
338M	nehidta
1.6G	neorca
2.4M	nevadacyberexchange
37M	nhiac
887M	njuasi
8.7M	nmfisoa
1.3G	nmhidta
2.6M	nnorca
21M	nnric
597M	northtexasfusion
585M	northtexashidta
6.8M	novatopolicedept
61M	ntacnv
719M	nvhidta
2.4G	nymorca
1.4M	oaklandsheriffshield
1.3M	oaktac
4.9G	ociac
2.2M	okorca
16M	orcaid
2.1M	orcaor
8.0M	orocc
9.5M	otewg
13M	pchidta
2.4M	phillymostwanted
1.2G	pleasantonpolice
1.6M	prvihidta
3.7M	pspddoc
6.0M	publicsafetycadets
46G	repo
3.3M	richlandshield
69M	rlpsaroc
5.9G	rmhidta
6.0M	rockhillyorkcountyconnect
5.2M	ruasi
1.9M	ruralcountysummit
94M	sacrttac
24M	safecityabq
39M	safecityfw
4.3M	sanbrunopolice
1.4M	sccpca
8.3M	scgcsandiego
78M	sciic
3.4M	sdciaa
33M	sdfusion
6.3M	sdorca
22M	sduasi
3.6M	seattleshield
30M	Securitypartnership
6.6G	seffc
2.3M	semacp
2.5M	sfbay-infragard
214M	sicrime
26M	sltew
29M	snctc
9.5M	snorca
15M	sogtraining
2.7M	spottinglies
3.3M	stopabqgangs
126M	stopeasttexasgangs
55M	stophoustondrugs
153M	stoplubbockgangs
1.4M	stopnorthtexasgangs
1.7M	stopsanantoniogangs
3.9M	stopseattledrugs
570M	stopspokanegangs
129M	stopwesttexasgangs
2.5G	stxhidta
5.8M	sunnyvalebriefing
5.3M	swtxfusion
1008K	terrorismtip
8.1M	texasorca
214M	tnoa
25M	twnsg
168M	unmpd
2.2G	usao
6.1M	utahsiac
9.6M	utorca
8.0M	vlnsn
124M	vslea
1.5M	wifusion
14M	wsorca
```

## Measure disk space of each BlueLeaks folder in bytes

```sh
for FOLDER in $(ls); do du -s --bytes $FOLDER; done
```

Example:

```sh
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ for FOLDER in $(ls); do du -s --bytes $FOLDER; done
2944592140	211sfbay
226985525	acprlea
67988648	acticaz
784512854	akorca
600132564	alabamafusioncenter
26196795	alabamalecc
784630687	alertmidsouth
128374848	aorca
9995631094	arictexas
1455518974	atlantahidta
215412038	attackwa
5920005958	azhidta
1740127875	azorca
1053401537	bostonbric
1238995907	burlingamepolice
512167353	calema
2058728104	cal-orca
2810180846	calstas
217146509	cbaghidta
396390568	ccroc
860869794	chicagoheat
124731427	chicagolandfsg
3062419669	ciacco
854529626	cnoa3
107859406	cnoatraining
353890180	cnyorca
3360726552	coorca
1303967392	corca
5368456742	counterdrugtraining
23823992	crimestopperslea
219427089	cvchidta
13296757211	dediac
78111468	dvicphila
11697952	energysecuritycouncil
30909959	eousa
5576945017	fbicahouston
76095247	fbinaakansaswmissouri
366884245	fbinaamichigan
136497120	fbinaatexas
7709530	fcpddoc
846632434	flinttownshippolice
625899641	fwintex
42010898	gatlinburglec
1604611445	graorca
859450146	hcsovcp
6660477	hennepincountyshield
50887752	hidtatraining
1651626231	hiorca
820824462	houstonhidta
472726881	houstonhidtatraining
4878534513	hpdlineup
12144092	hpdretired
2224526558	icefishx
1790956172	ilcrime
492814752	ileatraining
1073551865	iowaintex
4419973093	jerseyvillagepd
14440684104	jric
6594498	kcpers
4910116	kyorca
13145195646	lacleartraining
31324632	lapdtraining
1889254	leapsla
1670287057	losaltospdbc
56431816	lupd
2374124633	mactf
1588466378	maorca
565672635	membersfaithbased-isao
5107913683	memiac
193869396	metrohoustonpolice
475336430	mhidta
38132797321	miacx
12288	miacxold
1201267	millvalleypolice
318653894	miorca
511860248	mlrin
2025576	mnorca
1316467416	morciu
3098011	mtorca
12703122416	mvpddoc
45512047	mvpdtx
20009469932	ncric
12288	ncric-history-good
12288	ncricSteveBackup
294054722	nctccounterdrug
1337372	ndslic
345897400	nehidta
1617769203	neorca
1549096	nevadacyberexchange
36351851	nhiac
923568087	njuasi
8369315	nmfisoa
1319313891	nmhidta
1976425	nnorca
21058299	nnric
620712782	northtexasfusion
601493026	northtexashidta
6283999	novatopolicedept
62464067	ntacnv
740971346	nvhidta
2496686229	nymorca
665062	oaklandsheriffshield
566274	oaktac
5177628314	ociac
1513778	okorca
15207078	orcaid
1419838	orcaor
7607507	orocc
9205590	otewg
12420769	pchidta
1695921	phillymostwanted
1172817397	pleasantonpolice
868373	prvihidta
3117563	pspddoc
5482185	publicsafetycadets
49268450478	repo
2629378	richlandshield
70933599	rlpsaroc
6227649212	rmhidta
5472028	rockhillyorkcountyconnect
4692245	ruasi
1170151	ruralcountysummit
97462327	sacrttac
24179662	safecityabq
39672825	safecityfw
3700657	sanbrunopolice
644887	sccpca
7932757	scgcsandiego
80841405	sciic
2744472	sdciaa
33237121	sdfusion
5809050	sdorca
22204701	sduasi
3031954	seattleshield
30315332	Securitypartnership
7031720065	seffc
1440924	semacp
1776771	sfbay-infragard
222206413	sicrime
25982181	sltew
29442932	snctc
9180985	snorca
14374746	sogtraining
2055392	spottinglies
2674579	stopabqgangs
130243203	stopeasttexasgangs
56096892	stophoustondrugs
156728244	stoplubbockgangs
701853	stopnorthtexasgangs
986750	stopsanantoniogangs
3250974	stopseattledrugs
591352936	stopspokanegangs
132566964	stopwesttexasgangs
2663871769	stxhidta
5291263	sunnyvalebriefing
4766738	swtxfusion
270559	terrorismtip
7764329	texasorca
220650654	tnoa
24594992	twnsg
168400743	unmpd
2228728006	usao
5647272	utahsiac
9304775	utorca
7585103	vlnsn
128047446	vslea
787905	wifusion
13014650	wsorca
```

## Sort this output numerically

```sh
for FOLDER in $(ls); do du -s --bytes $FOLDER; done | sort -n
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ for FOLDER in $(ls); do du -s --bytes $FOLDER; done | sort -n
12288	miacxold
12288	ncric-history-good
12288	ncricSteveBackup
270559	terrorismtip
566274	oaktac
644887	sccpca
665062	oaklandsheriffshield
701853	stopnorthtexasgangs
787905	wifusion
868373	prvihidta
986750	stopsanantoniogangs
1170151	ruralcountysummit
1201267	millvalleypolice
1337372	ndslic
1419838	orcaor
1440924	semacp
1513778	okorca
1549096	nevadacyberexchange
1695921	phillymostwanted
1776771	sfbay-infragard
1889254	leapsla
1976425	nnorca
2025576	mnorca
2055392	spottinglies
2629378	richlandshield
2674579	stopabqgangs
2744472	sdciaa
3031954	seattleshield
3098011	mtorca
3117563	pspddoc
3250974	stopseattledrugs
3700657	sanbrunopolice
4692245	ruasi
4766738	swtxfusion
4910116	kyorca
5291263	sunnyvalebriefing
5472028	rockhillyorkcountyconnect
5482185	publicsafetycadets
5647272	utahsiac
5809050	sdorca
6283999	novatopolicedept
6594498	kcpers
6660477	hennepincountyshield
7585103	vlnsn
7607507	orocc
7709530	fcpddoc
7764329	texasorca
7932757	scgcsandiego
8369315	nmfisoa
9180985	snorca
9205590	otewg
9304775	utorca
11697952	energysecuritycouncil
12144092	hpdretired
12420769	pchidta
13014650	wsorca
14374746	sogtraining
15207078	orcaid
21058299	nnric
22204701	sduasi
23823992	crimestopperslea
24179662	safecityabq
24594992	twnsg
25982181	sltew
26196795	alabamalecc
29442932	snctc
30315332	Securitypartnership
30909959	eousa
31324632	lapdtraining
33237121	sdfusion
36351851	nhiac
39672825	safecityfw
42010898	gatlinburglec
45512047	mvpdtx
50887752	hidtatraining
56096892	stophoustondrugs
56431816	lupd
62464067	ntacnv
67988648	acticaz
70933599	rlpsaroc
76095247	fbinaakansaswmissouri
78111468	dvicphila
80841405	sciic
97462327	sacrttac
107859406	cnoatraining
124731427	chicagolandfsg
128047446	vslea
128374848	aorca
130243203	stopeasttexasgangs
132566964	stopwesttexasgangs
136497120	fbinaatexas
156728244	stoplubbockgangs
168400743	unmpd
193869396	metrohoustonpolice
215412038	attackwa
217146509	cbaghidta
219427089	cvchidta
220650654	tnoa
222206413	sicrime
226985525	acprlea
294054722	nctccounterdrug
318653894	miorca
345897400	nehidta
353890180	cnyorca
366884245	fbinaamichigan
396390568	ccroc
472726881	houstonhidtatraining
475336430	mhidta
492814752	ileatraining
511860248	mlrin
512167353	calema
565672635	membersfaithbased-isao
591352936	stopspokanegangs
600132564	alabamafusioncenter
601493026	northtexashidta
620712782	northtexasfusion
625899641	fwintex
740971346	nvhidta
784512854	akorca
784630687	alertmidsouth
820824462	houstonhidta
846632434	flinttownshippolice
854529626	cnoa3
859450146	hcsovcp
860869794	chicagoheat
923568087	njuasi
1053401537	bostonbric
1073551865	iowaintex
1172817397	pleasantonpolice
1238995907	burlingamepolice
1303967392	corca
1316467416	morciu
1319313891	nmhidta
1455518974	atlantahidta
1588466378	maorca
1604611445	graorca
1617769203	neorca
1651626231	hiorca
1670287057	losaltospdbc
1740127875	azorca
1790956172	ilcrime
2058728104	cal-orca
2224526558	icefishx
2228728006	usao
2374124633	mactf
2496686229	nymorca
2663871769	stxhidta
2810180846	calstas
2944592140	211sfbay
3062419669	ciacco
3360726552	coorca
4419973093	jerseyvillagepd
4878534513	hpdlineup
5107913683	memiac
5177628314	ociac
5368456742	counterdrugtraining
5576945017	fbicahouston
5920005958	azhidta
6227649212	rmhidta
7031720065	seffc
9995631094	arictexas
12703122416	mvpddoc
13145195646	lacleartraining
13296757211	dediac
14440684104	jric
20009469932	ncric
38132797321	miacx
49268450478	repo
```

## What are the largest and smaller folders in BlueLeaks?

The largest folder is `repo`, which takes 49268450478 bytes. This is 45.88 gigabytes.

The three smallest folders are `miacxold`, `ncric-history-good`, and `ncricSteveBackup`, each taking 12288 bytes. This is 12 kilabytes.

## List all filenames in BlueLeaks

```sh
find . -type f
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ find . -type f
./Securitypartnership/CreditCardForm.csv
./Securitypartnership/IncidentMapComments.csv
./Securitypartnership/ProductSelectorTree.csv
./Securitypartnership/RandomInfoCategory.csv
./Securitypartnership/CatalogImages.csv
./Securitypartnership/Survey.csv
./Securitypartnership/PasswordHistory.csv
./Securitypartnership/EventBuilder.csv
./Securitypartnership/SignupOptions.csv
./Securitypartnership/LinkDownloadHistory.csv
--snip--
```

## Save list of BlueLeaks filenames into a file

```sh
find . -type f > ../BlueLeaks-filenames.txt
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ find . -type f > ../BlueLeaks-filenames.txt
```

## Open that file in VS Code

```sh
code ../BlueLeaks-filenames.txt
```
![Screenshot of VS Code](./homework-4-9-blueleaks-filenames.png)

## Count files in BlueLeaks with `wc -l`

```sh
find . -type f | wc -l
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ find . -type f | wc -l
1031660
```

Number of files: **1,031,660**

## Count files again, using saved `BlueLeaks-filenames.txt`

```sh
cat ../BlueLeaks-filenames.txt | wc -l
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | wc -l
1031660
```

## Find files with "antifa" in the filenames

```sh
cat ../BlueLeaks-filenames.txt | grep antifa
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep antifa
```

(No results.)

Try again, but ignore case with `-i`:

```sh
cat ../BlueLeaks-filenames.txt | grep -i antifa
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep -i antifa
./arictexas/files/DDF/ARIC-LES - Situational Awareness - Antifa Activity.pdf
./arictexas/files/DDF/SWTFC-LES - Situational Awareness - ANTIFA Event Notification.pdf
./arictexas/files/DPI/SWTFC-LES - Situational Awareness - ANTIFA Event Notification.png
./arictexas/files/DPI/ARIC-LES - Situational Awareness - Antifa Activity.png
./dediac/files/DDF/ANTIFA Sub Groups and Indicators - LES.pdf
./dediac/files/DDF/ANTIFA - Fighting in the Streets.pdf
./dediac/files/DDF/FBI_PH_SIR_Tactics_and_Targets_Identified_for_4_November_2017_ANTIFA_Rally_in_Philadelphia_PA-2.pdf
./dediac/files/EBAT1/ANTIFA Sub Groups and Indicators - LES.pdf
./dediac/files/EBAT1/ANTIFA - Fighting in the Streets.pdf
./dediac/files/DPI/ANTIFA - Fighting in the Streets.png
./dediac/files/DPI/FBI_PH_SIR_Tactics_and_Targets_Identified_for_4_November_2017_ANTIFA_Rally_in_Philadelphia_PA-2.png
./ociac/files/EBAT1/U-FOUO_CFIX__OCIAC_JRA_DVE Use of Social Media_ANTIFA_ANTI-ANTIFA MOVEMENTS.pdf
```

## Count Word (`.docx`) documents

```sh
cat ../BlueLeaks-filenames.txt | grep -i .docx$ | wc -l
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep -i .docx$ | wc -l
8737
```

There are **8,737** `.docx` files.

## Count Word documents in the `ncric` folder

```sh
cat ../BlueLeaks-filenames.txt | grep ^./ncric/ | grep -i .docx$ | wc -l
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep ^./ncric/ | grep -i .docx$ | wc -l
600
```

There are **600** `.docx` files in `ncric`.

## Count PDFs and Excel documents

Count PDFs:

```sh
cat ../BlueLeaks-filenames.txt | grep -i .pdf$ | wc -l
```

Count Excel documents:

```sh
cat ../BlueLeaks-filenames.txt | grep -i .xlsx$ | wc -l
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep -i .pdf$ | wc -l
263536
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep -i .xlsx$ | wc -l
668
```

There are **263,536** PDFs and **668** Excel documents.

## Search for CSV files that mention "Black Lives Matter"

```sh
grep -i "black lives matter" */*.csv
```

Example (with redactions):

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ grep -i "black lives matter" */*.csv
alabamafusioncenter/EmailBuilder.csv:of groups such as the Nation of Islam, Black Lives Matter, New Black Panther
arictexas/IncidentMap.csv:2498,"05/31/20 00:00:00",REDACTED,REDACTED,"TX",,"TLO","A Crime-Stoppers tip alerted police of a subject who had posted threatening messages on social media.  The subject had allegedly posted a message that read: ""I WISH....I FUCKING WISH SOME ""Black Lives Matter"" PROTEST WOULD HAPPEN HERE IN AUSTIN TX!!!! AR-15 trigger time baby!!!!"".  The subject was contacted by law enforcement and advised of the severity of making these sorts of statements.
arictexas/IncidentMap.csv:The third letter also lists several prominent political figures and organizations, such as Jeb Bush, Marco Rubio, Obama, Clinton (both), the Media, the NFL, AARP, Black Lives Matter, and others.",,"REDACTED",,,,,,,,,20180443,,,,,,"11/01/18 13:41:01",,,,,,0,"b94965dc-824b-462b-bb09-1beb5d18a03d","ARICTLOLESSARIncidents",,0,7,,,,,,,,"AUSTIN",1,"REDACTED",,,,,"Travis",,,,,,,,,"TLO LES",,,,,,,,,,"1045",,,"Expressed or Implied Threat","18-3020546",0,0,,,,,,,,,,,,,,"Austin Police Department",,"REDACTED","REDACTED","AllTLOPartners",0,0,,,,,,,,,,,,,,,,"12/27/18 09:12:46 PM ap3768 changed IncidentMapStatusID from  to 7,ap3768 changed GenericField30 from ENCR: to 
--snip--
```
