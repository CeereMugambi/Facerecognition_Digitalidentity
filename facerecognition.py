
import cv2
import time
import random,os
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
import PySimpleGUI as sg
from urllib.parse import urlparse
from io import BytesIO

from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

import cv2
import time
import numpy as py
import random,os
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO

from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person


# Microsoft Azure subscriotion key for Face resource
KEY = "033a424bec9f4f8f91bfe4c3fdf9394e"

# microsoft Azure Endpoint for face resource
ENDPOINT = "https://faceapi-dev-we.cognitiveservices.azure.com/"


PERSON_GROUP_ID = str(uuid.uuid4()) 

# Used for the Delete Person Group example.
TARGET_PERSON_GROUP_ID = str(uuid.uuid4()) 

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
import cv2
import time
import numpy as py
import random,os
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO

from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person


# Microsoft Azure subscriotion key for Face resource
KEY = "033a424bec9f4f8f91bfe4c3fdf9394e"

# microsoft Azure Endpoint for face resource
ENDPOINT = "https://faceapi-dev-we.cognitiveservices.azure.com/"


PERSON_GROUP_ID = str(uuid.uuid4()) 

# Used for the Delete Person Group example.
TARGET_PERSON_GROUP_ID = str(uuid.uuid4()) 

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


'''
Create the PersonGroup
'''
# Create empty Person Group
print('Person group:', PERSON_GROUP_ID)
face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)


# Define man friend
#add persons into persongroup
janetceere = face_client.person_group_person.create(PERSON_GROUP_ID, "Janetceere")



'''
Detect faces and register to correct person
'''


# Find random jpeg images of friends in working directory
janetceere_images = [file for file in glob.glob('*.png')]
i = len(janetceere_images)
f = []

#randomly select 2 images of person for training
randomlist_images = random.sample(range(0,i), 4)
 
# Add to a janet person 
for image in randomlist_images:
    f.append(janetceere_images[image])
    print(randomlist_images)
    

    for image in f: 
        k = open(image,'r+b')
        face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, janetceere.person_id,k)
    



  
'''
Train PersonGroup
'''
print()
print('Training the person group...')
# Train the person group
face_client.person_group.train(PERSON_GROUP_ID)

while (True):
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status is TrainingStatusType.succeeded):
        break
    elif (training_status.status is TrainingStatusType.failed):
        face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)
        sys.exit('Training the person group unsuccessful.')
    time.sleep(5)


    '''
Identify a face against a defined PersonGroup
'''
# Group image for testing against
test_image_array = glob.glob('testimage/testimage.png')
image = open(test_image_array[0], 'r+b')


# Detect faces
face_ids = []
 #We use detection model 3 to get better performance.
faces = face_client.face.detect_with_stream(image, detection_model='detection_03')
for face in faces:
    face_ids.append(face.face_id)


# Identify faces
results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
print('Identifying faces in {}'.format(os.path.basename(image.name)))
if not results:
    print('Unidentified person in the person group for faces from {}.'.format(os.path.basename(image.name)))
for person in results:
    if len(person.candidates) > 0:
        sg.theme('DarkGreen')
        sg.popup("MATCH FOUND")
       # print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence)) # Get topmost confidence score
    else:
        sg.theme('HotDogStand')
        sg.popup("MATCH NOT FOUND!!")
        #print('Unidentified person for face ID {} in {}.'.format(person.face_id, os.path.basename(image.name)))


























'''
Create the PersonGroup
'''
# Create empty Person Group
print('Person group:', PERSON_GROUP_ID)
face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)


# Define man friend
#add persons into persongroup
janetceere = face_client.person_group_person.create(PERSON_GROUP_ID, "Janetceere")



'''
Detect faces and register to correct person
'''


# Find random jpeg images of friends in working directory
janetceere_images = [file for file in glob.glob('*.jpg')]
i = len(janetceere_images)
f = []

#randomly select 2 images of person for training
randomlist_images = random.sample(range(0,i), 4)
 
# Add to a janet person 
for image in randomlist_images:
    f.append(janetceere_images[image])
    print(randomlist_images)
    

    for image in f: 
        k = open(image,'r+b')
        face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, janetceere.person_id,k)
    



  
'''
Train PersonGroup
'''
print()
print('Training the person group...')
# Train the person group
face_client.person_group.train(PERSON_GROUP_ID)

while (True):
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status is TrainingStatusType.succeeded):
        break
    elif (training_status.status is TrainingStatusType.failed):
        face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)
        sys.exit('Training the person group unsuccessful.')
    time.sleep(5)


    '''
Identify a face against a defined PersonGroup
'''
# Group image for testing against
test_image_array = glob.glob('testimage/testimage.jpg')
image = open(test_image_array[0], 'r+b')


# Detect faces
face_ids = []
 #We use detection model 3 to get better performance.
faces = face_client.face.detect_with_stream(image, detection_model='detection_03')
for face in faces:
    face_ids.append(face.face_id)


# Identify faces
results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
print('Identifying faces in {}'.format(os.path.basename(image.name)))
if not results:
    print('Unidentified person in the person group for faces from {}.'.format(os.path.basename(image.name)))
for person in results:
    if len(person.candidates) > 0:
        print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0].confidence)) # Get topmost confidence score
        sg.popup("Match found!")
    else:
        print('Unidentified person for face ID {} in {}.'.format(person.face_id, os.path.basename(image.name)))

























