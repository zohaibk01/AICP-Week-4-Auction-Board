class AuctionItem:
    def __init__(self, item_number, description, reserve_price):
        self.item_number = item_number
        self.description = description
        self.reserve_price = reserve_price
        self.highest_bid = 0
        self.num_bids = 0



    def place_bid(self, buyer_number, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.num_bids += 1
            print(f"Bid placed successfully for item {self.item_number}.")

    def is_sold(self):
        return self.highest_bid >= self.reserve_price


def setup_auction():
    items = []
    num_items = int(input("Enter the number of items in the auction (must be at least 10): "))
    if num_items < 10:
        print("Error: There must be at least 10 items in the auction.")
        return []

    for i in range(num_items):
        item_number = input(f"Enter item number for item {i+1}: ")
        description = input(f"Enter description for item {i+1}: ")
        reserve_price = float(input(f"Enter reserve price for item {i+1}: $"))
        item = AuctionItem(item_number, description, reserve_price)
        items.append(item)

    return items


def buyer_bids(items):
    while True:
        item_number = input("Enter item number you want to bid on (or 'exit' to quit): ")
        if item_number == 'exit':
            break

        found_item = False
        for item in items:
            if item.item_number == item_number:
                found_item = True
                print(f"Item Number: {item.item_number}")
                print(f"Description: {item.description}")
                print(f"Current Highest Bid: ${item.highest_bid}")
                buyer_number = input("Enter your buyer number: ")
                bid_amount = float(input("Enter your bid amount: $"))
                item.place_bid(buyer_number, bid_amount)
                break

        if not found_item:
            print("Item not found in the auction.")


def end_auction(items):
    total_fee = 0
    num_sold = 0
    num_not_met_reserve = 0
    num_no_bids = 0

    print("\nAuction Results:")
    for item in items:
        if item.is_sold():
            sold_fee = item.highest_bid * 0.1
            total_fee += sold_fee
            num_sold += 1
            print(f"Item {item.item_number} sold for ${item.highest_bid}. Auction company fee: ${sold_fee:.2f}")
        else:
            if item.num_bids == 0:
                num_no_bids += 1
                print(f"Item {item.item_number} received no bids.")
            else:
                num_not_met_reserve += 1
                print(f"Item {item.item_number} did not meet the reserve price with highest bid: ${item.highest_bid}")

    print("\nTotal auction company fee from sold items: ${:.2f}".format(total_fee))
    print(f"Number of items sold: {num_sold}")
    print(f"Number of items not meeting reserve price: {num_not_met_reserve}")
    print(f"Number of items with no bids: {num_no_bids}")


def main():
    print("Auction Setup:")
    items = setup_auction()

    if items:
        print("\nBuyer Bidding Process:")
        buyer_bids(items)

        print("\nEnd of Auction:")
        end_auction(items)


if __name__ == "__main__":
    main()
