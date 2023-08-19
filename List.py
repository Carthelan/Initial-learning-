#All Questions
question1 = "Q1. What is the vlue of the expression: 2*3-4?" \
    "\n(a)1"\
    "\n(b)2"\
    "\n(c)3"\
    "\n(d)None"\
    
question2 = "Q2. What is the vlue of the expression: 1+(2*3)/4?" \
    "\n(a)1.5"\
    "\n(b)3"\
    "\n(c)3.5"\
    "\n(d)None"\
    
question3 = "Q3. The set data type can hold duplicate values." \
    "\n(a)False"\
    "\n(b)True"\
    "\n(c)Partially Correct"\
    "\n(d)None"\
    
question_bank = {question1: "b", question2: "c", question3: "a"}
score = 0
for key in question_bank:
    print(key)
    user_input = input("Type your answer(a/b/c/d):")
    if user_input == question_bank[key]:
        score += 1
score_percent = 100 * (score / len(question_bank))

print(f"You scored a {score_percent} %")