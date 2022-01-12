#Jaccard Similarity of Bags

from collections import Counter
  
#Returns the number of elements of x and y intersection
def find_intersection_size(x: list, y: list) -> int:
    intersection = list((Counter(x) & Counter(y)).elements())
    return len(intersection)

#Return the number of elements in both x and y.
def find_union_size(x: list, y: list) -> int:
    return len(x) + len(y)

#Get the Jaccard similarity of two bags
def find_jaccard_similarity_of_bags(x: list, y: list) -> float:
    intersection_size = find_intersection_size(x, y)
    union_size = find_union_size(x, y)
    return (intersection_size/union_size)  

if __name__ == "__main__":
