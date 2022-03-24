from tkinter import *
from functools import partial
import random

array4 = []
array6 = []
array8 = []
array10 = []
array12 = []
array20 = []
array100 = []

def click(a, output, array, sumx):
    sumx.delete(0.0, END)
    result = random.randint(1,a)
    output.insert(END, str(result)+" | ")
    array.append(result)
    #print(array)
    sumx.insert(END, "*"+str(len(array))+"\n\n"+str(sum(array)))
    return result

def clear(output, array, sumx):
    output.delete(0.0, END)
    sumx.delete(0.0, END)
    array.clear()

window = Tk()
window.title("Dick roller")
window.configure(height=500, width=500)

output4 = Text(window, width=15, height=6, wrap=WORD, background="white")
output4.grid(row=0, column=1, columnspan=2)
output6 = Text(window, width=15, height=6, wrap=WORD, background="white")
output6.grid(row=1, column=1, columnspan=2)
output8 = Text(window, width=15, height=6, wrap=WORD, background="white")
output8.grid(row=2, column=1, columnspan=2)
output10 = Text(window, width=15, height=6, wrap=WORD, background="white")
output10.grid(row=3, column=1, columnspan=2)
output12 = Text(window, width=15, height=6, wrap=WORD, background="white")
output12.grid(row=4, column=1, columnspan=2)
output20 = Text(window, width=15, height=6, wrap=WORD, background="white")
output20.grid(row=5, column=1, columnspan=2)
output100 = Text(window, width=15, height=6, wrap=WORD, background="white")
output100.grid(row=6, column=1, columnspan=2)

sum4 = Text(window, width=4, height=3, wrap=WORD, background="white")
sum4.grid(row=0, column=4, columnspan=1)
sum6 = Text(window, width=4, height=3, wrap=WORD, background="white")
sum6.grid(row=1, column=4, columnspan=1)
sum8 = Text(window, width=4, height=3, wrap=WORD, background="white")
sum8.grid(row=2, column=4, columnspan=1)
sum10 = Text(window, width=4, height=3, wrap=WORD, background="white")
sum10.grid(row=3, column=4, columnspan=1)
sum12 = Text(window, width=4, height=3, wrap=WORD, background="white")
sum12.grid(row=4, column=4, columnspan=1)
sum20 = Text(window, width=4, height=3, wrap=WORD, background="white")
sum20.grid(row=5, column=4, columnspan=1)
sum100 = Text(window, width=4, height=3, wrap=WORD, background="white")
sum100.grid(row=6, column=4, columnspan=1)

d4 = Button(window, text="4", fg="white", font = "none 12 bold", bg="red3", width=10, height=5, command=partial(click,4,output4,array4,sum4)).grid(row=0, column=0)
d6 = Button(window, text="6", fg="white", font = "none 12 bold", bg="darkorange1", width=10, height=5, command=partial(click,6,output6,array6,sum6)).grid(row=1, column=0)
d8 = Button(window, text="8", fg="white", font = "none 12 bold", bg="yellow3", width=10, height=5, command=partial(click,8,output8,array8,sum8)).grid(row=2, column=0)
d10 = Button(window, text="10", fg="white", font = "none 12 bold", bg="forestgreen", width=10, height=5, command=partial(click,10,output10,array10,sum10)).grid(row=3, column=0)
d12 = Button(window, text="12", fg="white", font = "none 12 bold", bg="royalblue1", width=10, height=5, command=partial(click,12,output12,array12,sum12)).grid(row=4, column=0)
d20 = Button(window, text="20", fg="white", font = "none 12 bold", bg="navy", width=10, height=5, command=partial(click,20,output20,array20,sum20)).grid(row=5, column=0)
d100 = Button(window, text="100", fg="white", font = "none 12 bold", bg="darkorchid", width=10, height=5, command=partial(click,100,output100,array100,sum100)).grid(row=6, column=0)

delete4 = Button(window, text="DEL", fg="black", font="none 8 bold", bg="white", width=3, height=1, command=partial(clear,output4,array4,sum4)).grid(row=0, column=6)
delete6 = Button(window, text="DEL", fg="black", font="none 8 bold", bg="white", width=3, height=1, command=partial(clear,output6,array6,sum6)).grid(row=1, column=6)
delete8 = Button(window, text="DEL", fg="black", font="none 8 bold", bg="white", width=3, height=1, command=partial(clear,output8,array8,sum8)).grid(row=2, column=6)
delete10 = Button(window, text="DEL", fg="black", font="none 8 bold", bg="white", width=3, height=1, command=partial(clear,output10,array10,sum10)).grid(row=3, column=6)
delete12 = Button(window, text="DEL", fg="black", font="none 8 bold", bg="white", width=3, height=1, command=partial(clear,output12,array12,sum12)).grid(row=4, column=6)
delete20 = Button(window, text="DEL", fg="black", font="none 8 bold", bg="white", width=3, height=1, command=partial(clear,output20,array20,sum20)).grid(row=5, column=6)
delete100 = Button(window, text="DEL", fg="black", font="none 8 bold", bg="white", width=3, height=1, command=partial(clear,output100,array100,sum100)).grid(row=6, column=6)

'''
def click(a):
    result = random.randint(1,a)
    return result
    
zmienna = click(999)
Label(window, text=zmienna, font="none 12 bold", relief=RAISED).grid(column=0, row=7)
'''

window.mainloop()
