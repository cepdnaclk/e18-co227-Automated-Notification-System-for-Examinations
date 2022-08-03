from django.shortcuts import render
import sys
#------------copy path to sheetToDB and paste it to here--------------
sys.path.insert(0,'C:/_code_/django_project/e18-co227-Automated-Notification-System-for-Examinations')
import sheetToDB

#before clicking the button
def button(request):
    return render(request,"home.html")

#once button is clicked
def output(request):
    data = sheetToDB.fromsheet()
    return render(request,"home.html",{'data':data})
