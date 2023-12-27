import csv, statistics

def read_data():
    jewellery = []
    with open("jewelley.csv", "r", encoding="UTF-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) != 7:
                continue
            jewellery_item = {
                "type": row[0],
                "material": row[1],
                "colour": row[2],
                "shape": row[3],
                "size": int(row[4]),
                "weight": int(row[5]),
                "price": int(row[6])
            }
            jewellery.append(jewellery_item)
            
    return jewellery

def get_price(jewellery_item):
    return jewellery_item["price"]

def get_item_count_by_type(jewellery):
    item_count_by_type = {}
    for jewellery_item in jewellery:
        type = jewellery_item["type"]
        if type in item_count_by_type:
            item_count_by_type[type] += 1
        else:
            item_count_by_type[type] = 1
    return item_count_by_type	

def find_most_expensive_item(jewellery):
    most_expensive_item = jewellery[0]
    for jewellery_item in jewellery:
        if jewellery_item["price"] > most_expensive_item["price"]:
            most_expensive_item = jewellery_item
    return most_expensive_item

def find_cheapest_item(jewellery):
    cheapest_item = jewellery[0]
    for jewellery_item in jewellery:
        if jewellery_item["price"] < cheapest_item["price"]:
            cheapest_item = jewellery_item
    return cheapest_item
       
if __name__ == "__main__":
    pass
