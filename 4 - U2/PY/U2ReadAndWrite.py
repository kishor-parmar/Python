# import the u2py module
import u2py

# Open file
try:
    cust_file = u2py.File("CUSTOMER")
except Exception as open_exception:
    print(f"Cannot Open CUSTOMER ")

# Read Record
try:
    cust_id = "1002"
    cust_rec = cust_file.read(cust_id)
except Exception as read_exception:
    print(f"Cannot Read {cust_id}")

print(f"xxxx B4 {cust_rec} xxxx")

# Update Fields
cust_rec.replace(1, 0, 0, "xxx Kishor xxx")
the_date = u2py.DynArray("20/02/2024").iconv("d4/")
cust_rec.replace(5, 0, 0, the_date)
print(f"xxxx {the_date} xxxx")

# Write Record
cust_file.write(cust_id, cust_rec)
print(f"xxxx Aft {cust_rec} xxxx")

# New record
new_custRec = u2py.DynArray()
new_custRec.insert(1, 0, 0, "Kishor")
new_custRec.insert(2, 0, 0, 34)
print(f"*** new_custRec= {new_custRec}")

# Write New Record
cust_file.write("NewRec", new_custRec)

# Convert Record to a Python List
cust_rec = u2py.DynArray(
    b"A" + u2py.FM + b"B" + u2py.FM + b"C1" + u2py.VM + b"C2" + u2py.FM + b"D"
)
new_rec = cust_rec.to_list()
for item in new_rec:
    print(item)

# Update List
new_rec[1] = "Kish"
print(f"xxxx new_rec =  {new_rec} xxxx")

# Delete a Record
cust_file.write("Temp", new_rec)

cust_file.delete("Temp")
