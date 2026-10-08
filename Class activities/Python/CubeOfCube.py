def Cube(num):
    return num*3

def cubeChecker(num):
    if num%3==0:
        return Cube(num)
    else:
        return False

print(cubeChecker(24))
print(cubeChecker(2409))