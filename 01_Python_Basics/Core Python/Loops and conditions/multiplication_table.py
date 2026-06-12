def print_multiplication_table(size):
    """Print a multiplication table from 1 to size."""
    if size < 1:
        raise ValueError("Size must be at least 1")

    # Print header row
    header = "    " + " ".join(f"{i:3d}" for i in range(1, size + 1))
    print(header)
    print("    " + "----" * size)

    # Print each row of the table
    for row in range(1, size + 1):
        row_values = [f"{row * col:3d}" for col in range(1, size + 1)]
        print(f"{row:3d} |" + " ".join(row_values))


if __name__ == "__main__":
    table_size = 10
    print(f"Multiplication table from 1 to {table_size}")
    print_multiplication_table(table_size)
