hand_value = draw_starting_hand("YOUR")
while hand_value < 21:
  should_hit = input('You have ' + str(hand_value) + ". Hit (y/n)? ")
  if should_hit == 'n':
    break
  elif should_hit == 'y':
    newcard_value = draw_card()

    hand_value = hand_value + newcard_value
  else:
    print("Sorry I didn't get that.")
print_end_turn_status(hand_value)
user_hand = hand_value

hand_value1 = draw_starting_hand("DEALER")

while hand_value1 < 17:
    if hand_value1 > 1 and hand_value1 < 17:
        print("Dealer has {}.".format(hand_value1))
    newcard_value = draw_card()
    hand_value1 = hand_value1 + newcard_value
  
print_end_turn_status(hand_value1)
dealer_hand = hand_value1
print_end_game_status(user_hand, dealer_hand)
