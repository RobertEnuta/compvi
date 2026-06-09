from datetime import datetime
import json
from eyetrax import GazeEstimator, run_9_point_calibration
import cv2
import time
RECORD_SECONDS = 5
LIST_POSITIONS =[]

def create_model(): 
    # Create estimator and calibrate
    estimator = GazeEstimator()
    run_9_point_calibration(estimator)

    # Save model
    estimator.save_model("gaze_model.pkl")
    return

# skip creating a model every time and just run the data logging
def run_tracker():
    # Load model
    estimator = GazeEstimator()
    estimator.load_model("gaze_model.pkl")

    cap = cv2.VideoCapture(cv2.CAP_DSHOW) # selects the default camera
    time_on = 0 # sum total of time spent on screen
    nr = 0 # nr of entries in the data log
    # save the time for the recording
    start = time.time()
    current = start 
    while (current < start + RECORD_SECONDS):
        nr+=1
        current = time.time()
        # Extract features from frame
        ret, frame = cap.read()
        features, blink = estimator.extract_features(frame)
        # Predict screen coordinates
        if features is not None and not blink:
            x, y = estimator.predict([features])[0]
            bounds = "in"
            if x < -20 or y < -20 or x > 2000 or y > 2000:
                bounds = "out"
            else:
                time_on += time.time() - current # calculate the time it took to execute the code this loop
            # add positions to the list
            position_dict={
                "nr":f"{nr}",
                "x":f"{x:.0f}",
                "y":f"{y:.0f}",
                "bounds":f"{bounds}"
            }
            LIST_POSITIONS.append(position_dict)
            print(f"Gaze: ({x:.0f}, {y:.0f}, Bounds:{bounds})")
    # dump the list to a json file
    time_Recorded=time.time() - start # calculate the REAL time it took to record
    # transform the data into json format
    d = datetime.now()
    d = str(d.strftime("%d/%m/%Y, %H:%M:%S"))
    print(d)
    meta = {
        "date":d,
    }
    data= {
        "positions":LIST_POSITIONS,
        "time_onscree":time_on,
        "recorded_time":time_Recorded
    }
    jdata= {
        "meta":meta,
        "data":data
    }
    # dump data to file
    with open("..\\collected\\eyegaze.json", "w") as f:
        json.dump(jdata, f)
    # folowing code records ONLY data that is sent to the AI mdoel
    ai_data= {
        "time_onscree":time_on,
        "recorded_time":time_Recorded
    }
    # dump data to file
    with open("..\\collected\\ai.json", "w") as f:
        json.dump(ai_data, f)

if __name__ == '__main__':
    create_model()