from playsound import playsound
import pyttsx3
import os
 

while True:
    print("Chat with me with your Requreiment :" , end='')
    p = input()
    if("run" in p) and ("chrome" in p)or("open" in p):
        os.system("chrome")
    elif ("run" in p)and ("vlc" in p):
        os.system("vlc")
    elif ("run" in p) and("notepad++" in p):
        os.system("notepad++")  
    elif ("exit" in p):
        pyttsx3.speak("Thankyou for Using")
        break
    elif ("talk" in p)or("listen" in p):
        print("yes I allways for their")
    elif ("run" in p)or("telegram" in p):
        os.system("telegram")
    elif("good" in p)and ("morning" in p):
        pyttsx3.speak("Good Morning Sir")
    elif("good" in p)and ("evening" in p):
        pyttsx3.speak("Good Evening Sir")
    elif("Hii" in p) and ("Hello" in p):
        print("Hello Sir")
    elif("tell" in p) or ("Jokes" in p):
        print("What kind of shorts do clouds wear? Thunderpants.")
        pyttsx3.speak("What kind of shorts do clouds wear? Thunderpants.")
        playsound("C:/Users/WedNesDay/Desktop/Class/Baby-Hard-Laughing-www.fesliyanstudios.com.mp3")
    elif("tell" in p) and ("jokes" in p) or ("more" in p):
        print("My doctor said I have 3 months to live. So I shot him and the judge gave me 25 years.")
        pyttsx3.speak("My doctor said I have 3 months to live. So I shot him and the judge gave me 25 years.")
        playsound("C:/Users/WedNesDay/Desktop/Class/Baby-Hard-Laughing-www.fesliyanstudios.com.mp3")
    else :
        print("Dont Support")         
#print(p)
#os.system(p)


  

