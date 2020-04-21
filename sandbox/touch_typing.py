import random

# chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{};'\":<>/,./?\\|")
chars = list("uiop()90[]{};'<>?,./\"-=_+:\"")


res = []
for i in range(100):
	res.append("".join(chars[:]))
	random.shuffle(chars)

[print(i*5) for x in res for i in x]



