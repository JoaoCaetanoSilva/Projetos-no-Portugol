medida = int(input('Metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('-' * 12)

if mm < 999:
    print('mm: {}'.format(mm))
if mm > 1000:
    print('mm: {:,.0f} mil'.format(mm))
if mm > 1000000:
    print('mm: {:,.0f} milhoes'.format(mm))
else:
    print('mm: {:,.0f}'.format(mm))

if cm < 999:
    print('cm: {}'.format(cm))
if cm > 1000:
    print('cm: {} mil'.format(cm))
if cm > 1000000:
    print('cm: {} milhoes'.format(cm))
else:
    print('cm: {:,.0f}'.format(cm))

if dm < 999:
    print('dm: {}'.format(dm))
if dm > 1000:
    print('dm: {} mil'.format(dm))
if dm > 1000000:
    print('dm: {} milhoes'.format(dm))
else:
    print('dm: {:,.0f}'.format(dm))

print('m: {:2}'.format(m))

if dam < 999:
    print('dam: {}'.format(dam))
else:
    print('dam: {:,.0f}'.format(dam))

if hm < 999:
    print('hm: {}'.format(hm))
else:
    print('hm: {:,.0f}'.format(hm))

if km < 999:
    print('km: {}'.format(km))
else:
    print('km: {:,.0f}'.format(km))