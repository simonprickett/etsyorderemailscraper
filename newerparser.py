import quopri
import sys

with open('mbox') as fp:
	emailBuffer = []

	for line in fp:
		if (line.startswith("From: Etsy Transactions <transaction@etsy.com>")):
			emailStr = quopri.decodestring("".join(emailBuffer))

			strPos = emailStr.find("Order Total:")
			if (strPos > -1):
				newLinePos = emailStr.find("\n", strPos)
				orderTotal = emailStr[strPos + 12:newLinePos]
				sys.stdout.write(orderTotal.replace("USD", "").strip())
				sys.stdout.write(",")

			strPos = emailStr.find("* Email")
			if (strPos > -1):
				newLinePos = emailStr.find("\n", strPos)
				emailAddress = emailStr[strPos + 7:newLinePos]
				sys.stdout.write(emailAddress.strip())
				sys.stdout.write(",")

			strPos = emailStr.find("Shipping Address:")
			if (strPos > -1):
				newLinePos = emailStr.find("\n", strPos + 19)
				customerName = emailStr[strPos + 18:newLinePos]
				sys.stdout.write(customerName.strip())
				sys.stdout.write("\n")

			emailBuffer = []
		else:
			emailBuffer.append(line)
