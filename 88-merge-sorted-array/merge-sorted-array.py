class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1          # last valid element in nums1
        j = n - 1          # last element in nums2
        k = m + n - 1      # last position in nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
