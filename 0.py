num_of_pieces:int = input('num_of_pieces : ')
height:int = input('height : ')
width:int = input('width : ')
height = int(height)
width = int(width)
num_of_pieces = int(num_of_pieces)/2
total = height + width

print(round(width/num_of_pieces)/2)
print(round(height/num_of_pieces)/2)
