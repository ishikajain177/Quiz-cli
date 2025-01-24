import os
import time

def load_questions(file_name):
    questions = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 7:  # Ensure all parts are present
                    question = {
                        "number": parts[0],
                        "question": parts[1],
                        "options": parts[2:6],
                        "answer": parts[6]
                    }
                    questions.append(question)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return questions

def playQuiz(questions):
    os.system("clear")
    score=0
    for question in questions:
        os.system("clear") 
        print(f"\n{question['number']}. {question['question']}")
        for option in question['options']:
            print(option)       

        usr_ans=input("enter your answer or press 0 to quit:: ").lower()
        if usr_ans!='0':
            if usr_ans==question['answer']:
                print("\nCORRECT ANSWER")
                score+=10
            else:
                print("\nWRONG ANSWER")
                print(f"The correct answer is {question['answer']}")
            print(f"\nYour score:: {score}")
            time.sleep(1)
        else:
            print("\nYou decided to quit")
            return score
    print("\nHURRAY!! You complete the game")
    return score
        

def main():
    while(1):
        os.system("clear")
        questions=[]
        print("WELCOME TO THE QUIZ")
        print("1. General Knowlege")
        print("2. Indian Sports")
        print("3. Business Enthusiast")
        print("4. Nonsense questions")
        print("5. Exit")
        choice=int(input("Select a genre to play that quiz(1-5):: "))
        if choice in [1,2,3,4]:
            match choice:
                case 1: questions=load_questions("python/projects/generalknowledge.txt")
                case 2: questions=load_questions("python/projects/indiansports.txt")
                case 3: questions=load_questions("python/projects/business.txt")
                case 4: questions=load_questions("python/projects/nonsense.txt")

            score=playQuiz(questions)
            print(f"\nTotal Score {score} points")
            time.sleep(2)
        else: exit(0)
        
if __name__ == "__main__":
    main()