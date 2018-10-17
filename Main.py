
import sys, getopt


def main(argv):
	period = 10
	pair = "BTC_XML"

	try:
		opts, args = getopt.getopt(argv,"hp:c:n:s:e:",["period=","currency=","points="])
	except getopt.GetoptError:
		print ("trading-bot.py -p <period length> -c <currency pair> -n <period of moving average>")
		sys.exit(2)
    #arguments
	for opt, arg in opts:
		if opt == '-h':
			print ('trading-bot.py -p <period length> -c <currency pair> -n <period of moving average>')
			sys.exit()
		elif opt in ("-p", "--period"):
			if (int(arg) in [300,900,1800,7200,14400,86400]):
				period = arg
			else:
				print 'Poloniex requires periods in 300,900,1800,7200,14400, or 86400 second increments'
				sys.exit(2)
		elif opt in ("-c", "--currency"):
			pair = arg
		elif opt in ("-n", "--points"):
			lengthOfMA = int(arg)
		elif opt in ("-s"):
			startTime = arg
		elif opt in ("-e"):
			endTime = arg



	#conn = poloniex('key goes here','key goes here') # connection au api

	if (startTime):
		historicalData = conn.api_query("returnChartData",{"currencyPair":pair,"start":startTime,"end":endTime,"period":period})

	while True:

    #implementer stratégie


if __name__ == "__main__":
	main(sys.argv[1:])