def search_book(book_list, target_id):
    """
    Strategy: Linear Search
    Iterates through the list of book IDs sequentially from beginning to end.
    
    Time Complexity: O(n) where n is the number of books in the list.
    Space Complexity: O(1) auxiliary space.
    """
    for index, book_id in enumerate(book_list):
        if book_id == target_id:
            return index  # Return the index/position if found
    return -1  # Return -1 if the book is not found

# --- Input Identification ---
# 1. book_list: The list of book IDs maintained by the library
library_books = [101, 305, 208, 412, 507, 99]

# 2. target_id: The specific book ID to search for
search_id = 412

print("=== Library Book Search Program ===")
print(f"Input List of Books: {library_books}")
print(f"Input Book ID to Search: {search_id}")
print("-" * 35)

# --- Execution & Output Identification ---
position = search_book(library_books, search_id)

if position != -1:
    # output: position of the book (using 1-based indexing for user readability)
    print(f"Output: Book is available! Found at Position: {position + 1} (Index: {position})")
else:
    # output: book not found
    print("Output: Book not found")
