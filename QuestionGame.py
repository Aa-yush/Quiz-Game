import requests
import json
import pprint
import html
import random

url = "https://opentdb.com/api.php?amount=1"
endGame = ""
score_correct = 0
score_incorrect = 0

while endGame.lower() != "q":
    r = requests.get(url)
    if (r.status_code != 200):
        endGame = input("Sorry ,there is a problem for retriving the questions. For try again press enter or press 'q' to quit..")
    else:
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answers = data['results'][0]['correct_answer']

        answers.append(correct_answers)
        random.shuffle(answers)                    #We shuffle answers because when we append correct answer is always placed at last


        print("\n Question - "+html.unescape(question)+"\n")
        
        for ans in answers:
            print(answer_number," - "+html.unescape(ans))
            answer_number+=1


        user_answer = input("\nEnter the number of your answer : ")

        if(answers[int(user_answer)-1]==correct_answers):
             print("Congrats !! your answer was correct - ",html.unescape(correct_answers),"\n")
             score_correct += 1
        else:
            print("your answer is incorrect. The Correct answer is - ",html.unescape(correct_answers),"\n")
            score_incorrect += 1

        print("-------------------------------")
        print("Your Score : ")
        print("Correct answer : ",score_correct)
        print("Incorrect answer : ",score_incorrect)
        print("Accuracy : ",(score_correct/(score_correct+score_incorrect))*100,"%")

        print("-------------------------------\n")

        endGame = input("Press Enter to play or 'q' to quit the game .. ")

print("\nThank you for playing game .. ")
    
            
                 
        
       
            


        
