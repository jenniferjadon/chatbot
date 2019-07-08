import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)
question = ['How are you?']
responses = [" Im fine thanks for asking"]
random_response = random.choice(responses)
que1=["how are you doing?"]
res1=["Iam doing good...Are you free now?"]
random_res1=random.choice(res1)
que2=["yes iam"]
res2=["Can you teach me some apptitude problems now?"]
random_res2=random.choice(res2)
que3=["yes..."]
res3=["ok i will call u, bye!"]
random_res3=random.choice(res3)
que4=["bye"]
res4=["c u later"]
random_res4=random.choice(res4)
while True:
	userInput = input(">>> ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)
	elif userInput in que1:
	    print(random_res1)
	elif userInput in que2:
	    print(random_res2)
	elif userInput in que3:
	    print(random_res3)
	elif userInput in que4:
	    print(random_res4)
	else:
	    print("I did not understand what you said")
