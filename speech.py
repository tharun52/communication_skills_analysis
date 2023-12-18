import speech_recognition as sr
import sys

def recognize_speech(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as audio_file:
        # Adjust for ambient noise before recognizing speech
        recognizer.adjust_for_ambient_noise(audio_file)

        try:
            # Perform speech recognition
            audio_data = recognizer.record(audio_file)
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            sys.exit("Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            sys.exit("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    wav_file_path = "harvard.wav"
    recognize_speech(wav_file_path)
