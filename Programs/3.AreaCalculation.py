#Area Calculation
def rectangle():
    l=int(input("Enter the length of the rectangle: "))
    b=int(input("Enter the breadth of the rectangle: "))
    area=l*b
    print("The area of the rectangle is ", area)
def triangle():
    b=int(input("Enter the base of the triangle: "))
    h=int(input("Enter the height of the triangle: "))
    area=(1/2)*b*h
    print("The area of the triangle is ", area)
def circle():
    r=int(input("Enter the radius of the circle: "))
    area=3.14*r**2
    print("The area of the circle is ", area)

while True:
    choice = int(input(
        "Area calculation program\n1. Area of rectangle\n2. Area of triangle\n3. Area of circle\n4. exit\nEnter your choice: "))
    if choice==1:
        rectangle()
    elif choice==2:
        triangle()
    elif choice==3:
        circle()
    else:
        break
