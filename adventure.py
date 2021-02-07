import sys
name = str(input("What is your name?  "))
print("Good afternoon, "+name)
ask = str(input("Do you want to play this game:(y/n)"))
if ask == "y":
    print("Let's get started then")
    print("So you girlfriend or boyfirend just broke up with you. ")
    print("You have been crying all day, when your mom tells you to go to a therapist.")
else:
    exit()
go = str(input("Do go to the therapist: (y/n)"))
if go == "y":
    print("You went to the therapist")
    print("Now you are finally over your ex.")
elif go == "n":
    print("Since you didn't go to the therapist, you became more depressed day by day, and you killed yourself")
    exit()
print("However, just when you are begging to be happy and social agian, your ex says let's get back")
back = str(input("Do you go back: (y/n)"))
if back == "y":
    print("You got back with your ex, and are now happy togther")
    print("Your ex cheats on you, and now you are more angry than ever")
    print("So you decide to kill yourself")
    exit()
elif back == "n":
    print("Now you bestfriend, says you should date someone")
new = str(input("Do start dating again: (y/n)"))
if new == "y":
    print("The person you are dating is very lovable, and you have a great relationship")
    exit()
elif new == "n":
    print("Now you are just bored, and decide to go on a hike")
    print("However, while you were hiking, you slipped and died")
    exit()
