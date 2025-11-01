import matplotlib.pyplot as plt
from calculator import washingDishes, disposableTableware

PRICE_OF_A_PLATE = 350 # рублей - цена за тарелку

def show_cost_comparison(numberOfPlates, pricePerPlate, priceColdWater, priceHotWater, timeSpentWashing, priceOfHumanTime, volumeOfDetergent, priceOfBottleOfDetergent):
	try:
		numberOfPlates = float(numberOfPlates)
		pricePerPlate = float(pricePerPlate)
		priceColdWater = float(priceColdWater)
		priceHotWater = float(priceHotWater)
		timeSpentWashing = float(timeSpentWashing)
		priceOfHumanTime = float(priceOfHumanTime)
		volumeOfDetergent = float(volumeOfDetergent)
		priceOfBottleOfDetergent = float(priceOfBottleOfDetergent)

		disposable_cost_per_plate = disposableTableware(numberOfPlates, pricePerPlate)
		washing_cost_per_plate = washingDishes(
			priceColdWater,
			priceHotWater,
			timeSpentWashing,
			priceOfHumanTime,
			priceOfBottleOfDetergent,
			volumeOfDetergent
			)

		# Количество использований
		x = list(range(1, 60))

		# Затраты
		y_disposable = [disposable_cost_per_plate * i for i in x]
		y_washing = [PRICE_OF_A_PLATE + washing_cost_per_plate * i for i in x]

		# Ищем точку, где линии пересекаются
		break_even_index = None
		for i in range(len(x)):
			if y_disposable[i] > y_washing[i]:
				break_even_index = i
				break

		plt.figure(figsize=(8, 5))
		plt.plot(x, y_disposable, label="Одноразовая посуда", color="orange")
		plt.plot(x, y_washing, label="Мытьё посуды", color="skyblue")
		plt.xlabel("Количество использований")
		plt.ylabel("Затраты (₽)")
		plt.legend()

		# Отмечаем точку окупаемости
		if break_even_index:
			plt.scatter(
				break_even_index,
				y_washing[break_even_index],
				color="red",
				s=30,
				label="Точка окупаемости"
				)

		plt.grid(True, linestyle="--", alpha=0.6)
		plt.tight_layout()
		plt.show()
	except ValueError:
		print("Ошибка: введены некорректные данные")