class Solution:

	def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
		if len(arr) > 2:
			res = []  # list for storing the list: [prime fraction of arr[i]/arr[j], arr[i], arr[j]]

			for i in range(len(arr)):
				for j in range(i + 1, len(arr)):
					# creating and adding the sublist to res
					tmp = [arr[i] / arr[j], arr[i], arr[j]]
					res.append(tmp)

			# sorting res on the basis of value of arr[i] 
			res.sort(key=lambda x: x[0])

			# creating and returning the required list
			return [res[k - 1][1], res[k - 1][2]]
		else:
			return arr