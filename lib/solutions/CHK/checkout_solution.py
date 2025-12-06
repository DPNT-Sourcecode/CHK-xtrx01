
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        if not isinstance(skus, str):
            return -1 

        valid_items = {'A','B','C','D'}

        for char in skus:
            if char not in valid_items:
                return -1

        a = skus.count('A')
        b = skus.count('B')
        c = skus.count('C')
        d = skus.count('D')
        
        return (a//3)*130 + (a%3)*50 + (b//2)*45 + (b%2)*30 + c*20 + d*15
