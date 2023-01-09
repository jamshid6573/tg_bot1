import json

with open("functions/price.json", encoding="utf8") as price:
    info = json.load(price)

def get_info(gold):
    price = 0
    commission = gold / 100 * 25 + gold + 1.17
    if gold <= 999:
        price = gold * info['1g']
    elif gold >= 1000 and gold <= 2999:
        price = gold * info['1000g']
    elif gold >= 3000:
        price = gold * info['3000g']        
    data = {
        'price': price,
        'commission': commission
    }
    return data

def get_info_sum(sum):
    gold = 0
    if sum <= 165999:
        gold = sum // info['1g']
    elif sum >= 166000 and sum <= 389999:
        gold = sum // info['1000g']
    elif sum >= 390000:
        gold = sum // info['3000g']
    commission = gold / 100 * 25 + gold + 1.17
    data = {
        'gold': gold,
        'commission': commission
    }
    return data

def sum_correct(sum):
    text = str(sum)
    lenght = len(text)
    if lenght == 5:
        half1 = text[:2]
        half2 = text[2:]
        som = half1 + "." + half2
        return som
    elif lenght == 6:
        half1 = text[:3]
        half2 = text[3:]
        som = half1 + "." + half2
        return som
    elif lenght == 7:
        half1 = text[:1]
        half2 = text[1:4]
        half3 = text[4:]
        som = half1 + "." + half2 + "." + half3
        return som
    