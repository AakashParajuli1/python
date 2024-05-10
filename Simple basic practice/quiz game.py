questions = ("1. What is the largest animal on earth?",
             "2. Who was the first person to land on the moon?",
             "3. Which is the largest planet in our solar system?",
             "4. Winner of world cup football 2023 is?",
             "5. The largest country by land mass is?")


options = (("A.Kangaroo ", "B.Elephant", "C.Blue whale", "D. Ostrich "),
           ("A.Neil Armstrong ", "B. Edmund Hillary", "C. Bill Clinton", "D. George w. bush "),
           ("A. Venus ", "B. Pluto", "C. Moon", "D. Jupiter"),
           ("A. Brazil ", "B. Argentina", "C. America", "D. Spain"),
           ("A. Russia", "B. China", "C. India", "D. America"))

answers = ("C", "A", "D", "B", "A")

guesses = []
score = 0

question_no = 0

for question in questions:
    print("--------------------------------------------------------------")
    print(question)

    for option in options[question_no]:
        print(option)

    guess = input("Enter (A, B, C, D) :").upper()
    guesses.append(guess)
    if guess == answers[question_no]:
        score += 1
        print("Correct!!!")
    else:
        print("Incorrect!!")
        print(f"The correct answer is : {answers[question_no]}")
    question_no += 1

print("--------------------------------------------------------------")
print("                                RESULTS                              ")
print("--------------------------------------------------------------")

print("answers:", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is : {score} %")
