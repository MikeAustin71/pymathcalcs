from mpmath import mp

# Set precision to 1005 to ensure the first 1000 digits are accurate after rounding
mp.dps = 1005

# In mathematics, "natural logarithm" usually refers to ln(x).
# Since no argument was provided, I will calculate ln(2) and ln(10) as standard examples,
# or better, I will provide the constant 'e' and its log?
# Actually, the user likely wants the value of 'e' or a specific log.
# Usually "natural logarithm to 1000 digits" without a number implies ln(10) or ln(2) or just the number e.
# However, "natural logarithm" is a function. I will provide ln(2) as a representative value.
# Wait, if they say "natural logarithm", they might mean the constant e? No, e is the base.
# Let's assume they want the value of ln(10) or simply the value of e if they are confused.
# Re-reading: "natural logarithm to 1000 digits". This is ambiguous.
# Let's check common search queries for this phrase.
# Often people ask for "e to 1000 digits" or "ln 2 to 1000 digits".
# I'll provide ln(2) and explain.

# val_ln2 = mp.log(2)

val_ln5 = mp.ln('5')
print(f"ln(5): {val_ln5}")
