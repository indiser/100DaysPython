questions=[
    {"text": "Python is a compiled language.", "answer": "False"},
    {"text": "The capital of France is Paris.", "answer": "True"},
    {"text": "A list in Python is immutable.", "answer": "False"},
    {"text": "HTML stands for HyperText Markup Language.", "answer": "True"},
    {"text": "The Earth is flat.", "answer": "False"},
    {"text": "Python was created by Guido van Rossum.", "answer": "True"},
    {"text": "1 + 1 equals 3.", "answer": "False"},
    {"text": "Water boils at 100 degrees Celsius at sea level.", "answer": "True"},
    {"text": "There are 12 months in a year.", "answer": "True"},
    {"text": "The sun revolves around the Earth.", "answer": "False"}
]

score=0
while True:
    for i in range(len(questions)):
        ans=input(f"Q{i+1}. {questions[i]["text"]} (True/False)?\n").lower()
        if ans==questions[i]["answer"].lower():
            print("Correct")
            score+=1
        else:
            print("Wrong answer")
            score+=0
    break

print(f"Your final score is:{score}/{len(questions)}")