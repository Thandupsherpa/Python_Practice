# Define the bubble_sort function that takes a list of book heights
def bubble_sort(books_by_height):
    
    # Get the number of books in the list
    n = len(books_by_height)
    
    # Outer loop: Repeat the process n times to ensure full sorting
    for i in range(n):
        
        # Inner loop: Go through the list and compare each pair of neighbors

        for j in range(n - 1):
            
            # If the book on the left is taller than the one on the right, swap them
            if books_by_height[j] > books_by_height[j + 1]:
                
                books_by_height[j], books_by_height[j + 1] = books_by_height[j + 1], books_by_height[j]
    
   
    return books_by_height


print(bubble_sort([3, 2, 1]))
