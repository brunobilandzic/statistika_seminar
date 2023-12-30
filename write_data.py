import random, math, csv
from constants import types, materials, colours, shapes,observed_features, MAX_COUNT, MAX_SIZE, MAX_WEIGHT, MAX_PRICE

def create_data():
    jewellery = []
    jewellery_count = random.randint(200, MAX_COUNT)
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
        "price": get_price()
    }
    return jewellery_item

def get_price():
    r = random.randint(0, 100)
    if r < 25:
        return random.randint(2000, 3000)
    if r<40:
        return random.randint(3000, 4000)
    if r<47:
        return random.randint(4000, 5000)
    if r<63:
        return random.randint(5000, 6000)
    if r<86:
        return random.randint(6000, 7000)
    return random.randint(7000, MAX_PRICE)

if __name__ == "__main__":
    jewellery = create_data()
    write_data(jewellery)