#这个游戏我打算用面向过程的方式写一下
import random
def Clue(MysticNumber,num):
	list1 = list(str(MysticNumber))
	list2 = list(str(num))
	result = []
	for i in range(len(list2)):
		if list2[i] == list1[i]:
			result.append('fermi')
		elif list2[i] in list1:
			result.append('pico')
		else:
			pass
	if len(result)==0:
		return 'Begals'
	else:
		return " ".join(sorted(result))
		
def Begals(Guess):
	MysticNumber = random.randint(100,1000)
	flag = True
	while Guess:
		if not flag:
			#假如不是第一次，给出提示
			print(Clue(MysticNumber,num))
		num = input(">")
		if int(num) == MysticNumber:
			print("You Win!")
			return 
		else:
			flag = False
		Guess = Guess - 1
	
	print(f"I'm sorry you're lose,the MysticNumber is {MysticNumber}")
	
def main():
	Exit = False
	while not Exit:
		Begals(5)
		print('one more Game?(Y/N)')
		choice = input('>')
		if choice == 'N':
			Exit = True
			
if __name__ == "__main__":
	main()
