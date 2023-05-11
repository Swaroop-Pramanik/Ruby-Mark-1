import pyttsx3
loading_ruby = pyttsx3.init()
voices = loading_ruby.getProperty("voices")
loading_ruby.setProperty("voice", voices[2].id)
password = input("Enter your password: ")
if password == "10710122010":
    import app
    loading_ruby.say("Welcome boss.")

loading_ruby.runAndWait()
