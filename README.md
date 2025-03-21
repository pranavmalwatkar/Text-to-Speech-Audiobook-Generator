# Text-to-Speech-Audiobook-Generator
**📖 Text-to-Speech Audiobook Generator using gTTS**
**📝 Description**
This project converts a text file into an audiobook using Google Text-to-Speech (gTTS). It supports multiple languages and can generate high-quality speech output.

**🔹 Features**
✅ Converts text files into MP3 audiobooks
✅ Supports 40+ languages for multilingual speech synthesis
✅ Uses Google Text-to-Speech (gTTS) for natural voice generation
✅ Simple and easy-to-use Python script
✅ Works offline after downloading the required TTS model

**🌍 Supported Languages**
gTTS supports many languages, including:

English (US, UK, Australia, India) - en, en-uk, en-au, en-in
Hindi - hi
Marathi - mr
Spanish - es
French - fr
German - de
Portuguese (Brazil, Portugal) - pt, pt-pt
Chinese (Simplified, Traditional) - zh-cn, zh-tw
Japanese - ja
Korean - ko
Russian - ru
Bengali - bn
Tamil - ta
Telugu - te

📌 To see the full list of supported languages, run:
from gtts.lang import tts_langs
print(tts_langs())

**⚙️ How It Works
1️⃣ Install Required Libraries**
pip install gtts
**2️⃣ Prepare a Text File**

Create a .txt file with the text you want to convert.
Example: example.txt
**3️⃣ Run the Python Script**
from gtts import gTTS

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
    input_file = "example.txt"  # Replace with your file path
    output_file = "audiobook.mp3"
    create_audiobook(input_file, output_file, lang='en')  # Change 'en' to other language codes
**4️⃣ Play the Audiobook**

Open the generated audiobook.mp3 file and listen! 🎧
**📦 Module Import Process**
This project requires the following Python module:
gtts ::	Google Text-to-Speech API for generating audio from text
**To install it, run:**
pip install gtts
**🚀 Future Improvements**
Add voice selection for different accents
Support PDF to Audiobook conversion
Implement real-time speech synthesis
