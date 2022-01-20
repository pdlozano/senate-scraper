from typing import List


def get_author_ids(names: str) -> List[int]:
    items = names.split(", ")
    last_names = items[::2]
    names = []

    for name in last_names:
        if "Angara".lower() in name.lower():
            names.append(1)
        elif "Binay".lower() in name.lower():
            names.append(2)
        elif "Cayetano".lower() in name.lower():
            names.append(3)
        elif "De Lima".lower() in name.lower():
            names.append(4)
        elif "Dela Rosa".lower() in name.lower():
            names.append(5)
        elif "Drilon".lower() in name.lower():
            names.append(6)
        elif "Gatchalian".lower() in name.lower():
            names.append(7)
        elif "Go".lower() in name.lower():
            names.append(8)
        elif "Gordon".lower() in name.lower():
            names.append(9)
        elif "Hontiveros".lower() in name.lower():
            names.append(10)
        elif "Lacson".lower() in name.lower():
            names.append(11)
        elif "Lapid".lower() in name.lower():
            names.append(12)
        elif "Marcos".lower() in name.lower():
            names.append(13)
        elif "Pacquiao".lower() in name.lower():
            names.append(14)
        elif "Pangilinan".lower() in name.lower():
            names.append(15)
        elif "Pimentel".lower() in name.lower():
            names.append(16)
        elif "Poe".lower() in name.lower():
            names.append(17)
        elif "Recto".lower() in name.lower():
            names.append(18)
        elif "Revilla Jr.".lower() in name.lower():
            names.append(19)
        elif "Sotto III".lower() in name.lower():
            names.append(20)
        elif "Tolentino".lower() in name.lower():
            names.append(21)
        elif "Villanueva".lower() in name.lower():
            names.append(22)
        elif "Villar".lower() in name.lower():
            names.append(23)
        elif "Zubiri".lower() in name.lower():
            names.append(24)

    return names
