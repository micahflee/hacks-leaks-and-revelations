# Homework 4-3: Grepping for Revelations

The homework teaches you to use `grep`.

## Grep for `antifa`

```sh
cat ../BlueLeaks-filenames.txt | grep antifa
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep antifa
```

(No results.)

## Case insensative grep for `antifa`

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

## Find Word (`.docx`) documents

```sh
cat ../BlueLeaks-filenames.txt | grep -i .docx$
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep -i .docx$
./houstonhidta/files/EBAT1/TABC Overview.docx
./houstonhidta/files/EBAT1/Houston HIDTA Course Evaluation for Hash Oil Extraction Hazards Training 06-27-14.docx
./houstonhidta/files/EBAT1/legaltedno 12012.docx
./houstonhidta/files/EBAT1/Houston HIDTA Course Evaluation for Hash Oil Extraction Hazards Training 06-27-142.docx
./houstonhidta/files/EBAT1/Training flyer for Dec 4 Prison Gang Class 20121.docx
./houstonhidta/files/EBF00000/Training flyer for Dec 4 Prison Gang Class 20121.docx
./houstonhidta/files/EBAT2/Info for TCLEOSE Credit - Writing Search Warrants.docx
./houstonhidta/files/EBAT3/DTO Validation Committee.docx
--snip--
```

## Count Word (`.docx`) documents

```sh
cat ../BlueLeaks-filenames.txt | grep -i .docx$ | wc -l
```

Example:

```
micah@rogue:/media/micah/datasets/BlueLeaks-extracted$ cat ../BlueLeaks-filenames.txt | grep -i .docx$ | wc -l
8861
```

There are **8,861** `.docx` files.

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