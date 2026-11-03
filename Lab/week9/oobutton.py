from tkinter import *

def on_button_click(event):
    print(f"버튼이 클릭되었습니다! {event}")

root = Tk()
root.title("OOB Button ")
root.geometry("600x400")

label = Label(root, text="객체지향 왼도우 프로그래밍", font=("Arial", 24))
label.bind("<Button-1>", lambda event: print(f"라벨이 클릭되었습니다!: {event}"))
label.pack(pady=20)

#button = Button(root, text="클릭해볼까요?" , command=on_button_click )
button = Button(root, text="클릭해볼까요?" ,  )
button.bind("<Button-1>", on_button_click)
button.pack(pady=20)



root.mainloop()