import asyncio
import json
import os
from vision.identity import use_token
from vision import eyegaze as eye
from vision import voiceRecord as voice
from multiprocessing import Process
import datetime
from models import apiGateway as AI
import db.Connector as conn

def model_check():
    """ Checks and creates gaze_model.pkl
    """
    t = datetime.datetime.now()
    print(f"app: {t}")
    for dirpath,dirname,files in os.walk('.'):
        for file in files:
            if file == "gaze_model.pkl":
                return
    eye.create_model()

if __name__ == '__main__':
    # check first if a token needs to be created
    if os.stat(".\\collected\\token.txt").st_size != 0:
       token = use_token()
    model_check()
    p2 = Process(target=eye.run_tracker)
    p2.start()
    p1 = Process(target=voice.record_audio)
    p1.start()
    p2.join()
    p1.join()
    # wait for recording to finish before transcribing
    script = asyncio.run(AI.transcription()) 
    asyncio.run(AI.get_feedback(script))

    with open(".\\collected\\token.txt", "r") as f:
        UUID = f.read()
    with open(".\\collected\\ai.json", "r") as f:
        e = json.load(f)
    with open(".\\collected\\feedback.json", "r") as f:
        feedback = json.load(f)
    feedback = feedback["choices"][0]["message"]["content"]

    conn.create_user(UUID,"rob")
    conn.create_training(UUID,e,feedback)

    print(conn.read_prog())

    