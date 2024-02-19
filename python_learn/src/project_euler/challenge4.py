is_found = False

answer = 0

for x in range(999, 100, -1):
    for y in range(999, 100, -1):
        number = x*y
        if number > 99999:
            hundred_thousands = int(number/100000) % 10 
            ten_thousands = int(number/10000) % 10 
            thousands = int(number/1000) % 10
            hundreds = int(number/100) % 10
            tens = int(number/10) % 10
            units = number % 10
            if hundred_thousands == units and ten_thousands == tens and thousands == hundreds:
                answer = max(answer , number)

print(number)
  
  