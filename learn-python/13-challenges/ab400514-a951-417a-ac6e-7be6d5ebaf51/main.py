def area_sum(rectangles):
    result = 0
    for rectangle in rectangles:
        height = rectangle["height"]
        width = rectangle["width"]
        area = height * width
        result += area
    return result 
