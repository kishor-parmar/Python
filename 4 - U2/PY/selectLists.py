import u2py

mcmd = u2py.Command("SELECT VOC TO 1")
mcmd.run()

myList = u2py.List(1)
for x in range(0, 10):
    id = myList.next()
    print(id)

myList.clear()
