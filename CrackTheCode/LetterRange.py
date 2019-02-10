phrase = "NEPALSERBIASWITZERLANDBURKINAFASOKYRGYZSTANLUXEMBOURGSLOVAKIATAJIKISTANUGANDACHADANDAUSTRIA"

posT = []
rangesT = []

for i in range(0,len(phrase)):
    if phrase[i] == "T":
        posT.append(i)

print("Position of T ", posT)

for i in range(0, len(posT) -1):
    rangesT.append(posT[i+1]-posT[i])

print("Ranges of T ", rangesT)

print("-------------------------------")
#---------------------------------------#

ciphertext = "ETEVHTWGSAHGWYVPNKQOEGWYVPNKPDEPHWAOVWPFWNHANEVWXAVOAEAJEUXTAOWBTEVHTWGSAHGWYVPNQAOQVGTYHAVAXETOANFQEOIQPLANTEVHFYNSQVEBEOWSKNCKLOPEVTYJAUFWYNCOTWZESQEPERQSQOPEVYCEVHEGDEHEVHEYOPNQEEHWYFTKTEVHTWGSAHGWYVPNKQOWVAPDEPWVTKFWNHANOTEVHTWGSAHGWYVPNQAOPDANAENAWVTKPIWHWYFTKTEVHTWGSAHGWYVPNQAOQVPDAIWNTHWVAWBPDAUQOYLFASQOPEVIDEPQOPDAWPDANWVA"
posRandom = []
rangesRandom = []

for i in range(0,len(ciphertext)):
    if ciphertext[i] == "P":
        posRandom.append(i)

print("Position of P ", posRandom)

for i in range(0, len(posRandom) -1):
    rangesRandom.append(posRandom[i+1]-posRandom[i])

print("Ranges of P ", rangesRandom)

#So T in phrase corresponds to P in Ciphertext
ciphertextwithPhrase = "ETEVHTWGSAHGWYVPNKQOEGWYVPNKPDEPHWAOVWPFWNHANEVWXAVOAEAJEUXTAOWBTEVHTWGSAHGWYVPNQAOQVGTYHA(VAXETOANFQEOIQPLANTEVHFYNSQVEBEOWSKNCKLOPEVTYJAUFWYNCOTWZESQEPERQSQOPEVYCEVHEGDEHEVHEYOPNQE)EHWYFTKTEVHTWGSAHGWYVPNKQOWVAPDEPWVTKFWNHANOTEVHTWGSAHGWYVPNQAOPDANAENAWVTKPIWHWYFTKTEVHTWGSAHGWYVPNQAOQVPDAIWNTHWVAWBPDAUQOYLFASQOPEVIDEPQOPDAWPDANWVA"

