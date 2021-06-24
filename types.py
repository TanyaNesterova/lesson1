def get_vat(payment):
	try:
		payment = float(payment)
		vat = payment/100*18
		return round(vat,2)