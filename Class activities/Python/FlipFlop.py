def palindrome(t):
    e=len(t)-1
    s=0

    while s<e:
        if (t[s]!=t[e]):
            return False
        s+=1
        e-=1
    return True

t1=(1,2,3,2,1)
if palindrome(t1):
    print("The tuple is Flip Flop🩴")
else:
    print("The tuple is not flip flop ❌🩴")