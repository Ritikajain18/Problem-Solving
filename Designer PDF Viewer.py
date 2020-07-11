'''
When you select a contiguous block of text in a PDF viewer, the selection is highlighted
with a blue rectangle. In this PDF viewer, each word is highlighted independently. 
In this challenge, you will be given a list of letter heights in the alphabet and a string. 
Using the letter heights given, determine the area of the rectangle highlight in mm2 assuming 
all letters are 1mm wide.

For example, the highlighted word = torn. Assume the heights of the letters are t=2, o=1, r=1, n=1.
The tallest letter is 2 high and there are 4 letters. The hightlighted area will be 2*4=8 mm
so the answer is 8.'''

def get_rect_height(word, height_arr):
    height = 0
    for c in word:
        height = max(height, height_arr[ ord(c) - ord("a") ])
        #ord(character) gives the ascii value
    return height

heights = [int(x) for x in input().split()]    #scan heights
word = input()

print(len(word) * get_rect_height(word, heights))

