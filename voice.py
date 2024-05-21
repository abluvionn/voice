import speech_recognition as sr

recognizer = sr.Recognizer()

def capture_voice_input():
    
    with sr.Microphone() as source:
        print("Listening... Please speak clearly into the microphone.")
        audio = recognizer.listen(source)
    return audio

def convert_voice_to_text(audio):
   
    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        text = ""
        print("Sorry, I didn't understand that.")
    except sr.RequestError as e:
        text = ""
        print(f"Error: {e}")
    return text

def process_voice_command(text):
   
    text = text.lower()
    if "hello" in text:
        print("Hello! How can I help you?")
    elif "goodbye" in text:
        print("Goodbye! Have a great day!")
        return True
    elif "how are you" in text:
        print("I'm just a program, but I'm doing great! How about you?")
    elif "thank you" in text:
        print("You're welcome!")
    elif "what is your name" in text:
        print("I'm a voice recognition assistant created with Python.")
    else:
        print("I didn't understand that command. Please try again.")
    return False

def main():
    
    print("Voice Recognition Program Started. Say 'goodbye' to end the program.")
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()
