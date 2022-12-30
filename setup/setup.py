import mediapipe as mp
from tensorflow.keras.models import load_model

hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

model = load_model('setup/mp_hand_gesture')

# f = open('gesture.names', 'r')
# classNames = f.read().split('\n')
# f.close()

classNames = ['okay', 'peace', 'thumbs up', 'thumbs down',
              'call me', 'stop', 'rock', 'live long', 'fist', 'smile']
