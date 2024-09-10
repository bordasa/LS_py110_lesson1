def transactions_for(item_id, list_of_transactions):
    return [transaction 
            for transaction in list_of_transactions
            if transaction["id"] == item_id]

def is_item_available(item_id, all_transactions):
    item_transactions = transactions_for(item_id, all_transactions)

    actual_quantity = 0

    for transaction in item_transactions:
        if transaction["movement"] == 'in':
            actual_quantity += transaction["quantity"]
        elif transaction["movement"] == 'out':
            actual_quantity -= transaction["quantity"]
        else:
            print("Error in Transaction Log")
    
    return actual_quantity > 0


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True