
nama_makanan = ['nasi','bubur','lalapan','tahu']

pesan = input('Apa yang anda pesan :')

print ('==================Nama-nama makanan===========================')
for n in nama_makanan:
    print('-',n)

if pesan in nama_makanan:
    print (' makanan yang anda pesan ada')
else:
    print ('makanan yang anda pesan tidak ada')

