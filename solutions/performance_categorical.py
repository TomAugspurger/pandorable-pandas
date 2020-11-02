
character_bytes = 50 * sys.getsizeof("AL")  # Store all the states once
bytes_per_person = 1  # np.int8 = 1 byte per element
print("{:,d} MB".format((character_bytes + (population * bytes_per_person)) // 1_000_000))
