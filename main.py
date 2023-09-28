import json
import random
#------------------------------
def new_game():
    questions = quiz_data()
    random.shuffle(questions)
    list_of_questions = []
    list_of_answers = []
    correct_answer = 0
    question_num = 1

    index = 1
    for i in range(len(questions[0: 5])):
        index_question = questions[i]
        list_of_questions.append(index_question["answer"])
        print("---------------------------")
        print("{}. ".format(i) + index_question["question"],)
        print("     A. "+ index_question["A"])
        print("     B. "+ index_question["B"])
        print("     C. " + index_question["C"])
        print("     D. " + index_question["D"])

        selection = False
        while(selection == False):
            choice = input("Enter (A,B,C, or D): ")
            choice = choice.upper()
            if(choice == 'A' or choice == 'B' or choice == 'C' or choice == 'D'):
                selection = True
            else:
                print("Please choose only (A,B,C, or D) ")
                selection = False

        

        list_of_answers.append(choice)

        correct_answer += check_answer(questions[i]["answer"], choice)

        question_num += 1
        index+=1

    display_score(correct_answer, list_of_answers, list_of_questions)

#------------------------------
def check_answer(answer, choice):
    if(answer == choice):
        print("CORRECT!")
        return 1
    print("INCORRECT")

    return 0
#------------------------------
def display_score(correct_answers, answers, questions):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")

    print("Correct Answers: ", end="")
    for i in range(len(questions)):
        print(questions[i], end=" ")
    print()

    print("Answers: ", end="")
    for i in range(len(answers)):
        print(answers[i], end=" ")
    print()

    score = int((correct_answers/len(questions)) * 100)
    print("\nYour score is: " + str(score) + "%")

#------------------------------
def play_again():
   response = input("Do you want to play again? (yes or no): ")
   response = response.upper()

   if(response == "YES" or response == 'Y'):
       return True
   return False
#------------------------------

def quiz_data():
# Opening JSON file
    quiz_list = None
    with open('QuizGame\\data.json', 'rb') as json_file:
        quiz_list = json.load(json_file)
    return quiz_list
    

new_game()

while play_again():
    new_game()

print("\nThanks for playing! \nByeeeeeeeeeeeeeeeeeeeeeeeee!!!!!!")