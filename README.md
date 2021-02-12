# Women-s-Safety

This website is designed to alert contacts of a women in case of an emergency. 

Tech used is HTML, CSS, Bootstrap, Python, Django and Sqlite

Features offered are as follows:

1)User can register using name and password. Session is created for each user.

2)Name and Email id of contacts is updated by the user and it's stored in database.

3)There is an emergency button which does the following 4 things:

    i) SMTP module is used to send emails to all the contacts (Can include email Id of State and central gov
    
    offices). Mail also contains the latitude and longitude of the user and it is used with Google API and 
    
    link opens using Google maps
    
    ii) Twilio is used to send calls with information. Number should be registered with Twilio.
    
    iii) Twilio is used to send text messages along with location of the user (can be opened directly 
    
    with google maps)
    
    iv) Messages is sent on twitter using Twitter API (twitter developer account is mandatory). Relevant 
    
    hashtags are sent on the  message which changes for each user and this can be tracked by officals.

4) Helpline numbers for each state is given and information about women safety is provided too

5) fill mail id and password in main_app/mail.py

6) access token code and secret key for twitter needs to be filled in main_app/twitterapi.py and 
   details for Twilio need to be filled in main_app/smscall.py

7)to run website, use

    python manage.py migrate

    python manage.py runserver
