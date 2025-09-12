temp = eval(input(" Enter Temperature --> "))

if temp <= 1:
	print("the temperature outside is freezing cold ")

elif temp >= 1 and temp <= 20:
	print("the temperature outside is cold ")

elif temp >= 21 and temp <= 30:
	print("the temperature outside is lukewarm ")

elif temp >=31 and temp <= 40:
	print("the temperature outside is warm ")

elif temp >= 41 and temp <= 50:
	print("the temperature outside is hot ")

elif temp >= 50:
	print("the temperature outside is boiling hot ")

else:
	print("invalid temperature")
