import heapq

class Solution:
	def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:

		result , current_min_cost = float('inf') , 0
		workers , max_heap = [] , []

		for index in range(len(quality)):

			workers.append([wage[index] / quality[index] , quality[index]])

		workers = sorted(workers)

		for ratio , current_quality in workers:

			heapq.heappush(max_heap , -current_quality)

			current_min_cost = current_min_cost + current_quality

			if len(max_heap) > k:
				current_min_cost = current_min_cost + heapq.heappop(max_heap)

			if len(max_heap) == k:
				result = min(result , current_min_cost * ratio)

		return result