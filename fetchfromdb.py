from ast import Assign
from time import strftime
import mysql.connector
from datetime import datetime
import mailTest
import configparser

config = configparser.ConfigParser()    # read the configuration file
config.read('config.ini')               # get all the connections

mydb = mysql.connector.connect(
    host=config.get('DB', 'host'),
    user=config.get('DB', 'username'),
    passwd=config.get('DB', 'password'),
    database = config.get('DB', 'db')
)

mycursor = mydb.cursor()

phase_code=0

#Following snippet loops for every phase code fron 1 to 7
for phase_code in range (1,8):

    assignee1=""
    assignee2=""
    task=""

    #enter assignees for below tasks
    if(phase_code==1):
        task = "Sending the paper for Moderation"
        assignee1 = "moderator_id"
        assignee2 = "sub_moderator_id"
    elif(phase_code==2):
        task = "Printing the Paper and Submitting to AR"
        assignee1 = "moderator_id"
        assignee2 = "coordinator_id"
    elif(phase_code==3):
        task = "Collecting Answer Scripts"
        assignee1 = "coordinator_id"
        assignee2 = "sub_coordinator_id"
    elif(phase_code==4):
        task = "Completion of First Marking"
        assignee1 = "moderator_id"
        # assignee2 = "sub_moderator_id"
    elif(phase_code==5):
        task = "Completion of Second Marking"
        assignee1 = "sub_moderator_id"
        # assignee2 = "moderator_id"
    elif(phase_code==6):
        task = "Releasing Provincial Results"
        assignee1 = "coordinator_id"
        assignee2 = "sub_coordinator_id"
    elif(phase_code==7):
        task = "Submission of Final Grades"
        assignee1 = "coordinator_id"
        assignee2 = "sub_coordinator_id"
    else:
        task = ""
        assignee1 = ""
        assignee2 = ""

    #part of the sql query for assignees
    if(len(assignee2)):     #if there are two assignees
        queryLine = "(p."+assignee1+" = l.id or p."+assignee2+"=l.id)"
    else:                   #if there is one assignees
        queryLine = "p."+assignee1+" = l.id"


    #sql query for selecting data
    mycursor.execute("select l.Email_address, e.examination_name, p.course_code, l.title, l.name, ph.phase_code, ph.due_date, l.channel_id from paper as p JOIN phase as ph ON ph.course_code = p.course_code JOIN lecturer as l ON "+queryLine+" JOIN examination as e ON p.examination_id=e.examination_id where ph.phase_code="+str(phase_code))
    # -----------------------------------------------------------------------
    # records can be filtered by due dates (comparing them with current date)
    #   ex: <above query> + where ph.due_date = <current_date-3days>
    # -----------------------------------------------------------------------

    result = mycursor.fetchall()

    #By following loop, email message for each phase code of every course is composed
    for row in result:
        #each row containes receiver's email address, examination name, course code, title, assignee name, phase code and due date as a tuple
        receiver_email = row[0]
        exam_name = row[1]
        course_code = row[2]
        assignee_title = row[3]
        assignee_name = row[4]
        due_date = row[6]
        channel_id1 = row[7]
        subjectLine = '{}: {} Task reminder'.format(exam_name , course_code)   #The subject line
        msg = "To:-"+receiver_email+"\n"+task+" - "+course_code+" - "+exam_name+"\n "+assignee_title+" "+assignee_name+",\n Due date for "+task.lower()+" is "+due_date.strftime('%d/%m/%Y')+". Please ignore this message if the task is already completed\n"
        msgDiscord = "\n\n" + task+" - "+course_code+" - "+exam_name+"\n "+assignee_title+" "+assignee_name+",\n Due date for "+task.lower()+" is "+due_date.strftime('%d/%m/%Y')+". \n Please ignore this message if the task is already completed\n\n\n"
        
        print (msg)

        # printed example below---------------------------------------------------------------------------------------------------
        # Sending the paper for Moderation - CO224 - E18_4thSem_end_semester_examination
        # Prof Isuru_Nawinna,
        # Due date for sending the paper for moderation is 28/06/2022. Please ignore this message if the task is already completed
        # -------------------------------------------------------------------------------------------------------------------------

        # -----------------------------------------------------------------------------
        # MAIL
        # CAN
        # BE
        # SENT
        # HERE
        mailTest.sendRemainder(receiver_email,subjectLine,msg)
        token = "add your discord token here"
        sendMessage(token,channel_id1,msgDiscord)
        
        # -----------------------------------------------------------------------------

        print("\n------------------------------------------")
    
    print("\n")
    print("***************************************************")
