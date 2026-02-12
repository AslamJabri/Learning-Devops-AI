def insertion_sort(cards):
    total_cards = len(cards)
    
    for position in range(1,total_cards):
        card_to_insert = cards[position]
        left_side_position = position -1
        
        while left_side_position >= 0 and cards[left_side_position] > card_to_insert:
            cards[left_side_position + 1] = cards[left_side_position]
            left_side_position -= 1
            
        cards[left_side_position+1] = card_to_insert
    return cards

cards = [5, 3, 4, 1, 2]
print(insertion_sort(cards))

def insertion_sorting(card):
    total_cards = len(card)
    
    for position in range(1,total_cards):
        card_to_insert = card[position]
        left_side = position -1
        
        while left_side >= 0 and card[left_side] > card_to_insert:
            card[left_side +1] = card[left_side]
            left_side -=1
        card[left_side+1] = card_to_insert
    return card

arr = [2,4,6,8,3]
print(insertion_sorting(arr))


def count_shift(arr):
    total_card = len(arr)
    count = 0
    for i in range(1,total_card):
        current = arr[i]
        left = i - 1
        
        while left >= 0 and arr[left] > current:
            arr[left+1] = arr[left]
            left -=1
            count +=1
        arr[left +1] = current
    return count
arr2 = [9,7,5,3,1]

print(count_shift(arr2))