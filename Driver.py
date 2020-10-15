from search_dict import find_word

print("Input 'go' to begin: ")
userIn = input()

def getUserNum():
    print("How long should the words be? (input an integer):")
    return input()


def getInput():
    print("Input comma separated list of letters (ex: a,b,c): ")
    userIn = input()
    word_list = userIn.split(',')
    return word_list


def runFindWord(word_list):
    userNum = getUserNum()
    try:
        userNum = int(userNum)
    except:
        print("INPUT MUST BE AN INTEGER")
        userNum = getUserNum()
    print(find_word(word_list, userNum))


while input() != "exit":
    word_list = getInput()
    runFindWord(word_list)
    print("Go again with same list? (type 'exit' to stop, 'y' to continue, and 'n' to continue with different list): ")
    userIn = input()
    if userIn.lower() == 'y':
        runFindWord(word_list)
        print(
            "Go again with same list? (type 'exit' to stop, 'y' to continue, and 'n' to continue with different list): ")
    elif userIn.lower() == 'exit':
        break
    else:
        continue






