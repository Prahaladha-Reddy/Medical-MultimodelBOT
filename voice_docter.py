
import os
from gtts import gTTS
import base64
import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from pydub import AudioSegment
import subprocess
import platform

load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

os.environ["GROQ_API_KEY"]=GROQ_API_KEY


ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

os.environ['ELEVENLABS_API_KEY']=ELEVENLABS_API_KEY



""" def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

 """
input_text="Welcome to the future of intelligent communication! With advancements in artificial intelligence, technology has become more intuitive and accessible than ever before. Imagine a world where virtual assistants understand your needs, medical bots offer timely healthcare guidance, and everyday tasks are automated seamlessly. This is not just a vision of tomorrow; it is happening today. Let’s explore how innovation can transform lives, making technology a companion that empowers, inspires, and simplifies. Together, we are shaping a smarter, more connected future!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="first_test.mp3")

""" 
def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")  """


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    # Generate MP3 first
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    mp3_filepath = output_filepath
    audioobj.save(mp3_filepath)
    
    # Convert to WAV for playing
    wav_filepath = output_filepath.replace('.mp3', '.wav')
    
    os_name = platform.system()
    try:
        if os_name == "Windows":
            # Convert MP3 to WAV using subprocess and ffmpeg
            subprocess.run([
                r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",  # Adjust this path to your ffmpeg installation
                "-i", mp3_filepath,
                "-y",  # Overwrite output file if it exists
                wav_filepath
            ], check=True)
            
            # Play the WAV file
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        
        elif os_name == "Darwin":  # macOS
            subprocess.run(['afplay', mp3_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', mp3_filepath])
        else:
            raise OSError("Unsupported operating system")
            
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
        
              
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")
