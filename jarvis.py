import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import random
import smtplib
import pywhatkit as pwk
from contact import myContact , mailContact , mailer

# we will create text to speech function
def speak_text(command):
	# we will set speak  engine
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice',voices[0].id)
	engine.say(command)
	engine.runAndWait()

# we will take microphone input
def voice_input():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		#setting microphone
		r.adjust_for_ambient_noise(source, duration=0.2)
		r.pause_threshold = 1
		r.energy_threshold = 4000
		print("Listening.....")
		input_audio = r.listen(source)

		# we will recognize voice
		try:
			print("Recognizing.......")
			text = r.recognize_google(input_audio,language="en-in")
		except Exception as e:
			return "None"
		return text

# this function wishing me good morning afternoon evning
def wish_me():
	hour,mint,period = datetime.datetime.now().strftime("%I:%M:%p").split(":")
	hour = int(hour) + 12 if period == "PM" else int(hour)
	if hour>=0 and hour<12:
		speak_text("Good Morning Sir")
		speak_text("How can I help you")
	elif hour>=12 and hour<18:
		speak_text("Good afternoon Sir")
		speak_text("How can I help you")
	else:
		speak_text("Good Evening Sir")
		speak_text("How can I help you")
# remove word
def remove_word(string,word):
	string = string.split(" ")
	string.remove(word)
	return " ".join(string)

if __name__ == '__main__':
	wish_me()
	# we will handle order
	while True:
		input_text = voice_input().lower()
		print(input_text)
		# exit command handle
		if "jarvis quit" in input_text or "jarvis quick" in input_text:
			speak_text("ok sir")
			exit()
		# jarvis name command handle
		elif "what is your name" in input_text or "what's your name" in input_text:
			speak_text("My name is Jarvis i am from avengers")
		# youtube cammand handle
		elif "open youtube" in input_text:
			speak_text("ok sir")
			webbrowser.open("youtube.com")
		# google command handle
		elif "open google" in input_text:
			speak_text("ok sir")
			webbrowser.open("google.com")
		# searching people in wikipedia
		elif "who is" in input_text:
			input_text = remove_word(remove_word(input_text,"who"),"is")
			print(input_text)
			speak_text("searching wikipedia")
			try:
				result = wikipedia.summary(input_text,sentences=2)
				speak_text(f"acording to wikipedia {result}")
			except Exception as e:
				speak_text("No result found")
		# jarvis introduction
		elif "who are you" in input_text:
			speak_text("i am Artificial intelligence. Artificial intelligence  is the ability of a computer or a robot controlled by a computer to do tasks that are usually done by humans because they require human intelligence and discernment. zeeshan raza was made in 2022")
		# play song and naat
		elif "play naat" in input_text:
			speak_text("ok sir")
			path = "G:\\naat"
			naat_list = os.listdir(path)
			os.startfile(os.path.join(path,naat_list[random.randint(0,len(naat_list))-1]))
		# open code editor	
		elif "open code" in input_text:
			speak_text("ok sir")
			os.startfile("C:\\Program Files\\Sublime Text\\sublime_text.exe")
		# search anything in google
		elif "google search" in input_text:
			speak_text("ok sir")
			input_text = remove_word(remove_word(input_text,"google"),"search")
			webbrowser.open(f"https://www.google.com/search?q={input_text}")
		# anything seacrh in youtube 
		elif "youtube search" in input_text:
			speak_text("ok sir")
			input_text = remove_word(remove_word(input_text,"youtube"),"search")
			webbrowser.open(f"https://www.youtube.com/results?search_query={input_text}")
		# send whatsapp message
		elif "send whatsapp message to" in input_text:
			speak_text("ok sir")
			contact_find = False
			for i in myContact:
				if i in input_text:
					contact_find = True
					hour,mint,period = datetime.datetime.now().strftime("%I:%M:%p").split(":")
					hour = int(hour) + 12 if period == "PM" else int(hour) 
					speak_text("what i say")
					text = voice_input()
					try:
						pwk.sendwhatmsg(myContact[i],text,int(hour),int(mint)+1)
						# speak_text("message send succesfully")
					except Exception as e:
						speak_text("message faild")
					break
			if not contact_find:
				speak_text(f"{input_text[input_text.find('to')+3:]} not in contact list")
		# send mail
		elif "send mail to" in input_text:
			speak_text("ok sir")
			contact_find = False
			for i in mailContact:
				if i in input_text:
					contact_find = True
					speak_text("what i say")
					text = voice_input()
					print(text)
					result = mailer(mailContact[i],text)
					speak_text(result)
			if not contact_find:
				speak_text(f"{input_text[input_text.find('to')+3:]} not in mail contact list")
			