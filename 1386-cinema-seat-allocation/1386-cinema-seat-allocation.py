class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:



        reserved_by_rows = {}
        
        for rows, seats in reservedSeats:
            if rows not in reserved_by_rows:
                reserved_by_rows[rows] = []
            reserved_by_rows[rows].append(seats)    


        count = 0
        

        for rows, res_seats in reserved_by_rows.items():
            seats = [False]*11

            for seatno in res_seats:
                seats[seatno]= True

            #left block check
            left_block_free = True
            for seatno in [2,3,4,5]:
                if seats[seatno] == True:
                    left_block_free = False

            #mid block check
            mid_block_free = True
            for seatno in [4,5,6,7]:
                if seats[seatno] == True:
                    mid_block_free = False

            #left block check
            right_block_free = True
            for seatno in [6,7,8,9]:
                if seats[seatno] == True:
                    right_block_free = False
            
            if left_block_free and right_block_free:
                count+=2
            
            elif left_block_free or mid_block_free or right_block_free:
                count+=1
            
        no_of_res_seats = len(reserved_by_rows)
        total_seats = n
        empty_seats = n - no_of_res_seats
        count+= 2 * empty_seats

        return count




