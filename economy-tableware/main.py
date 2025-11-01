from calculator import calculator
from plots import show_cost_comparison
import tkinter

def run_app():
	root = tkinter.Tk()
	root.title("Экономика посуды")
	root.geometry("360x360")

	lb1 = tkinter.Label(root, text="Количество посуды в наборе (шт):")
	lb1.place(x = 20, y = 10)
	en1 = tkinter.Entry(root)
	en1.place(x = 300, y = 10, width = 30, height = 20)


	lb2 = tkinter.Label(root, text="Цена набора (₽):")
	lb2.place(x = 20, y = 40)
	en2 = tkinter.Entry(root)
	en2.place(x = 300, y = 40, width = 30, height = 20)

	lb3 = tkinter.Label(root, text="Стоимость холодной воды за m^3 (₽):")
	lb3.place(x = 20, y = 70)
	en3 = tkinter.Entry(root)
	en3.place(x = 300, y = 70, width = 30, height = 20)

	lb4 = tkinter.Label(root, text="Стоимость горячей воды за m^3 (₽):")
	lb4.place(x = 20, y = 100)
	en4 = tkinter.Entry(root)
	en4.place(x = 300, y = 100, width = 30, height = 20)

	lb5 = tkinter.Label(root, text="Время на мытьё тарелки (сек):")
	lb5.place(x = 20, y = 130)
	en5 = tkinter.Entry(root)
	en5.place(x = 300, y = 130, width = 30, height = 20)


	lb6 = tkinter.Label(root, text="Стоимость часа вашего времени (₽):")
	lb6.place(x = 20, y = 160)
	en6 = tkinter.Entry(root)
	en6.place(x = 300, y = 160, width = 30, height = 20)

	lb7 = tkinter.Label(root, text="Объем бутылки моющего средства (мл):")
	lb7.place(x = 20, y = 190)
	en7 = tkinter.Entry(root)
	en7.place(x = 300, y = 190, width = 30, height = 20)

	lb8 = tkinter.Label(root, text="Стоимость бутылки моющего средства (₽):")
	lb8.place(x = 20, y = 220)
	en8 = tkinter.Entry(root)
	en8.place(x = 300, y = 220, width = 30, height = 20)

	bt1 = tkinter.Button(
		root,
		text = "Рассчитать",
		command = lambda:calculator(en1.get(), en2.get(), en3.get(), en4.get(), en5.get(), en6.get(), en7.get(), en8.get()))
	bt1.place(x = 70, y = 280, width = 100)

	bt2 = tkinter.Button(
		root,
		text = "Визуализировать",
		command = lambda:show_cost_comparison(en1.get(), en2.get(), en3.get(), en4.get(), en5.get(), en6.get(), en7.get(), en8.get()))
	bt2.place(x = 200, y = 280, width = 100)

	root.mainloop()

if __name__ == "__main__":
	run_app()