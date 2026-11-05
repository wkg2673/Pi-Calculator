from mpmath import mp

mp.dps = 5000  # Number of digits of pi to calculate

pi_value = mp.pi

print(f"Pi to {mp.dps} decimal places: {pi_value}")
