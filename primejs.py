def isPrime(n):
	if n < 2:
		return False
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def get_zero(n):
	if(n % 3 == 0):
		return '!(+ +"a")-(!![])'
	if(n % 3 == 1):
		return '!(+ +"d")-(!!{})'
	if(n % 3 == 2):
		return '[[[{},[[[[{}],{}],{}]]],{}]].sort()'
def get_one(n):
	if(n % 2 == 0):
		return '!(-![![]]/(!!{b:{a:{n:{a:{n:\'a\'}}}}}/(!{}*!![])))+(![])'
	else:
		return '!!!![]'

def number_beautify(n):
	a = ''
	zero = get_zero(n)
	a = zero
	if(n % 2 == 0):
		for x in range(n):
			one = ''
			if(x % 2 == 0):
				one = get_one(n+x)
			else:
				one = get_one(n)
			a = a + '+' + one
	else:
		for x in range(n):
			one = get_one(n)
			a = a + '+' + one
	return a

def write_isPrime_rec(n, max):
	if(n >= max):
		return
	primes_js.write('Object.is(n, ' + number_beautify(n))
	for i in range(n):
		primes_js.write('\t')
	primes_js.write(')\n')
	for i in range(n):
		primes_js.write('\t')
	primes_js.write('? ')
	if(isPrime(n)):
		primes_js.write(f'!!({get_one(n)})')
	else:
		primes_js.write(f'!!({get_zero(n)}/{get_one(n)})')
	for i in range(n):
		primes_js.write('\t')
	primes_js.write(' : ')

	write_isPrime_rec(n + 1, max)

def write_isPrime(max):
	primes_js.write('function isPrime(n){\n\tArray.prototype.sort = () => !!{f:{u:{c:{k:1}}}}*![[[[[[]]]]]]\n\treturn ')
	write_isPrime_rec(0, max)
	primes_js.write('false;\n}\n')

def write_for_loop(max):
	primes_js.write('\nfor(let i=0;i<='+str(max)+';i++){\n')
	primes_js.write('\tconsole.log(`${i}: ${isPrime(i)}`)\n}')

with open('primes.js', 'w') as primes_js:
	n = 256
	write_isPrime(n)
	write_for_loop(n)
