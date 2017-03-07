def data_type(var):
	if type(var) == str:
		return len(var)
	elif type(var) == bool:
		return var
	elif type(var) == int:
		if var < 100:
			return "less than 100"
		elif var == 100:
			return 'equal to 100'
		else:
			return "more than 100"
	elif type(var) == list:
		if len(var) < 3:
			return None
		else:
			return var[2]
	else:
	  return 'no value'