import random, math, csv
from constants import types, materials, colours, shapes,observed_features, MAX_COUNT, MAX_SIZE, MAX_WEIGHT, MAX_PRICE

def create_data():
    jewellery = []
    jewellery_count = random.randint(50, MAX_COUNT)
    print(f"Generating {jewellery_count} jewellery items...")
    for i in range(jewellery_count):
        jewellery.append(create_jewellery_item())
        
    return jewellery

def write_data(jewellery):
    with open("jewelley.csv", "w", encoding="UTF-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(observed_features)
        for jewellery_item in jewellery:
            if not jewellery_item:
                continue
            if len(jewellery_item) != 7:
                continue
            writer.writerow([
                jewellery_item["type"],
                jewellery_item["material"],
                jewellery_item["colour"],
                jewellery_item["shape"],
                jewellery_item["size"],
                jewellery_item["weight"],
                jewellery_item["price"]
            ])
    
    
        
def create_jewellery_item():
    jewellery_item = {
        "type": random.choice(types),
        "material": random.choice(materials),
        "colour": random.choice(colours),
        "shape": random.choice(shapes),
        "size": random.randint(1, MAX_SIZE),
        "weight": random.randint(10, MAX_WEIGHT),
        "price": random.randint(2000, MAX_PRICE)
    }
    return jewellery_item

if __name__ == "__main__":
    jewellery = create_data()
    write_data(jewellery)