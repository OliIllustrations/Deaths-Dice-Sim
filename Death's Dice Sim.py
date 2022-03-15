import random
import statistics

times = []

immortal = 0
chance = 2
counter = 0

i=input("How many iterations? ")
t=input("Threshold? ")

for n in range(0,int(i)):
    stop = 0
    while stop == 0:
        a = random.randint(1,chance)
        b = random.randint(1,chance)
        if a == 1 and b == 1 or counter == int(t):
            times.append(counter)
            print(int(i)-n,counter)
            if counter == int(t):
                immortal = immortal + 1
            chance = 2
            counter = 0
            stop = 1
        else:
            counter = counter + 1
            chance = chance + 2

average = (sum(times)/len(times))
mode = ((max(set(times), key = times.count)))
immortal = immortal / (int(i))

my_file = open("Death's Dice Data.txt", "w")

my_file.write("iterations:\n")
my_file.write(str(i))
my_file.write("\nthreshold:\n")
my_file.write(str(t))
my_file.write("\naverage:\n")
my_file.write(str(average))
my_file.write("\nmode:\n")
my_file.write(str(mode))
my_file.write("\nmedian:\n")
my_file.write(str(statistics.median(times)))
my_file.write("\nchance of immortality:\n")
my_file.write(str(immortal))
my_file.write("\ndata:\n")
my_file.write(str(times))

my_file.close()

    
    

    
