import cv2
import numpy as np

output_path = 'output_video.mp4'

frame_width = 640
frame_height = 480
frame_rate = 30

pixel_scale = 32

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))

message = """
    seek them out 
"""
print(len(message))
message = message.lower()

letter_color_dict = {
    ',': (255, 0, 0),    
    '.': (0, 255, 0),    
    ' ': (0, 0, 0),  
    'a': (255, 0, 255),   
    'b': (0, 0, 255),     
    'c': (0, 150, 255),   
    'd': (128, 0, 128),   
    'e': (255, 140, 0),    
    'f': (255, 255, 0),    
    'g': (128, 128, 0),    
    'h': (0, 128, 25),     
    'i': (154, 205, 50),  
    'j': (173, 216, 230), 
    'k': (255, 228, 196),  
    'l': (255, 192, 203), 
    'm': (240, 30, 0),      
    'n': (218, 112, 214),  
    'o': (0, 128, 128),   
    'p': (0, 255, 255),    
    'q': (255, 99, 71),   
    'r': (0, 255, 127),    
    's': (244, 164, 96),   
    't': (190, 20, 50),    
    'u': (128, 77, 25),      
    'v': (50, 0, 128),     
    'w': (255, 255, 255),   
    'x': (192, 192, 192), 
    'y': (150, 255, 150),  
    'z': (128, 128, 128)  
}

message_ctr = 0
ctr = 0
for frame_count in range((len(message) * frame_rate // ((frame_width * frame_height)//(pixel_scale))) + 2):
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

    for i in range(0, frame_height, pixel_scale):

        for j in range(0, frame_width, pixel_scale):

            if message_ctr < len(message):
                letter = message[message_ctr]

                if letter in letter_color_dict:
                    frame[i:i+pixel_scale, j:j+pixel_scale, :] = letter_color_dict[letter]

                message_ctr += 1

    video_writer.write(frame)

    ctr += 1
    if ctr >= frame_rate:
        ctr = 0
        message_ctr += 1

video_writer.release()
