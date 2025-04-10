import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

recognizer = sr.Recognizer()
GOOGLE_API_KEY = 'AIzaSyA5VOPs7m3FLQeFJ3MLuYVn5mrn2PuhApk' # Kripya Apni API daale

genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-exp')
chat = model.start_chat(history=[])

while True:
    # Using input() to manually break the loop
    user_input = input("Press Enter to continue or type 'exit' to quit: ").strip().lower()
    if user_input == 'exit':
        print("Exiting program...")
        break

    try:

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)

            # Convert audio to text using Google Speech Recognition API
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Text: {text}")
            output = chat.send_message(text)
            print(output.text)

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio. Please try again.")
        continue
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        break
