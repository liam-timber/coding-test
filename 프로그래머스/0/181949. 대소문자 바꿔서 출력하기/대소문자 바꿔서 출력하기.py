str = input()
answer = ""
for alphabet in str:
	if alphabet.islower():
		answer += alphabet.upper()
	else :
		answer += alphabet.lower()
print(answer)
