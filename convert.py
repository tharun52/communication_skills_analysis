from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)

    # Export the audio to WAV
    audio.export(wav_file, format="wav")

# Replace 'input.mp3' with the name of your MP3 file
# Replace 'output.wav' with the desired name for the WAV file
if __name__=="__main__":
    convert_mp3_to_wav('hello.mp3', 'output.wav')
