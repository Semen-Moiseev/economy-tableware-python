import calculator
import tkinter

def run_app():
	root = tkinter.Tk()
	root.title("Экономика посуды")
	root.geometry("600x400")

	lb1 = tkinter.Label(root, text="Количество посуды в наборе (шт):")
	lb1.place(x = 20, y = 10)
	en1 = tkinter.Entry(root)
	en1.place(x = 250, y = 10, width = 30, height = 20)


	lb2 = tkinter.Label(root, text="Цена набора (₽):")
	lb2.place(x = 20, y = 40)
	en2 = tkinter.Entry(root)
	en2.place(x = 250, y = 40, width = 30, height = 20)


	lb3 = tkinter.Label(root, text="Время на мытьё тарелки (сек):")
	lb3.place(x = 20, y = 70)
	en3 = tkinter.Entry(root)
	en3.place(x = 250, y = 70, width = 30, height = 20)


	lb4 = tkinter.Label(root, text="Стоимость часа вашего времени (₽):")
	lb4.place(x = 20, y = 100)
	en4 = tkinter.Entry(root)
	en4.place(x = 250, y = 100, width = 30, height = 20)

	bt = tkinter.Button(root,text = "Рассчитать", command = calculator)
	bt.place(x = 150, y = 150, width = 100)

	root.mainloop()

if __name__ == "__main__":
	run_app()