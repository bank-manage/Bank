


# 存钱,
put_cardno = 123456     # 假设输入了一个卡号
userbase = {123456:["身份证号","姓名","1234",500,1]}   # {卡號：[身份證號碼，姓名，密碼，金額，狀態]}




def func2():
    answer1 = input("是否显余额？y/n")
    if answer1 == "y":
        print("尊敬的{}客户，您目前的余额为{}元".format(userbase[put_cardno][1], userbase[put_cardno][-2]))
        answer2 = input("是否选择继续交易？y/n")
        if answer2 == "y":
            selfchange()
        else:
            print("交易完成，你已经退出存款页面")
    else:
        selfchange()

def selfchange():
    choice = input("请输入你想要的业务:1取钱   2存钱  3 退出 ")
    if userbase[put_cardno][-1] == 1 and choice != "3":
        cmoney = int(input("请输入交易金额："))
        if choice == "1":        # 取钱
            if userbase[put_cardno][-2] >= cmoney:
                userbase[put_cardno][-2] -= cmoney
                func2()
            else:
                print("您输入金额大于您的余额，请重新选择交易类型")
                selfchange()
        elif choice == "2":         # 存钱
            userbase[put_cardno][-2]+=cmoney
            func2()

        elif choice == "3":
            print("交易完成，你已经退出存款页面")
    else :
        if userbase[put_cardno][-1] == 0:
            print("对不起，您的账户由于其他操作不当今日已经被锁定，无法进行交易")
        else:
            print("交易完成，你已经退出存款页面")





selfchange()





















