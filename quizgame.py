questions = [
    {
        "prompt": "what is the captial of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "which lnguage is primarily spoken in brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "what is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
        "answer": "B"
    },
    {
        "prompt": "who wrote 'To kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
]


def run_quiz (questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer: ").upper()
        if answer == question["answer"]:
            print("Correct\n")
            score += 1
        else :
            print("Wrong, The correct ans was", question["answer"],"\n")

    print(f" You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)


            