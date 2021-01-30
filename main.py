# Fetch data from search.txt and pallete.txt and store it in search and pallete arrays respectively

def fetch_data():
    with open('search.txt', 'r') as f:                      #Opening search.txt
        search = f.read().split()                           #Store the colors from search.txt in search as array
    with open('pallete.txt', 'r') as r:                     #Opening pallete.txt
        pallete = r.read().split()                          #Store the colors from pallete.txt in pallete as array
    return ([search,pallete])


#Function for converting the hex colors to rgb and return an array contaning seperate values of r,g,b(   [r,g,b]  )
def splitColors(hex):
    r = int(hex[1:3],16)                                    #Convert the red part of the hex color from hex to decimal
    g = int(hex[3:5],16)                                    #Convert the green part of the hex color from hex to decimal
    b = int(hex[5:7],16)                                    #Convert the blue part of the hex color from hex to decimal
    return [r,g,b]

#Function for converting the rgb array returned by splitColors to their XYZ values and returns X,Y,Z as seperate values (  [X,Y,Z]  )
def convert_RGBtoXYZ(hex):

    #Algorithm for converting rgb to XYZ

    rgb = splitColors(hex)
    R=  int(rgb[0])/255
    G = int(rgb[1])/255
    B = int(rgb[2])/255
    print(R,G,B)
    if(R > 0.04045):
        R = ((R+0.055) / 1.055) ** 2.4 
    else:
        R = R/12.92
    if(G > 0.04045):
        G = ((G+0.055) / 1.055) ** 2.4 
    else:
        G = G/12.92
    if(B > 0.04045):
        B = ((B+0.055) / 1.055) ** 2.4 
    else:
        B = B/12.92

    R = R * 100
    G = G * 100
    B = B * 100

    X = R * 0.4124 + G * 0.3576 + B * 0.1805
    Y = R * 0.2126 + G * 0.7152 + B * 0.0722
    Z = R * 0.0193 + G * 0.1192 + B * 0.9505
    return([X,Y,Z])

#Function for converting XYZ returned by convert_RGBtoXYZ() to CIELAB values using D65 Standard 2degree illuminants and returns L,A,B as seperate values (  [L,A,B]  )
def CIELAB(hex):

    #Algorithm for converting XYZ to LAB

    XYZ = convert_RGBtoXYZ(hex)
    X = XYZ[0] / 95.0489
    Y = XYZ[1] / 100
    Z = XYZ[2] / 108.8840

    if X > 0.008856:
        X = X ** (1/3)
    else:
        X = (7.787 * X) + (16/116)
    if Y > 0.008856:
        Y = Y ** (1/3)
    else:
        Y = (7.787 * Y) + (16/116)
    if Z > 0.008856:
        Z = Z ** (1/3)
    else:
        Z = (7.787 * Z) + (16/116)

    L = (116 * Y) -16
    A = 500 * (X - Y)
    B = 200 * (Y - Z)
    return(L,A,B)

#Calculates the distance between 2 hex colors using LAB values returned by CIELAB()
def distance(hex1,hex2):
    lab1=CIELAB(hex1)       #Store the lab value for the first hex color(hex1)
    lab2=CIELAB(hex2)       #Store the lab value for the second hex color(hex2)
    l1=lab1[0]              #L value of hex1
    a1=lab1[1]              #A value of hex1
    b1=lab1[2]              #B value of hex1
    l2=lab2[0]              #L value of hex2
    a2=lab2[1]              #A value of hex2
    b2=lab2[2]              #B value of hex2
    return int((((l2 - l1)**2 + (a2 - a1)**2 + (b2 - b1)**2) ** (1/2)))         #Return the eucledian distance between two hex colors


#Compare the search array with the pallete array and store it in results.txt
def result():
    f = open("results.txt", "w")                #Open the results text file
    search = fetch_data()[0]
    pallete = fetch_data()[1]
    least = []                          
    for i in range(len(search)):                #Iterate through the search array
        least.append(distance(search[i],pallete[i]))    #Array to store the least distance between colors initialized with a default value
        least_val = pallete[i]                          #For storing closest color found from the database. In this line it is initialized with a default value from the pallete which will be change in the next loop if a closer color is found
        for j in range(len(pallete)):                   #Iterate through pallete array
            if(distance(search[i],pallete[j])<least[i]):    #Check if the distance between two colors is lesser than the value of least[i]
                least[i] = distance(search[i],pallete[j])   #Store the least distance in least[i]
                least_val = pallete[j]                      #Store the closest color from pallete
        f.write(least_val)                                  #Write the closest color to results.txt
        f.write('\n')                                       #Change to the next line after each write
    f.close()                                   #Closing the results text file
    return 0

result()                    #Calling the result function


