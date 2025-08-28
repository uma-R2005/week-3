def flatten(nested):
    return (
        item
        for sublist in nested
        for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])
    )

# Example usage
nested_list = [1, [2, [3, 4], 5], [6, [7, [8]]]]

# Convert generator to a list
flat_list = list(flatten(nested_list))

# Print the result
print("Flattened list:", flat_list)
