import re
import json

def parse_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Extract Date and Time
    date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', content)
    time_match = re.search(r'(\d{2}:\d{2}:\d{2})', content)
    
    # 2. Extract Total Amount
    total_match = re.search(r'ИТОГО:\s+([\d\s,]+)', content)
    total_val = float(total_match.group(1).replace(' ', '').replace(',', '.')) if total_match else 0

    # 3. Extract Payment Method
    payment_method = "Unknown"
    if "Банковская карта" in content:
        payment_method = "Банковская карта"
    elif "Наличные" in content:
        payment_method = "Наличные"

    # 4. Extract Items (Regex for "Name \n Quantity x Price \n Total \n Стоимость \n Total")
    # This pattern captures the indexed lines and the calculation row below it
    item_pattern = re.compile(r'\d+\.\n(.*?)\n([\d,]+)\s+x\s+([\d\s,.]+)\n([\d\s,.]+)', re.DOTALL)
    
    items = []
    for match in item_pattern.finditer(content):
        name = match.group(1).strip().replace('\n', ' ')
        qty = float(match.group(2).replace(',', '.'))
        price_unit = float(match.group(3).replace(' ', '').replace(',', '.'))
        total_item = float(match.group(4).replace(' ', '').replace(',', '.'))
        
        items.append({
            "name": name,
            "quantity": qty,
            "price_per_unit": price_unit,
            "total": total_item
        })

    return {
        "date": date_match.group(1) if date_match else None,
        "time": time_match.group(1) if time_match else None,
        "payment_method": payment_method,
        "items": items,
        "total_amount": total_val
    }

# Execute and Print
if __name__ == "__main__":
    # Assuming 'raw.txt' is in the same directory
    try:
        data = parse_receipt('raw.txt')
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except FileNotFoundError:
        print("Error: raw.txt not found.")
