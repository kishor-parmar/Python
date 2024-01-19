import u2py
import sys


# Open files
def open_file(x):
    try:
        open_file = u2py.File(x)
        return open_file
    except u2py.U2Error as open_exception:
        print(f"Cannot Open {x}")
        print(open_exception)
        input()
        sys.exit(0)


# Read Records
def read_rec(file, id):
    try:
        rec = file.read(id)

    except u2py.U2Error:
        rec = u2py.DynArray("")

    finally:
        return rec


# Update Fields
def update_rec(rec, field_no, mv, sm, data):
    rec.replace(field_no, mv, sm, data)
    return rec


# Insert Fields
def insert_rec(rec, field_no, mv, sm, data):
    rec.insert(field_no, mv, sm, data)
    return rec


# Display Record
def display_rec(rec):
    new_rec = rec.to_list()
    cnt = 1
    for item in new_rec:
        print(f"<{cnt}> {item}")
        cnt += 1


# Main
def main():
    cust_file = open_file("CUSTOMER")
    print(cust_file.name)
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

    display_rec(cust_rec)
    print(f"cust_rec = '{cust_rec}'")


if __name__ == "__main__":
    main()
