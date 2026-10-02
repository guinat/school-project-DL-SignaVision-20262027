CLASS_NAMES = [
    "Speed limit 20 km/h", "Speed limit 30 km/h", "Speed limit 50 km/h", "Speed limit 60 km/h",
    "Speed limit 70 km/h", "Speed limit 80 km/h", "End of speed limit 80 km/h", "Speed limit 100 km/h",
    "Speed limit 120 km/h", "No passing", "No passing for vehicles over 3.5 t",
    "Right-of-way at next intersection", "Priority road", "Yield", "Stop",
    "No vehicles", "Vehicles over 3.5 t prohibited", "No entry", "General caution",
    "Dangerous curve left", "Dangerous curve right", "Double curve", "Bumpy road",
    "Slippery road", "Road narrows on the right", "Road work", "Traffic signals",
    "Pedestrians", "Children crossing", "Bicycles crossing", "Beware of ice/snow", "Wild animals crossing",
    "End of all speed and passing limits", "Turn right ahead", "Turn left ahead", "Ahead only",
    "Go straight or right", "Go straight or left", "Keep right",
    "Keep left", "Roundabout mandatory", "End of no passing",
    "End of no passing for vehicles over 3.5 t",
]
NUM_CLASSES = len(CLASS_NAMES)

FAMILIES = {
    "Speed limit": [0, 1, 2, 3, 4, 5, 7, 8],
    "End of restriction": [6, 32, 41, 42],
    "Prohibition": [9, 10, 15, 16, 17],
    "Priority": [11, 12, 13, 14],
    "Danger": list(range(18, 32)),
    "Mandatory": list(range(33, 41)),
}
CLASS_FAMILY = {c: family for family, ids in FAMILIES.items() for c in ids}

assert sorted(CLASS_FAMILY) == list(range(NUM_CLASSES))
