numbers = [1, 2, 3, 4, 5]
def rotate_first_second_item(sequnce):
    sequnce = [*sequnce[2:], sequnce[0]]
    return sequnce
print(rotate_first_second_item(numbers))