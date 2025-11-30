# 1. Python Sets
print("--- 1. Set Creation ---")
my_set = {"apple", "banana", "cherry", "orange"}
print(f"Original Set: {my_set}")
print("-" * 30)
print("--- 2. Access Set Items (Checking for a specific item) ---")
if "banana" in my_set:
    print("Yes, 'banana' is in the set.")
else:
    print("No, 'banana' is not in the set.")
print("-" * 30)
print("--- 3. Add Set Items ---")
my_set.add("grape")
print(f"Set after using add('grape'): {my_set}")
another_fruit_list = ["mango", "kiwi"]
my_set.update(another_fruit_list)
print(f"Set after using update(['mango', 'kiwi']): {my_set}")
print("-" * 30)
print("--- 4. Remove Set Items ---")
try:
    my_set.remove("banana")
    print(f"Set after using remove('banana'): {my_set}")
except KeyError:
    print("Error: 'banana' not found in the set.")
my_set.discard("kiwi")
print(f"Set after using discard('kiwi'): {my_set}")
removed_item = my_set.pop()
print(f"Set after using pop(). Removed item: {removed_item}")
print(f"Set now: {my_set}")
print("-" * 30)
print("--- 5. Loop Sets (Iterating through the items) ---")
print("Items in the set are:")
for item in my_set:
    print(f"- {item}")
print("-" * 30)
print("--- 6. Join Sets (Union and Intersection) ---")
set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}
set3_union = set1.union(set2)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union (set1 | set2): {set3_union}")
set4_intersection = set1.intersection(set2)
print(f"Intersection (set1 & set2): {set4_intersection}")
print("-" * 30)
print("--- 7. Frozenset ---")
immutable_set = frozenset(["bike", "car", "plane"])
print(f"Frozenset: {immutable_set}")
try:
    immutable_set.add("train")
except AttributeError as e:
    print(f"Error when trying to add to a frozenset: {e}")
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozensets: {set_of_sets}")
print("-" * 30)
print("--- 8. Set Methods (Example: Difference) ---")
set_A = {10, 20, 30, 40}
set_B = {30, 40, 50, 60}
set_difference = set_A.difference(set_B)
print(f"Set A: {set_A}")
print(f"Set B: {set_B}")
print(f"A - B (Difference): {set_difference}")
print("-" * 30)