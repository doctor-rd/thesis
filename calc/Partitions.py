def potenzmenge(a):
	if a == set([]):
		return set([frozenset()])
	else:
		b = set(a)
		x = b.pop()
		out=set()
		for y in potenzmenge(b):
			out.add(y)
			out.add(y|set([x]))
		return out

def partitions(a):
	out=set()
	for x in potenzmenge(a)-set([frozenset([])]):
		if x==a:
			out.add(Partition([x]))
		else:
			b=a-x
			for y in partitions(b):
				out.add(y|set([x]))
	return out

class Partition(frozenset):
	def __lt__(self, other):
		if len(self)<=len(other):
			return False

		for x in self:
			fertig = 0
			for y in other:
				if x<=y:
					fertig = 1
					break
			if fertig == 0:
				return False
		return True

	def op(self,f):
		out=set()
		for y in self:
			yziel=set()
			for x in y:
				yziel.add(f(x))
			out.add(frozenset(yziel))
		return Partition(out)
