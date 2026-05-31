import os
from eyegaze import create_model, run_tracker
from voiceRecord import record_audio
from multiprocessing import Process
import datetime

def model_check():
    t = datetime.datetime.now()
    print(f"app: {t}")
    for dirpath,dirname,files in os.walk('.'):
        for file in files:
            if file == "gaze_model.pkl":
                return
    create_model()

if __name__ == '__main__':
    model_check()
    p2 = Process(target=run_tracker)
    p2.start()
    p1 = Process(target=record_audio)
    p1.start()
    p2.join()
    p1.join()