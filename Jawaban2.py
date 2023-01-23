def convert(s):
    '''convert to integer'''
    try:
        x = int(s)
        print("Konversi berhasil!, x = ", x)
    except ValueError:
        print("Konversi gagal!")
        x = -1
    return x
