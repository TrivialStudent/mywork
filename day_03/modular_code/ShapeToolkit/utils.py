import shapes
def convertCm2ToM2(x):
    return x / 1000

def compareTwoShapes(x, y):
    if x.area > y.area:
        print(f"Shape 1 is larger than shape 2")
    else:
        print(f"Shape 1 is smaller than shape 2")
