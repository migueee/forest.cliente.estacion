import time

while True:
    time.sleep(60)
    outfile = open('controlestacion.txt', 'a') # Indicamos el valor 'w'.
    
    fecha=time.strftime('%d-%m-%y')
    hora=time.strftime('%H:%M:%S')

    outfile.write('data'+fecha+'--'+hora+'\n')
    outfile.close()

    # Leemos el contenido para comprobar que ha sobreescrito el contenido.
    infile = open('controlestacion.txt', 'r')
    print('>>> Escritura de fichero concatenando su contenido.')
    print(infile.read())
    # Cerramos el fichero.
    infile.close()
