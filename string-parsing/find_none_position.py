names = ['Kamara', None, 'Mounika', 'Waleed']
total = 0
for name in names:
  total = total + 1
  if name is None:
    print('Empty space found in position:', total-1 )
    break
else:
  print('No empty spaces found')
