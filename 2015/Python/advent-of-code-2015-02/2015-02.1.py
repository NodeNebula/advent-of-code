total = 0

with open("input.txt") as file:
    for line in file.readlines():
        dim = line.strip().split("x")

        dim1 = int(dim[0])*int(dim[1])
        dim2 = int(dim[1])*int(dim[2])
        dim3 = int(dim[2])*int(dim[0])

        if dim1 <= dim2 and dim1 <= dim3:
            smallest = dim1
        elif dim2 <= dim1 and dim2 <= dim3:
            smallest = dim2
        elif dim3 <= dim1 and dim3 <= dim2:
            smallest = dim3

        total += 2*dim1 + 2*dim2 + 2*dim3 + smallest

print(total)
