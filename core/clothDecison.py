top_wear = ['T-shirt', 'Long-sleeve shirt', 'Sweater', 'Jacket', 'Heavy jacket', 'Heavy winter coat']
bottom_wear = ['Shorts', 'Pants']
footwear = ['Sandals', 'Sneakers', 'Boots']
accessories = ['Gloves', 'Scarf', 'Hat']

def get_outfit(temperature):
    outfit = []
    if temperature >= 70:
        outfit.append(top_wear[0])
        outfit.append(bottom_wear[0])
        outfit.append(footwear[0])
    elif temperature >= 60:
        outfit.append(top_wear[1])
        outfit.append(bottom_wear[1])
        outfit.append(footwear[1])
    elif temperature >= 50:
        outfit.append(top_wear[1])
        outfit.append(bottom_wear[1])
        outfit.append(footwear[1])
    elif temperature >= 40:
        outfit.append(top_wear[3])
        outfit.append(top_wear[1])
        outfit.append(bottom_wear[1])
        outfit.append(footwear[1])
    elif temperature >= 30:
        outfit.append(top_wear[4])
        outfit.append(top_wear[1])
        outfit.append(bottom_wear[1])
        outfit.append(footwear[2])
        outfit.extend(accessories[:2])
    elif temperature >= 20:
        outfit.append(top_wear[4])
        outfit.append(top_wear[2])
        outfit.append(bottom_wear[1])
        outfit.append(footwear[2])
        outfit.extend(accessories)
    else:
        outfit.append(top_wear[5])
        outfit.append(top_wear[2])
        outfit.append(bottom_wear[1])
        outfit.append(footwear[2])
        outfit.extend(accessories)
    return outfit