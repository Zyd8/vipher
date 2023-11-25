import cv2
import numpy as np

output_path = 'output_video.mp4'

frame_width = 640
frame_height = 480
frame_rate = 1

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))

message = "Most opportunities are created by luck. It takes skill to grasp those opportunities and turn it into success."
message = message.lower()

letter_color_dict = {
    ',': (190, 20, 50),
    '.': (50, 250, 100),
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
    'p': (0, 50, 128),  # Aqua
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

message_ctr = 0
ctr = 0
for frame_count in range(frame_rate * len(message)):
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

    if message_ctr < len(message):
        letter = message[message_ctr]
        if letter in letter_color_dict:
            frame[:, :] = letter_color_dict[letter]  

    video_writer.write(frame)

    ctr += 1
    if ctr >= frame_rate:
        ctr = 0
        message_ctr += 1

video_writer.release()
