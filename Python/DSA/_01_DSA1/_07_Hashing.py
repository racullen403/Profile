"""

Hashing is the technique of mapping large data sets to tabular indexes, using a hash function. It allows us to lookup,
retrieve and update data in O(1), whereas a linear or binary search would take O(n) and O(logn) time respectively.

We represent a hash table as a structure that stores key-value pairs:
    - Key: the unique integer that is used for indexing the data
    - Value: the data associated with the key

In a hash table, the new index is processed using the keys, and the element corresponding to the key is stored at the
new index in the table, this is hashing.

    E.G.    Suppose we have key=k and data=val, for some hash table, we use the associated hash function
            h(x)=i to find the index i, where we will store key:value pair

                so, h(k) = i, then at hash_table[i] we insert k:val


Hash Collisions:

    When a hash function h(x)=i produces the same index i for different keys k, we have a hash collision. There are
    different methods we can introduce to resolve this issue.

    - Chaining: when we get the same hash for multiple elements, we store the elements at that hash using a linked list

    - Open Addressing: Instead of storing multiple elements at the same hash, we use a method to find the next valid
    index to store data at.


        Linear Probing: This method finds a new hash by simply looking to the next available position in the table

            h(x, i) = (h(x, 0) + i) % m    where i runs [0, ..., m-1] and m is the size of the table

            - so if a collision occurs at h(k, 0) we simply look to the next index, and continue until a spot found.

            - One of the issues with this is that clusters of adjacent slots will be filled, so when inserting
            elements or looking for elements, we may need to look through large amounts of data, adding to the
            operation times.


        Quadratic Probing: This is similar to linear probing however we increase the search in quadratic steps

            h(x, i) = (h(x, 0) + a*i + b*(i^2)) % m, where m is size of table, a and b are constants

            - This helps address the large clusters of adjacent slots, however may require much larger hash tables
            to fit the data at the correct hash.


        Double Hashing: If a collision occurs, we apply another hash function

            h(x, i) = (h(x, 0) + i*h'(x)) % m, where m is size of table and h'(x) is second hash function


A good hashing method is one that aims to reduce the number of collisions:

    Division Method: h(x) = x % m, where m is the size of the table

    Multiplication method: h(x) = floor(m((a*x) % 1)) where a is some constant between 1 and 0 and modulo 1 returns
        the fractional part of a number (3.456 % 1 -> 0.456)



"""

