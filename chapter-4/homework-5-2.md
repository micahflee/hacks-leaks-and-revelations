# Homework 5-2: Explore BlueLeaks With the Terminal

## Mac users, install GNU coreutils

This homework uses the `du` command. Both macOS and Linux come with `du`, but they're slightly different, and the Linux version (part of GNU coreutils) is better and more up-to-date. If you're using macOS, install coreutils like this:

```sh
brew install coreutils
```

Now, `du` is the Mac version and `gdu` is the coreutils version you just installed. Below I'll be showing you examples with the `du` command, but you should change that command to `gdu` instead.

## Change to the `BlueLeaks-extracted` folder

```sh
cd /media/micah/datasets/BlueLeaks-extracted/
```

## Measure disk space of all of `BlueLeaks-extracted`

```sh
du -sh --apparent-size .
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ du -sh --apparent-size .
269G	.
```

## Measure disk space of the `ncric` folder

```sh
du -sh --apparent-size ncric
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ du -sh --apparent-size ncric
19G	ncric
```

## Measure disk space of each BlueLeaks folder

```sh
for FOLDER in $(ls); do du -sh --apparent-size $FOLDER; done
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ for FOLDER in $(ls); do du -sh --apparent-size $FOLDER; done
2.8G	211sfbay
217M	acprlea
65M	acticaz
749M	akorca
573M	alabamafusioncenter
25M	alabamalecc
749M	alertmidsouth
123M	aorca
9.4G	arictexas
1.4G	atlantahidta
206M	attackwa
5.6G	azhidta
1.7G	azorca
1005M	bostonbric
1.2G	burlingamepolice
489M	calema
2.0G	cal-orca
2.7G	calstas
208M	cbaghidta
379M	ccroc
821M	chicagoheat
119M	chicagolandfsg
2.9G	ciacco
815M	cnoa3
103M	cnoatraining
338M	cnyorca
3.2G	coorca
1.3G	corca
5.0G	counterdrugtraining
23M	crimestopperslea
210M	cvchidta
13G	dediac
75M	dvicphila
12M	energysecuritycouncil
30M	eousa
5.2G	fbicahouston
73M	fbinaakansaswmissouri
350M	fbinaamichigan
131M	fbinaatexas
7.4M	fcpddoc
808M	flinttownshippolice
597M	fwintex
41M	gatlinburglec
1.5G	graorca
820M	hcsovcp
6.4M	hennepincountyshield
49M	hidtatraining
1.6G	hiorca
783M	houstonhidta
451M	houstonhidtatraining
4.6G	hpdlineup
12M	hpdretired
2.1G	icefishx
1.7G	ilcrime
470M	ileatraining
1.0G	iowaintex
4.2G	jerseyvillagepd
14G	jric
6.3M	kcpers
4.7M	kyorca
13G	lacleartraining
30M	lapdtraining
1.9M	leapsla
1.6G	losaltospdbc
54M	lupd
2.3G	mactf
1.5G	maorca
540M	membersfaithbased-isao
4.8G	memiac
185M	metrohoustonpolice
454M	mhidta
36G	miacx
12K	miacxold
1.2M	millvalleypolice
304M	miorca
489M	mlrin
2.0M	mnorca
1.3G	morciu
3.0M	mtorca
12G	mvpddoc
44M	mvpdtx
19G	ncric
12K	ncric-history-good
12K	ncricSteveBackup
281M	nctccounterdrug
1.3M	ndslic
330M	nehidta
1.6G	neorca
1.5M	nevadacyberexchange
35M	nhiac
881M	njuasi
8.0M	nmfisoa
1.3G	nmhidta
1.9M	nnorca
21M	nnric
592M	northtexasfusion
574M	northtexashidta
6.0M	novatopolicedept
60M	ntacnv
707M	nvhidta
2.4G	nymorca
650K	oaklandsheriffshield
554K	oaktac
4.9G	ociac
1.5M	okorca
15M	orcaid
1.4M	orcaor
7.3M	orocc
8.8M	otewg
12M	pchidta
1.7M	phillymostwanted
1.1G	pleasantonpolice
849K	prvihidta
3.0M	pspddoc
5.3M	publicsafetycadets
46G	repo
2.6M	richlandshield
68M	rlpsaroc
5.8G	rmhidta
5.3M	rockhillyorkcountyconnect
4.5M	ruasi
1.2M	ruralcountysummit
93M	sacrttac
24M	safecityabq
38M	safecityfw
3.6M	sanbrunopolice
630K	sccpca
7.6M	scgcsandiego
78M	sciic
2.7M	sdciaa
32M	sdfusion
5.6M	sdorca
22M	sduasi
2.9M	seattleshield
29M	Securitypartnership
6.6G	seffc
1.4M	semacp
1.7M	sfbay-infragard
212M	sicrime
25M	sltew
29M	snctc
8.8M	snorca
14M	sogtraining
2.0M	spottinglies
2.6M	stopabqgangs
125M	stopeasttexasgangs
54M	stophoustondrugs
150M	stoplubbockgangs
686K	stopnorthtexasgangs
964K	stopsanantoniogangs
3.2M	stopseattledrugs
564M	stopspokanegangs
127M	stopwesttexasgangs
2.5G	stxhidta
5.1M	sunnyvalebriefing
4.6M	swtxfusion
265K	terrorismtip
7.5M	texasorca
211M	tnoa
24M	twnsg
161M	unmpd
2.1G	usao
5.4M	utahsiac
8.9M	utorca
7.3M	vlnsn
123M	vslea
770K	wifusion
13M	wsorca
```

## Sort the BlueLeaks folders from smallest to largest

```sh
for FOLDER in $(ls); do du -sh --apparent-size $FOLDER; done | sort -h
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ for FOLDER in $(ls); do du -sh --apparent-size $FOLDER; done | sort -h
12K	miacxold
12K	ncric-history-good
12K	ncricSteveBackup
265K	terrorismtip
554K	oaktac
630K	sccpca
650K	oaklandsheriffshield
686K	stopnorthtexasgangs
770K	wifusion
849K	prvihidta
964K	stopsanantoniogangs
1.2M	millvalleypolice
1.2M	ruralcountysummit
1.3M	ndslic
1.4M	orcaor
1.4M	semacp
1.5M	nevadacyberexchange
1.5M	okorca
1.7M	phillymostwanted
1.7M	sfbay-infragard
1.9M	leapsla
1.9M	nnorca
2.0M	mnorca
2.0M	spottinglies
2.6M	richlandshield
2.6M	stopabqgangs
2.7M	sdciaa
2.9M	seattleshield
3.0M	mtorca
3.0M	pspddoc
3.2M	stopseattledrugs
3.6M	sanbrunopolice
4.5M	ruasi
4.6M	swtxfusion
4.7M	kyorca
5.1M	sunnyvalebriefing
5.3M	publicsafetycadets
5.3M	rockhillyorkcountyconnect
5.4M	utahsiac
5.6M	sdorca
6.0M	novatopolicedept
6.3M	kcpers
6.4M	hennepincountyshield
7.3M	orocc
7.3M	vlnsn
7.4M	fcpddoc
7.5M	texasorca
7.6M	scgcsandiego
8.0M	nmfisoa
8.8M	otewg
8.8M	snorca
8.9M	utorca
12M	energysecuritycouncil
12M	hpdretired
12M	pchidta
13M	wsorca
14M	sogtraining
15M	orcaid
21M	nnric
22M	sduasi
23M	crimestopperslea
24M	safecityabq
24M	twnsg
25M	alabamalecc
25M	sltew
29M	Securitypartnership
29M	snctc
30M	eousa
30M	lapdtraining
32M	sdfusion
35M	nhiac
38M	safecityfw
41M	gatlinburglec
44M	mvpdtx
49M	hidtatraining
54M	lupd
54M	stophoustondrugs
60M	ntacnv
65M	acticaz
68M	rlpsaroc
73M	fbinaakansaswmissouri
75M	dvicphila
78M	sciic
93M	sacrttac
103M	cnoatraining
119M	chicagolandfsg
123M	aorca
123M	vslea
125M	stopeasttexasgangs
127M	stopwesttexasgangs
131M	fbinaatexas
150M	stoplubbockgangs
161M	unmpd
185M	metrohoustonpolice
206M	attackwa
208M	cbaghidta
210M	cvchidta
211M	tnoa
212M	sicrime
217M	acprlea
281M	nctccounterdrug
304M	miorca
330M	nehidta
338M	cnyorca
350M	fbinaamichigan
379M	ccroc
451M	houstonhidtatraining
454M	mhidta
470M	ileatraining
489M	calema
489M	mlrin
540M	membersfaithbased-isao
564M	stopspokanegangs
573M	alabamafusioncenter
574M	northtexashidta
592M	northtexasfusion
597M	fwintex
707M	nvhidta
749M	akorca
749M	alertmidsouth
783M	houstonhidta
808M	flinttownshippolice
815M	cnoa3
820M	hcsovcp
821M	chicagoheat
881M	njuasi
1005M	bostonbric
1.0G	iowaintex
1.1G	pleasantonpolice
1.2G	burlingamepolice
1.3G	corca
1.3G	morciu
1.3G	nmhidta
1.4G	atlantahidta
1.5G	graorca
1.5G	maorca
1.6G	hiorca
1.6G	losaltospdbc
1.6G	neorca
1.7G	azorca
1.7G	ilcrime
2.0G	cal-orca
2.1G	icefishx
2.1G	usao
2.3G	mactf
2.4G	nymorca
2.5G	stxhidta
2.7G	calstas
2.8G	211sfbay
2.9G	ciacco
3.2G	coorca
4.2G	jerseyvillagepd
4.6G	hpdlineup
4.8G	memiac
4.9G	ociac
5.0G	counterdrugtraining
5.2G	fbicahouston
5.6G	azhidta
5.8G	rmhidta
6.6G	seffc
9.4G	arictexas
12G	mvpddoc
13G	dediac
13G	lacleartraining
14G	jric
19G	ncric
36G	miacx
46G	repo
```

## Make a list of filenames

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
![Screenshot of VS Code](./homework-5-2-blueleaks-filenames.png)

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