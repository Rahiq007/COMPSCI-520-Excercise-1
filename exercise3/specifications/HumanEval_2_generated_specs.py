# Generated Specifications for HumanEval_2: truncate_number
# Problem: Return the decimal part of a positive floating point number
# Signature: def truncate_number(number: float) -> float
# Let 'res' denote the expected return value

# Specification 1: Result is the decimal part
assert res == (number - int(number))  # Result equals the number minus its integer part

# Specification 2: Result range constraint
assert 0 <= res < 1  # Decimal part must be between 0 (inclusive) and 1 (exclusive)

# Specification 3: Reconstruction property
assert number == int(number) + res  # Original number can be reconstructed from integer part and result

# Specification 4: Non-negativity
assert res >= 0  # Decimal part is always non-negative

# Specification 5: Integer input handling
assert (number == int(number)) <= (res == 0)  # If input is an integer, result should be 0