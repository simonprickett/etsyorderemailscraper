import sys

processingShippingAddress = False
requestedAddress = 0

with open('mbox') as fp:
	for line in fp:
		if (requestedAddress == 2):
			sys.stdout.write(line.strip())
			sys.stdout.write(",")
			requestedAddress = 0
		
		if (requestedAddress == 1):
			requestedAddress = 2
		
		if (line.startswith("The buyer has requested that the item be shipped to the following address.")):
			requestedAddress = 1
		
		if (line.startswith("Order Total:") or line.startswith("Total:") or line.startswith("Total Sale:") or line.startswith("TOTAL SALE:")):
			dollarAmount = (line.replace("Order Total:", "").replace("Total:", "").replace("Total Sale:", "").replace("TOTAL SALE:", "").replace("(USD)", "").replace("(US)", "").replace("USD", "").strip())
			dollarAmount = dollarAmount[dollarAmount.find("$"):]
			dollarAmount = dollarAmount.replace("<br>", "").strip()
			sys.stdout.write(dollarAmount)
			sys.stdout.write(',')
		
		if (processingShippingAddress):
			buyerName = line.replace("<br>", "").strip()
			
			if (len(buyerName) > 0):
				sys.stdout.write(buyerName)
				sys.stdout.write(',')
			else:
				requestedAddress = 2

			processingShippingAddress = False
		
		if (line.startswith("Shipping Address:") or line.startswith("The buyer has requested that the item be shipped to:")):
			processingShippingAddress = True
		
		if (line.startswith(" * Send an email to ") or line.startswith("* Email") or line.startswith(" * Email") or line.startswith("If you need to contact the buyer, you may do so by sending an email to:") or line.startswith("If you would like to contact the buyer, send an email to")):
			emailData = line.replace(" * Send an email to ", "").replace(" * Email:", "").replace("* Email", "").replace("If you need to contact the buyer, you may do so by sending an email to:", "").replace("If you would like to contact the buyer, send an email to", "").strip()
			orStartPos = emailData.find("or start")
			if (orStartPos > -1):
				emailData = emailData[:orStartPos]

			emailData = emailData.replace("<br>", "").replace("</a>", "").strip()
			sys.stdout.write(emailData)
			sys.stdout.write("\n")