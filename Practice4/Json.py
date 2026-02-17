import json

# Load the JSON data from the file
with open('sample-data.json') as f:
    data = json.load(f)

# Print the Header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 50, "-" * 20, "-" * 6, "-" * 6)

# Iterate through the imdata list to extract attributes
for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    descr = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    
    # Print the formatted row
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
