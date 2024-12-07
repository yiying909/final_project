class Cloth:
    def __init__(self, filename, subtypename, typename=None) -> None:
        self.filename = filename
        self.typename = typename
        self.subtypename = subtypename
        # Cloth.clothes.append(self)
        pass

    def __repr__(self) -> str:
        return f'cloth {self.typename} {self.subtypename} in {self.filename}'

def create_cloth(data):
    clothes = []
    for lst in data:
        # var = lst
        clothes.append(Cloth(lst[0],lst[1]))
    return clothes

def filter(data, typename):
    lst = [elem for elem in data if elem.subtypename == typename]
    # lst = []
    # for elem in data:
    #     if elem.typename == typename:
    #         lst.append(elem)
    return lst






