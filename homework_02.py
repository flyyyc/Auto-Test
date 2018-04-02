# coding=utf-8

#一个命令行小游戏guess number
#当用户输入的不是整数的时候，能够提示用户重新输入
#用户最多尝试7次，7次失败以后游戏结束
#当用户输入“q” 或者 “Q”的时候，退出游戏

import random

def guess_number(min,max):
	print("***注意：输入'q'或'Q'可退出游戏。***")
	counter = 0

	#先在后台生成一个不大于100的随机数
	number_random = (random.randint(min,max))	

	while True:
		counter += 1

		if counter <= 7:

			#命令行提示用户输入一个猜想的数
			number_input = input("请输入数字：")

			if number_input not in {"q","Q"}:

				#判断是否为整数
				if number_input.isdigit():
					number_input = int(number_input)

					#用户猜对该数，游戏结束
					if number_input == number_random:
						print(f"正确数字为:{number_random},共猜了{counter}次。")
						break

					#如果大于随机数，则提示过大
					elif number_input > number_random:
						print("输入值过大")

					#如果小于随机是，提示过小
					else:
						print("输入值过小")
						continue

				#如果非整数，跳出提示
				else:
					print("请输入整数！")
			else:
				break

		else:
			print("最多只能猜7次！")
			break

guess_number(0,101)

