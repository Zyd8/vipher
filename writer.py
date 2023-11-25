import cv2
import numpy as np

output_path = 'output_video.mp4'

frame_width = 640
frame_height = 480
frame_rate = 1

pixel_scale = 32

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_writer = cv2.VideoWriter(output_path, fourcc, frame_rate, (frame_width, frame_height))

message = """Once upon a time, in a small village nestled between rolling hills and meandering streams, there lived a curious young boy named jason. jason, with his mop of unruly brown hair and a perpetual twinkle in his hazel eyes, spent his days exploring the dense forests that bordered the village.

One sunny day, as jason wandered deeper into the woods, he stumbled upon a hidden cave concealed behind a curtain of ivy. The entrance was marked by a peculiar arrangement of rocks, forming a mysterious pattern on the ground. jason's curiosity got the better of him, and he cautiously entered the dimly lit cavern.

Inside, he discovered a vast underground world, adorned with shimmering crystals that dotted the cave walls. The air was thick with an enchanting aura, and the ground beneath jason's feet felt strangely alive. As he ventured further, he noticed peculiar markings etched onto the walls, resembling a forgotten language.

Intrigued, jason continued his exploration, guided only by the soft glow of the crystals. Along the way, he encountered friendly creatures—small, luminescent insects that emitted a gentle hum. They seemed to communicate with jason through subtle movements, guiding him deeper into the heart of the cave.

Eventually, jason stumbled upon an ancient chamber, where a massive, ancient tree stood tall, its roots intertwining with the very essence of the cave. At the base of the tree, he found a weathered journal, its pages filled with cryptic messages and faded illustrations.

As he leafed through the journal, jason uncovered the tale of a forgotten civilization that once thrived in harmony with nature. The cave served as a bridge between their world and the surface, allowing them to coexist with the vibrant ecosystem of the forest.

Determined to unravel the mysteries of the cave, jason spent days deciphering the forgotten language and understanding the symbiotic relationship between the ancient tree and the creatures that inhabited the cave. Dot by dot, and comma by comma, he pieced together the story of a civilization that revered the balance between the mundane and the mystical.

In his quest for knowledge, jason discovered that the cave held secrets beyond his wildest imagination. It was a sanctuary for those who sought solace in the gentle embrace of nature, and the markings on the walls were a testament to the enduring connection between the worlds above and below.

With newfound wisdom, jason returned to his village, sharing the tale of the hidden cave and the ancient tree. His fellow villagers listened in awe, inspired by the idea that magic and wonder could be found in the most unexpected places.

And so, the tale of jason and the enchanted cave became a cherished legend, passed down through generations, with dots and commas preserving the magic of a world where nature and mystery danced together in perfect harmony."""
message = message.lower()

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

# 9600 per frame 

message_ctr = 0
ctr = 0
break_ctr = 0
for frame_count in range((frame_rate * len(message))//250):
    frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

    if break_ctr >= 30:
        break

    for i in range(0, frame_height, pixel_scale):
        for j in range(0, frame_width, pixel_scale):
            if message_ctr < len(message):
                letter = message[message_ctr]
                if letter in letter_color_dict:
                    frame[i:i+pixel_scale, j:j+pixel_scale, :] = letter_color_dict[letter]
                else:
                    break_ctr += 1
                message_ctr += 1

    video_writer.write(frame)

    ctr += 1
    if ctr >= frame_rate:
        ctr = 0
        message_ctr += 1

video_writer.release()
