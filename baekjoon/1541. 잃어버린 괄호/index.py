input_f = input()
f = input_f.split('-')

result = 0
if input_f[0] == '-':
    result -= sum(map(int, f[0].split('+')))
else:
    result += sum(map(int, f[0].split('+')))

for formular in f[1:]:
    result -= sum(map(int, formular.split('+')))

print(result)
