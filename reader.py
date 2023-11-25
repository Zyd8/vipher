import cv2
import numpy as np

#video_path = 'output_video.mp4'
#video_path = 'compressed_video.mp4'
video_path = './videos/test480.mp4'


cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
    exit()

letter_color_dict = {
    ' ': (0, 0, 0),      # Black
    'a': (0, 0, 255),    # Red
    'b': (0, 255, 0),    # Green
    'c': (255, 0, 0),    # Blue
    'd': (255, 255, 0),  # Yellow
    'e': (255, 0, 255),  # Magenta
    'f': (0, 255, 255),  # Cyan
    'g': (128, 128, 128),  # Gray
    'h': (192, 192, 192),  # Silver
    'i': (128, 0, 0),    # Maroon
    'j': (0, 128, 0),    # Olive
    'k': (0, 128, 128),  # Teal
    'l': (128, 0, 128),  # Purple
    'm': (255, 165, 0),  # Orange
    'n': (0, 0, 128),    # Navy
    'o': (255, 192, 203),  # Pink
    'p': (0, 128, 128),  # Aqua
    'q': (255, 99, 71),   # Tomato
    'r': (0, 255, 127),   # SpringGreen
    's': (218, 112, 214),  # Orchid
    't': (173, 216, 230),  # LightBlue
    'u': (255, 228, 196),  # Bisque
    'v': (154, 205, 50),   # YellowGreen
    'w': (244, 164, 96),   # SandyBrown
    'x': (0, 200, 0),        
    'y': (255, 255, 255),  # White
    'z': (128, 128, 0),    # OliveDrab
}

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = cap.get(5)
total_frames = int(cap.get(7))
video_length = total_frames / frame_rate

print(f"Video Details - Width: {frame_width}, Height: {frame_height}, Frame Rate: {frame_rate}, Total Frames: {total_frames}, Total seconds: {video_length}")

decoded_message = ""

ctr = 0
first_loop = True
while True:

    def calculate_squared_differences(color1, color2):
        return sum((a - b) ** 2 for a, b in zip(color1, color2))

    def key_function(key):
        return calculate_squared_differences(letter_color_dict[key], average_color)


    ret, frame = cap.read()

    if not ret:
        print("End of video")
        break
    
    if ctr == frame_rate or first_loop:
        average_color = np.mean(frame, axis=(0, 1)).astype(int)

        closest_color = min(letter_color_dict, key=key_function)

        decoded_message += closest_color

        cv2.imshow('Video', frame)

        ctr = 0
        first_loop = False

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    ctr += 1

print(decoded_message)

cap.release()
cv2.destroyAllWindows()