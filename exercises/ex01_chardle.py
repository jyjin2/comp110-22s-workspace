"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730530395"

five_chr_word: str = input("Enter a 5-character word: ")
count_chr: int = 0

if len(five_chr_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    single_chr: str = input("Enter a single character: ")
    
    if len(single_chr) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for", single_chr, "in", five_chr_word)

        if single_chr in five_chr_word:
            if single_chr == five_chr_word[0]:
                print(single_chr, "found at index 0")
                count_chr = count_chr + 1
            if single_chr == five_chr_word[1]:
                print(single_chr, "found at index 1") 
                count_chr = count_chr + 1
            if single_chr == five_chr_word[2]:
                print(single_chr, "found at index 2")
                count_chr = count_chr + 1
            if single_chr == five_chr_word[3]:
                print(single_chr, "found at index 3")
                count_chr = count_chr + 1  
            if single_chr == five_chr_word[4]:
                print(single_chr, "found at index 4")
                count_chr = count_chr + 1

            if count_chr == 1:
                print("1 instance of", single_chr, "found in", five_chr_word)
            else:
                print(count_chr, "instances of", single_chr, "found in", five_chr_word)
        else:
            print("No instances of", single_chr, "found in", five_chr_word)