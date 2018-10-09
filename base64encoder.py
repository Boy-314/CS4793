fileName = input("Input file name: ");
with open(fileName,"rb") as binary_file:
    data = binary_file.read();
    print(data);
