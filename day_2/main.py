# A = Taş      X = kayıp   Makas      1 puan
# B = Kağıt    Y = beraber Kağıt      2 puan
# C Makas      Z = kazan   Makas      3 puan

puan = 0
 
cumleler = []
with open("tas_kagit_kalem.txt", "+r") as dosya:
    for satir in dosya:
        print(satir)

        rakip, ben = satir[0], satir[2]
        match ben:
            case "X":
                match rakip:
                    case "A":
                        puan += 0 + 3

                    case "B":
                        puan += 0 + 1

                    case "C":
                        puan += 0 + 2 
            case "Y":
                match rakip:
                    case "A":
                        puan += 3 + 1

                    case "B":
                        puan += 3 + 2

                    case "C":
                        puan += 3 + 3
            case "Z":
                match rakip:
                    case "A":
                        puan += 6 + 2

                    case "B":
                        puan += 6 + 3

                    case "C":
                        puan += 6 + 1

print(f"puan: {puan}")
