#Wordle solver
from asyncio.windows_events import NULL
from operator import truediv
f= open ("wordle-nyt-answers-alphabetical.txt", "r")
output = f.read().splitlines()
f.close()
inputs = [
    ["blank","blank","green","yellow","blank"],
    ["green","blank","yellow","yellow","blank"],
    ["green","green","green","blank","blank"],
    ["blank","green","green","green","blank"],
    ["green","blank","green","blank","blank"]

]
filtered=[]
answers=[]
for input in inputs:
    green=[]
    yellow=[]
    for index, value in enumerate(input):
        if value=="green":
            green.append(index)
    for index, value in enumerate(input):
        if value=="yellow":
            yellow.append(index)
    filtered=[]
    for i in range(0,len(output)):
        for j in range(i+1,len(output)):
            if i!=j:
                green_match = 0
                yellow_match=0
                if len(green)>0 and len(yellow)==0:
                    for position in green:
                        if output[i][position] == output[j][position]:
                            green_match+=1
                        if green_match == len(green):
                            filtered.append(output[i])
                            filtered.append(output[j])
                            filtered=list(dict.fromkeys(filtered))#remove duplicates
                elif len(green)==0 and len(yellow)>0:
                    for position in yellow:
                        if output[i][position] in output[j] and output[i][position] != output[j][position]:
                            yellow_match+=1
                        if yellow_match == len(yellow):
                            filtered.append(output[i])
                            filtered.append(output[j])
                            filtered=list(dict.fromkeys(filtered))#remove duplicates

                elif len(green)>0 and len(yellow)>0:
                    for g_position in green:
                        if output[i][g_position] == output[j][g_position]:
                            green_match+=1
                    for y_position in yellow:
                        if output[i][y_position] in output[j] and output[i][y_position] != output[j][y_position]:
                            yellow_match+=1
                    if yellow_match == len(yellow) and green_match ==len(green):
                        filtered.append(output[i])
                        filtered.append(output[j])
                        filtered=list(dict.fromkeys(filtered))#remove duplicates             
    answers.append(filtered)
#    
def consolidate(*args):
    if len(args) == 1:
        return args[0]

    sets = [set(lst) for lst in args]
    common = set.intersection(*sets)
    return list(common)

consolidated_list = consolidate(*answers)
consolidated_list.sort()
with open('filtered wordle list.txt', 'w') as f:
    for word in consolidated_list:
        f.write(f'{word}\n')
#
#def actual(viable):
#    shortlist=[]
#    for k in range (0,len(viable)):
#        if "a" not in viable[k] and "d" not in viable[k] and "m" not in viable[k] and "i" in viable[k][1] and "n" in viable[k][2] and "b" not in viable[k] and "g" not in viable[k] and "e" not in viable[k]:
#            shortlist.append(viable[k])
#    return shortlist
#print(actual(consolidated_list))
