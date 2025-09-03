# ✅↓ Write your code here ↓✅
def number_of_bottles():
    song = ""
    for i in range(99,-1,-1):
        if i == 0:
            song += "No more bottles of milk on the wall, no more bottles of milk. Go to the store and buy some more, 99 bottles of milk on the wall."
        elif i == 1:
            song += "1 bottle of milk on the wall, 1 bottle of milk. Take one down and pass it around, no more bottles of milk on the wall.\n"
        elif i == 2:
            song += "2 bottles of milk on the wall, 2 bottles of milk. Take one down and pass it around, 1 bottle of milk on the wall.\n"
        else:
            song += f"{str(i)} bottles of milk on the wall, {str(i)} bottles of milk. Take one down and pass it around, {str(i-1)} bottles of milk on the wall.\n"
    print(song)

number_of_bottles()