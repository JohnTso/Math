from get_gcf import get_gcf


def factor_polynomial():
    answer = input('Ex: 2,5,2 => 2x^2 + 5x + 2\noutput => (x+2)(2x+1)\nyour input: ')
    answer = answer.split(',')

    if len(answer) != 3:
        print('input must be 3 numbers!')

    if '0' in answer:
        print('zero error')

    def get_factor_pairs(num):
        factors = []
        pairs = []
        
        if num < 0:

            for i in range(1,(-num)+1):
                if not (-num) % i:
                    factors.append(i)
                    factors.append(-i)
            for i in range(len(factors)):
                pair = []

                if i > len(factors) // 2 - 1 and factors[-1] != 1:
                    pairs.append([factors[-1], 1])
                    return pairs

                else:
                    pair.append(factors[i])
                    pair.append(factors[-(i+1)])
                    pairs.append(pair)

            return pairs if num != -1 else [[1,-1],[-1,1]]

        else:

            for i in range(1, num+1):
                if not num % i:
                    factors.append(i)
                    factors.append(-i)
            for i in range(len(factors)-1):
                pair = []
                if i < len(factors):
                    s = factors[i:]
                    for j in s:
                        if factors[i]*j == num:
                            pairs.append([factors[i],j])
            return pairs if num != 1 else [[1,1],[-1,-1]]
            

    col1 = get_factor_pairs(int(answer[0]))
    col2 = get_factor_pairs(int(answer[2]))

    n_to_s = lambda n : "+"+str(n) if (n > 0) else str(n)
    for i in col1:
        for j in col2:
            factor = 1
            a,b,c,d = i[0],i[1],j[1],j[0]
            check_x_co = a*d + b*c 
            if check_x_co == int(answer[1]):
                a,b,c,d = n_to_s(a),n_to_s(b),n_to_s(c),n_to_s(d)
                if a == b and c == d:
                    return f'{factor}({a}x{c})^2' if abs(factor) > 1 else f'({a}x{c})^2'
                return f'{factor}({a}x{c})({b}x{d})' if abs(factor) > 1 else f'({a}x{c})({b}x{d})'

    else:
        
        print('it cannot be factored')

print(factor_polynomial())