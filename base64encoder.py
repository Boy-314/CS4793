fileName = input("Input file name: ");
with open(fileName,"rb") as binary_file:
    data = binary_file.read();
lengthInput = len(data);
bits = "";
for i in range(lengthInput):
    bits += '{0:08b}'.format(data[i]);
splitBy = 6;
splitBits = [bits[i:i+splitBy] for i in range(0,len(bits),splitBy)];
base64 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"];
lengthOutput = len(splitBits);
if(len(splitBits[lengthOutput-1]) <= 6):
    padding = 6 - len(splitBits[lengthOutput - 1]);
    for i in range(padding):
        splitBits[lengthOutput - 1] += "0";
output = "";
for i in range(lengthOutput):
    output += base64[int(splitBits[i],2)];
if(len(output) % 4 == 0):
    addEquals = 0;
else:
    addEquals = 4 - (len(output) % 4);
for i in range(addEquals):
    output += "=";
outputFileName = fileName + ".BASE64";
fileOutput = open(outputFileName,"w+");
fileOutput.write(output);
fileOutput.close();
