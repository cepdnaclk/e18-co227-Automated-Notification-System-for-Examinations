___
# Automated Notification System for Examinations
___



Advisor
* Dr. Mahanama Wickramasinghe

Team Members
* Rajasooriya J.M.
* Ranasinghe R.D.J.M.
* De Silva M.S.G.M.

This is an automated system that can be used on examination tasks. The system is able to send reminders (basically via email) to respective parties, which consist of the details about their task. The reminders are sent before 3 days to the deadline.

The task schedule is to be filled by a user on a Google Sheet. The program fetches data in the Sheet and send it to a predesigned database table. The system runs periodically (once a day) and checks for any deadlines that should be reminded of and if any, the system designs a reminder email and sends to respective party/parties.

Technologies and Protocols which are used in this project are,
* Google Sheets and Sheets API (data input and fetching)
* Python (programming language)
* MySQL (DBMS)
* Github (Version Control)

System is projected to be extended to a further phase in which it can also send reminders via discord.
