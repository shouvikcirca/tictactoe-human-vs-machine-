import random


collectionOfWinningSequences = []




def playerOneWhileTraining(movestaken):

	ini = [0,3,6]
	# print (movestaken)
	for i in ini:
		if movestaken[i]=='-2' and movestaken[i+1]=='-2' and movestaken[i+2]==str(i+2):
			return str(i+2)
		elif movestaken[i]==str(i) and movestaken[i+1]=='-2' and movestaken[i+2]=='-2':
			return str(i)
		elif movestaken[i]=='-2' and movestaken[i+1]==str(i+1) and movestaken[i+2]=='-2':
			return str(i+1)

	ini = [0,1,2]
	for i in ini:
		if movestaken[i]=='-2' and movestaken[i+3]=='-2' and movestaken[i+6]==str(i+6):
			return str(i+6)
		elif movestaken[i]==str(i) and movestaken[i+3]=='-2' and movestaken[i+6]=='-2':
			return str(i)
		elif movestaken[i]=='-2' and movestaken[i+1]==str(i+1) and movestaken[i+2]=='-2':
			return str(i+1)


	if movestaken[0]=='-2' and movestaken[4]=='-2' and movestaken[8]=='8':
		return str(i+6)
	elif movestaken[0]=='0' and movestaken[4]=='-2' and movestaken[8]=='-2':
		return str(i)
	elif movestaken[0]=='-2' and movestaken[4]=='4' and movestaken[8]=='-2':
		return str(i+1)


	if movestaken[2]=='-2' and movestaken[4]=='-2' and movestaken[6]=='6':
		return str(i+6)
	elif movestaken[2]=='2' and movestaken[4]=='-2' and movestaken[6]=='-2':
		return str(i)
	elif movestaken[2]=='-2' and movestaken[4]=='4' and movestaken[6]=='-2':
		return str(i+1)




	tmovestaken = [i for i in movestaken]
	move = random.randint(0, len(tmovestaken)-1)	
	if tmovestaken[move] == '-1' or tmovestaken[move] == '-2':
		del tmovestaken[move]
		if tmovestaken != []:
			return playerOneAgainstUser(tmovestaken)
		else:
			return 'draw'
	else:
		return tmovestaken[move]








def playerOneAgainstUser(movestaken):



	tmovestaken = [i for i in movestaken]
	move = random.randint(0, len(tmovestaken)-1)	
	if tmovestaken[move] == '-1' or tmovestaken[move] == '-2':
		del tmovestaken[move]
		if tmovestaken != []:
			return playerOneAgainstUser(tmovestaken)
		else:
			return 'draw'
	else:
		return tmovestaken[move]





def playerTwo(movestaken):
	tmovestaken = [i for i in movestaken]
	move = random.randint(0, len(tmovestaken)-1)	
	if tmovestaken[move] == '-1' or tmovestaken[move] == '-2':
		del tmovestaken[move]
		if tmovestaken != []:
			return playerTwo(tmovestaken)
		else:
			return 'draw'
	else:
		return tmovestaken[move]

# The boxes of the criss cross are numbered from 0-9 left to right top to bottom
def checkStatusOne(movestaken):
	winningcombosubstring = []	
	winningcombosubstring.append(movestaken[0] + movestaken[1] + movestaken[2])
	winningcombosubstring.append(movestaken[0] + movestaken[4] + movestaken[8])
	winningcombosubstring.append(movestaken[0] + movestaken[3] + movestaken[6])
	winningcombosubstring.append(movestaken[1] + movestaken[4] + movestaken[7])
	winningcombosubstring.append(movestaken[2] + movestaken[4] + movestaken[6])
	winningcombosubstring.append(movestaken[2] + movestaken[5] + movestaken[8])
	winningcombosubstring.append(movestaken[3] + movestaken[4] + movestaken[5])
	winningcombosubstring.append(movestaken[6] + movestaken[7] + movestaken[8])

	if '-1-1-1' in winningcombosubstring:
		return 1
	else:
		return 0


def checkStatusTwo(movestaken):
	winningcombosubstring = []	
	winningcombosubstring.append(movestaken[0] + movestaken[1] + movestaken[2])
	winningcombosubstring.append(movestaken[0] + movestaken[4] + movestaken[8])
	winningcombosubstring.append(movestaken[0] + movestaken[3] + movestaken[6])
	winningcombosubstring.append(movestaken[1] + movestaken[4] + movestaken[7])
	winningcombosubstring.append(movestaken[2] + movestaken[4] + movestaken[6])
	winningcombosubstring.append(movestaken[2] + movestaken[5] + movestaken[8])
	winningcombosubstring.append(movestaken[3] + movestaken[4] + movestaken[5])
	winningcombosubstring.append(movestaken[6] + movestaken[7] + movestaken[8])

	if '-2-2-2' in winningcombosubstring:
		return 1
	else:
		return 0




	
# victory checking will start when this value is 3 for its not possible to win before 3 moves
numberofPlayerOneMoves = 0

for numberOfGames in range(362880):
	movestaken = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
	playSequence = ''
	for i in range(5):
		move = playerOneWhileTraining(movestaken)
		if move == 'draw':
			break
		movestaken[int(move)] = '-1'
		numberofPlayerOneMoves +=1	
		playSequence = playSequence + str(move)	
		if numberofPlayerOneMoves >=3:
			winStatus = checkStatusOne(movestaken)
			if winStatus == 1:
				collectionOfWinningSequences.append(playSequence)
				break
				# print (movestaken)

		
		move = playerTwo(movestaken)
		if move == 'draw':
			break
		movestaken[int(move)] = '-2'
		playSequence = playSequence + str(move)	
		if checkStatusTwo(movestaken) == 1:
			break
			
		


sortedcollectionOfWinningSequences = sorted(collectionOfWinningSequences,key = lambda x:len(x))
	
# print (sortedcollectionOfWinningSequences)


def moveSearch(sub,i,sortedcollectionOfWinningSequences,movestaken):
	



	if i == 0:
		return sortedcollectionOfWinningSequences[0][0]
	

	temp = []
	for i in movestaken:
		if i!='-1' and i!='-2':
			temp.append(i)
	if temp == []:
		return 'draw'
	
	ini = [0,3,6]
	# print (movestaken)
	for i in ini:
		if movestaken[i]=='-2' and movestaken[i+1]=='-2' and movestaken[i+2]==str(i+2):
			return str(i+2)
		elif movestaken[i]==str(i) and movestaken[i+1]=='-2' and movestaken[i+2]=='-2':
			return str(i)
		elif movestaken[i]=='-2' and movestaken[i+1]==str(i+1) and movestaken[i+2]=='-2':
			return str(i+1)

	ini = [0,1,2]
	for i in ini:
		if movestaken[i]=='-2' and movestaken[i+3]=='-2' and movestaken[i+6]==str(i+6):
			return str(i+6)
		elif movestaken[i]==str(i) and movestaken[i+3]=='-2' and movestaken[i+6]=='-2':
			return str(i)
		elif movestaken[i]=='-2' and movestaken[i+1]==str(i+1) and movestaken[i+2]=='-2':
			return str(i+1)


	if movestaken[0]=='-2' and movestaken[4]=='-2' and movestaken[8]=='8':
		return str(i+6)
	elif movestaken[0]=='0' and movestaken[4]=='-2' and movestaken[8]=='-2':
		return str(i)
	elif movestaken[0]=='-2' and movestaken[4]=='4' and movestaken[8]=='-2':
		return str(i+1)


	if movestaken[2]=='-2' and movestaken[4]=='-2' and movestaken[6]=='6':
		return str(i+6)
	elif movestaken[2]=='2' and movestaken[4]=='-2' and movestaken[6]=='-2':
		return str(i)
	elif movestaken[2]=='-2' and movestaken[4]=='4' and movestaken[6]=='-2':
		return str(i+1)


	


	for item in sortedcollectionOfWinningSequences:
		if item[:i] == sub:
			return item[i]
		else:
			return playerOneAgainstUser(movestaken)








# Function to start playing as player 1
def asPlayerOne(sortedcollectionOfWinningSequences):
	
	playSequence = ''
	movestaken = [str(i) for i in range(0,9)]
	numberofMoves = 0
	for i in range(5):
		move = moveSearch(playSequence,numberofMoves,sortedcollectionOfWinningSequences,movestaken)
		playSequence+=move
		print ('I choose {}'.format(move))
		if move == 'draw':
			print ('Draw')
			break
		movestaken[int(move)] = '-1'
		numberofMoves +=1	
		# playSequence = playSequence + str(move)	
		if numberofPlayerOneMoves >=3:
			winStatus = checkStatusOne(movestaken)
			if winStatus == 1:
				# collectionOfWinningSequences.append(playSequence)
				print (' I win You lose')
				break
				# print (movestaken)

		if len(playSequence) == 9:
			print ('Draw')
		else:
			move = input('Your move please')
			numberofMoves +=1
			move = int(move)
			playSequence+=str(move)
			movestaken[move] = '-2'	
			if checkStatusTwo(movestaken) == 1:
				print ('You win')
				break
			









asPlayerOne(sortedcollectionOfWinningSequences)









