def bubble_sort(items):
  """Sort left to right: the largest elements 'bubble' to the end."""
  n = len(items)
  for i in range(n - 1):
    swapped = False
    for j in range(n - 1 - i):
      if items[j] > items[j + 1]:
        items[j], items[j + 1] = items[j + 1], items[j]
        swapped = True
    if not swapped:  # no swaps means the list is already sorted
      break
  return items

def bubble_sort_right_to_left(items):
  """Sort right to left: the smallest elements 'bubble' to the start."""
  n = len(items)
  for i in range(n - 1):
    swapped = False
    for j in range(n - 1, i, -1):
      if items[j] < items[j - 1]:
        items[j], items[j - 1] = items[j - 1], items[j]
        swapped = True
    if not swapped:
      break
  return items