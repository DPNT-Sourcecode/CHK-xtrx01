
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1 

        valid_items = {'A','B','C','D','E','F'}

        for char in skus:
            if char not in valid_items:
                return -1

        a = skus.count('A')
        b = skus.count('B')
        c = skus.count('C')
        d = skus.count('D')
        e = skus.count('E')
        f = skus.count('F')

        free_b_e = e // 2
        b = max(0, b - free_b_e)

        f_to_pay = f - (f // 3)

        a_total = (a // 5) * 200 + ((a % 5) // 3) * 130 + ((a % 5) % 3) * 50
        b_total = (b // 2) * 45 + (b % 2) * 30 
        c_total = c * 20
        d_total = d * 15
        e_total = e * 40
        f_total = f_to_pay * 10

        return a_total + b_total + c_total + d_total + e_total + f_total

