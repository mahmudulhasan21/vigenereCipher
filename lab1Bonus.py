
outputfile = open("output1Bouns.txt", "w") 

i = 0
with open("key1.txt") as keyfile:
  k= keyfile.read()
  print (k)
  keylength = len(k)
  print(keylength)

  keyvalue={}
  for i in range(keylength):
      x = ord(k[i])
      if (x >= 65 and x <= 90):
          x = x-65
      else:
          x = x-97+26
        
      keyvalue[i] = x
      print(keyvalue[i])
      i= i+1
      
      
i=0
with open("output1.txt") as inputfile:
  while True:
    c = inputfile.read(1)
    if not c:
      print ("End of file")
      keyfile.close()
      inputfile.close()
      outputfile.close()
      break
    print ("Read a character:", c)
    if (i == keylength):
        i=0
    x = ord(c)
    if (x >= 65 and x <= 90):
        x = x-65
    else:
        x = x-97+26
    print (x)
    y = x - keyvalue[i]
    i = i+1
    print (y)
    z = y % 52
    print (z)
    
    if (z >= 0 and z <= 25):
          z = z+65
    else:
          z = z+71
    output = chr(z)
    print (output)
    outputfile.write(output)



