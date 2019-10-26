with open('KAI Logo Scaled 1.txt') as f:
    my_list = f.read().splitlines()


f= open("output.txt","w+")

for i in range(len(my_list)):
    if (my_list[i] == 'on' or my_list[i] == 'off' ):
        f.write(my_list[i])
        f.write("\n")
        
    else:
        x,y,z = my_list[i].split(',')

        x = float(x)
        y = float(y)
        z = float(z)

        f.write("%f,%f,%f\n" %(x,0,y))
    
f.close()
