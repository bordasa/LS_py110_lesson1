#Problem 1
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# asc_list = sorted(lst)
# desc_list = sorted(lst, reverse = True)

# print(asc_list)
# print(desc_list)

#Problem 2
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst.sort()
# print(lst)

# lst.sort(reverse = True)
# print(lst)

#Problem 3
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# asc_lst = sorted(lst, key = str)
# desc_lst = sorted(lst, key = str, reverse = True)

# print(asc_lst)
# print(desc_lst)

#Problem 4

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def clean_publish_data(book):
    return (int(book['published']), book['author'], book['title'])

books_sorted = sorted(books, key = clean_publish_data)
print(books_sorted)