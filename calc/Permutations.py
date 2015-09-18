class Permutation:
	def __init__(self, other=None):
		if other==None:
			self.values=[]
		else:
			self.values=list(other.values)

	def __call__(self, x):
		return self.values[x]

	def __repr__(self):
		return str(self.values)

	def __mul__(self, other):
		res=Permutation()
		for i in range(len(other.values)):
			res.add(self(other(i)))
		return res

	def __eq__(self, other):
		if other==None:
			return False
		return self.values==other.values

	def __hash__(self):
		return 0

	def add(self,v):
		if v in self.values:
			return False
		self.values.append(v)
		return True

	def sign(self):
		res=1
		for i in range(len(self.values)):
			for j in range(i+1,len(self.values)):
				if self.values[i]>self.values[j]:
					res*=-1
		return res

def transposition(n, a=0, b=0):
	res=Permutation()
	for i in range(n):
		if a==i:
			res.add(b)
		else:
			if b==i:
				res.add(a)
			else:
				res.add(i)
	return res

def symmetrie(n,start=None,out=None):
	if out==None:
		out=[]
	if start==None:
		start=Permutation()
	done=True
	for i in range(n):
		neu=Permutation(start)
		if neu.add(i):
			done=False
			symmetrie(n,neu,out)
	if done:
		out.append(neu)
	return out
