# List Processing - Find None Position

This script checks a list for missing values (`None`) and prints the 0-based index/position where the first one is found.

## What it does
- Loops through a list of names
- Counts positions manually
- Prints the position if `None` is found, or a message if none exist
- Uses `for-else` to handle the "no match" case

## Code file
`find_none_position.py`

## Example run
```python
names = ['Kamara', 'Tuba', 'Mounika', None]
# Output: Empty space found in position: 3
