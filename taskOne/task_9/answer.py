import math

class Answer:
    
    @staticmethod
    def factorial(n):
        result = 1
        if n == 0 or n == 1:
            return result
        else:
            for i in range (1, n + 1):
                result *= i
            return result
            
    @staticmethod
    def list_number(n):
        result = list()
        for i in range (2, n):
            flag = True
            for j in range (2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result
    
    @staticmethod
    def list_result(factorial_n, number_list):
        result = list()
        flag = True
        i = 0
        while flag:
            count = 0
            while factorial_n % number_list[i] == 0:
                count += 1
                factorial_n = factorial_n / number_list[i]
            result.append((number_list[i], count))
            if factorial_n == 1:
                flag = False
            i += 1
        return result
    
    @staticmethod
    def string_result(result_list):
        result_list.reverse()
        result ="Ответ: "
        count = 1
        for i, j in result_list:
            result += f"{i}^{j}"
            if count < len(result_list):
                count += 1
                result += " * "
        return result
            
    def decomp(self, n):
        factorial_n = self.factorial(n)
        number_list = self.list_number(n)
        number_list.reverse()
        result_list = self.list_result(factorial_n, number_list)
        result = self.string_result(result_list)
        return result
    