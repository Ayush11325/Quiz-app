import string
import random
import time
from datetime import datetime

login_user = ''
marks = 0
login_status = False
quiz_topic = ''
print(f"{'#'*30}\n {'*'*6} QUIZ APPLICATION {'*'*6}\n{'#'*30}")
print(f"{'#'*5}MSG{'#'*5}")

def main():
    choice = input("""
    Choose your choice:
    1. Register
    2. Login
    3. Attempt Quiz
    4. Result
    5. Exit
    \tEnter your choice:  """)
    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        attempt_quiz()
    elif choice == '4':
        show_result()
    elif choice == '5':
        exit_()
    else:
        print("#"*70)
        print("You choosed incorrect option please choose correct option".upper())
        print("#"*70)
        main()

def register():
    print(f"{'#'*10}WELCOME to QUIZ {'#'*10}")
    print("REGISTER HERE, Enter your details to explore world of Quiz!!!")
    name = input("Enter your name: ").upper()
    email = input("Enter your Email: ").lower()
    contact = input("Enter your contact number: ")
    pwd = input("Enter your password: ")

    l = string.ascii_lowercase #['abcdefghijklmnopqrstuvwxyz']
    u = string.ascii_uppercase #['ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    d = string.digits #['0123456789']
    rl = random.sample(l,4) 
    ru = random.sample(u,1)
    rd = random.sample(d,2)
    username = rl + ru +rd #abcdR45
    random.shuffle(username) #list
    username = ''.join(username) #string

    us_details = f"{name}, {email}, {contact}, {username}, {pwd}"
    login_details = f"{username},{pwd}"
    
    with open('user_details.txt','a') as file:
        file.write(str(us_details))
        file.write("\n")

    with open('user_login.txt','a') as file:
        file.write(str(login_details))
        file.write("\n")

    print(f"HELLO {name} your useraname is {username} and password is {pwd}, PLEASE SAVE IT FOR FUTURE LOGIN")
    ch = input("Do you want to login and attempt quiz y/n: ").lower()
    if ch == 'y' or ch == 'yes':
        login()
    else:
        exit_()

def login():
    global login_user
    global login_status
    print(f"{'#'*10}WELCOME to QUIZ {'#'*10}")
    print("LOGIN HERE, Enter your details to explore world of Quiz!!!")
    
    ch = input("""
        CHOOSE OPTION:
        1. If you registered earlier please select login option 1
        2. If you haven't register with us please register yourself select register option 2
        \tEnter your choice 1 or 2: """)
    
    if ch == '1':
        print(f"{'#'*10}WELCOME to QUIZ {'#'*10}")
        print("LOGIN HERE, Enter your details to explore world of Quiz!!!")
        username = input("Enter your username: ")
        users = []
        userpass = {}
        with open('user_login.txt','r') as file:
            data = file.readlines()
            for i in data:
                da = i.split(',')
                ps = da[1].replace('\n','')
                userpass[da[0]] = ps
                users.append(da[0])

        if username in users:
            pwd = input("Enter your password: ")
            if pwd == userpass[username]:
                print(f"WELCOME user {username} you LOGGED IN SUCCESSFUL!!!")
                login_status = username
                with open('user_details.txt','r') as file:
                    data = file.readlines()
                
                for i in data:
                    da = i.split(',')
                    if username == da[3].strip():
                        login_user = da[0]
                after_login()
            else:
                print(f"Hello {username} you entered wrong password please do login again")
                login()
        else:
            print("PLEASE ENTER CORRECT USERNAME OR FIRST REGISTER YOURSELF!!!")
            login()
    elif ch == '2':
        register()
    else:
        print("PLEASE CHOOSE CORRECT OPTION")
        login()

def after_login():
    ch = input("Select option for process\n 1. Attempt Quiz \n 2. Show Result\n 3. See Profile\n 4. exit\n Enter your choice: ")
    if ch == '1':
        attempt_quiz()
    elif ch == '2':
        show_result()
    elif ch == '3':
        show_profile()
    elif ch == '4':
        exit_()
    else:
        print("SELECT CORRECT OPTION")
        after_login()

def attempt_quiz():
    global login_user
    global quiz_topic

    print(f"Hello {login_user.upper()} Welcome in Quiz. GOOD LUCK!")
    print("#"*20)
    print()
    quiz_choice = input("Please select an category to attempt quiz: \n 1. Python\n 2. Java\n 3. C/C++\n Enter your option: ")
    if quiz_choice == '1':
        quiz_topic = "PYTHON"
        python_quiz()
    elif quiz_choice == '2':
        quiz_topic = "JAVA"
        pass
    elif quiz_choice == '3':
        quiz_topic = "C/C++"
        pass
    else:
        print("Please Choose correct quiz option: ")
        attempt_quiz()

def python_quiz():
    global quiz_topic
    global login_user
    global marks
    print(f"Hello {login_user} welcome in {quiz_topic} quiz")
    print()

    with open('python_quiz.txt','r') as file:
        data = file.readlines()
        que = random.sample(data,5)
        # print(que)
        q = 1
    
    for i in range(len(que)):
        da = que[i].split(',')
        # print(da)
        print(f"Que.{q}: {da[0]}")
        print(f" A. {da[1]}\n B. {da[2]}\n C. {da[3]}\n D. {da[4]}")
        ans = input("Enter your answer option A/B/C/D: ").lower()
        print()
        res = da[-1].replace("\n",'')
        if ans == res:
            marks += 1
        q += 1

    percentage = (marks/5)*100
    da = datetime.now()
    quiz_time = da.strftime("%d/%m/%Y %H:%M %p")
    
    final_result = f"{login_user},{quiz_topic},{percentage},{quiz_time}"

    with open('quiz_results.txt', 'a') as file:
        file.write(final_result)
        file.write('\n')

    print(f"Hello {login_user} Thanks for attempt MCQ Quiz You obtain {marks} marks out of 5")
    print(f"{'#'*10} CORRECT ANSWERS: {'#'*10}")

    s = 1
    for i in range(len(que)):
        da = que[i].split(',')
        ans = ''
        an = da[-1].replace("\n",'')
        if an == 'a':
            ans = da[1]
        elif an == 'b':
            ans = da[2]
        elif an == 'c':
            ans = da[3]
        elif an == 'd':
            ans = da[4]
        else:
            ans = ans
        print(f"Que.{s}: {da[0]}, ANS: {ans}")
        s += 1

def show_result():
    print("Show result")

def show_profile():
    pass

def exit_():
    global login_status
    ch = input("IF you want to access quiz again press n, or if you want to close the quiz press y: ").lower()
    if ch == 'n' or ch == 'no':
        main()
    else:
        print("THANKS TO VISIT OUR QUIZ, PLEASE VISIT AGAIN!!!")
        login_status = False
        exit()

if __name__ == "__main__":
    main()
