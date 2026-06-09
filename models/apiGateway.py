import os
from dotenv import load_dotenv
from portkey_ai import Portkey
import asyncio


load_dotenv() 
KEY=os.getenv("AI_KEY")
URL =os.getenv("AI_URL")
PROVIDER="azure-openai" 
MODEL="whisper"


async def transcription(file="output.wav",language="en",format="json") -> str:
    """
    File must point to the name of the audio file in the 'collected' folder. Language is in ISO 639 format en=english/nl=dutch.\n
    Response type json(default) = short or verbose_json - for more details 
    """
    client = Portkey(
        api_key = KEY,
        provider = PROVIDER
    )

    audio_file = open(f".\\collected\\{file}", "rb")
    transcript = client.audio.transcriptions.create(
        model=MODEL,
        file=audio_file,
        langauge=language,
        response_format=format 
    )
    print(transcript.text)
    return transcript.text



if __name__ == "__main__":
    asyncio.run(transcription())