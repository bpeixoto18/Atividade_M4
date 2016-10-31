import random
import smtplib

def emailChores(rchore, remail):
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtpObj.ehlo()
    smtpObj.login('bpeixoto@gmail.com', '********') ##O programa só roda quando trocar a senha pela senha certa##
    body = 'Subject: Your Chore\n\nYour weekly assigned chore is: %s' % rchore
    print('Sending chore email to ' + remail + '...')
    smtpObj.sendmail('bpeixoto@gmail.com', remail, body)
    smtpObj.quit()


chores = ['dishes', 'bathroom', 'vaccum', 'trash']
emails = ['someone@emailaddress.com', 'someone@emailaddress.com'\
          'someone@emailaddress.com', 'someone@emailaddress.com'] ##Deve-se substituir por um e-mail existente

for i in range(0, len(emails)):
    randomChore = random.choice(chores)
    emailChores(randomChore, emails[i])
    chores.remove(randomChore)