import time

counter=0

hours =   int(input("Aantal uren: "))
print("")

minutes = int(input("Aantal minuten: "))
print("")

seconds = int(input("Aantal seconds: "))
print("")



h = hours

m = minutes

s = seconds



def klok(h, m, s):
    print('{:02d}:{:02d}:{:02d}'.format(h,m,s))


while True:
    klok(hours, minutes, seconds)

    time.sleep(0.2)


    seconds += 1


    counter+=1



    for uren in range(hours,24):
        time.sleep(1)
        hours = 0
        if(hours == 24):
            minutes = 0
            seconds = 0
        for minuten in range(minutes,60):
            time.sleep(1)
            minutes = 0
            for secondes in range(seconds,60):
                time.sleep(1)
                seconds = 0
                klok(uren, minuten, secondes)



