class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude=float("-inf")
        sum_alt=0
        for val in gain:
            sum_alt+=val
            # max_altitude=max(sum_alt,max_altitude)
            max_altitude=sum_alt if sum_alt>=max_altitude else max_altitude

        return max_altitude if max_altitude>=0 else 0

        #You could have just used 0, for max_altitude since you don't actually want -ve values to be returned or them. 
        # Then you would have just returned max_altitude without condition.