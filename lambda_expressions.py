# Lambda Expressions Example

# Lambda function inside the filter()
student_name = ['Marie', 'Bobi', 'John', 'Andy',
                'Sally', 'Anthony', 'Willy', 'Aaron', 'Ross']

result = list(filter(lambda x: (x[0] == 'A'), student_name))

print(result)


# Match the username with their email using zip()
username = ['marie_coyman', 'bobi_garcia', 'john_smith', 'andy_tartakowsky',
            'sally_simon', 'anthony_hopkins', 'willy_deniro', 'aaron_jason', 'ross_kane']
email = ['marie_coyman@mail.com', 'bobi_garcia@mail.com', 'john_smith@mail.com', 'andy_tartakowsky@mail.com',
         'sally_simon@mail.com', 'anthony_hopkins@mail.com', 'willy_deniro@mail.com', 'aaron_jason@mail.com', 'ross_kane@mail.com']

print(list(zip(username, email)))


# Square using Lambda function inside the map()
print(list(map(lambda num: num**2, [1, 2, 3])))


# Sort the numbers in tuples by having in mind second index
a = [(0, 2), (5, 2), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])

print(a)


# Find duplicates using Lambda function
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
