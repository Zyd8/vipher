import cv2
import numpy as np

video_path = 'output_video.mp4'
#video_path = 'compressed_video.mp4'
#video_path = './videos/test144.mp4'

pixel_scale = 32

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
    exit()


letter_color_dict = {
    ',': (255, 0, 0),      # Red
    '.': (0, 255, 0),      # Green
    ' ': (0, 0, 0),  # White
    'a': (255, 0, 255),    # Magenta
    'b': (0, 0, 255),      # Blue
    'c': (0, 150, 255),    # Cyan
    'd': (128, 0, 128),    # Purple
    'e': (255, 140, 0),    # Orange
    'f': (255, 255, 0),    # Yellow
    'g': (128, 128, 0),    # OliveDrab
    'h': (0, 128, 25),      # Green
    'i': (154, 205, 50),   # YellowGreen
    'j': (173, 216, 230),  # LightBlue
    'k': (255, 228, 196),  # Bisque
    'l': (255, 192, 203),  # Pink
    'm': (240, 30, 0),      # Red
    'n': (218, 112, 214),  # Orchid
    'o': (0, 128, 128),    # Teal
    'p': (0, 255, 255),    # Cyan
    'q': (255, 99, 71),    # Tomato
    'r': (0, 255, 127),    # SpringGreen
    's': (244, 164, 96),   # SandyBrown
    't': (190, 20, 50),    # Crimson
    'u': (128, 77, 25),      # Maroon
    'v': (50, 0, 128),      # Navy
    'w': (255, 255, 255),      # Lime
    'x': (192, 192, 192),  # Silver
    'y': (150, 255, 150),  # White
    'z': (128, 128, 128)   # Gray
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

    for i in range(0, frame_height, pixel_scale):
        for j in range(0, frame_width, pixel_scale):
            pixel = frame[i:i+pixel_scale, j:j+pixel_scale, :]
            average_color = np.mean(pixel, axis=(0, 1)).astype(int)
            closest_color = min(letter_color_dict, key=lambda x: np.linalg.norm(np.array(letter_color_dict[x]) - average_color))
            decoded_message += closest_color

    cv2.imshow('Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    ctr += 1

print(decoded_message)

cap.release()
cv2.destroyAllWindows()