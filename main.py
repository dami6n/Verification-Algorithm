import os
import info_coding_scheme
import minimum_cover_algorithm
import certificate


# Ask user for file name
opt = input("Introduzca el numero de ejercicio de la practica que desea probar (opciones validas = 1 o 2): ")
print("----------------------------------")
errorMsg=""

try:

    if opt==1:
        #Ask the user for the input file.
        file_name = raw_input("Introduzca el nombre del archivo de entrada con la informacion del ejemplar: ")
        print("----------------------------------")

        #Ask the user for the name of the result file.
        output_file_name = raw_input("Introduzca el nombre del archivo de salida en donde se guardara el certificado generado: ")
        print("----------------------------------")

        # Check if file exists in project folder
        if os.path.isfile(file_name):
            # Open file and read its contents
            with open(file_name, "r") as file:
                contents = file.read()
        else:
            errorMsg="File not found."
            assert os.path.isfile(file_name)

        # print(contents)
        # List with finite set "S", collection of subsets "C", and number "k"
        componentList = contents.split("&&")

        # Validate that the input of the file has the correct format: S&&C&&k
        if (len(componentList)!= 3):
            errorMsg="Se ingreso una cadena con formato incorrecto."
            assert len(componentList)== 3

        # Assign value of "S"
        set_s=componentList[0].split(",")

        # Assign value of "C"
        collection_c=componentList[1].split("#")

        # Assign value of "k"
        value_k=componentList[2]


        # Generamos certificado aleatorio
        cert = certificate.generate_random_certificate(set_s, collection_c, int(value_k))
        cer=""
        for x in cert:
            cer=cer + str(x)

        # Abre el archivo en modo escritura
        with open(output_file_name, 'w') as archivo:
            # Escribe la cadena de texto en el archivo
            archivo.write(cer)

    elif opt==2:
        #Ask the user for the input file.
        file_name = raw_input("Introduzca el nombre del archivo de entrada con la informacion del ejemplar: ")
        print("----------------------------------")

        #Ask the user for the name of the result file.
        certificate_file_name = raw_input("Introduzca el nombre del archivo con el certificado a probar: ")
        print("----------------------------------")


         # Check if file exists in project folder
        if os.path.isfile(file_name):
            # Open file and read its contents
            with open(file_name, "r") as file:
                contents = file.read()
        else:
            errorMsg="File not found."
            assert os.path.isfile(file_name)




         # Check if file exists in project folder
        if os.path.isfile(certificate_file_name):
            # Open file and read its contents
            with open(certificate_file_name, "r") as file:
                contents_certificate = file.read()
        else:
            errorMsg="File not found."
            assert os.path.isfile(certificate_file_name)



        # print(contents)
        # List with finite set "S", collection of subsets "C", and number "k"
        componentList = contents.split("&&")

        # Validate that the input of the file has the correct format: S&&C&&k
        if (len(componentList)!= 3):
            errorMsg="Se ingreso una cadena con formato incorrecto."
            assert len(componentList)== 3

        # Assign value of "S"
        set_s=componentList[0].split(",")

        # Assign value of "C"
        collection_c=componentList[1].split("#")

        # Assign value of "k"
        value_k=componentList[2]

        aux = info_coding_scheme.print_coding_scheme_info(set_s, collection_c, value_k, list(contents_certificate))




    # if opt==2:
    #     info_coding_scheme.print_coding_scheme_info(set_s, collection_c,value_k)
    # elif opt==3:
    #     minimum_cover_algorithm.min_cover_alg(set_s, collection_c, value_k)
except:
    print("Error:" + errorMsg)

