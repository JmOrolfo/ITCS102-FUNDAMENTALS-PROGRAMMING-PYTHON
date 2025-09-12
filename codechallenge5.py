#Manga and Anime Recommendation 
#Manga or Anime 
#Genre
#Short, Medium, Long
#2000, 2010, 2020
#Ongoing/New
#Finished

print("Welcome to Manga// Anime Recommendation")
am = input("What are you looking for ? (anime or manga) -> ")

if am.lower() == "manga":
	g = input("What genre do you like? (shonen, harem, isekai,) -> ")
	c = eval(input("Which Decade? (2000, 2010, 2020) -> "))
	l = input("How long should this manga be? (short, medium, long) -> ")
	print("Here are the recommended" ,l ,g, am, "from" ,c)
 