#dictionory
#membuat dictionary daftar kontak
kontak   = {'ari': '081267888', 'dina': '087677776'}
print ( "| nama | nomor telepon |" )
print ( 21 * "=")
print ( " #ari  | " , kontak ['ari'])
print ( " #dina | " , kontak ['dina'])

#tampilkan kontaknya ari
print ( "ari", '081267888')

#tambah kontak baru
kontak['riko']='087654544'
print (kontak)

#ubah kontak dina
kontak['dina'] = '088999776'
print(kontak['dina'])

#tampilkan semua nama
print (kontak.keys())

#tampilkan semua nomor
print (kontak.values())

#tampilkan daftar nama dan nomornya
print (kontak.items())

#hapus kontak dina
del kontak['dina']
print (kontak.items())
 