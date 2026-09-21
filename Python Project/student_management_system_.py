def x(): 
    print('='*100) 

x() 
print('\t\t\t\t\tlogin system'.upper()) 
x() 

username='' 
password='' 

while username!='admin'or password!='python123': 
    username=input('enter username:').lower() 
    password=input('enter your password:').lower() 

    if username!='admin'or password!='python123': 
        print('your password or username is incorrect') 

print('login successful') 


while True: 
    x() 
    print('\t\t\t\t\t\tstudent management system'.upper()) 
    x() 

    print('1. Student Report Card') 
    print('2. Quiz Competition') 
    print('3. Student Attendance') 
    print('4. Election Voting') 
    print('5. Calculator') 
    print('6. Exit') 

    user_choice = input('enter your choice(1|2|3|4|5|6): ').strip() 

    if user_choice == '1': 
        print("\n--> Opening Student Report Card...\n") 

        student_list=[] 

        print() 
        print('\t---record manager---'.upper()) 
        print('-'*50) 

        num=int(input('how many student:')) 
        print() 

        for i in range(num): 
            name=(input('enter your name:')) 
            mark=int(input('enter your mark:')) 

            print('-'*20) 

            student_detials={'name':name,'mark': mark} 
            student_list.append(student_detials) 

        print() 
        print('\t---generating output---'.upper()) 

        for i in student_list: 
            print(f"name : {i['name']}") 
            print(f"mark : {i['mark']}") 

            # FIXED GRADE CONDITIONS
            if i['mark'] >=90: 
                print('grade A+') 
            elif i['mark'] >=80: 
                print('grade A') 
            elif i['mark'] >=70: 
                print('grade B') 
            elif i['mark'] >=60: 
                print('grade C') 
            elif i['mark'] >=50: 
                print('grade D') 
            else: 
                print('grade F') 

            if i['mark'] >=50: 
                print('pass') 
            else: 
                print('fail') 

        x() 


    elif user_choice == '2': 
        print("\n--> Opening Quiz Competition...\n") 

        name=input('enter participant name : ') 
        print('*'*35) 

        correct_answer=0 
        incorrect_answer=0 

        for i in range(1,6): 
            print(f"\nquestion {i}") 

            if i==1: 
                print('who developed the python programming language?') 
                answer= input('enter your answer: ') 

                if answer.lower()=='guido van rossum': 
                    print('correct!👌') 
                    correct_answer+=1 
                else: 
                    print('incorrect❌') 
                    incorrect_answer+=1 

            elif i==2: 
                print(' which keyword is used to create a function in python?') 
                answer=input('enter your answer: ') 

                if answer.lower()=='def': 
                    print('correct!👌') 
                    correct_answer+=1 
                else: 
                    print('incorrect❌') 
                    incorrect_answer+=1 

            elif i==3: 
                print('what is the output of the print(10==10)?') 
                answer=input('enter your answer: ') 

                if answer.lower()=='true': 
                    print('correct!👌') 
                    correct_answer+=1 
                else: 
                    print('incorrect❌') 
                    incorrect_answer+=1 

            elif i==4: 
                print('what is the output of print("python"*2)?') 
                answer=input('enter your answer: ') 

                if answer.lower()=='pythonpython': 
                    print('correct!👌') 
                    correct_answer+=1 
                else: 
                    print('incorrect❌') 
                    incorrect_answer+=1 

            elif i==5: 
                print('what is the output of print(10//3)') 
                answer=input('enter your answer: ') 

                if answer.lower()=='3': 
                    print('correct!👌') 
                    correct_answer+=1 
                else: 
                    print('incorrect❌') 
                    incorrect_answer+=1 

        percentage=(correct_answer/5*100) 

        if percentage >=90: 
            remark='excellent' 
            result='pass' 
        elif percentage >=80: 
            remark='very good👌' 
            result='pass' 
        elif percentage>=70: 
            result='pass' 
            remark='good👍' 
        elif percentage >=50: 
            remark='average😊' 
            result='pass' 
        else: 
            remark='need practice📚' 
            result='fail' 

        x() 
        print('\t\t\t\tfinal result'.upper()) 
        x() 

        print() 
        print(f'participant     :{name}') 
        print(f'correct answer  :{correct_answer}') 
        print(f'wrong answer    :{incorrect_answer}') 
        print(f'percentage      :{percentage}') 
        print(f'result          :{result}')   
        print(f'remark          :{remark}') 

        x() 


    elif user_choice == '3': 
        print("\n--> Student Attendance...\n") 
        print() 

        teacher_name=input('enter teachers name:') 
        class_name=input('enter class name   :') 
        no_of_student=int(input('how many students? :')) 

        print() 

        present_student=0 
        absent_student=0 

        for i in range(1,no_of_student+1): 
            print(f'\nstudent {i}') 

            student_name=input('\nenter student name     :') 
            attendance=input('enter attendance (P/A) :') 

            if attendance.lower()=='p': 
                print(f'{student_name} marked as present.') 
                present_student+=1 

            # FIXED: only A is absent
            elif attendance.lower()=='a':
                print(f'{student_name} marked as absent.') 
                absent_student+=1 

            else:
                print('invalid attendance. please enter P or A.')
                # Don't count invalid input


        # FIXED: prevent division by zero
        if no_of_student != 0:
            attendance_percentage=present_student/no_of_student*100 
        else:
            attendance_percentage=0

        x() 
        print('\t\t\t\t\tfinal attendance report'.upper()) 
        x() 

        print() 
        print(f'teacher         :{teacher_name}') 
        print(f'class           :{class_name}') 
        print(f'total student   :{no_of_student}') 
        print(f'present student :{present_student}') 
        print(f'absent student  :{absent_student}') 
        print(f'attendance rate :{attendance_percentage}%') 

        print('_'*100) 
        x() 


    elif user_choice == '4': 
        print("\n--> Opening Election Voting...\n") 
        print() 

        print('candidates:') 
        print() 

        print('\t1. srinithi') 
        print('\t2. akhilan') 
        print('\t3. mani') 

        print() 

        no_of_voters=int(input('how many voters? :')) 
        print() 

        srinithi=0 
        akhilan=0 
        mani=0 

        print('-'*100) 

        for i in range(1,no_of_voters+1): 
            print(f'\nstudent {i}') 

            vote=input('enter vote (1/2/3) :') 

            if vote=='1': 
                print(f'vote recorded successfully👍') 
                srinithi+=1 

            elif vote=='2': 
                print(f'vote recorded successfully👍') 
                akhilan+=1 

            elif vote=='3': 
                print(f'vote recorded successfully👍') 
                mani+=1 

            else: 
                # FIXED MESSAGE
                print('invalid vote.') 

        if srinithi > akhilan and srinithi > mani: 
            result='srinithi' 

        elif akhilan > srinithi and akhilan > mani: 
            result='akhilan' 

        elif mani > srinithi and mani > akhilan: 
            result='mani' 

        else: 
            result='tie (no single winner)' 

        print() 

        x() 
        print("FINAL RESULT") 
        x() 

        print("Srinithi :", srinithi) 
        print("Akhilan  :", akhilan) 
        print("Mani     :", mani) 
        print("Winner   :", result) 

        x() 


    elif user_choice == '5': 
        print("\n--> Opening Calculator...\n") 

        num_1=int(input('enter a number:')) 
        num_2=int(input('enter a number:')) 
        operator=input('enter an operator(+,-,*,/):') 

        print('-'*100) 

        if operator=='+': 
            output=(num_1+num_2) 

        elif operator=='-': 
            output=(num_1-num_2) 

        elif operator=='*': 
            output=(num_1*num_2) 

        elif operator == "/": 

            # FIXED: division by zero
            if num_2 != 0:
                output=(num_1/num_2) 
            else:
                print('cannot divide by zero.')
                output=None

        # FIXED: invalid operator
        else:
            print('invalid operator.')
            output=None


        # Only print result if calculation was successful
        if output is not None:

            print(f'{num_1} {operator} {num_2} = {output}') 

            if output>0: 
                print('result is positive.') 

            elif output<0: 
                print('result is negative.') 

            # FIXED: handle zero
            else:
                print('result is zero.')

        print('='*100) 
        x() 


    elif user_choice == '6': 
        print("\nExiting program. Goodbye!") 
        break 


    else: 
        print("\n[!] Invalid choice. Please enter a number between 1 and 6.\n") 
        x()
