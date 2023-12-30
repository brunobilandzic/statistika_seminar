from read_data import read_data, get_price, get_item_count_by_type, find_most_expensive_item, find_cheapest_item
import statistics, math, tabulate

def print_line():
    print("\n----------------------------------------\n")
    

def prvi():
    jewellery = read_data()
    jewellery.sort(key=get_price)
    
    item_count_by_type = get_item_count_by_type(jewellery)

    print(f"Types: {list(item_count_by_type.keys())}")
    print(f"Type count: {len(item_count_by_type)}")
    print(f"Item count: {len(jewellery)}")
    print("Item count by type:")
    for type in item_count_by_type:
        print(f"\t{type}: {item_count_by_type[type]}")
        
    print_line()
    
    prices = list(map(get_price, jewellery))
    
    print(f"Average price of an item: {statistics.mean(prices)}")
    print(f"Median price of an item: {statistics.median(prices)}")
    print(f"Mod: {statistics.mode(prices)}")
    
    print_line()
    print("Characteristic five:\n")
    print(f"Most expensive item: {find_most_expensive_item(jewellery)}")
    print(f"Cheapest item: {find_cheapest_item(jewellery)}")
    print(f"Average price of an item: {statistics.mean(prices)}")
    quantiles = statistics.quantiles(prices)
    print(f"Quartiles: {quantiles}")
    print(f"Median: {statistics.median(prices)}")
    print_line()
    print(f"Standard deviation: {statistics.stdev(prices)}")
    print(f"Variance: {statistics.variance(prices)}")
    print_line()
    print(f"Interquartile range: {quantiles[2] - quantiles[0]}")
    print(f"Range: {prices[-1] - prices[0]}")
    print_line()
    return jewellery

def num_classes(prices):
    return math.ceil(math.sqrt(len(prices)))

def add_prices_to_classes_dict(prices, classes_dict):
    pass

def make_classes_dict(prices):
    min_price = min(prices)
    max_price = max(prices)
    range_width = max_price - min_price
    n_c = num_classes(prices)
    class_width = range_width / n_c
    classes_dict = {}
    
    print(f"Min price: {min_price}")
    print(f"Max price: {max_price}")
    print(f"Range width: {range_width}")
    print(f"Number of classes: {n_c}")
    print(f"Class width: {class_width}")
    print_line()
    for price in prices:
        class_index = int((price - min_price) / class_width)
        class_range = (class_index * class_width + min_price, (class_index + 1) * class_width + min_price)
        if class_range not in classes_dict:
            classes_dict[class_range]= []
        classes_dict[class_range].append(price)
            

    return add_frequencies(classes_dict)

def add_frequencies(classes_dict):
    num_items = sum([len(classes_dict[class_range]) for class_range in classes_dict])
    for class_range in classes_dict:
        classes_dict[class_range] = {
            "prices": classes_dict[class_range],
            "frequency": len(classes_dict[class_range]),
            "relative_frequency": len(classes_dict[class_range]) / num_items    
        }
        
    for class_range in classes_dict:
        cumulative_frequency = 0
        for class_range2 in classes_dict:
            if class_range2 <= class_range:
                cumulative_frequency += classes_dict[class_range2]["frequency"]
        classes_dict[class_range]["cumulative_frequency"] = cumulative_frequency
        classes_dict[class_range]["relative_cumulative_frequency"] = cumulative_frequency / num_items
        
    return classes_dict

def frequency_table(prices):
    classes_dict = make_classes_dict(prices)
    print(tabulate.tabulate(
        [
            [
                class_range[0],
                class_range[1],
                classes_dict[class_range]["frequency"],
                classes_dict[class_range]["relative_frequency"],
                classes_dict[class_range]["cumulative_frequency"],
                classes_dict[class_range]["relative_cumulative_frequency"]
            ] for class_range in classes_dict
        ],
        headers=[
            "Lower bound",
            "Upper bound",
            "Frequency",
            "Relative frequency",
            "Cumulative frequency",
            "Relative cumulative frequency"
        ]
    ))
    print_line()
    
    

def drugi():
    jewellery = prvi()
    prices = list(map(get_price, jewellery))
    prices.sort()
    frequency_table(prices)

if __name__ == "__main__":
    drugi()
    