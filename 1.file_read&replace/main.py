def readandreplace(filename,original,replace):

    with open(filename,"r") as file:
        data=file.read()                  # reading original
        print(data)
        data=data.replace(original,replace)
    with open(filename, "w") as file:
        file.write(data)
    with open(filename,"r") as file:
        print(file.read())                # reading updated

filename="example.txt"
original="placement"
replace="screening"

readandreplace(filename,original,replace)