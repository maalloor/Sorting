from sorting import bubble_sort, bubble_sort_right_to_left

def main():
  numbers = [5, 2, 9, 1, 7, 3, 8, 4, 6]
  print("Original list:", numbers)
  print("Left to right:", bubble_sort(numbers.copy()))
  print("Right to left:", bubble_sort_right_to_left(numbers.copy()))

if __name__ == "__main__":
    main()