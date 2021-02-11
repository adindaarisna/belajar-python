def kembalian(uang,lembar):
    nmilo,ncola,nsosro,naqua=0,0,0,0
    sisa=uang*lembar
    if sisa//9000>0:
        nmilo=sisa//9000
        sisa=sisa%9000
        print(f'{nmilo} milo')
    if sisa//7000>0:
        ncola=sisa//7000
        sisa=sisa%7000
        print(f'{ncola} cola')
    if sisa//5000>0:
        nsosro=sisa//5000
        sisa=sisa%5000
        print(f'{nsosro} sosro')
    if sisa//2000>0:
        naqua=sisa//2000
        sisa=sisa%2000
        print(f'{naqua} aqua')
    if sisa<2000:
        print(f'sisa kemabalian {sisa}')

print('Hasil: ')
kembalian(5000, 2)