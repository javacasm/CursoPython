# from https://www.learnpythonwithrune.org/find-all-possible-webcam-resolutions-with-opencv-in-python/
import pandas as pd
import cv2


url = "https://en.wikipedia.org/wiki/List_of_common_resolutions"
table = pd.read_html(url)[0]
table.columns = table.columns.droplevel()

cap = cv2.VideoCapture(2)
resolutions = {}

for index, row in table[["W", "H"]].iterrows():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, row["W"])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, row["H"])
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    resolutions[str(width)+"x"+str(height)] = "OK"

print(resolutions)