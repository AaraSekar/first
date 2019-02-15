w=input()
if w.isalpha():
	xa=w.lower()
	if xa=='a' or xa=='e' or xa=='i' or xa=='o' or xa=='u':
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
