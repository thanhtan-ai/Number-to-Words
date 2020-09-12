t = int(input())

for l in range(t):
    n = str(input())
    thousands = ["", "Thousand", "Million", "Billion", "Trillion"]
    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
             "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    lisn = []
    for i in range(len(n), 0, -3):
        lisn += [n[i - 3:i]]
    if len(n) % 3 != 0:
        lisn[len(n) // 3] = n[:len(n) - (len(n) // 3) * 3]

    for i in range(len(lisn)):
        lisn[i] = str(int(lisn[i]))
    for i in range(len(lisn)):
        if len(lisn[i]) == 1:
            lisn[i] = units[int(lisn[i])]
        elif len(lisn[i]) == 2:
            if int(lisn[i]) < 20:
                lisn[i] = teens[int(lisn[i][1])]
            else:
                if int(lisn[i][1]) == 0:
                    lisn[i] = tens[int(lisn[i][0])] + ' ' + 'Zero'
                elif int(lisn[i][1]) != 0:
                    lisn[i] = tens[int(lisn[i][0])] + ' ' + units[int(lisn[i][1])]
        elif len(lisn[i]) == 3:
            if lisn[i][1] == '0':
                if lisn[i][2] == '0':
                    lisn[i] = units[int(lisn[i][0])] + ' ' + 'Hundred'
                elif lisn[i][2] != '0':
                    lisn[i] = units[int(lisn[i][0])] + ' ' + 'Hundred' + ' ' + units[int(lisn[i][2])]
            else:
                lis = units[int(lisn[i][0])] + ' ' + 'Hundred' + ' '
                str_ = int(lisn[i][1:])
                if str_ < 10:
                    lis += units[str_]
                elif 10 <= str_ < 20:
                    lis += teens[int(str(str_)[1])]
                elif str_ >= 20:
                    if str(str_)[1] == 0:
                        lis += tens[int(str(str_)[0])]
                    else:
                        lis += tens[int(str(str_)[0])] + ' ' + units[int(str(str_)[1])]
                lisn[i] = lis
    for i in range(len(lisn)):
        if lisn[i] != '':
            lisn[i] += " " + thousands[i]
    lisn.reverse()
    i = 0
    while i < len(lisn):
        if lisn[i] == '':
            lisn.remove(lisn[i])
            i += -1
        i += 1
    if len(lisn) == 0:
        print('0:','Zero')
    else:
        print(n,':',*lisn)
