from tkinter import *
from tkinter import messagebox
import random
import math

gui = Tk() 
gui.configure(background="#35363A") 
gui.title("Sientific Calculator | Pariya Tavangar") 
gui.geometry("660x520") 
gui.resizable(False,False)
gui.iconbitmap('img/calicon.ico')

# ------------- Initials -------------
pi_id = 3.1415926
neper_id = 2.71828
nlist = {'+':[],'-':[],'*':[],'/':[],'%':[],'xy':[]}
history_list=op_prime=buffer_num=len_lbl=slist=''
xy_id=neperx_id=plus_id=sub_id=div_id=multi_id=perc_id=perc_total=x2_id=x3_id=rand_id=sin_id=cos_id=tan_id=conv_num=forge2_id=forge3_id=log_id=ln_id=tanh_id=0

# ------------- commands ---------------
def savings():
    global slist,nlist,neperx_id,xy_id
    global conv_num, buffer_num , forge2_id, forge3_id, log_id, ln_id, sinh_id,cosh_id, tanh_id
    global plus_id,sub_id,multi_id,div_id,x2_id,x3_id,perc_id,perc_total,sin_id,cos_id,tan_id

    plus_id = int(buffer_num)
    sub_id = int(buffer_num)
    multi_id = int(buffer_num)
    div_id = int(buffer_num)
    x2_id = int(buffer_num)
    x3_id = int(buffer_num)
    xy_id = int(buffer_num)
    perc_id = int(buffer_num)
    perc_total = int(buffer_num)
    sin_id = int(buffer_num)
    cos_id = int(buffer_num)
    tan_id = int(buffer_num)
    forge2_id = int(buffer_num)
    forge3_id = int(buffer_num)
    log_id = int(buffer_num)
    ln_id = int(buffer_num)
    sinh_id = int(buffer_num)
    cosh_id = int(buffer_num)
    tanh_id = int(buffer_num)
    neperx_id = int(buffer_num)

def emptying():
    global plus_id, sub_id , multi_id , div_id ,x3_id,x2_id , buffer_num , ln_id,xy_id,neperx_id
    global sin_id, cos_id, tan_id, cosh_id, sinh_id, tanh_id
    buffer_num = ''
    plus_id = 0
    sub_id = 0
    multi_id = 0
    div_id = 0
    x2_id = 0
    x3_id = 0
    xy_id = 0
    ln_id = 0
    cos_id = 0
    sin_id = 0
    tan_id = 0
    sinh_id = 0
    cosh_id = 0
    tanh_id = 0
    neperx_id = 0

def equaling(s_all):
    global plus_id, sub_id , multi_id , div_id ,x3_id, buffer_num,ss
    plus_id = s_all
    sub_id = s_all
    multi_id = s_all
    div_id = s_all
    x3_id = s_all

def btn0():
    global slist , nlist, buffer_num
    num0 = '0'
    buffer_num += num0 # 1 int
    slist += str(num0) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn1():
    global slist , nlist, buffer_num
    num1 = '1'
    buffer_num += num1 # 1 int
    slist += str(num1) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn2():
    global slist , nlist, buffer_num    
    num2 = '2'
    buffer_num += num2 # 1 int
    slist += str(num2) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn3():
    global slist , nlist ,buffer_num
    num3 = '3'
    buffer_num += num3 # 1 int
    slist += str(num3) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn4():
    global slist , nlist , buffer_num    
    num4 = '4'
    buffer_num += num4 # 1 int
    slist += str(num4) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn5():
    global slist , nlist, buffer_num
    num5 = '5'
    buffer_num += num5 # 1 int
    slist += str(num5) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn6():
    global slist , nlist, buffer_num
    num6 = '6'
    buffer_num += num6 # 1 int
    slist += str(num6) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn7():
    global slist , nlist, buffer_num
    
    num7 = '7'
    buffer_num += num7 # 1 int
    slist += str(num7) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn8():
    global slist , nlist, buffer_num
    
    num8 = '8'
    buffer_num += num8 # 1 int
    slist += str(num8) #'1' str
    savings()
    resultframe.configure(text = slist)

def btn9():
    global slist , nlist , buffer_num
    num9 = '9'
    buffer_num += num9 # 1 int
    slist += str(num9) #'1' str
    savings()
    resultframe.configure(text = slist)

def add_op():
    global nlist , slist, op_prime
    op_prime = '+'
    slist += '+'
    nlist['+'].append(plus_id)
    resultframe.configure(text = slist)
    emptying()

def subs_op():
    global nlist, slist, op_prime
    op_prime = '-'
    slist += '-'
    nlist['-'].append(sub_id)
    resultframe.configure(text = slist)
    emptying()

def multi_op():
    global nlist , slist, op_prime
    op_prime = '*'
    slist += '*'
    nlist['*'].append(multi_id)
    resultframe.configure(text = slist)
    emptying()

def div_op():
    global nlist , slist, op_prime
    op_prime = '/'
    slist += '/'
    nlist['/'].append(div_id)
    resultframe.configure(text = slist)
    emptying()

def percent_op():
    global nlist , slist, op_prime

    op_prime = '%'
    slist += '%'
    nlist['%'].append(perc_id)
    resultframe.configure(text = slist)
    emptying()

def x2():
    global nlist , slist, buffer_num
    x2_res = 0
    x2_res = x2_id ** 2
    slist = str(x2_res)
    resultframe.configure(text = slist)
    equaling(x2_res)

def x3():
    global nlist , slist, buffer_num
    x3_res = 0
    x3_res = x3_id ** 3
    slist = str(x3_res)
    resultframe.configure(text = slist)
    equaling(x3_res)

def xy():
    global nlist , slist, op_prime
    op_prime = 'xy'
    slist += '^'
    nlist['xy'].append(xy_id)
    resultframe.configure(text = slist)
    emptying()

def pi():
    global nlist , slist,buffer_num
    pi_res = 0
    pi_res = pi_id
    slist = str(pi_res)
    resultframe.configure(text = slist)
    equaling(pi_res)

def neper():
    global nlist , slist,buffer_num
    neper_res = 0
    neper_res = neper_id
    slist = str(neper_res)
    resultframe.configure(text = slist)
    equaling(neper_res)

def neperx():
    neperx_res = 0
    neperx_res = neper_id ** neperx_id
    slist = str(neperx_res)
    resultframe.configure(text = slist)
    equaling(neperx_res)

def log10():
    global nlist , slist, buffer_num
    log10_res = 0
    log10_res = math.log10(log_id) 
    slist = str(log10_res)
    resultframe.configure(text = slist)
    equaling(log10_res)

def ln_op():
    global nlist , slist,buffer_num
    ln_res = 0
    ln_res = math.log(ln_id)
    slist = str(ln_res)
    resultframe.configure(text = slist)
    equaling(ln_res)

def rand():
    global nlist , slist,buffer_num
    rand_res = 0
    rand_res = random.uniform(0,1)
    slist = str(rand_res)
    resultframe.configure(text = slist)
    equaling(rand_res)

def sin():
    global nlist , slist, buffer_num
    rad = 0
    rad = math.radians(sin_id)
    sin_res = math.sin(rad)
    slist = str(sin_res)
    resultframe.configure(text = slist)
    equaling(sin_res)

def sinh():
    global nlist , slist, buffer_num
    rad = 0
    rad = math.radians(sinh_id)
    sinh_res = math.sinh(rad)
    slist = str(sinh_res)
    resultframe.configure(text = slist)
    equaling(sinh_res)

def cos():
    global nlist , slist, buffer_num
    rad = 0
    rad = math.radians(cos_id)
    cos_res = math.cos(rad)
    slist = str(cos_res)
    resultframe.configure(text = slist)
    equaling(cos_res)

def cosh():
    global nlist , slist, buffer_num
    cosh_res = math.cosh(cosh_id)
    slist = str(cosh_res)
    resultframe.configure(text = slist)
    equaling(cosh_res)

def tan():
    global nlist , slist, buffer_num
    rad = 0
    rad = math.radians(tan_id)
    tan_res = math.tan(rad)
    slist = str(tan_res)
    resultframe.configure(text = slist)
    equaling(tan_res)

def tanh():
    global nlist , slist, buffer_num
    tanh_res = math.tanh(tanh_id)
    slist = str(tanh_res)
    resultframe.configure(text = slist)
    equaling(tanh_res)

def forge2():
    global nlist , slist, buffer_num , forge2_id
    forge2_res = 0
    temp = (forge2_id ** (1/2))
    form ="%." + str(3) + "f"
    forge2_res =  float(form % temp)
    slist = str(forge2_res)
    resultframe.configure(text = slist)
    equaling(forge2_res)

def forge3():
    global nlist , slist,forge3_id
    forge3_res = 0
    temp = (forge3_id ** (1/3))
    form ="%." + str(3) + "f"
    forge3_res =  float(form % temp)
    slist = str(forge3_res)
    resultframe.configure(text = slist)
    equaling(forge3_res)

def equal_op ():

    global op_prime , history_list
    global plus_id , sub_id , multi_id , div_id , perc_id ,perc_total,xy_id
    
    if len(resultframe.cget('text'))>23:
        resultframe.configure(text = 'Input Overflow')
    else:
        if op_prime == '+':
            nlist['+'].append(plus_id) 

        elif op_prime == '-':
            nlist['-'].append(sub_id)

        elif op_prime == '*':
            nlist['*'].append(multi_id)
                
        elif op_prime == '/':
            nlist['/'].append(div_id)
                
        elif op_prime == '%':
            nlist['%'].append(perc_total)

        elif op_prime == 'xy':
            nlist['xy'].append(xy_id)

        perc_total = 0
        perc_id = 0
        plus_id = 0 
        sub_id = 0
        multi_id = 0
        div_id = 0

        #? sum result
        plus_res = sum(nlist['+'])
                
        #?substract result
        sub_res = 0
        count = 0

        for i in nlist['-']:
            if count == 0:
                sub_res += i
                count +=1
            else:
                sub_res += -(i)
                count +=1

        #?multiple result
        multi_res = 1
        final_res = 0
        for j in nlist['*']:
            multi_res *= j 

        #?division result
        count = 0
        d1= 0
        d2 =0
        div_res = 0
        for l in nlist['/']:
            if count == 0:
                d1 = l
                count += 1
            else:
                d2 = l
                d1 /= d2
                d2 = 0
            div_res = d1
                
        #?percentage result
        perc_res = 0
        c1 = 0
        xp = 0
        yp = 0
        for p in nlist['%']:
            if c1 == 0:
                xp += p
                c1 += 1
            else:
                yp += p
                perc_res = (xp * yp) / 100
                
        #?xy result
        xy_res = 0
        c2 = 0
        xp2 = 0
        yp2 = 0
        for k in nlist['xy']:
            if c2 == 0:
                xp2 += k
                c2 += 1
            else:
                yp2 += k
                xy_res = xp2 ** yp2

        final_res = 0

        if '*' in slist:
            final_res += plus_res + sub_res + multi_res
        else:
            multi_res = 0
            final_res = plus_res + sub_res + multi_res + div_res + perc_res + xy_res

        resultframe.configure(text='')
        resultframe.configure(text=final_res)

    history_list += slist + '\n'
    historyframe.configure(text=history_list)

def history_clear():
    global history_list
    historyframe.configure(text='')
    history_list = ''
    
def clearing():

    global slist
    global buffer_num
    global plus_id , sub_id, multi_id,div_id

    nlist['+'].clear()
    nlist['*'].clear()
    nlist['-'].clear()
    nlist['/'].clear()
    nlist['%'].clear()
    nlist['xy'].clear()

    print(nlist)
    slist = ''
    buffer_num =''
    resultframe.configure(text='')

    plus_id = 0 
    sub_id = 0
    multi_id = 0
    div_id = 0

def exit():
    result = messagebox.askyesno("خروج","آیا مایل به خروج از برنامه هستید؟")
    if result:
        gui.destroy()
    else:
        return

# -------------- Layout -----------------
#* --------- Operators -----------
resultframe = Label(gui,bg='#e4eaf5',width=22,height=1,pady=16,relief='sunken',borderwidth=10,font=('Digital-7',30))
resultframe.place(x=33,y=30)

titleframe = Label(gui,width=16,height=2,pady=5,font=('B titr',11),fg='white',bg='#35363A',text='ماشین حساب علمی\n Scientific Calculator')
titleframe.place(x=472,y=15)

exitframe = Button(gui,width=15,height=1,font=('B titr',10),fg='white',bg='#840808',text='خروج از برنامه',command=exit)
exitframe.place(x=482,y=100)

btnhistory = Button(gui,bg='#F0A440',width=17,height=1
                    ,relief='raised',borderwidth=3,font=('B titr',9),fg='black',text='پاک کردن تاریخچه',command=history_clear)
btnhistory.place(x=482,y=150)

historyframe = Label(gui,bg='black',width=21,height=16,pady=16,relief='sunken',borderwidth=3,font=('Arial',10),fg='white')
historyframe.place(x=465,y=195)

img_plus = PhotoImage(file='img/plus.png')
plus_btn = Button(gui,image=img_plus,width=50,height=40,relief='ridge',borderwidth=3,command=add_op)
plus_btn.place(x=390,y=200)

img_subs = PhotoImage(file='img/substract.png')
subs_btn = Button(gui,image=img_subs,width=50,height=40,relief='ridge',borderwidth=3,command=subs_op)
subs_btn.place(x=390,y=260)

img_divi = PhotoImage(file='img/division.png')
div_btn = Button(gui,image=img_divi,width=50,height=40,relief='ridge',borderwidth=3,command=div_op)
div_btn.place(x=390,y=320)

img_multi = PhotoImage(file='img/multi.png')
multi_btn = Button(gui,image=img_multi,width=50,height=40,relief='ridge',borderwidth=3,command=multi_op)
multi_btn.place(x=390,y=380)

img_equal = PhotoImage(file='img/equal.png')
equal_btn = Button(gui,image=img_equal,width=120,height=40,relief='ridge',borderwidth=3,command=equal_op)
equal_btn.place(x=320,y=440)

#* --------- numbers -----------
img_one = PhotoImage(file='img/1.png')
one_btn = Button(gui,image=img_one,width=50,height=40,relief='ridge',borderwidth=3,command=btn1)
one_btn.place(x=180,y=380)

img_two = PhotoImage(file='img/2.png')
two_btn = Button(gui,image=img_two,width=50,height=40,relief='ridge',borderwidth=3,command=btn2)
two_btn.place(x=250,y=380)

img_three = PhotoImage(file='img/3.png')
three_btn = Button(gui,image=img_three,width=50,height=40,relief='ridge',borderwidth=3,command=btn3)
three_btn.place(x=320,y=380)

img_four = PhotoImage(file='img/4.png')
four_btn = Button(gui,image=img_four,width=50,height=40,relief='ridge',borderwidth=3,command=btn4)
four_btn.place(x=180,y=320)

img_five = PhotoImage(file='img/5.png')
five_btn = Button(gui,image=img_five,width=50,height=40,relief='ridge',borderwidth=3,command=btn5)
five_btn.place(x=250,y=320)

img_six = PhotoImage(file='img/6.png')
six_btn = Button(gui,image=img_six,width=50,height=40,relief='ridge',borderwidth=3,command=btn6)
six_btn.place(x=320,y=320)

img_seven = PhotoImage(file='img/7.png')
seven_btn = Button(gui,image=img_seven,width=50,height=40,relief='ridge',borderwidth=3,command=btn7)
seven_btn.place(x=180,y=260)

img_eight = PhotoImage(file='img/8.png')
eight_btn = Button(gui,image=img_eight,width=50,height=40,relief='ridge',borderwidth=3,command=btn8)
eight_btn.place(x=250,y=260)

img_nine = PhotoImage(file='img/9.png')
nine_btn = Button(gui,image=img_nine,width=50,height=40,relief='ridge',borderwidth=3,command=btn9)
nine_btn.place(x=320,y=260)

#* ---------- Advance Operation -----------------

img_zero = PhotoImage(file='img/0.png')
zero_btn = Button(gui,image=img_zero,width=120,height=40,relief='ridge',borderwidth=3,command=btn0)
zero_btn.place(x=180,y=440)

img_percent = PhotoImage(file='img/percent.png')
percent_btn = Button(gui,image=img_percent,width=50,height=40,relief='ridge',borderwidth=3,command=percent_op)
percent_btn.place(x=320,y=200)

img_clear = PhotoImage(file='img/clear.png')
clear_btn = Button(gui,image=img_clear,width=50,height=40,relief='ridge',borderwidth=3,command=clearing)
clear_btn.place(x=180,y=200)

img_tanh = PhotoImage(file='img/tanh.png')
tanh_btn = Button(gui,image=img_tanh,width=50,height=40,relief='ridge',borderwidth=3,command=tanh)
tanh_btn.place(x=250,y=200)

img_x2 = PhotoImage(file='img/x2.png')
x2_btn = Button(gui,image=img_x2,width=50,height=40,relief='ridge',borderwidth=3,command=x2)
x2_btn.place(x=110,y=200)

img_x3 = PhotoImage(file='img/x3.png')
x3_btn = Button(gui,image=img_x3,width=50,height=40,relief='ridge',borderwidth=3,command=x3)
x3_btn.place(x=110,y=260)

img_xy = PhotoImage(file='img/xy.png')
xy_btn = Button(gui,image=img_xy,width=50,height=40,relief='ridge',borderwidth=3,command=xy)
xy_btn.place(x=110,y=320)

img_ex = PhotoImage(file='img/ex.png')
ex_btn = Button(gui,image=img_ex,width=50,height=40,relief='ridge',borderwidth=3,command=neperx)
ex_btn.place(x=110,y=380)

img_e = PhotoImage(file='img/e.png')
e_btn = Button(gui,image=img_e,width=50,height=40,relief='ridge',borderwidth=3,command=neper)
e_btn.place(x=110,y=440)

img_pi = PhotoImage(file='img/pi.png')
pi_btn = Button(gui,image=img_pi,width=50,height=40,relief='ridge',borderwidth=3,command=pi)
pi_btn.place(x=40,y=200)

img_ln = PhotoImage(file='img/ln.png')
ln_btn = Button(gui,image=img_ln,width=50,height=40,relief='ridge',borderwidth=3,command=ln_op)
ln_btn.place(x=40,y=260)

img_sin = PhotoImage(file='img/sin.png')
sin_btn = Button(gui,image=img_sin,width=50,height=40,relief='ridge',borderwidth=3,command=sin)
sin_btn.place(x=40,y=320)

img_cos = PhotoImage(file='img/cos.png')
cos_btn = Button(gui,image=img_cos,width=50,height=40,relief='ridge',borderwidth=3,command=cos)
cos_btn.place(x=40,y=380)

img_tan = PhotoImage(file='img/tan.png')
tan_btn = Button(gui,image=img_tan,width=50,height=40,relief='ridge',borderwidth=3,command=tan)
tan_btn.place(x=40,y=440)

img_rad2 = PhotoImage(file='img/rad2.png')
rad2_btn = Button(gui,image=img_rad2,width=50,height=40,relief='ridge',borderwidth=3,command=forge2)
rad2_btn.place(x=40,y=140)

img_rad3 = PhotoImage(file='img/rad3.png')
rad3_btn = Button(gui,image=img_rad3,width=50,height=40,relief='ridge',borderwidth=3,command=forge3)
rad3_btn.place(x=110,y=140)

img_log = PhotoImage(file='img/log.png')
log_btn = Button(gui,image=img_log,width=50,height=40,relief='ridge',borderwidth=3,command=log10)
log_btn.place(x=180,y=140)

img_sinh = PhotoImage(file='img/sinh.png')
sinh_btn = Button(gui,image=img_sinh,width=50,height=40,relief='ridge',borderwidth=3,command=sinh)
sinh_btn.place(x=250,y=140)

img_cosh = PhotoImage(file='img/cosh.png')
cosh_btn = Button(gui,image=img_cosh,width=50,height=40,relief='ridge',borderwidth=3,command=cosh)
cosh_btn.place(x=320,y=140)

img_rand = PhotoImage(file='img/rand.png')
rand_btn = Button(gui,image=img_rand,width=50,height=40,relief='ridge',borderwidth=3,command=rand)
rand_btn.place(x=390,y=140)

gui.mainloop()