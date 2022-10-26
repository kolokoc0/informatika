def checkio(heslo:str)->bool:
    if len(heslo)>=10 and heslo.isascii():
        status1,status2,status3 = False, False, False
        for i in heslo:
            if i.isdigit():
                status1 = True
                break;
        for i in heslo:
            if i.isupper():
                status2 = True
                break;
        for i in heslo:
            if i.islower():
                status3 = True
                break;

        if status1 and status2 and status3:
            return True
        else:
            return False
    else:
        return False
print(checkio("asssdsadksadlksaJ10"))
# DU vylepsit kod
