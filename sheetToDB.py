from __future__ import print_function
import mysql.connector
from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import datetime
import createJson
import configparser


#---------------------------------------function to convert date and time in to the required format--------------------------
def convertDatetime(dateInSheetFormat):
   my_date_string = dateInSheetFormat.strip() + " 12:00AM"
   
   datetime_object = datetime.strptime(my_date_string, '%d %b %Y %I:%M%p')

   #YYYY-MM-DD HH:mm:SS
   datetime_string = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
   
   return datetime_string
#--------------------------------------------------------------------------------------------------------------------------
def fromsheet():
   config = configparser.ConfigParser()# read the configuration file
   
   #------------copy the config.ini file path and paste it to here--------------
   config.read('C:\_code_\django_project\e18-co227-Automated-Notification-System-for-Examinations\config.ini')# get all the connections

   #******************************************** CREDENTIALS FOR THE GOOGLE SHEET ****************************************


   # The file keys.json stores the user's access and refresh tokens, and is
   # created automatically when the authorization flow completes for the first
   # time.
   #createJson.createJsonKeyFile()
   #------------copy the config.ini file path and paste it to here--------------
   SERVICE_ACCOUNT_FILE = 'C:\_code_\django_project\e18-co227-Automated-Notification-System-for-Examinations\keys.json'
   SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

   creds = None
   creds = service_account.Credentials.from_service_account_file(
         SERVICE_ACCOUNT_FILE, scopes=SCOPES)


   #for my testing google sheet
   #https://docs.google.com/spreadsheets/d/1caUzbQ6q5jRDB9D0iNNTBwi2cC0jTvzctiRMD09DBGM/edit#gid=0
   #SAMPLE_SPREADSHEET_ID = '1caUzbQ6q5jRDB9D0iNNTBwi2cC0jTvzctiRMD09DBGM'
   #SAMPLE_RANGE_NAME = 'Class Data!A2:E'

   #for the project google sheet sample - my copy
   #https://docs.google.com/spreadsheets/d/1mDfQQFO-akrOuuU9C9fGnDpt9DqEJmKB1swsRw3_gkE/edit#gid=0
   #SAMPLE_SPREADSHEET_ID = '1mDfQQFO-akrOuuU9C9fGnDpt9DqEJmKB1swsRw3_gkE'
   SAMPLE_SPREADSHEET_ID = '18u8I6lo2HbbafjsXdxWQNYz6vGu0RyhZ2GBdGYYQ8MI'

   service = build('sheets', 'v4', credentials=creds)


   # ************************************************ Call the Sheets API *************************************************
   sheet = service.spreadsheets()
   result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                              range='E/17 - Semester 6 (May 2022)!A8:K22').execute()
   values = result.get('values', []) #list of list
   NumberOfCourses = int(len(values)/4) #so the values are takes only the data entered cells

   print(values)
   
   #***************************************************** DATABASE *********************************************************
   #establishing the connection

   #------------------------------ Enter the credentials of db using config file-----------------------------
   conn = mysql.connector.connect(user=config.get('DB', 'username'), password=config.get('DB', 'password'), host=config.get('DB', 'host'), database=config.get('DB', 'db'))
   #------------------------------------------------------------------------------------------------

   #Creating a cursor object using the cursor() method
   cursor = conn.cursor()
   print(cursor)


   #entering data to the database
   query1 = """INSERT IGNORE INTO Examination(Examination_id,Examination_name) VALUES('{}','{}')"""
   query2 = """INSERT IGNORE INTO PAPER(COURSE_CODE,EXAMINATION_ID,COORDINATOR_ID,SUB_COORDINATOR_ID,MODERATOR_ID,SUB_MODERATOR_ID) VALUES('{}','{}','{}','{}','{}','{}')"""
   query3 = """SELECT Id FROM lecturer WHERE Name = '{}'"""
   query5 = """INSERT IGNORE INTO PHASE(PHASE_CODE,COURSE_CODE,DUE_DATE) VALUES('{}','{}','{}')"""

   lecturer_id = []



   try:
      #Entering data to examination table : for now one examination
      cursor.execute(query1.format(1,'E/17 - Semester 6 (May 2022)'))
      conn.commit()
      starting = 0
      
      # outer loop for courses
      for j in range(NumberOfCourses):
         #inner for loop to go through the evaluational panel
         for i in range(starting,4+starting):
            lecturerName = (values[i][2]).split()
            lecturer = lecturerName[1]+" "+lecturerName[2]
            cursor.execute(query3.format(lecturer)) #getting the id's of evaluation panel
            id = cursor.fetchall()
            lecturer_id.append(id[0][0])
            conn.commit()
            
         # 0 - printing
         # 1 - paper moderating
      
         #entering data to paper table 
         #values[starting][0] is the course code
         cursor.execute(query2.format(values[starting][0],1,lecturer_id[0],lecturer_id[1],lecturer_id[2],lecturer_id[3]))
         conn.commit()

         #entering data to phase table 
         for task in range(2): #for 7 tasks of each course (need to update when the sheet is updated with all dates)
            cursor.execute(query5.format(task+1,values[starting][0],convertDatetime(values[starting][3+task])))
            conn.commit()
         

         print("Successful!")
         starting = starting + 4
         lecturer_id.clear() #list of id's is cleared
      
      conn.close()
      return "Database update: Successful"
   except:
      # Rolling back in case of error
      print("error occured! ---1")
      conn.rollback()
      conn.close()
      return "Database update: Not successful"
   

if __name__ == '__main__':
   fromsheet()
