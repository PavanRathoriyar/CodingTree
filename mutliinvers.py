def modInverse(a, m):
     
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
 
 
# Driver Code
a=int(input())
m =int(input())
 
# Function call
print(modInverse(a, m))
