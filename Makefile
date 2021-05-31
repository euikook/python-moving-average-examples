
SS := weight sma wma ema

all: ${SS}

${SS}:
	python ${@}.py 
	
