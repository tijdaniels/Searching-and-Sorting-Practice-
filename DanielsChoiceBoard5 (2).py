
def main():

    infile = open("colleges.csv", "r")
    colleges = infile.readlines()

    schools = []
    schools2 = []
    total = 0
    
    for x in range(len(colleges)):

        colleges[x] = (colleges[x].rstrip("\n"))
        
        colleges[x] = (colleges[x].split(","))

        schools2.append(colleges[x][0])

        if colleges[x][1] == "GA":
            schools.append(colleges[x][0])
            total += 1
    print(schools)
    print("number of schools in GA is ", total)
        

    #print(schools)3
    

    mergeSort(schools2)

    #print(colleges)

   

    Cname = (input("what school are you looking for? :"))

    search = binarySearch(schools2, 0, len(schools2)-1, Cname)

    if search != -1: 
        print(Cname, "is in the list!")

    else: 
        print(Cname, "is not present in list")

def mergeSort(schools2):

    if len(schools2) > 1:

        mid = len(schools2)//2
        l = schools2[:mid]
        r = schools2[mid:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                schools2[k] = l[i]
                i+=1
            else:
                schools2[k] = r[j]
                j+=1
            k+=1

        while i < len(l):
            schools2[k] = l[i]
            i+=1
            k+=1

        while j < len(r):
            schools2[k] = r[j]
            j+=1
            k+=1



def binarySearch (schools2, l, r, x):
            
  
    if r >= l: 
  
        mid = l + (r - l)//2
  
        if schools2[mid] == x: 

            return mid 
           
        elif schools2[mid] > x: 

            return binarySearch(schools2, l, mid-1, x) 
       
        else: 
            return binarySearch(schools2, mid + 1, r, x) 
  
    else: 

        return -1  
main()
    
