class Voting():

    def __init__(self):
        
        self.db : dict = {}
        self.db_Vote : dict = {}
        self.filename : str= 'Content_Assignment4.txt'
        self.voteFile : str = 'Candidate_Assignment4.txt'


    def readUserFromFile(self):

        with open(self.filename, 'r') as readFile:

            i = 0
            for line in readFile:
                accList = line.split(' ')
                remove = accList[5]
                accList[5] = remove.strip()
                self.db.update({i:{'u_name':accList[0],'password':accList[1],
                         'email':accList[2],'phone':accList[3],
                         'money':int(accList[4]),'points':int(accList[5])}})
                i += 1


    def loadVoteData(self):

        with open(self.voteFile, 'r') as readFile:

            i = 0
            for line in readFile:
                voter = []
                candidateList = []
                candidateList = line.split(' ')

                if len(candidateList) <= 2:
                    remove = candidateList[1]
                    candidateList[1] = remove.strip()
                else:
                    remove = candidateList[-1]
                    candidateList[-1] = remove.strip()

                length = len(candidateList)-2
                for v in range(length):
                    voterStr : str = candidateList[v+2]
                    if voterStr == " " or voterStr == "":
                        pass
                    else:
                        voter.append(voterStr)

                self.db_Vote.update({i:{'candidate':candidateList[0],
                                     'voteCount':int(candidateList[1]),
                                     'voter':voter}})
                i += 1


    def mainMenu(self):

        self.readUserFromFile()
        self.loadVoteData()
        option = 0

        try:
            print('')
            print('1) Register')
            print('2) Log In')
            print('3) Exit')
            option = int(input('Enter No. > '))
        except Exception as ex:
            print('\nPlz enter only the number mentioned!')

        if option == 1:
            self.register()
        
        elif option == 2:
            self.login()

        elif option == 3:
            print('Exit')
            exit(1)

        else:
            print('\nInvalid Number!')
            self.mainMenu()


    def checkUser(self,username):

        length = len(self.db)
        for i in range(length):
            if self.db[i]["u_name"] == username:
                return i
        return -1
    

    def appendToFile(self,username,password,email,phone,money,orderPoint):

        with open(self.filename, 'a') as appendFile:
            appendFile.write('{} {} {} {} {} {}\n'.format(username,password,email,phone,money,orderPoint))


    def register(self):

        print('\nRegister Account')
    
        u_name : str = ''
        password : str = ''
        confirmPass : str = ''
        email : str = ''
        phone : int = 0
        money : int = 0
        orderPoint : int = 0

        while True:
            try:
                print('Enter -1 to quit')
                u_name = str(input('Enter username     > '))
            except Exception as ex:
                print('\nInvalid Input!')
                self.register()

            if u_name == '-1':
                break

            if u_name.find(" "):
                username = u_name.replace(" ","_")
            else:
                username = u_name

            result = self.checkUser(username)

            if result != -1:
                print('\nUsername already registered!')
            else:
                break

        if u_name != '-1':
            while True:
                try:
                    password = input('Enter passwrod     > ')
                    confirmPass = input('Confirm password   > ')

                    if confirmPass == password:
                        break
                    else:
                        print('\nPasswords must be matched.')
                except Exception as ex:
                    print('\nInvalid Input!')
                    self.register

            email = input('Enter email        > ')

            while True:
                try:
                    phone = int(input('Enter phone number > '))
                    if type(phone) is int:
                        break
                except Exception as ex:
                    print('\n{}'.format(ex))
                    print('Invalid Input!\n')

            while True:
                try:
                    money = int(input('Enter showmoney (at least 50$) > '))

                    if type(money) is int:
                        if money >= 50:
                            break
                        else:
                            print('\nShowmoney must at least 50$ or more!')
                except Exception as ex:
                    print('\n{}'.format(ex))
                    print('Invalid Input!\n')

            try:
                print('\nWanna buy points to VOTE!')
                print('1 point = 50$')
                print('Enter 1 to buy point(s)')
                print('Or another interger to pass this step.')
                choice = int(input('> '))
            except Exception as ex:
                print('\n{}'.format(ex))
                print('Invalid Input!\n')

            if choice == 1:
                print('\nYour money = {}$.'.format(money))
                availablePoints = int(money/50)
                print('Point(s) u available to buy = {} point(s).'.format(availablePoints))
                
                while True:
                    try: 
                        orderPoint = int(input('How muny point(s) u wanna buy? > '))

                        if orderPoint <= 0:
                            print('\nPoint wanna buy must be greater than 0!')
                        
                        else:
                            if orderPoint > availablePoints:
                                print('\nU cannot buy more than available points!')
                            else:
                                print('\nYour point(s) = {}'.format(orderPoint))
                                cost = orderPoint*50
                                money = money-cost
                                print('Money left = {}$.'.format(money))
                                break

                    except Exception as ex:
                        print('\n{}'.format(ex))
                        print('Invalid Input!\n')
            else:
                orderPoint = 0

            self.appendToFile(username,password,email,phone,money,orderPoint)
            print('\nRegisteration Successful!')

        self.mainMenu()


    def login(self):

        print('\nLog In Account')
        print('Enter -1 to quit')
    
        accIndex : int = 0
        lusername : str = ''

        while True:
            try:
                lusername = input('Enter username > ')

                if lusername == '-1':
                    break

                if lusername.find(" "):
                    lusername = lusername.replace(" ","_")
                
                accIndex = self.checkUser(lusername)
                
                if accIndex != -1:
                    break
                else:
                    print('\nInvalid Username!')

            except Exception as ex:
                print('\n{}'.format(ex))
                print('Invalid Input!\n')
        
        if lusername == '-1':
            self.mainMenu()
        else:
            while True:
                try:
                    lpassword : str = input('Enter password > ')

                    if lpassword == self.db[accIndex]["password"]:
                        break
                    else:
                        print('\nInvalid Password! Try again...')
                except Exception as ex:
                    print('\n{}'.format(ex))
                    print('Invalid Input!\n')
            
            self.profile(accIndex)


    def profile(self,acc_index):

        option : int = 0
        accIndex : int = acc_index
        print('\nWelocome!')
        print('Username : {} , Email : {} , Phone : {} , Money : {} , Point(s) : {}'
              .format(self.db[accIndex]["u_name"],self.db[accIndex]["email"],
                  self.db[accIndex]["phone"],self.db[accIndex]["money"],
                  self.db[accIndex]["points"]))
        
        while True:
            print('\n1) Cash In')
            print('2) Buy point(s)')
            print('3) Vote')
            print('4) Exit')

            try:
                option = int(input('Enter > '))
            except Exception as ex:
                print('\n{}'.format(ex))

            if option == 1:
                self.cashIn(accIndex)

            elif option == 2:
                self.buyPoints(accIndex)

            elif option == 3:
                self.vote(accIndex)
                
            elif option == 4:
                break
            else:
                print('\nInvalid Number!\n')

        self.mainMenu()


    def cashIn(self,acc_index):
        
        accIndex : int = acc_index
        currentCash : int = self.db[accIndex]["money"]
        print('\nCurrent Money = {}$'.format(currentCash))
        print('Enter 0 to quit!')
        
        while True:
            try:
                cash : int = int(input('Enter amount > '))

                if cash == 0:
                    break

                elif cash < 50:
                    print('\nSorry... Cash in amount must be more than 50$')
                    print('Because 1 point = 50$\n')

                else:
                    self.db[accIndex]["money"] = cash + currentCash
                    print('Money in Account Updated!')
                    break

            except Exception as ex:
                print('\n{}'.format(ex))
                print('Invalid Input!\n')

        self.saveProfile()
        self.profile(accIndex)


    def buyPoints(self,acc_index):

        accIndex : int = acc_index
        currentCash : int = self.db[accIndex]["money"]
        print('\nYour Money = {}$'.format(currentCash))
        availablePoints : int = int(currentCash/50)
        print('Point(s) u available to buy = {} point(s).'.format(availablePoints))
        print('Enter 0 to quit!')

        while True:
            try: 
                orderPoint = int(input('How muny point(s) u wanna buy? > '))

                if orderPoint == 0:
                    break

                elif orderPoint < 0:
                    print('\nPoint wanna buy must be greater than 0!')
                
                else:
                    if orderPoint > availablePoints:
                        print('\nU cannot buy more than available points!')
                    else:
                        currentPoint = self.db[accIndex]["points"] + orderPoint
                        print('\nYour point(s) = {} + {} ({} points)'
                              .format(self.db[accIndex]["points"],orderPoint,
                                      currentPoint))
                        self.db[accIndex]["points"] = currentPoint 
                        cost = orderPoint*50
                        currentCash = currentCash-cost
                        print('Money left = {}$.'.format(currentCash))
                        self.db[accIndex]["money"] = currentCash
                        print('Point(s) have been Purchased!')
                        break

            except Exception as ex:
                print('\n{}'.format(ex))
                print('Invalid Input!\n')

        self.saveProfile()
        self.profile(accIndex)

    
    def showCandidates(self):

        print('\nCandidates List')
        for i in range(len(self.db_Vote)):
            no = i+1
            voteCount : int = self.db_Vote[i]["voteCount"]
            candidate : str = self.db_Vote[i]["candidate"]
            print('Id {} - {} - Current Vote Count : {} '
                  .format(no,candidate,voteCount))
            
    def saveProfile(self):

        with open(self.filename,'w') as saveProfile:
            for i in range(len(self.db)):
                saveProfile.write('{} {} {} {} {} {}\n'
                                  .format(self.db[i]['u_name'],self.db[i]['password'],
                                          self.db[i]['email'],self.db[i]['phone'],
                                          self.db[i]['money'],self.db[i]['points']))
                
    def saveVote(self):

        with open(self.voteFile, 'w') as saveVote:
            for v in range(len(self.db_Vote)):
                length = len(self.db_Vote[v]['voter'])
                voteList = self.db_Vote[v]['voter']
                voters = " ".join(voteList)
                saveVote.write('{} {} {} \n'
                               .format(self.db_Vote[v]['candidate'],
                                       self.db_Vote[v]['voteCount'],
                                       voters))
                    

    def vote(self,acc_index):

        accIndex : int = acc_index
        currentPoints : int = self.db[accIndex]["points"]

        while True:
            print('\nYour Point(s) = {}'.format(currentPoints))
            print('Enter 0 to quit!')
            
            if currentPoints == 0:
                print('Sorry.. U cannot vote anymore!')
                print('No point in your acc.')
                break
            else:
                self.showCandidates()
                try:
                    voteId = int(input('\nEnter Id to vote > '))
                
                    if voteId == 0:
                        break
                    else:
                        currentPoints -= 1
                        self.db[accIndex]["points"] = currentPoints
                        voterList : list = self.db_Vote[voteId-1]["voter"]
                    
                        for i in range(len(self.db_Vote)):
                            c = i + 1
                            if c == voteId:
                                self.db_Vote[i]["voteCount"] += 1
                                voter : str = self.db[accIndex]["u_name"]
                                voterList.append(voter)
                                self.db_Vote[i]["voter"] = voterList
                                print('Now u vote {}.'.format(self.db_Vote[i]["candidate"]))
                                break

                except Exception as ex:
                    print('\n{}'.format(ex))
                    print('Invalid Input!\n')

        self.saveProfile()
        self.saveVote()
        self.profile(accIndex)