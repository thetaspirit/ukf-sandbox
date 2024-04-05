with open('log57-filter.csv', 'r') as f:
	filt = f.readlines()[1:]

with open('log57-covar.csv', 'r') as f:
	cov = f.read()

lines = []

parts = cov.split(',')
parts = parts[1:]

while len(parts) > 0:
	lines.append(','.join(parts[:9]))
	parts = parts[9:]

print(len(lines))
print(len(filt))
assert(len(lines) == len(filt))

result = ''

for i in range(len(lines)):
	t = filt[i].split(',')[0]

	result += t + ',' + lines[i] + '\n'

with open('log57-covar-fixed.csv', 'w') as f:
	f.write(result)

