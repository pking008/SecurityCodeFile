def securityFile(): 
    '''reading the security file and adding items to a list'''
    fileRead = open("security.txt", 'r')
    userID = []
    for line in fileRead:
        startList = line.split('|')
        userID.append(startList[0])
    fileRead.close()
    return userID

def inputSecFile(secList):
    while True:
        username = input("Enter your username or End to terminate program: ")
        if username == "End":
            break
        elif username in secList:
            print("Username is already listed.")
        else: 
            password = input("Enter password: ")
            authCode = input("Enter Authorization Code: ")
            appendSecFile= open("security.txt", 'a')
            appendSecFile.write(str(username)+"|"+str(password)+"|"+str(authCode))
            appendSecFile.write("\n")
            appendSecFile.close()

def readSecFile():
    fileReads = open("security.txt", 'r')
    for line in fileReads:
        fields = line.split('|')
        print("----------Employee Authorization Information------------")
        print("User ID: \t\t\t" + fields[0])
        print("Password: \t\t\t" + fields[1])
        print("Authorization Code: \t\t" + fields[2]) 
        print("-------------------------------------------------------")
    fileReads.close()

            
             

secList = securityFile()
inputSecFile(secList)
readSecFile()

