
character_bytes = 50 * sys.getsizeof("AL")  # Store all the states once
bytes_per_person = 1  # np.int8 = 1 byte per element
nbytes = (character_bytes + (population * bytes_per_person))
print("{:,d} MB".format(nbytes // 1_000_000))
