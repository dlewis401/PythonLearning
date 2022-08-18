places = ["Flordia", "Canada", "America", "Disney World", "Dubai"]

print(f'The original list: {places}')
print(f'The sorted() list: {sorted(places)}')
print(f'The original list again: {places}')
print(f'The sorted() list: {sorted(places, reverse=True)}')
places.sort()
print(f'The sorted list: {places}')
places.sort(reverse=True)
print(f'The sorted-reversed list: {places}')
places.reverse()
print(f'The reversed list: {places}')
places.reverse()
print(f'The re-reversed list: {places}')
