from read_data import read_data, get_price, get_item_count_by_type, find_most_expensive_item, find_cheapest_item
import statistics, math, tabulate, matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

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
    return classes_dict

def treci():
    jewellery = prvi()
    prices = list(map(get_price, jewellery))
    prices.sort()
    classes_dict = frequency_table(prices)


    plt.subplot(3, 1, 1)
    
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    bins = [class_range[0] for class_range in classes_dict]  + [max(prices)]
    plt.hist(prices, bins, edgecolor='black')
    
    plt.xticks(bins, rotation='vertical')


    plt.subplot(3, 1, 2)
    class_midpoints = [(class_range[0] + class_range[1]) / 2 for class_range in classes_dict]
    frequencies = [classes_dict[class_range]['frequency'] for class_range in classes_dict]  
    
    plt.title('Frequency Polygon')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.plot(class_midpoints, frequencies, marker='o', linestyle='-')
    plt.xticks(class_midpoints, rotation='vertical')
    
    plt.subplot(3, 1, 3)
    plt.title('Relative Frequency Histogram')
    plt.xlabel('Price')
    plt.ylabel('Relative Frequency')


    total_count = sum(frequencies)
    relative_frequencies = [freq / total_count for freq in frequencies]

    bins = [class_range[0] for class_range in classes_dict]

    
    plt.bar(bins, relative_frequencies, width=350, edgecolor='black', align='edge')
    plt.xticks(bins, rotation='vertical')
    
    
    plt.tight_layout() 
    plt.show()    
    

def drugi():
    jewellery = prvi()
    prices = list(map(get_price, jewellery))
    prices.sort()
    frequency_table(prices)
    
    
def calculate_confidence_interval(prices, confidence):
    mean = np.mean(prices)
    std_dev = np.std(prices)
    n = len(prices)
    t = stats.t.ppf((1 + confidence) / 2, n - 1) # Z-score for the desired confidence level

    margin_of_error = t * (std_dev / np.sqrt(n))
    confidence_interval = (mean - margin_of_error, mean + margin_of_error)

    return confidence_interval

def cetvrti():
    jewellery = prvi()
    prices = list(map(get_price, jewellery))
    confidence_intervals = {        
        '90%': calculate_confidence_interval(prices, 0.90),
        '95%': calculate_confidence_interval(prices, 0.95),
        '99%': calculate_confidence_interval(prices, 0.99)
    }

    for confidence, interval in confidence_intervals.items():
        print(f"The {confidence} confidence interval is {interval}")
    print_line()
if __name__ == "__main__":
    cetvrti()
    