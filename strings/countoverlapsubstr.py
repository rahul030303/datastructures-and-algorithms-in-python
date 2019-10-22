# str1 = "HelloHiiHelloHiiHey"
# print(str1.count('hey'.capitalize()))

def CountOccurrences(string, substring): 
    # Initialize count and start to 0 
    count = 0
    start = 0
  
    # Search through the string till 
    # we reach the end of it 
    while start < len(string): 
        #  Check if a substring is present from 
        # 'start' position till the end 
        flag = string.find(substring, start) 
        print(flag)
  
        if flag != -1: 
            # If a substring is present, move 'start' to 
            # the next position from start of the substring 
            start = flag + 1
  
            # Increment the count 
            count += 1
        else: 
            # If no further substring is present 
            # return the value of count 
            return count 
  
# Driver Code 
string = "GeeksforGeeksforGeeksforGeeks"
print(CountOccurrences(string, "GeeksforGeeks")) 
    