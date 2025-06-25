TrainingSession = int(input("How long is your training session in minutes? "))
Song_Duration = []
Total_Songs = []
Total_Songs = int(input("How many songs do you have? "))
for i in range(Total_Songs):                                        
    print("Enter the duration of each song")
    Song_Duration = int(input("Enter the duration of the song in seconds: "))
print("The total duration of all the songs is:", (Song_Duration * Total_Songs) ,"seconds")
Total_Duration = (Song_Duration * Total_Songs)
if Total_Duration > TrainingSession:
    print("You have selected too many songs for your training session.")
elif Total_Duration < TrainingSession:
    print("You have selected the right amount of songs for your training session.")