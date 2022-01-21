from typing import List


def get_author_ids(names: str) -> List[int]:
    items = names.split(", ")
    last_names = items[::2]
    names = []

    for name in last_names:
        if "Angara" == name:
            names.append(1)
        elif "Binay" == name:
            names.append(2)
        elif "Cayetano" == name:
            names.append(3)
        elif "De Lima" == name:
            names.append(4)
        elif "Dela Rosa" == name:
            names.append(5)
        elif "Drilon" == name:
            names.append(6)
        elif "Gatchalian" == name:
            names.append(7)
        elif "Go" == name:
            names.append(8)
        elif "Gordon" == name:
            names.append(9)
        elif "Hontiveros" == name:
            names.append(10)
        elif "Lacson" == name:
            names.append(11)
        elif "Lapid" == name:
            names.append(12)
        elif "Marcos" == name:
            names.append(13)
        elif "Pacquiao" == name:
            names.append(14)
        elif "Pangilinan" == name:
            names.append(15)
        elif "Pimentel" == name:
            names.append(16)
        elif "Poe" == name:
            names.append(17)
        elif "Recto" == name:
            names.append(18)
        elif "Revilla Jr." == name:
            names.append(19)
        elif "Sotto III" == name:
            names.append(20)
        elif "Tolentino" == name:
            names.append(21)
        elif "Villanueva" == name:
            names.append(22)
        elif "Villar" == name:
            names.append(23)
        elif "Zubiri" == name:
            names.append(24)

    return names
