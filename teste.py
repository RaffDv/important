
import ipaddress
file = open("input.csv", "r")

output = open("insert.sql", "w")


def calcMask(ip):
    rede = ipaddress.IPv4Network(ip)
    return rede


for line in file:
    line = line.replace('\'', '\\\'')[0:-1]
    fixline = ''
    dentroDeAspa = False
    for letra in line:
        if (letra == '"'):
            dentroDeAspa = not dentroDeAspa
        else:
            if (letra == "," and not dentroDeAspa):
                fixline += "\t"
            else:
                fixline += letra

    fields = fixline.split("\t")

    masks = calcMask(fields[0])
    fields.append(masks[0])
    fields.append(masks[-1])

    newLine = ''

    for field in fields:

        newLine += f"'{field}',"

    newLine = 'INSERT INTO aux_IPv4Blocks values (DEFAULT,' + \
        newLine[0:-1] + ');\n'

    output.writelines(newLine)

output.close()
