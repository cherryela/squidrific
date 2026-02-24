'''
bool_dict = {"T" : True,
    "F" : False,
    "t" : True,
    "f" : False
   }


def haltstates(h,a,l,t):
    state = sum([h,a,l,t])
    return(state)

# collect user inputs
hungry = bool_dict[input("Are you hungry? T/F \n")] 
angry = bool_dict[input("Are you angry? T/F \n")]
lonely = bool_dict[input("Are you lonely? T/F \n")]
tired = bool_dict[input("Are you tired? T/F \n")]


# Create the result, which calls the halstates function to 
# put the user's answers into a list and then sums them.

result = haltstates(hungry,angry,lonely,tired)

def answer(result):
    if result == 0:
        print("You're doing great!")
    elif result <= 2:
        print("Hmmm...")
    else:
        print("Go do some self care, sweetheart!")
    return(result)

answer(result)

'''

bool_dict = {"T": True, "F": False, "t": True, "f": False} 
# Create a dictionary to map the short answers to the full boolean

questions = ["Are you hungry?", "Are you angry?", "Are you lonely?", "Are you tired?"] # A list of the questions
answers = [] # Define an empty list to put the user input answers into

'''
for question in questions: # Create a for loop to iterate through the questions, 
# collecting user input at each step
    user_input = input(f"{question} Enter T/F: ")
    answers.append(bool_dict[user_input]) # Use the append func to add inputs to answers list
'''

# Add error handling. AI helped.
for question in questions:
    while True: # This is a simple loop statement. 
    #It tells python to keep looping forever, because true is always true.
        user_input = input(f"{question} Enter T/F: \n")
        if user_input in bool_dict:
            answers.append(bool_dict[user_input])
            break 
            # break exits the nested while loop, and the code will 
            # go back to the for loop and iterate to the next question
        else:
            print("Invalid input. Please enter T or F.")



def answer(result): # Define a function that gives a "result" based on a list of answers
    if sum(result) == 0:
        print("You're doing great!")
    elif sum(result) <= 2:
        print("Hmmm... Can you address what's bothering you?")
    else:
        print("Go do some self care, sweetheart!")
    return(result)

answer(answers) # Prints the answer statement based on the sum of the results.
    

