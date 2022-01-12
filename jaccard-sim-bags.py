#Jaccard Similarity of Bags
  
#Returns the number of elements of x and y intersection
def find_intersection_size(x: list, y: list) -> int:
    size = 0
    fewest, most = (x, y) if len(x) < len(y) else (y, x)
    most = most.copy()
    for value in fewest:
        try:
            most.remove(value)
        except ValueError:
            pass
        else:
            size += 1
    return size

#Return the number of elements in both x and y.
def find_union_size(x: list, y: list) -> int:
    return len(x) + len(y)

#Get the Jaccard similarity of two bags
def find_jaccard_similarity_of_bags(x: list, y: list) -> float:
    intersection_size = find_intersection_size(x, y)
    union_size = find_union_size(x, y)
    return (intersection_size/union_size)  

if __name__ == "__main__":
