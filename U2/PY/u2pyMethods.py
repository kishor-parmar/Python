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


# Write Record
def write_rec(file, id, rec):
    file.write(id, rec)
    return None


# Delete Record
def delete_rec(file, id):
    file.delete(id)
    return None


# Display Record
def display_rec(rec):
    new_rec = rec.to_list()
    cnt = 1
    for item in new_rec:
        print(f"<{cnt}> {item}")
        cnt += 1
