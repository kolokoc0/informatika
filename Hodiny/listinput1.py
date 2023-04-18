def vypis_typy(zoznam):
    for i in zoznam:
        if type(i) == str:
            print(f"{i} = retazec")
        elif type(i) == int or type(i) == float:
            print (f"{i} = cislo")
        else:
            print (f"{i} = iny typ")
vypis_typy([12, 'x', None, 3.14, [], range(5), '123'])

