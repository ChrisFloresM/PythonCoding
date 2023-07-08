class Solution(object):
    def maximumWealth(self, accounts):
        wealthiest = 0
        for customer in accounts:
            if sum(customer) > wealthiest:
                wealthiest = sum(customer)
        return customer
            
"""         customer_1 = accounts[0]
        customer_2 = accounts[1]

        total_cstm_1 = sum(customer_1)
        total_cstm_2 = sum(customer_2)

        if(total_cstm_1 > total_cstm_2):
            weltst_customer = total_cstm_1

        elif(total_cstm_2 > total_cstm_1):
            weltst_customer = total_cstm_2
            
        else:
            weltst_customer = total_cstm_1

         return weltst_customer  """
         
"""         :type accounts: List[List[int]]
        :rtype: int """
        
        
acc = [[1, 12, 3], [1, 23, 0]]
acc_2 = [[1,5], [7,3], [3,5]]
my_solution = Solution()
print(my_solution.maximumWealth(acc))
print(my_solution.maximumWealth(acc_2))