processingShippingAddress = False

with open('mbox') as fp:
	for line in fp:
		# TODO Date:
		if (line.startswith("Order Total:") or line.startswith("Total:") or line.startswith("Total Sale:") or line.startswith("TOTAL SALE:")):
			print line.replace("Order Total:", "").replace("Total:", "").replace("Total Sale:", "").replace("TOTAL SALE:", "").replace("(USD)", "").replace("(US)", "").strip()
		if (processingShippingAddress):
			print line.strip()
			processingShippingAddress = False
		if (line.startswith("Shipping Address:") or line.startswith("The buyer has requested that the item be shipped to:")):
			processingShippingAddress = True
		if (line.startswith("* Email") or line.startswith(" * Email") or line.startswith("If you need to contact the buyer, you may do so by sending an email to:")):
			print ((line.replace("* Email", "")).replace("If you need to contact the buyer, you may do so by sending an email to:", "")).strip()