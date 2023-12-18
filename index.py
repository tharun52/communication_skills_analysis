from speech import recognize_speech
from formality_score import calculate_formality_score
from tk import show_triple_section_dialog
from correct_text import correct_grammar
import sys

print("1. From audio file")
print("2. From video file")
while True:
    choice = int(input("Enter your choice : "))  
    if choice == 1:
        path = input("Enter the audio file path : ")
        if path[-4:].lower()!='.wav':
            sys.exit("non Wav error")
        else:
            transcribed_text = recognize_speech(path)
            correct_text = correct_grammar(transcribed_text)
            score = calculate_formality_score(transcribed_text)

            show_triple_section_dialog(transcribed_text, correct_text, score)
            break
    elif choice == 2:
        pass
    else:
        print("Enter choice again")