___
# Simple UI: Edit the google sheet & Submit changes to Database
___


This frontend was developed using Django framework and connect with sheetToDB.py
We only needed few buttons for this system only for executing codes.

* Google sheet button:  it will be redirect to the google sheet that need to be update.
* Update Database button is clicked then the sheetToDB.py will be executed and database will be updated.

Get into buttonpython directory - cd buttonpython
run command: python manage.py runserver [if specifically needed - 127.0.0.1:0002]
             python manage.py migrate
             
Go to the web browser and search for 127.0.0.1:0002 - this will be change if you does not mention an IP address
in above command. In that case get the IP address via terminal.