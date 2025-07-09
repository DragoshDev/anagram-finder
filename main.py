from collections import defaultdict

def find_anagrams(input_file):
    groups = defaultdict(list)

    with open(input_file, "r") as f:
        for line in f:
            word = line.strip()
            key = "".join(sorted(word))
            groups[key].append(word)

    return groups

def display_groups(groups):
    for group in groups.values():
        print(" ".join(group))

if __name__ == "__main__":
    file_name = "sample.txt"
    result = find_anagrams(file_name)
    display_groups(result)
