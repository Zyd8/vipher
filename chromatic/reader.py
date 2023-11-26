import cv2
import numpy as np

video_path = 'output_video.mp4'

pixel_scale = 32

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
    exit()


letter_color_dict = {
    "'": (255, 0, 0),   
    '"': (255, 50, 50),   
    ';': (255, 100, 100),  
    '-': (255, 150, 150),   
    '?': (255, 200, 200),   
    '!': (255, 255, 0),  
    '(': (255, 10, 255),   
    ')': (255, 50, 255),   
    ':': (255, 100, 255),   
    ',': (100, 100, 255),    
    '.': (0, 255, 0),    
    ' ': (0, 0, 0),  
    'a': (255, 0, 255),   
    'b': (0, 0, 255),     
    'c': (0, 150, 255),   
    'd': (128, 0, 128),   
    'e': (255, 140, 0),    
    'f': (255, 255, 25),    
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
print(len(decoded_message))

cap.release()
cv2.destroyAllWindows()