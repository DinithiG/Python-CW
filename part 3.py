# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.

# Student ID: W1867585

# Date: 07/12/2021

#cw-test

def staff (): #function for staff version
    process = True  #boolean value for while loop
    total_progress = 0
    total_trailing = 0
    total_module_retriever = 0
    total_exclude =0
    scores = [] #starting a list called scores to append input later on
    while process: #process's value is assigned as True
        try:
            PASS = int(input('Enter your number of credits at pass:')) # not in range 
            if PASS not in range(0,130,20):
                out_of_range_PASS = print('Out of range.Try again!') #from 0 to 120,+20 steps (130 not included according to range)
                continue
            DEFER = int(input('Enter your number of credits at defer:')) # everything should be within 0-120 marks category
            if DEFER not in range(0,130,20):
                out_of_range_DEFER = print('Out of range.Try again!')
                continue
            FAIL = int(input('Enter your number of credits at fail:'))
            if FAIL not in range(0,130,20):
                out_of_range_FAIL = print('Out of range.Try again!')
                continue
            total = PASS + DEFER + FAIL
            if total != 120 : #if total != 120 gives an error
                total_incorrect = print('Total Incorrect. Try again!')
                continue #go to the begininng

            if PASS == 120: #if progress == 120,one and only result for progress
                    result_print = print('progression outcome:Progress')
                    result = 'Progress'
                    total_progress = total_progress + 1
            elif PASS == 100: # PASS == 100 for all Progress - module trailer
                    result_print = print('progression outcome:Progress (module trailer)')
                    result = 'Progress (module trailer)'
                    total_trailing = total_trailing + 1
            elif FAIL>= 80: #when it comes to all exclude results FAIL is more than or equals to 80
                    result_print = print('progression outcome:Exclude')
                    result = 'Exclude'
                    total_exclude = total_exclude + 1
            else: #everything else falls into the Do not progress - module retriever category
                    result_print = print('progression outcome:Do not progress – module retriever')
                    result = 'Module retriever'
                    total_module_retriever = total_module_retriever + 1

        
            PASS = str(PASS) # converting an int value to a string
            PASS_2 = ' - ' + PASS + ' , ' #string concatenation
            DEFER = str(DEFER) # converting an int value to a string
            DEFER_2 =  DEFER + ' , ' #string concatenation
            FAIL = str(FAIL) # converting an int value to a string
            FAIL_2 =  FAIL 
            list_add = result + PASS_2 + DEFER_2 + FAIL_2 #list_add is a string consists of all PASS,DEFER and FAIL data as a one single string
            scores.append(list_add) #appending list_add string to scores list
            
            choice = input("Would you like to enter another set of data?Enter 'y' to continue or 'q' to quit:").lower() #lower() just in case if user enters a capital letter
            
            if choice == 'y' :
                process = True #loop continues 

            elif choice =='q':
                
                print('---------------------------------------------------------------')  #stars multiplication to display the horizontal histogram
                print('Horizontal Histogram')
                print('Progress ',total_progress,':', '*' * total_progress)
                print('Trailer  ', total_trailing,':' ,'*' * total_trailing)
                print('Retriever',total_module_retriever,':','*' * total_module_retriever)
                print('Excluded ',total_exclude, ':','*'*total_exclude)

                print( total_progress + total_trailing + total_module_retriever + total_exclude ,'outcomes in total')
                print('----------------------------------------------------------------') # referred a code from a website and the lecture note about string  formatting
                print('Vertical Histogram') #https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops#:~:text=You%20can%20use,Improve%20this%20answer
                
                header = ['Progress',str(total_progress),'|', 'Trailing',str(total_trailing),'|', 'Retriever',str(total_module_retriever),'|', ' Excluded',str(total_exclude)]
                print(' '.join(header)) # using str function because of the sequence
                for x in range(max(total_progress, total_trailing,total_module_retriever,total_exclude)):
                    print("    {0}           {1}              {2}              {3}".format(
                    '*' if x < total_progress else ' ',
                    '*' if x < total_trailing else ' ',
                    '*' if x < total_module_retriever else ' ',
                    '*' if x < total_exclude else ' '
                    ))
                print( total_progress + total_trailing + total_module_retriever + total_exclude ,'outcomes in total')
                print('----------------------------------------------------------------')

                
                
                for i in scores : #for all content in the list scores printing them
                        print(i)

                process = False # loop breaks
    
            else:
                error_message = print('Wrong input entered') #if user enterd something else besides y and q
                continue #go to the beginning
            
        except ValueError : #works if user didn't enter an integer value for PASS,DEFER or FAIL
                value_error = print('Integer required!Enter again!')
                continue
                  
            
def students(): #function for students
    process = True  #boolean value for while loop
    total_progress = 0
    total_trailing = 0
    total_module_retriever = 0
    total_exclude =0
    while process:
        try:
         PASS = int(input('Enter your number of credits at pass:')) # not in range 
         if PASS not in range(0,130,20):
             out_of_range_PASS = print('Out of range') #from 0 to 120,+20 steps (130 not included according to range)
             continue
         DEFER = int(input('Enter your number of credits at defer:')) # everything should be within 0-120 marks category
         if DEFER not in range(0,130,20):
             out_of_range_DEFER = print('Out of range')
             continue
         FAIL = int(input('Enter your number of credits at fail:'))
         if FAIL not in range(0,130,20):
             out_of_range_FAIL = print('Out of range')
             continue
         total = PASS + DEFER + FAIL
         if total != 120 :
             total_incorrect = print('Total Incorrect')
             continue
        except ValueError :
            value_error = print('Integer required!') #works if user didn't enter an integer value
            continue
        
        if PASS == 120: #if progress == 120,one and only result for progress
         progress_result = print('progression outcome:progress')
         break #breaks the student version
        elif PASS == 100: # PASS == 100 for all Progress - module trailer
         progress_result = print('progression outcome:progress (module trailer)')
         break
        elif FAIL>= 80: #when it comes to all exclude results FAIL is more than or equals to 80
         exclude_result = print('progression outcome:exclude')
         break
        else:  #everything else falls into the Do not progress - module retriever category
         module_retriever_result = print('progression outcome:do not progress – module retriever')
         break
        
    

print('''
options: 
1 - staff version
2 - student version
''')
role = input('Enter the number of your option:') #staff and student options
if role == '1' :  #input function converts inputs to strings
    staff() #calls the staff function
elif role == '2':
    students() #calls the students function
else: #just in case if user inputs a wrong option in the beginning 
    wrong_option = print('Wrong option entered!') #have to restart the program if a wrong option is entered
   
