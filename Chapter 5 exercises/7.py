def main():
    class_a_sold=int(input("How many class A tickets were sold? "))
    class_b_sold=int(input("How many class B tickets were sold? "))
    class_c_sold=int(input("How many class C tickets were sold? "))
    a_total=class_a_sold*20
    b_total=class_b_sold*15
    c_total=class_c_sold*10
    total=sum(a_total,b_total,c_total)
    print(""+str(total)+" dollars were made in ticket sales")
def sum(a,b,c):
    result=a+b+c
    return result
main()


