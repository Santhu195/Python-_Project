import getpass
import time
import datetime
import smtplib
from email.mime.text import MIMEText

Master_input = ''
Master_confirm = ''

def master_pass():
    global Master_input
    global Master_confirm

    Master_input = input('****Please Set The Password*****\n')

    Master_confirm = input('Please confirm the Password you entered\n')

master_pass()

if Master_input == Master_confirm:
    pass

else:
    print('Both the password doesnt match' )
    master_pass()
   
App_pass = input('Enter the App password\n')
   
timer_count = 5                                                              # Wrong Password wait time
attempt = 0
Max_attempt = 3
Pass_input_lst = []
def login():
    global timer_count
    global Pass_input_lst
    Pass_input =  getpass.getpass(prompt='Enter the login Password :')
    Pass_input_lst.append(Pass_input)
    
    global attempt 
   
    if Pass_input == App_pass:
        print('-----Login Successful-----')
        attempt = 7
    else:
        print('-----Login Failed------\n Plese Enter the correct Password')
        attempt +=1
        if attempt == Max_attempt:
            print('Maximum Password limit reached please wait for {} sec'.format(timer_count)) 
            timer()                                                             # Calling wait time
            send_mail()                                                        # Sending mail for failed attempt
            attempt = 0
            print('If forgot password press yes or else no')                    # Asking to reset Passwrod 
            confirm = str(input())
            if confirm =='yes':
                reset_pass()
            elif confirm == 'no':
                login()
            else:
                print('Please enter proper response')

        while (attempt <=2):
            login()
        
def timer():
    global timer_count
    a = timer_count
    while (a>0):
                print(a, '\r',end ="")
                time.sleep(1)
                a -=1   
            
        
     
def send_mail():
    global Pass_input_lst
    body = "Security Alert, Login atttempt made more than 3 at {} and used password as {}".format(datetime.datetime.now(),Pass_input_lst)

    msg = MIMEText(body)
    msg['From'] = 'santhosh.can195@gmail.com'
    msg['To'] = 'santhosh.can195@gmail.com'
    msg['Subject'] = 'Pass Attempt made'
    

    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('santhosh.can195@gmail.com','Jayanthi')

    server.send_message(msg)

    server.quit()

    
def reset_pass():
    global Master_input
    global App_pass
    master = getpass.getpass(prompt='Enter the Master Password :')
    if master == Master_input:
        App_pass = input("Enter the New Password\n")
    
    else:
        print("Master password is wrong, you cant reset it")


login()