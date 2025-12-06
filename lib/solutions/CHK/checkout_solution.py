
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1 

        valid_items = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

        for char in skus:
            if char not in valid_items:
                return -1

        counts = {item: skus.count(item) for item in valid_items}

        counts['B'] = max(0, counts['B'] - counts['E'] // 2 )
        counts['M'] = max(0, counts['M'] - counts['N'] // 3 )
        counts['Q'] = max(0, counts['Q'] - counts['R'] // 3 )

        total = 0 

        total += (counts['A'] // 5) * 200 + ((counts['A'] % 5) // 3) * 130 + ((counts['A'] % 5) % 3) * 50 

        total += (counts['B'] // 2) * 45 + (counts['B'] % 2) * 30  
        total += (counts['F'] - counts['F'] // 3) * 10
        total += (counts['H'] // 10) * 80 + ((counts['H'] % 10) //5) * 45 + (counts['H'] % 5) * 10   
        total += (counts['K'] // 2) * 150 + (counts['K'] % 2) * 80  
        total += (counts['P'] // 5) * 200 + (counts['P'] % 5) * 50  
        total += (counts['Q'] // 3) * 80 + (counts['Q'] % 3) * 30  
        total += (counts['U'] - counts['U'] // 4) * 40  
        total += (counts['V'] // 3) * 130 + ((counts['V'] % 3) // 2) * 90  + (counts['V'] % 2) * 50

        prices = {
            'C':20, 'D':15, 'E':40, 'G':20, 'I':35, 'J':60, 'L':90,
            'M':15, 'N':40, 'O':10, 'R':50, 'S':30, 'T':20, 'W':20,
            'X':90, 'Y':10, 'Z':50
        }
       
        for item, price in prices.items():
            total += counts[item] * price

        return total




