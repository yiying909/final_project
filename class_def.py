class Cloth:
    def __init__(self, filename, typename) -> None:
        self.filename = filename
        self.typename = typename
        Cloth.clothes.append(self)
        pass

    def __repr__(self) -> str:
        return f'cloth {self.typename} in {self.filename}'

def create_cloth(data):
    clothes = []
    for lst in data:
        clothes.append(Cloth(lst[0],lst[1]))
    return clothes

def filter(data, typename):
    lst = [elem for elem in data if elem.typename == typename]
    return lst





