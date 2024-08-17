import cv2
import numpy as np

# Hàm phát hiện màu đỏ
def detect_red(frame, focal_length, actual_width):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask_red1 | mask_red2
    mask = cv2.GaussianBlur(mask, (5, 5), 0)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 900:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            width_on_image = min(w, h)
            distance = (actual_width * focal_length) / width_on_image
            center_x = x + w // 2
            center_y = y + h // 2
            frame_center_x, frame_center_y = frame.shape[1] // 2, frame.shape[0] // 2
            offset_x = center_x - frame_center_x
            offset_y = frame_center_y - center_y
            return frame, distance, offset_x, offset_y, area
    return frame, None, None, None, None

# Hàm phát hiện màu lục
def detect_green(frame, focal_length, actual_width):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([50, 120, 70])
    upper_green = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 900:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            width_on_image = min(w, h)
            distance = (actual_width * focal_length) / width_on_image
            center_x = x + w // 2
            center_y = y + h // 2
            frame_center_x, frame_center_y = frame.shape[1] // 2, frame.shape[0] // 2
            offset_x = center_x - frame_center_x
            offset_y = frame_center_y - center_y
            return frame, distance, offset_x, offset_y, area
    return frame, None, None, None, None

# Hàm phát hiện màu lam
def detect_blue(frame, focal_length, actual_width):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 150, 70])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 900:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            width_on_image = min(w, h)
            distance = (actual_width * focal_length) / width_on_image
            center_x = x + w // 2
            center_y = y + h // 2
            frame_center_x, frame_center_y = frame.shape[1] // 2, frame.shape[0] // 2
            offset_x = center_x - frame_center_x
            offset_y = frame_center_y - center_y
            return frame, distance, offset_x, offset_y, area
    return frame, None, None, None, None

# Main
url = 'http://10.220.5.230:8000/stream.mjpg'
cap = cv2.VideoCapture(url)

focal_length = 640
actual_width = 8.0
AREA_THRESHOLD = 1100

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Phát hiện màu
    frame_red, distance_red, offset_x_red, offset_y_red, area_red = detect_red(frame.copy(), focal_length, actual_width)
    frame_green, distance_green, offset_x_green, offset_y_green, area_green = detect_green(frame.copy(), focal_length, actual_width)
    frame_blue, distance_blue, offset_x_blue, offset_y_blue, area_blue = detect_blue(frame.copy(), focal_length, actual_width)

    # Khung hình kết hợp
    combined_frame = frame.copy()

    # Xử lý kết quả
    if distance_red and area_red > AREA_THRESHOLD:
        cv2.putText(combined_frame, "Red", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        combined_frame = frame_red
        print(f"Red: Khoảng cách {distance_red:.2f}cm, Độ lệch X: {offset_x_red}, Y: {offset_y_red}")

    if distance_green and area_green > AREA_THRESHOLD:
        cv2.putText(combined_frame, "Green", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        combined_frame = frame_green
        print(f"Green: Khoảng cách {distance_green:.2f}cm, Độ lệch X: {offset_x_green}, Y: {offset_y_green}")

    if distance_blue and area_blue > AREA_THRESHOLD:
        cv2.putText(combined_frame, "Blue", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        combined_frame = frame_blue
        print(f"Blue: Khoảng cách {distance_blue:.2f}cm, Độ lệch X: {offset_x_blue}, Y: {offset_y_blue}")

    # Hiển thị
    cv2.imshow('Combined Color Detection', combined_frame)
    # cv2.imshow('Noise Screen', )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
