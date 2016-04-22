import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold = 200
with sr.Microphone() as source:
	
	audio = r.listen(source)
try:
	s = r.recognize_google(audio)
	a = s.lower()
	print(a)
	
	

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")