import json
from eyetrax import GazeEstimator, run_9_point_calibration
import cv2

RECORD_SECONDS = 2
RATE = 44100              # Sample rate (44.1 kHz)
CHUNK = 1024              # Frames per buffer
LIST_POSITIONS =[]

def create_model(): 
    # Create estimator and calibrate
    estimator = GazeEstimator()
    run_9_point_calibration(estimator)

    # Save model
    estimator.save_model("gaze_model.pkl")
    return
def run_tracker():
    # Load model
    estimator = GazeEstimator()
    estimator.load_model("gaze_model.pkl")

    cap = cv2.VideoCapture(cv2.CAP_DSHOW)
    # cap = cv2.VideoCapture(0)

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    # while True:
        # Extract features from frame
        ret, frame = cap.read()
        features, blink = estimator.extract_features(frame)
        # Predict screen coordinates
        if features is not None and not blink:
            x, y = estimator.predict([features])[0]
            # add positions to the list
            position_dict={
                "x":f"{x:.0f}",
                "y":f"{y:.0f}"
            }
            LIST_POSITIONS.append(position_dict)
            print(f"Gaze: ({x:.0f}, {y:.0f})")
            if x < -20 or y < -20 or x > 2000 or y > 2000:
                print("Out of bonds")
    # dump the list to a json file
    with open("eyegaze.json", "w") as f:
        json.dump(LIST_POSITIONS, f)


if __name__ == '__main__':
    run_tracker()