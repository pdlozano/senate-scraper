from typing import List


def get_author_ids(names: str) -> List[int]:
    items = names.split(", ")
    last_names = items[::2]
    names = []

    for name in last_names:
        if name == "Angara":
            names.append(1)
        elif name == "Binay":
            names.append(2)
        elif name == "Cayetano":
            names.append(3)
        elif name == "De Lima":
            names.append(4)
        elif name == "Dela Rosa":
            names.append(5)
        elif name == "Drilon":
            names.append(6)
        elif name == "Gatchalian":
            names.append(7)
        elif name == "Go":
            names.append(8)
        elif name == "Gordon":
            names.append(9)
        elif name == "Hontiveros":
            names.append(10)
        elif name == "Lacson":
            names.append(11)
        elif name == "Lapid":
            names.append(12)
        elif name == "Marcos":
            names.append(13)
        elif name == "Pacquiao":
            names.append(14)
        elif name == "Pangilinan":
            names.append(15)
        elif name == "Pimentel":
            names.append(16)
        elif name == "Poe":
            names.append(17)
        elif name == "Recto":
            names.append(18)
        elif name == "Revilla Jr.":
            names.append(19)
        elif name == "Sotto III":
            names.append(20)
        elif name == "Tolentino":
            names.append(21)
        elif name == "Villanueva":
            names.append(22)
        elif name == "Villar":
            names.append(23)
        elif name == "Zubiri":
            names.append(24)

    return names
