import time
bank = {}

# 銀行大字典
# 取錢
def withdraw(account,password):
	# 登陸使用帳號和密碼
	out_money = 0
	if account in bank:
		# 這個銀行有這個卡
		 if bank[account][2] == password:
		 	print("密碼正確")
		 	while True:
			 	money = float(input("收入你要支出的金額").strip())
			 	if money % 100 == 0 and 10000> money > 0:
			 		config = input("確定支出{}元（y/n）".format(money))
			 		if config.upper() == 'N':
			 			out_money += money
			 			# bank[account][3] -= out_money
			 			# return out_money
			 		elif config.upper() == "Y":
			 			out_money += money
			 		configs = input("是否繼續取錢").strip() 
			 		if configs.upper() == 'N':
			 			print("你要取出的錢{}".format(out_money))
			 			if out_money < bank[account][3]:
			 				bank[account][3] -= out_money
			 				print("""
			 						賬單
			 					賬戶： {}
			 					支出金額：{}
			 					剩餘金額：{}
			 					支出時間：{}
			 					""".format(account,out_money,bank[account][3],time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
			 			else:
			 				print("你的錢都不夠，先存點錢")
			 			return bank[account][3]
			 			break
		 	else:
		 		print("輸入正確的金額")
	else:
		# 沒卡
		print("請先注冊卡號")





