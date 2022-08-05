# write your code here
import math
temp = 0
is_running_first_time = True
M = 0
while True:
    try:
        equation = input("Enter an equation").split()
        operator_used = ''
        integers = []
        operators = ["+", "-", "*", "/"]
        msg = ""
        for i in equation:
            if i in operators:
                operator_used += i
            else:
                if i == 'M':
                    integers.append(float(M))
                else:
                    integers.append(float(i))
        is_all_one_digit = True
        for i in range(len(integers)):

             if integers[i].is_integer():
                 i = int(integers[i])
                 if i == 1 and operator_used == '*':
                     msg += " ... very lazy"
                 elif i == 0 and operator_used in '+-*':
                     msg += " ... very, very lazy"
                 if not (i < 10 and i > -10):
                     is_all_one_digit = False
             else:
                 is_all_one_digit = False
        if is_all_one_digit:
            msg = " ... lazy" + msg
                    
        if msg != "":
            msg = "You are" + msg
            print(msg)
        a = 0 
        for j in range(len(integers)-1):
            if operator_used == '+':
                a = integers[j] + integers[j+1]
            elif operator_used == '-':
                a = integers[j] - integers[j+1]
            elif operator_used == '*':
                a = integers[j] * integers[j+1]    
            elif operator_used == '/':
                a = integers[j] / integers[j+1]
        print(a)
        msg_10 = "Are you sure? It is only one digit! (y / n)"
        msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
        msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
        store_result = input("Do you want to store the result? (y / n):")
        temp_2 = True
        if store_result == 'y':
            if a.is_integer():
                   num = math.floor(a)
                   if num < 10 and num > -10:
                       msg_index = 10
                       while msg_index < 13:
                           print(globals()[f'msg_{msg_index}'])
                           ans = input()
                           if ans == 'y':
                               msg_index += 1
                               
                           elif ans == 'n':
                               temp_2 = False
                               break
            if temp_2:
                M = a
        
        cont_calc = input("Do you want to continue calculations? (y / n):")
        if cont_calc == 'n':
                quit()
    except ValueError:
        if temp == 0:
            print("Do you even know what numbers are? Stay focused!")
            temp = 1
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
            temp = 0
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
        temp = 0


    




        
            
            
            
    
