---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e18-co227-Automated-Notification-System-for-Examinations
title:
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Automated Notification System for Examinations

---
<div class="figure container">
<img class="mx-auto d-block" src="./images/sample.jpg" alt="Sample Image" width="320"/>
<p class="caption text-center"></p>
</div>



## Team
-  E/18/276, Rajasooriya J.M.,[e18276@eng.pdn.ac.lk](mailto:e18276@eng.pdn.ac.lk)
-  E/18/283, Ranasinghe R.D.J.M.,[e18283@eng.pdn.ac.lk](mailto:e18283@eng.pdn.ac.lk)
-  E/18/412, De Silva M.S.G.M.,[e18412@eng.pdn.ac.lk](mailto:e18412@eng.pdn.ac.lk)

## Table of Contents
1. [Introduction](#introduction)
2. [Other Sub Topics](#other-sub-topics)
3. [Links](#links)

---

## Introduction

Normally holding examinations are not that easy. From making the paper to finalizing the marks, it has different phases that different lecturers are engaging in order to complete an examination completely.

Following are the sample procedure an examination of our department,

- Sent for Moderation
- Paper Printed and Submitted to AR
- Answer Scripts Collected
- First Marking Completed
- Second Marking Completed
- Provisional Results Released
- Final Grades Submitted


There are staff members who are incharge for each of these phases and there are deadlines for these as well.

Then those lecturers are supposed to complete these phases on or before the given deadlines. Several lecturers are engaging in these phases and also since they are tightly busy with their schedules there can be some mistakes like forgetting the deadlines. Therefore, we need to have a system to track the progress of the procedure and a reminder system to get the work done within the given time in order to finish the examinations as expected and send the results to the AR office. 


## Other Sub Topics
### Our solution

With this Automated Notification System that we are expecting to develop reminders, that will be sent automatically to the assigned lecturers before the deadlines.


### Data Flow

 - Data is entered into a table in a Google Sheet
 - After inputting, data in the Google Sheet is sent to the Database via Sheets API
 - Required records are fetched from the Database and due dates for tasks are compared with current date in Python on a daily basis
 - If due date is close for a particular task, an email is developed (by python) as sent to required parties

### ER Diagram of the Database

<div class="figure container">
<img class="mx-auto d-block" src="./images/er_diagram.png" alt="ER Diagram" width="420"/>
<p class="caption text-center"></p>
</div>

## Links

- [Project Repository](https://github.com/cepdnaclk/{{ page.repository-name }}){:target="_blank"}
- [Project Page](https://cepdnaclk.github.io/{{ page.repository-name}}){:target="_blank"}
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)


[//]: # (Please refer this to learn more about Markdown syntax)
[//]: # (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
