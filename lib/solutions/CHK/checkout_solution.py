
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1 

        valid_items = set('ABCDEFGHIJKLMNOPQKRSTUVWXYZ')

        for char in skus:
            if char not in valid_items:
                return -1

        counts = {item: skus.count(item) for item in valid_items}

        counts['B'] = max(0, counts['B'] - counts['E'] // 2 )
        counts['M'] = max(0, counts['M'] - counts['N'] // 2 )
        counts['Q'] = max(0, counts['Q'] - counts['R'] // 2 )

        total = 0 
        total += (counts['A'] // 5) * 200 + ((counts['A'] % 5) // 3) * 130 + ((counts['A'] % 5) % 3) * 50 

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

