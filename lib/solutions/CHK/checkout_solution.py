
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
        total += (counts['K'] // 2) * 120 + (counts['K'] % 2) * 70  
        total += (counts['P'] // 5) * 200 + (counts['P'] % 5) * 50  
        total += (counts['Q'] // 3) * 80 + (counts['Q'] % 3) * 30  
        total += (counts['U'] - counts['U'] // 4) * 40  
        total += (counts['V'] // 3) * 130 + ((counts['V'] % 3) // 2) * 90  + ((counts['V'] % 3) % 2) * 50

        group_items = ['S','T','X','Y','Z']

        group_counts = {item: counts[item] for item in group_items}

        group_total_items = sum(group_counts.values())

        group_offers = group_total_items // 3

        group_remainder = group_total_items % 3

        total += group_offers * 45

        items_by_price = [('Z', 21), ('S', 20), ('T', 20), ('Y', 20), ('X', 17)]

        for item, price in reversed(items_by_price):
            while group_counts[item] > 0 and group_remainder > 0:
                total += price
                group_counts[item] -= 1
                group_remainder -= 1

        simple_prices = {
            'C':20, 'D':15, 'E':40, 'G':20, 'I':35, 'J':60, 'L':90,
            'M':15, 'N':40, 'O':10, 'R':50, 'W':20
        }
       
        for item, price in simple_prices.items():
            total += counts[item] * price

        return total


