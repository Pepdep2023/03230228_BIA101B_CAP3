filename = "228.txt"

with open(filename, "r") as f:
  total_sum = 0  # Initialize total_sum inside the block
  for line in f:
    # Check if line is empty
    if not line:
      continue

    # Get first and last digits (handle cases with less than 2 digits)
    first_digit = int(line[0]) if line[0].isdigit() else 0
    last_digit = int(line[-1]) if line[-1].isdigit() else 0

    # Combine and add to total
    total_sum += first_digit * 10 + last_digit

print(f"Sum of combined first and last digits: {total_sum}")



