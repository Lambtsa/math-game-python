import datetime
import random

from questions import Add, Multiply

def log_time():
    now = datetime.datetime.now()
    return now.strftime('%H:%M:%S')

def calculate_elapsed_time(start, end):
    start_time = datetime.datetime.strptime(start, '%H:%M:%S')
    end_time = datetime.datetime.strptime(end, '%H:%M:%S')
    return end_time - start_time

class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # Generate 10 random questions with numbers from 1 to 10
        for i in range(1, 11):
            num = random.randint(1,2)
            random_number_1 = random.randint(1, 10)
            random_number_2 = random.randint(1, 10)
            if num == 1:
                question = Add(random_number_1, random_number_2)
            else:
                question = Multiply(random_number_1, random_number_2)
        # Add these questions to self.questions
            self.questions.append(question)
    
    def __str__(self) -> str:
        questions = []
        for question in self.questions:
            questions.append(f'* {question.answer}')
        return "\n".join(questions)

    def take_quiz(self):
        # Log the start time
        start_time = log_time()
        print(f"You have started the quiz at {start_time}")
        # ask all of the questions
        for question in self.questions:
            answer = self.ask(question)
            if answer:
                # log if they got the questions right
                self.answers.append(True)
            else: 
                self.answers.append(False)
        # log the end time
        end_time = log_time()
        time_elapsed = calculate_elapsed_time(start_time, end_time)
        # show the summary
        self.summary(time_elapsed)

    def ask(self, question):
        # log the start time
        start_time = log_time()
        # capture the answer
        answer = input(f'What is {question}?  ')
        # log the end time
        end_time = log_time()
        # check the answer 
        if int(answer) == question.answer:
            # if the answers right return True
            return True
        else: 
            # otherwise return False 
            return False
        # send back elapsed time

    def summary(self, time_elapsed):
        total_number_questions = len(self.questions)
        total_correct = self.answers.count(True)
        # print the total time for the quiz: 30 seconds.
        print(f"You completed this test in {time_elapsed} seconds")
        # print how many you got right and the total # of questions. 5/10
        if total_correct >= (total_number_questions / 2):
            print(f"Congratulations! You got {total_correct} questions right out of a possible {total_number_questions}!")
        elif total_correct == 0:
            print(f"Oh no!!! You really need to brush up on your maths!!")
        else:
            print(f"Oups! You only got {total_correct} questions correct out of a possible {total_number_questions}")


new_quiz = Quiz()
new_quiz.take_quiz()