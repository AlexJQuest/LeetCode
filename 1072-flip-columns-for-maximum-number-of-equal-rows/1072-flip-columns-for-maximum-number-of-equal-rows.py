class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row_count = {}
        for row in matrix:
            row_tuple = tuple(row)
            flipped_row = tuple(1 - digit for digit in row)
            row_count[row_tuple] = row_count.get(row_tuple, 0) + 1
            row_count[flipped_row] = row_count.get(flipped_row, 0) + 1
        return max(row_count.values())
 
    
    
    
        