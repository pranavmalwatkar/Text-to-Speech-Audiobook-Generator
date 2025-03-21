from gtts import gTTS
import os

def create_audiobook(input_text_file, output_audio_file, lang='en'):
    try:
        with open(input_text_file, 'r', encoding='utf-8') as file:
            text = file.read()

        tts = gTTS(text=text, lang=lang)
        tts.save(output_audio_file)

        print(f"Audiobook created successfully: {output_audio_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_text_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = r"D:\mca_project\read.txt"  
    output_file = "audiobook.mp3"
    create_audiobook(input_file, output_file, lang='hi')  # Change 'hi' for Hindi, 'mr' for Marathi
