from itertools import count


countries = ["United States", "Canada", "United Kingdom", "Brazil", "Nigeria"]

print(f'The total number of countries: {len(countries)}')
print(f'Here is a sorted() list: {sorted(countries)}')
print(f'Here is a reserved sorted() list: {sorted(countries, reverse=True)}')
countries.reverse()
print(f'Here is a reverse() list: {countries}')
countries.sort()
print(f'Here is a sort() list: {countries}')
countries.sort(reverse=True)
print(f'Here is a reversed sort() list: {countries}')
