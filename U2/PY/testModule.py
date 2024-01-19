from u2pyMethods import *


# Main
def main():
    cust_file = open_file("CUSTOMER")

    if cust_file:
        cust_id = "1002"
        cust_rec = read_rec(cust_file, cust_id)

    if cust_rec:
        update_rec(cust_rec, 2, 0, 0, "Hello World")
        update_rec(cust_rec, 2, 2, 3, "I am Here")
        update_rec(cust_rec, 2, 2, 4, "I am a svm")
    else:
        cust_rec = u2py.DynArray()
        insert_rec(cust_rec, 1, 2, 0, "Kishor")
        insert_rec(cust_rec, 1, 3, 0, 34)
        update_rec(cust_rec, 2, 0, 0, "Hello World")

    write_rec(cust_file, cust_id, cust_rec)
    display_rec(cust_rec)
    print(f"cust_rec = '{cust_rec}'")

    cmd = u2py.Command("SELECT CUSTOMER TO 1")
    cmd.run()
    sel_list = u2py.List(1)

    for item in range(0, 5):
        id = sel_list.next()
        if len(str(id)) > 0:
            print(id)
            cust_rec = read_rec(cust_file, id)
            display_rec(cust_rec)
            print()

    sel_list.clear()


if __name__ == "__main__":
    main()
