from pathlib import Path
from openai import OpenAI
from extract_content import extract_content
from dotenv import load_dotenv
import os
import warnings

# Ignore DeprecationWarning
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def text_to_speech(text, output_file="output.mp3", voice="alloy"):
    """
    Convert text to speech using OpenAI's TTS API
    
    Parameters:
    - text: The text to convert to speech
    - output_file: The name of the output audio file (default: output.mp3)
    - voice: The voice to use (options: alloy, echo, fable, onyx, nova, shimmer)
    """
    try:
        # Initialize the client with your API key
        client = OpenAI(api_key=OPENAI_API_KEY)  # Replace with your actual API key
        
        # Create speech from text
        response = client.audio.speech.create(
            model="tts-1",  # or "tts-1-hd" for higher quality
            voice=voice,
            input=text
        )
    
        # Save the audio file
        response.stream_to_file(output_file)        
        print(f"Audio saved successfully to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example text to convert
    url = input("Enter URL: ")
    content = extract_content(url)
    
    # Convert text to speech
    text_to_speech(
        text=content,
        output_file="result.mp3",
        voice="nova"  # You can change the voice here
    )