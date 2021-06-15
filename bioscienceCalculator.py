#Bioscience Calculator Ver.1.0
#Written by Jiyeon Choi
#Jun.09.2021.

from tkinter import *
from tkinter import ttk


#Initialize variables
result1 = 0
result2 = 0
result3 = 0
result4 = 0


#This method calculates the case 1.
def calculate_case1_pressed():
    global result1
    if entered_solute_case1.get() == "" or entered_solution_case1.get() == "":
        missed_value_entered("True")
        print("Type all values")
    else:
        missed_value_entered("False")
        result1 =float(entered_solute_case1.get())/float(entered_solution_case1.get())
        result_case1.delete(0, 'end')
        result_case1.insert("end", result1)
        print(result1)


def calculate_case2_pressed():
    global result2
    global result3
    if entered_mw_case2.get() == "" or entered_solute_case2.get() == "" or entered_solution_case2.get() == "":
        missed_value_entered("True")
        print("Type all values")
    else:
        missed_value_entered("False")
        result2 = float(entered_solute_case2.get())/float(entered_mw_case2.get())
        result_solute_case2.delete(0, 'end')
        result_solute_case2.insert("end", result2)
        print(result2)
        result3 = result2/float(entered_solution_case2.get())
        result_molarity_case2.delete(0, 'end')
        result_molarity_case2.insert("end", result3)
        print(result3)


def calculate_case3_pressed():
    global result4
    if entered_mw_case3.get() == "" or entered_molarity_case3.get() == "" or entered_solution_case3.get() == "":
        missed_value_entered("True")
        print("Type all values")
    else:
        missed_value_entered("False")
        result4 =float(entered_mw_case3.get())*float(entered_molarity_case3.get())*float(entered_solution_case3.get())
        result_case3.delete(0, 'end')
        result_case3.insert("end", result4)
        print(result4)


def missed_value_entered(status):
    text1 = StringVar()
    label = Label(textvariable=text1, foreground="red")

    if status == "True":
        text1.set("Please type all values.")
        label.grid(row=7, columnspan=9)
    elif status == "False":
        text1.set("                                               ")
        label.grid(row=7, columnspan=9)
    return


def image(button):
    img = PhotoImage(file="button.png")
    img = img.subsample(button, button)
    return img


#Create window
window = Tk()
window.title("Molarity Calculator")
window.geometry('800x260')
#Set the image button size
img = image(15)



#Ver 1 Calculator
#Solute(mol) & Volume -> Molarity Calculator
#Instruction
label = Label(text="😃 Case 1 \n "
                   "Solute(mol) & Volume ➜ Molarity", foreground="black")
label.grid(row=0, columnspan=3)

#Type values
label1 = Label(window, text="solute ", foreground="teal")
label1.grid(row=1, column=0)
entered_solute_case1 = ttk.Entry(window, width=20)
entered_solute_case1.grid(row=1, column=1)
label1_scale = Label(window, text="mol", foreground="teal")
label1_scale.grid(row=1, column=2)

label2 = Label(window, text="solution ", foreground="teal")
label2.grid(row=2, column=0)
entered_solution_case1 = ttk.Entry(window, width=20)
entered_solution_case1.grid(row=2, column=1)
label2_scale = Label(window, text="L", foreground="teal")
label2_scale.grid(row=2, column=2)

#Calculate button
button_case1 = Button(window, text="Calculate", compound=CENTER, fg="white", activeforeground="pink", font="arial 13",
    width=110,height=20,relief="groove", pady=10, bd=0, image=img, command=lambda :calculate_case1_pressed())
button_case1.grid(row=4, column=1)

#Show the result
label3 = Label(window, text="Molarity ", foreground="purple")
label3.grid(row=5, column=0)
result_case1 = ttk.Entry(window, width=20)
result_case1.grid(row=5, column=1)
label3_scale = Label(window, text="M", foreground="purple")
label3_scale.grid(row=5, column=2)


#Case 2 Calculator
#Molecular Weight & Solute(g) & Volume -> Solute(mol) & Molarity Calculator
#Instruction
label = Label(text="😃 Case 2 \n "
                   "M.W. & Solute(g) & Volume ➜ Solute(mol) & Molarity", foreground="black")
label.grid(row=0, column=3, columnspan=3)

#Type values
label4 = Label(window, text="Molecular Weight ", foreground="teal")
label4.grid(row=1, column=3)
entered_mw_case2 = ttk.Entry(window, width=20)
entered_mw_case2.grid(row=1, column=4)
label4_scale = Label(window, text="g/mol", foreground="teal")
label4_scale.grid(row=1, column=5)

label5 = Label(window, text="solute ", foreground="teal")
label5.grid(row=2, column=3)
entered_solute_case2 = ttk.Entry(window, width=20)
entered_solute_case2.grid(row=2, column=4)
label5_scale = Label(window, text="g", foreground="teal")
label5_scale.grid(row=2, column=5)

label6 = Label(window, text="solution ", foreground="teal")
label6.grid(row=3, column=3)
entered_solution_case2 = ttk.Entry(window, width=20)
entered_solution_case2.grid(row=3, column=4)
label6_scale = Label(window, text="L", foreground="teal")
label6_scale.grid(row=3, column=5)

#Calculate button
button_case2 = Button(window, text="Calculate", compound=CENTER, fg="white", activeforeground="pink", font="arial 13",
    width=110,height=20,relief="groove", pady=10, bd=0, image=img, command=lambda :calculate_case2_pressed())
button_case2.grid(row=4, column=4)

#Show the result
label7 = Label(window, text="Solute ", foreground="purple")
label7.grid(row=5, column=3)
result_solute_case2 = ttk.Entry(window, width=20)
result_solute_case2.grid(row=5, column=4)
label7_scale = Label(window, text="mol", foreground="purple")
label7_scale.grid(row=5, column=5)

label8 = Label(window, text="Molarity ", foreground="purple")
label8.grid(row=6, column=3)
result_molarity_case2 = ttk.Entry(window, width=20)
result_molarity_case2.grid(row=6, column=4)
label8_scale = Label(window, text="M", foreground="purple")
label8_scale.grid(row=6, column=5)


#Case 3 Calculator
#Molecular Weight & Molarity & Volume -> Solute(g) Calculator
#Instruction
label = Label(text="😃 Case 3 \n "
                   "M.W. & Molarity & Volume ➜ Solute(g)", foreground="black")
label.grid(row=0, column=6, columnspan=3)

#Type values
label9 = Label(window, text="Molecular Weight ", foreground="teal")
label9.grid(row=1, column=6)
entered_mw_case3 = ttk.Entry(window, width=20)
entered_mw_case3.grid(row=1, column=7)
label9_scale = Label(window, text="g/mol", foreground="teal")
label9_scale.grid(row=1, column=8)

label10 = Label(window, text="Molarity ", foreground="teal")
label10.grid(row=2, column=6)
entered_molarity_case3 = ttk.Entry(window, width=20)
entered_molarity_case3.grid(row=2, column=7)
label10_scale = Label(window, text="M", foreground="teal")
label10_scale.grid(row=2, column=8)

label11 = Label(window, text="solution ", foreground="teal")
label11.grid(row=3, column=6)
entered_solution_case3 = ttk.Entry(window, width=20)
entered_solution_case3.grid(row=3, column=7)
label11_scale = Label(window, text="L", foreground="teal")
label11_scale.grid(row=3, column=8)

#Calculate button
button_case3 = Button(window, text="Calculate", compound=CENTER, fg="white", activeforeground="pink", font="arial 13",
    width=110,height=20,relief="groove", pady=10, bd=0, image=img, command=lambda :calculate_case3_pressed())
button_case3.grid(row=4, column=7)

#Show the result
label12 = Label(window, text="Solute ", foreground="purple")
label12.grid(row=5, column=6)
result_case3 = ttk.Entry(window, width=20)
result_case3.grid(row=5, column=7)
label12_scale = Label(window, text="g", foreground="purple")
label12_scale.grid(row=5, column=8)

label_space = Label(window, text="\n\n")
label_space.grid(row=7, rowspan=5, column=7)
label_name = Label(window, text="©2021 Jiyeon Choi", foreground="blue")
label_name.grid(row=15, column=7)


window.mainloop()