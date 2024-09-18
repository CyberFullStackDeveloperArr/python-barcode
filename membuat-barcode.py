import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    barcode_format = barcode.get_barcode_class('ean13')
    
    my_barcode = barcode_format(data, writer=ImageWriter())
    
    my_barcode.save(filename)

generate_barcode('333331212333434', 'barcode')
