"""
We saw previously that by storing information (indexing) on the position of items in the collection,
we were able to improve the performance of our algorithm by using a binary search method O(logn).

We will take this a step further, and build a data structure that allows us to lookup an item
in O(1) time.

For this, we need to know where the item is stored in the collection when we go to look for it, that way
we can do a single comparison and see if it is there.


Hash Table:

    These use "slots" named by integer values to store items.

    e.g         0     1     2     3
            [ None, None, None, None ]      Could be our hash table, it is simply a lookup table

    The important part is the mapping between an item and the slot that item belongs in, this is
    determined by the Hash Function.


Hash Functions:

    The Hash Function will take an item in the collection, and return an integer value in the range
    of the slots in the hash table.

    A basic hash function is the "remainder method", we simply divide the item by the size of the
    hash table, and return the remainder as the hash value, this tells us where to store the item
    in the table.

    Note that this modulo arithmetic is typically involved in most hash functions as is allows us
    to ensure hash values remain within the range of the hash table.


Load Factor:

    This is simply the number of items in the hash table divided by the size of the hash table


Searching:

    When we want to search for an item, we find its hash value using the hash function, and then go
    to this slot in the hash table and check if the item is there. This process is O(1) constant.


Limitations:

    It is quite obvious that this only works if every item uniquely maps to a slot in the table,
    otherwise we get "collisions"/"clashes" which create problems.

    Luckily we do not require perfect hash functions to still gain performance efficiency.

    For small numbers, a solution might be to increase the size of the hash table as required,
    however for large numbers this is not feasible, we might only be storing a relatively small
    amount of values but the required table might have to be billions of slots long which would
    cause massive storage issues.


The goal is to create hash functions that minimise the number of collisions, while being
easy to compute and evenly distribute the items throughout the table.



Folding Method:

    This hash function takes a number and splits it into even size pieces (except possibly the end
    piece), and then adds them together to get the resulting hash value.

    e.g     take a phone number 90 654 733, we split into groups of 2 and add
            90+65+47+33=235, so we store this number 90654733 at slot 235

    If the hash table was only 10 slots then we could do 235%10=5 and store in slot 5



Mid-Square Method:

    In this method, you first square the item, then extract some portion of the resulting digits,
    and perform our remainder method to find the slot.

    e.g 44^2=1936, extract middle number, 93, then 93%10=3, store at slot 3.


We can construct hash functions for character based items like strings. Using ord("c") we get the
numeric value of c.


Collision Resolution:

    When 2 items hash to the same slot we say a collision has occurred, we must have a way of
    of placing this item into the table, this is called collision resolution.

    Probing:
        One method might be to look into the table and sequentially go through the slots until we
        find one that is empty, then place the item in it. Note if we reach the end we go to the start,
        that way we do not miss any slots before the collision slot. This process is called
        "open addressing" as it tries to find the next open slot, going slot by slot is an open
        addressing technique called "linear probing".

        - A problem with linear probing is when we come to searching for an item, if it is not found,
        we are forced to check every slot after the initial hash value until we either find the item
        or find an empty slot. This is a major problem due to clustering, the items form long
        sequential blocks that must be gone through before we know if it is or isn't there.

        One way to deal with the clustering problem in linear probing is to extend this technique. Instead
        of looking at the next slot sequentially, we skip a number of slots, this will more evenly
        distribute the items and hopefully reduce clustering.

        The general name for collision resolution techniques is "rehashing".

        e.g     hashvalue=hash(item)            this results in a collision so we rehash
                newhashvalue=rehash(hashvalue)  if this results in a collision we apply again

                rehash(value) = (value+1)%size_of_table     linear probing
                rehash(value) = (value+3)%size_of_table     "plus 3" probing

                Note: the skip value in the rehash must be one that allows all positions in the
                hash table to be visited. To ensure this, it is wise to always use a prime number
                for the size of the table.

        - A variation of the constant value skip in probing is to vary the amount we skip by each time.
        This can be done with "quadratic probing".

            rehash(value) = (value + i^2) where i is the number of successive rehashes we are on


    Chaining:

        An alternative technique to probing is to allow the slots in the table to hold a reference to
        some collection of items (chain), this means we can store more than one item at a slot. When
        a collision occurs, the item is still stored at its correct hash value, it will now just
        be in some position in the chain of items at that slot.

        This cause searching to increase in time as more items are added into a chain.

        The advantage to this is that on average, it is likely to be more efficient search times,
        however, in a worst case scenario you may have a very long lookup due to a long chain.


Note that in python, we can simply use the dictionary {} as our hash map. When creating our own
abstract data type, we might use 2 lists, one to store the key, and the other to store the
items, the same position (index/hashvalue) in both lists refers to the mapping key:value
"""
