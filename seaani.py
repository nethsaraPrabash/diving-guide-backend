# filepath: e:\ML\code\diving-guide-backend\seaani.py
import torch
import pickle
import torchvision.transforms as transforms
import torchvision.models as models
import torch.nn as nn
from PIL import Image
import os
from io import BytesIO

model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 23)

with open("model/saclassification.pkl", "rb") as f:
    state_dict = pickle.load(f)

model.load_state_dict(state_dict)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((300, 225)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

class_labels = [
    "Clams", "Corals", "Crabs", "Dolphin", "Eel", "Fish", "Jelly Fish", "Lobster", 
    "Nudibranchs", "Octopus", "Otter", "Penguin", "Puffers", "Sea Rays", "Sea Urchins",
    "Seahorse", "Seal", "Sharks", "Shrimp", "Squid", "Starfish", "Turtle_Tortoise", "Whale"
]

def predict_image_from_bytes(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    image_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image_tensor)
        _, predicted_idx = torch.max(output, 1)

    predicted_label = class_labels[predicted_idx.item()]
    return predicted_label