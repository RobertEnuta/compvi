import os
from dotenv import load_dotenv
from portkey_ai import Portkey
import asyncio


load_dotenv() 
KEY=os.getenv("AI_KEY")
URL =os.getenv("AI_URL")


async def transcription(file="output.wav",language="en",format="json") -> str:
    """
    File must point to the name of the audio file in the 'collected' folder. Language is in ISO 639 format en=english/nl=dutch.\n
    Response type json(default) = short or verbose_json - for more details 
    """
    client = Portkey(
        api_key = KEY,
        provider = "azure-openai" 
    )

    audio_file = open(f".\\collected\\{file}", "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper",
        file=audio_file,
        langauge=language,
        response_format=format 
    )
    print(transcript.text)
    return transcript.text

async def get_feedback(input="i love eat apple.",length=300,tokens=180):
    """Call to get feedback on reading. Currently using transcription for dummy feedback output from text.\n
    input  = the string containing the text for feedback\n
    length = the length of the response in letters\n
    tokens = tokens in the response\n
    """
    client = Portkey(
        api_key = KEY,
        provider = "google"
    )

    feedback = client.chat.completions.create(
    model="google/gemini-3.1-flash-lite-preview",
    messages=[
        {"role": "system", "content": f"You are a writing teacher for a 1st grade child.Give short feedback on this sentence, less than {length} characters. Be positive and encouraging"},
        {"role": "user", "content": input}
    ],
    max_completion_tokens=tokens
    )

    print(feedback.choices[0].message.content)
    with open(".\\collected\\feedback.json", "w") as f:
        f.write(str(feedback))

    return feedback

if __name__ == "__main__":
    asyncio.run(get_feedback())