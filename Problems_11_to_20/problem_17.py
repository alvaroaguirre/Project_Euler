# Problem 17
# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 

units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def round_up_10(x):
    return (int(x/10)+1)*10

def round_up_100(x):
    return (int(x/100)+1)*100
    
def to_string(x):
    
    if x - 100 < 0:
        if x - 19 <= 0:
            return units[x-1]
        else:
            if x % 10 == 0:
                return tens[int(x/10)-2]
            else:
                a = tens[int(x/10)-2]
                b = units[(10 - (round_up_10(x) - x))-1] 
                return a + ' ' + b
    else:
        if x % 100 == 0:
            return to_string(int(x/100)) + ' hundred'
        else:
            deci = x/100
            a = to_string(int(deci)) + ' hundred and '
            b = to_string(round((round(deci - int(deci),2))*100))
            return a + b

def count_letters(x):
    return len(x) - x.count(' ')

total = 0
for i in range(1,1000):
    total += count_letters(to_string(i))

total += count_letters('one thousand')
print(total)
