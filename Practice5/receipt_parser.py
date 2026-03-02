import re
import json
from pathlib import Path

FILE_PATH = "raw.txt"


def normalize_price(price: str) -> float:
    """Convert '1 526,00' -> 1526.00"""
    return float(price.replace(" ", "").replace(",", "."))


def parse_receipt(text: str) -> dict:
    # --- Product names ---
    product_pattern = re.compile(r"\d+\.\n(.+)")
    products = product_pattern.findall(text)

    # --- Prices ---
    price_pattern = re.compile(r"\n([\d ]+,\d{2})\nСтоимость")
    prices_raw = price_pattern.findall(text)
    prices = [normalize_price(p) for p in prices_raw]

    # --- Total ---
    total_match = re.search(r"ИТОГО:\n([\d ]+,\d{2})", text)
    total = normalize_price(total_match.group(1)) if total_match else None

    # --- Payment method ---
    payment_match = re.search(r"(Банковская карта)", text)
    payment_method = payment_match.group(1) if payment_match else "Unknown"

    # --- Date & time ---
    datetime_match = re.search(
        r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})",
        text
    )
    datetime = datetime_match.group(1) if datetime_match else None

    return {
        "products": products,
        "item_prices": prices,
        "total_amount": total,
        "payment_method": payment_method,
        "datetime": datetime
    }


def main():
    text = Path(FILE_PATH).read_text(encoding="utf-8")
    parsed_data = parse_receipt(text)

    print(json.dumps(parsed_data, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()
