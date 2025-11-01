

AMOUNT_OF_DETERGENT_PER_PLATE = 2.0 # мл - моющее средство на одну тарелку

def calculator(numberOfPlates, pricePerPlate, priceColdWater, priceHotWater, timeSpentWashing, priceOfHumanTime, volumeOfDetergent, priceOfBottleOfDetergent):
	try:
		numberOfPlates = float(numberOfPlates)
		pricePerPlate = float(pricePerPlate)
		priceColdWater = float(priceColdWater)
		priceHotWater = float(priceHotWater)
		timeSpentWashing = float(timeSpentWashing)
		priceOfHumanTime = float(priceOfHumanTime)
		volumeOfDetergent = float(volumeOfDetergent)
		priceOfBottleOfDetergent = float(priceOfBottleOfDetergent)

		disposable = disposableTableware(numberOfPlates, pricePerPlate)
		washing = washingDishes(
			priceColdWater,
			priceHotWater,
			timeSpentWashing,
			priceOfHumanTime,
			priceOfBottleOfDetergent,
			volumeOfDetergent
			)

		if disposable < washing:
			print(f"Выгоднее одноразовая посуда ({disposable:.2f} ₽ против {washing:.2f} ₽)")
		else:
			print(f"Выгоднее мыть посуду ({washing:.2f} ₽ против {disposable:.2f} ₽)")
	except ValueError:
		print("Ошибка: введены некорректные данные")

def disposableTableware(
		numberOfPlates: float,
		setPrice: float
):
	total = setPrice / numberOfPlates
	return total

def washingDishes(
		priceColdWater: float,
		priceHotWater: float,
		timeSpentWashing: float,
		PriceOfHumanTime: float,
		PriceOfBottleOfDetergent: float,
		VolumeOfDetergent: float
		) -> float:

	# Средняя цена воды (2 части холодной, 1 часть горячей)
	avgWaterPrice = ((priceColdWater / 3) * 2 + (priceHotWater / 3) * 1)
	# Расход воды: примерно 0.13 литра в секунду (в реальности ~8 л/мин)
	waterUsageLiters = 0.13 * timeSpentWashing
	# Стоимость воды, потраченной на мытье одной тарелки
	waterPrice = avgWaterPrice * waterUsageLiters / 1000 # делим на 1000, т.к. цена за м³

	# Стоимость времени человека
	timePrice = timeSpentWashing / 3600 * PriceOfHumanTime # делим на 3600, т.к. цена за час, а у нас время в секундах

	# Стоимость моющего средства
	detergentPrice = (PriceOfBottleOfDetergent / VolumeOfDetergent) * AMOUNT_OF_DETERGENT_PER_PLATE

	total = waterPrice + timePrice + detergentPrice
	return total