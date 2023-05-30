frames=int(input("Please enter the number of Page frames: "))
length=int(input("Enter the length of reference String: "))
string=[]
page_frame=[]
for i in range(length):
    no=int(input("Please enter the {0} character of the reference string: ".format(i+1,{0})))
    string.append(no)

print("The entered reference string is ",string)

#initailizing none values for page frames 
for i in range(frames):
    page_frame.append(None)

print("Here, None refers that the page frame in empty")
First_in=0
page_hit=0
continue_outer_loop=False
for i in string:
    for j in page_frame:
        if j==i:
            page_hit=page_hit+1
            continue_outer_loop=True
    #continue if element already in page frame        
    if continue_outer_loop:
        continue_outer_loop=False
        print(i," already in memory no fault for this reference")
        continue
    else:
        #replacing intial none or empty frames    
        if None in page_frame:
            for k in page_frame:
                if k==None:
                    page_frame[page_frame.index(k)]=i
                    break
        else:
            page_frame[First_in]=i
            #get the top element to remove     
            if First_in==(frames-1):
                First_in=0
            else:
                First_in=First_in+1
            
            
    print("Page Frame: ",page_frame,"  for reference: ",i )

#calculate page faults
page_fault=len(string)-page_hit
print("Page fault : ",page_fault)       
               


