""" description """

class ATM(object):
	"""docstring for ATM"""
	# установка переменных и констант

	# -------------------------------
	# переменые - что указывают на номинал банкнот в кассетах
	global K1, K2, K3, K4
	K1, K2, K3, K4 = 0, 0, 0, 0

	# константы
	global q_cassets, max_q_in_cassets, min_q_in_cassets, teh_limit, denom_list
	q_cassets = 4                     # количество касет а АТМ
	max_q_in_cassets = 2000           # Максимальное кол-во банкнот в касете
	min_q_in_cassets = 0              # Минимально в касете может быть 0 банкнот / хотя в коде можно без константы обойтись нолем
	teh_limit = 40                    # Технический лимит = 40 банкнот за одну выдачу
	denom_list = [10, 20, 50, 100, 200, 500, 1000]


	# настройка номинала касет
	def setDenomination(): # OK // !!! подумать может запихнуть setDenomination() в цикл пока не введутся корректные данные?

		# define check function
		def check_availability(element, collection: iter):
			return element in collection

		# UI block
		print("Please set denomination for casset with value from: [" + ", ".join(map(str, denom_list)) + "]")
		K1 = int(input('set denomination for casset 1: '))
		K2 = int(input('set denomination for casset 2: '))
		K3 = int(input('set denomination for casset 3: '))
		K4 = int(input('set denomination for casset 4: '))
		
		# chek
		K1 = 0 if check_availability(K1, denom_list) is False else K1
		K2 = 0 if check_availability(K2, denom_list) is False else K2
		K3 = 0 if check_availability(K3, denom_list) is False else K3
		K4 = 0 if check_availability(K4, denom_list) is False else K4

		col = [K1, K2, K3, K4]
		if 0 in col:
			K1, K2, K3, K4 = 0, 0, 0, 0
			print('Operation unsuccessful!\nPlease repeat.')
		else:
			print('OK')



	# заправка банкомата (добавление наличности)
	def AddCash():
		# select casset -> enter quantity of banknotes
		# UI
		print('|----------------------------------------------------|')
		print('| Please, select casset for suply                    |')
		print('| 1, 2, 3 or 4                                       |')
		print('|----------------------------------------------------|')
		while true:
			select = int(input('Selected casset: '))
			select = select if 0 > select > 4 else 
		# to be continued


	# функция проверки возможности выдать запрашиваемой суммы
print(denom_list)
atm_4700 = ATM
atm_4700.setDenomination()
