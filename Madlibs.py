#The user is prompted to enter four different words:
# A noun, a verb, an adjective, and an adverb. 
# The code then prints a sentence using the words entered by the user, 
# resulting in a unique and entertaining story each time the game is played.




def mad_libs():
    print("Mad Libs game")
    print("Enter the requested information below to play the game:")

    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    print(f"The {adjective} {noun} likes to {verb} {adverb}.")


if __name__ == "__main__":
    mad_libs()
