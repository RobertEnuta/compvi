import asyncio
import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vision import eyegaze as eye
from vision import voiceRecord as voice
from multiprocessing import Process
import datetime
from models import apiGateway as AI

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
    model_check()
    p2 = Process(target=eye.run_tracker)
    p2.start()
    p1 = Process(target=voice.record_audio)
    p1.start()
    p2.join()
    p1.join()
    # wait for recording to finish before transcribing
    asyncio.run(AI.transcription())
    