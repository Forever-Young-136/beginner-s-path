results = {}

x = 0
y = 0
flag = True
while flag:
print('Привет!')
print('Здесь проходит голосование за самого красивого кота!')
name = input('\tКак тебя зовут?')
result = input('Отдай свой голос за выбранного кота. Напиши "альпинист" или "сатори"!')
#if result != 'альпинист' or 'сатори':
if result == 'альпинист':
x += 1
elif result == 'Альпинист':
x += 1
elif result == 'сатори':
y += 1
elif result == 'Сатори':
y += 1
else:
print(f'Данного кота {result.title()} нет в голосовании! Пожалуйста напишите корректное имя кота!')
result = input('Отдай свой голос за выбранного кота. Напиши "альпинист" или "сатори"!')
if result == 'альпинист':
x += 1
elif result == 'Альпинист':
x += 1
elif result == 'сатори':
y += 1
elif result == 'Сатори':
y += 1
else:
print(f'Данного кота {result.title()} нет в голосовании! Пожалуйста напишите корректное имя кота!')
result = input('Отдай свой голос за выбранного кота. Напиши "альпинист" или "сатори"!')
if result == 'альпинист':
x += 1
elif result == 'Альпинист':
x += 1
elif result == 'сатори':
y += 1
elif result == 'Сатори':
y += 1
results[name] = result
repeat = input('Следом за тобой есть еще люди, которые хотят проголосовать? (да/ нет)')
if repeat == 'нет':
flag = False
print('\t---Опрос завершен!---')
for name, result in results.items():
print(f'{name.title()} отдал(а) свой голос за кота по имени {result.title()}')
if x == 0:
i = 'голосов'
elif x == 1:
i = 'голос'
elif x <= 4:
i = 'голоса'
elif x >= 5:
i = 'голосов'
if y == 0:
p = 'голосов'
elif y == 1:
p = 'голос'
elif y <= 4:
p = 'голоса'
elif y >= 5:
p = 'голосов'

print(f'\n\tИтоги голосования!')
print(f'\n\tАльпинист набрал {x} {i}')
print(f'\n\tСатори набрал {y} {p}')