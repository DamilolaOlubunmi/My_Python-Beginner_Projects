Question_Bank = {
    "Which python lecturer gave the quiz assignment?": {
        "options": ["A. Mr. Odusote", "B. Mr. Dami", "C. Ms. TiJesu", "D. Ms. Nathaniel"],
        "answer": "B"
    },
    "Who is Nigeria's president?": {
        "options": ["A. Goodluck Jonathan", "B. Abubakar Balewa", "C. Damilola Olubunmi", "D. Bola Tinubu"],
        "answer": "D"
    },
    "How old is the chancellor of Covenant University?": {
        "options": ["A. 60", "B. 61", "C. 70", "D. 71"],
        "answer": "C"
    },
    "Who was Jesus favourite disciple?": {
        "options": ["A. Doubting Thomas", "B. John, the beloved", "C. Saul turned Paul", "D. Judas the betrayer"],
        "answer": "B"
    },

}

score = 0
for question, quizdata in Question_Bank.items():
    print("\n" + question)
    for option in quizdata["options"]:
        print(option)
    response = input("Your answer: ").strip().upper()
    if response == quizdata["answer"]:
        print("That's correct!!!!!!!")
        score += 20
    else:
        print(f"Incorrect answer!, the correct answer was {quizdata["answer"]}")

print(f"Your final score is {score} out of {len(Question_Bank) * 20}")

