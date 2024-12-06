from mpmath import mp

# Set precision
mp.dps = 5000  # Number of decimal places

# Calculate Pi
pi_value = mp.pi

# Print Pi value
print(f"Pi to {mp.dps} decimal places: {pi_value}")
