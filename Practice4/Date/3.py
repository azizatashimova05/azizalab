from datetime import datetime

# Current time with microseconds
dt = datetime.now()

# Drop microseconds
dt_no_micros = dt.replace(microsecond=0)

print("Original:", dt)
print("Modified:", dt_no_micros)
