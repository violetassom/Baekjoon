
def is_prime_number(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def prime_factorization(num):
    if num == 1:
        pass
    else:
        result_list = []
        use_prime_list = []

        for i in range(2, num + 1):
            if num%i == 0:
                if is_prime_number(i) == True:
                    use_prime_list.append(i)

        # for j in use_prime_list:
        #     if num%j != 0:
        #         use_prime_list.remove(j)
        # print(use_prime_list)
        while True:
            if num ==1:
                break
            else:
                for i in use_prime_list:
                    if num % i == 0:
                        result_list.append(i)
                        num = num / i
        result_list.sort()
        if len(result_list)==1:
            print(result_list[0])
        else:
            for k in result_list:
                print(k)
import sys
n = int(sys.stdin.readline())
prime_factorization(n)