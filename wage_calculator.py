from tkinter import *

win=Tk()
win.title("Wage_calculator")
win.geometry("1200x700")
win.option_add("*Font","궁서 15")

# 사회문화 조교

# Label
lab11 = Label(win, bg= "aqua")
lab11.config(text="사회문화 조교")
lab11.place(relx=0.225, rely=0.01)

# 댓글 개수
lab12 = Label(win)
lab12.config(text="댓글 개수")
lab12.place(relx=0.01, rely=0.1)

ent12 = Entry(win)
ent12.place(relx=0.2, rely=0.1)

# 정규 근로
lab13 = Label(win)
lab13.config(text="정규 근로 시간")
lab13.place(relx=0.01, rely=0.2)

ent13 = Entry(win)
ent13.place(relx=0.2, rely=0.2)

# 특수 근로
lab14 = Label(win)
lab14.config(text="특수 근로 시간")
lab14.place(relx=0.01, rely=0.3)

ent14 = Entry(win)
ent14.place(relx=0.2, rely=0.3)

# 특수 근로 시급
lab15 = Label(win)
lab15.config(text="특수 근로 시급")
lab15.place(relx=0.01, rely=0.4)

ent15 = Entry(win)
ent15.place(relx=0.2, rely=0.4)


# 현우 과외

# Label
lab21 = Label(win, bg= "yellow")
lab21.config(text="과외 1")
lab21.place(relx=0.25, rely=0.6)

# 근로 시간
lab22 = Label(win)
lab22.config(text="근로 시간")
lab22.place(relx=0.01, rely=0.7)

ent22 = Entry(win)
ent22.place(relx=0.2, rely=0.7)

# 시급
lab23 = Label(win)
lab23.config(text="시급")
lab23.place(relx=0.01, rely=0.8)

ent23 = Entry(win)
ent23.place(relx=0.2, rely=0.8)


# 가인 과외

# Label
lab31 = Label(win, bg= "yellow")
lab31.config(text="과외 2")
lab31.place(relx=0.75, rely=0.01)

# 근로 시간
lab32 = Label(win)
lab32.config(text="근로 시간")
lab32.place(relx=0.5, rely=0.1)

ent32 = Entry(win)
ent32.place(relx=0.7, rely=0.1)

# 시급
lab33 = Label(win)
lab33.config(text="시급")
lab33.place(relx=0.5, rely=0.2)

ent33 = Entry(win)
ent33.place(relx=0.7, rely=0.2)


# 비경상소득

# Label
lab41 = Label(win, bg= "lightcyan")
lab41.config(text="비경상소득")
lab41.place(relx=0.73, rely=0.4)

# 추가 버튼과 비경상소득 항목

k=50
inconsistent_wage=0

def add_item():
    global k
    global inconsistent_wage
    # 날짜
    lab_date = Label(win)
    lab_date.config(text="날짜")
    lab_date.place(relx=0.5, rely=k/100)

    ent_date = Entry(win, width=10)
    ent_date.place(relx=0.57, rely=k/100)

    # 금액
    lab_amount = Label(win)
    lab_amount.config(text="금액")
    lab_amount.place(relx=0.7, rely=k/100)

    ent_amount = Entry(win, width=10)
    ent_amount.place(relx=0.77, rely=k/100)

    # 각 비경상소득 더해주기
    def add():
        global inconsistent_wage
        inconsistent_wage += int(ent_amount.get())

    # 버튼
    btn3 = Button(win)
    btn3.config(text="입력")
    btn3.config(command=add)
    btn3.place(relx=0.9, rely=k/100)

    k+=5

btn1 = Button(win)
btn1.config(text="추가")
btn1.config(command = add_item)
btn1.place(relx=0.85, rely=0.4)


# 소득 계산 함수
def calculator():
    assistant_wage_before_tax = int(ent12.get())*1500 + int(ent13.get())*12000 + int(ent14.get())*int(ent15.get())
    assistant_wage_after_tax = assistant_wage_before_tax*0.97
    tutoring_1_wage = int(ent22.get())*int(ent23.get())
    tutoring_2_wage = int(ent32.get())*int(ent33.get())

    Total_wage = assistant_wage_after_tax + tutoring_1_wage + tutoring_2_wage + inconsistent_wage

    lab = Label(win, bg="fuchsia", fg="white")
    lab.config(text="이번달 총소득은 " + str(Total_wage) + "원 입니다.")
    lab.place(relx=0.6, rely=0.92)


# 결과창 띄우기
def btn_f():
    for wg in win.grid_slaves():
        wg.destroy()
    calculator()

# 소득 계산 버튼
btn2 = Button(win)
btn2.config(text="소득 계산")
btn2.config(command = btn_f)
btn2.place(relx=0.75, rely=0.85)

win.mainloop()