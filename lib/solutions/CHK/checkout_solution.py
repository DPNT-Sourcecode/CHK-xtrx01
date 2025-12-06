
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1 

        valid_items = {'A','B','C','D','E'}

        for char in skus:
            if char not in valid_items:
                return -1

        a = skus.count('A')
        b = skus.count('B')
        c = skus.count('C')
        d = skus.count('D')
        e = skus.count('E')

        free_b_e = e // 2
        b = max(0, b - free_b_e)

        a_total = 0

        five_a = a // 5
        a_total += five_a * 200
        a_remaining = a % 5

        three_a = a_remaining // 3
        a_total += three_a * 130
        a_remaining = a_remaining % 3

        a_total += a_remaining * 50

        b_total = (b // 2) * 45 + (b % 2) * 30 

        c_total = c * 20
        d_total = d * 15
        e_total = e * 40

        return a_total + b_total + c_total + d_total + e_total


