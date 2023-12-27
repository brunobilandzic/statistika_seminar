from read_data import read_data, get_price, get_item_count_by_type, find_most_expensive_item, find_cheapest_item
import statistics
from write_data import write_data, create_data

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
        
    print("\n----------------------------------------\n")
    
    prices = list(map(get_price, jewellery))
    
    print(f"Average price of an item: {statistics.mean(prices)}")
    print(f"Median price of an item: {statistics.median(prices)}")
    print(f"Mod: {statistics.mode(prices)}")
    
    print("\n----------------------------------------\n")   
    print("Characteristic five:\n")
    print(f"Most expensive item: {find_most_expensive_item(jewellery)}")
    print(f"Cheapest item: {find_cheapest_item(jewellery)}")
    print(f"Average price of an item: {statistics.mean(prices)}")
    quantiles = statistics.quantiles(prices)
    print(f"Quartiles: {quantiles}")
    print(f"Median: {statistics.median(prices)}")
    print(f"\n----------------------------------------\n"   )
    print(f"Standard deviation: {statistics.stdev(prices)}")
    print(f"Variance: {statistics.variance(prices)}")
    print(f"\n----------------------------------------\n"   )
    print(f"Interquartile range: {quantiles[2] - quantiles[0]}")
    print(f"Range: {prices[-1] - prices[0]}")

def main():
    prvi()

if __name__ == "__main__":
    main()
