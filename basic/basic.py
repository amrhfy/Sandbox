# BASIC DATA TYPE
text_string = "Ammar Hafiy"
num_int = 25
num_float = 595.25

# SEQUENCE TYPE

## CHANGEABLE AND MOST USED SEQUENCE TYPE
list_car = ["Proton", "Perodua", "Nissan", "Bugatti", "Tesla"]

## UNCHANGEABLE || ALLOW DUPLICATE || ORDERED
tuple_food = ("Apple", "Banana", "Fried Rice", "Strawberry", "Banana")

## UNCHANGEABLE
set_brand = {"AMD", "Intel", "Nvidia", "Fantech"}

## DICTIONARY || CHANGEABLE AS OF 3.7
dict_app = {
    "name": "Whatsapp",
    "version": 5.6,
    "platform": {"Android", "IOS", "Windows", "MAC"}
}

# FOR LOOP - MOSTLY USE FOR ITERATION
count = 1
for a in set_brand:
    print(count, ". ", a)
    count += 1

