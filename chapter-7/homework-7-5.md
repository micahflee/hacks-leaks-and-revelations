# Homework 7-5: Import PST Files Into Thunderbird

In this homework you'll import the Heritage Foundation email dump into Thunderbird.

## Convert a PST File Into EML or MBOX

Install the `readpst` CLI tool.

In Windows (with WSL) or Linux:

```sh
sudo apt update
sudo apt install pst-utils
```

In macOS with Homebrew:

```sh
brew install libpst
```

Open a terminal, change to the folder with `backup.pst`, and run:

```sh
readpst -e backup.pst
```

For example:

```
micah@trapdoor datasets % cd HeritageFoundation 
micah@trapdoor HeritageFoundation % clear

micah@trapdoor HeritageFoundation % cd 
micah@trapdoor ~ % cd /Volumes/datasets/HeritageFoundation 
micah@trapdoor HeritageFoundation % readpst -e backup.pst 
Opening PST file and indexes...
Processing Folder "Deleted Items"
Processing Folder "Inbox"
	"Inbox" - 27 items done, 0 items skipped.
Processing Folder "Outbox"
Processing Folder "Sent Items"
	"Sent Items" - 595 items done, 0 items skipped.
Processing Folder "Calendar"
Processing Folder "Contacts"
	"Contacts" - 15 items done, 0 items skipped.
Processing Folder "Journal"
Processing Folder "Notes"
Processing Folder "Tasks"
Processing Folder "Drafts"
Processing Folder "Junk E-mail"
	"Junk E-mail" - 100 items done, 0 items skipped.
Processing Folder "Quarantine"
Processing Folder "Travel Info"
	"Travel Info" - 87 items done, 0 items skipped.
Processing Folder "Technical"
	"Technical" - 2 items done, 0 items skipped.
Processing Folder "Social Issues"
	"Social Issues" - 6 items done, 0 items skipped.
Processing Folder "Heritage"
Processing Folder "Call Reports"
	"Call Reports" - 66 items done, 0 items skipped.
Processing Folder "Weekly Reports"
	"Weekly Reports" - 31 items done, 0 items skipped.
Processing Folder "DPMC Weekly Income"
	"DPMC Weekly Income" - 40 items done, 0 items skipped.
Processing Folder "Email Mgt Service (EMS)"
	"Email Mgt Service (EMS)" - 2 items done, 0 items skipped.
	"Heritage" - 4 items done, 0 items skipped.
Processing Folder "Personal Items"
Processing Folder "Sanctuary"
Processing Folder "Elder, Chair 2008-2009"
Processing Folder "Painting"
	"Painting" - 9 items done, 0 items skipped.
Processing Folder "From Robert"
	"From Robert" - 5 items done, 0 items skipped.
Processing Folder "Disc. Spiritual Identity"
	"Disc. Spiritual Identity" - 1 items done, 0 items skipped.
Processing Folder "Gen. Info"
	"Gen. Info" - 7 items done, 0 items skipped.
Processing Folder "Elder-Member Survey"
	"Elder-Member Survey" - 1 items done, 0 items skipped.
Processing Folder "Budget Info"
	"Budget Info" - 3 items done, 0 items skipped.
Processing Folder "ministry leaders"
	"ministry leaders" - 2 items done, 0 items skipped.
Processing Folder "GIT"
	"GIT" - 5 items done, 0 items skipped.
Processing Folder "Finances"
	"Finances" - 2 items done, 0 items skipped.
Processing Folder "Meeting Agenda"
	"Meeting Agenda" - 4 items done, 0 items skipped.
Processing Folder "Goals"
	"Goals" - 2 items done, 0 items skipped.
Processing Folder "Toby"
	"Toby" - 2 items done, 0 items skipped.
Processing Folder "Prayer Emails"
Processing Folder "Church wide emails"
	"Church wide emails" - 1 items done, 0 items skipped.
Processing Folder "40 Days"
Processing Folder "Prayer Requests"
	"Prayer Requests" - 9 items done, 0 items skipped.
Processing Folder "prayer@sactuarycares.org"
	"prayer@sactuarycares.org" - 2 items done, 0 items skipped.
	"40 Days" - 16 items done, 0 items skipped.
	"Prayer Emails" - 7 items done, 0 items skipped.
Processing Folder "January Meeting"
	"January Meeting" - 3 items done, 0 items skipped.
Processing Folder "Facilities"
	"Facilities" - 3 items done, 0 items skipped.
Processing Folder "Budget Reductions"
	"Budget Reductions" - 3 items done, 0 items skipped.
Processing Folder "GH"
	"GH" - 1 items done, 0 items skipped.
Processing Folder "Family Ministry"
	"Family Ministry" - 3 items done, 0 items skipped.
Processing Folder "Sunday Evening Cong. Meeting"
	"Sunday Evening Cong. Meeting" - 2 items done, 0 items skipped.
	"Elder, Chair 2008-2009" - 19 items done, 0 items skipped.
Processing Folder "Marcie.Church Information"
	"Marcie.Church Information" - 2 items done, 0 items skipped.
Processing Folder "General Info"
	"General Info" - 2 items done, 0 items skipped.
Processing Folder "Discipline"
Processing Folder "Hubs"
	"Hubs" - 16 items done, 0 items skipped.
Processing Folder "GH Counseling"
	"GH Counseling" - 1 items done, 0 items skipped.
Processing Folder "Doug"
	"Doug" - 5 items done, 0 items skipped.
Processing Folder "Woody"
	"Woody" - 1 items done, 0 items skipped.
Processing Folder "Restoration"
	"Restoration" - 16 items done, 0 items skipped.
	"Discipline" - 16 items done, 0 items skipped.
Processing Folder "Prayer"
Processing Folder "Mentoring"
Processing Folder "Elder 2009-10"
Processing Folder "Meetings"
	"Meetings" - 6 items done, 0 items skipped.
	"Elder 2009-10" - 3 items done, 0 items skipped.
	"Sanctuary" - 9 items done, 0 items skipped.
Processing Folder "Alie's School"
	"Alie's School" - 2 items done, 0 items skipped.
Processing Folder "Online Purchases"
Processing Folder "Running"
	"Running" - 6 items done, 0 items skipped.
Processing Folder "Ads"
	"Ads" - 2 items done, 0 items skipped.
Processing Folder "Craigs List"
	"Craigs List" - 4 items done, 0 items skipped.
Processing Folder "Computer"
	"Computer" - 5 items done, 0 items skipped.
Processing Folder "Ebay"
	"Ebay" - 2 items done, 0 items skipped.
Processing Folder "Amazon"
	"Amazon" - 7 items done, 0 items skipped.
	"Online Purchases" - 27 items done, 0 items skipped.
Processing Folder "Ameritrade"
	"Ameritrade" - 2 items done, 0 items skipped.
Processing Folder "CarFax"
	"CarFax" - 1 items done, 0 items skipped.
Processing Folder "Insurance"
	"Insurance" - 11 items done, 0 items skipped.
Processing Folder "Homeschool"
	"Homeschool" - 1 items done, 0 items skipped.
Processing Folder "LIFE"
	"LIFE" - 5 items done, 0 items skipped.
Processing Folder "Personal"
	"Personal" - 1 items done, 0 items skipped.
Processing Folder "Credit/Finances"
	"Credit/Finances" - 3 items done, 0 items skipped.
Processing Folder "Economic Club"
	"Economic Club" - 3 items done, 0 items skipped.
Processing Folder "Republic Trash"
	"Republic Trash" - 1 items done, 0 items skipped.
Processing Folder "LifeLock"
	"LifeLock" - 5 items done, 0 items skipped.
Processing Folder "CopyTalk"
	"CopyTalk" - 4 items done, 0 items skipped.
	"Personal Items" - 14 items done, 0 items skipped.
	"Personal Folders" - 17 items done, 0 items skipped.
```

All of the emails from the PST have been extracted in EML format in the `Personal Folders` folder.

## Create a Local Folder

- Click the Thunderbird menu icon in the top-right corner and choose Account Settings.
- Click the Account Actions drop-down menu on the left side of the screen and choose Add Feed Account.
- Under "Account Name" type `Heritage Foundation`, click Next, then click Finish.

## Import the EML Files

- Switch back to the main tab.
- Right-click on the `Heritage Foundation` feed and choose New Folder.
- Name your folder `backup.pst` and click Create Folder.
- Right-click on the `backup.pst` folder and choose ImportExportTools NG > Import all messages from a directory > also from its subdirectories.
- Browse for your `Personal Folders` folder and import it.

![Heritage Foundation email in Thunderbird](./homework-7-5.png)