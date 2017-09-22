Ivan ={
    "name": "ivan",
    "age": 34,
    "children":[{
        "name": "vasja",
        "age": 22,
    },{
        "name": "petja",
        "age": 19,
    }],
}
darja = {
     "name": "darja",
     "age": 41,
     "children": [{
         "name": "kirill",
         "age": 21,
     },{
         "name": "pavel",
         "age": 15,
     }],
}
emps = [Ivan, darja]
for names in emps:
    for child in names["children"]:
        if child["age"]>18:
            print (names["name"])
            break
