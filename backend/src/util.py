import  numpy as np
import  cv2

def preprocessing_image(img):
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx = 1.5, fy = 1.5, interpolation=cv2.INTER_LINEAR)
    preprocessed_image = cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )
    return preprocessed_image