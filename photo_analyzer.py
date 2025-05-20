from djitellopy import Tello
import cv2
import base64
import openai

# Initialize OpenAI client and Tello
client = openai.OpenAI(api_key='your-openai-key-here')
tello = Tello()
tello.connect()
tello.streamon()

# Capture a single frame from the video stream
frame = tello.get_frame_read().frame
cv2.imwrite('snapshot.jpg', frame)

with open('snapshot.jpg', 'rb') as f:
    img_b64 = base64.b64encode(f.read()).decode()

response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{
        'role': 'user',
        'content': [
            {'type': 'text', 'text': 'Describe this image.'},
            {
                'type': 'image_url',
                'image_url': {'url': f'data:image/jpeg;base64,{img_b64}'}
            }
        ],
    }]
)

print(response.choices[0].message.content)

# Clean up the video stream
tello.streamoff()
