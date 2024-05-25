# https://github.com/Pepdep2023/03230228_BIA101B_CAP3
# Phuntsho Dema
# BBI 'B'
# 03230228
########################################################################
# References:
# https://medium.com/@promoterseo.com/python-read-text-file-in-visual-studio-code-how-to-read-a-text-file-e672fbd2024c
# https://www.google.com/gasearch?q=how%20to%20read%20txt%20file%20in%20python%20using%20vscide&tbm=&source=sh/x/gs/m2/5#fpstate=ive&vld=cid:20840800,vid:XPO6ITK2Ecc,st:0
# https://stackoverflow.com/questions/55191397/vscode-read-file-from-current-folder-where-py-file-is
########################################################################
# Solution
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

print(f"Sum of first digit and last digit from each 10,000 lines: {total_sum}")

# Solution I got in my terminal
# Sum of first digit and last digit from each 10,000 lines: 217780






