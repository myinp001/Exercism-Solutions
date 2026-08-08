def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    if card in ("J","K","Q"):
        return 10   
    elif card in ("A"):
        return 1
    else:
        return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """
    if card_one in ("J","K","Q"):
        card_holdone = 10   
    elif card_one in ("A"):
        card_holdone = 1
    else:
        card_holdone = int(card_one)
    if card_two in ("J","K","Q"):
        card_holdtwo = 10   
    elif card_two in ("A"):
        card_holdtwo = 1
    else:
        card_holdtwo = int(card_two)
    if card_holdone == card_holdtwo:
        return (card_one, card_two)
    elif card_holdone > card_holdtwo:
        return card_one
    else:
        return card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    if card_one in ("J","K","Q"):
        card_one = int(10)   
    elif card_one in ("A"):
        return 1
    else:
        card_one = int(card_one)
    if card_two in ("J","K","Q"):
        card_two = int(10)   
    elif card_two in ("A"):
        return 1
    else:
        card_two = int(card_two)
    sum = card_one + card_two
    if sum <= 10:
        return 11
    elif sum > 10 and sum < 21:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """
    if card_one in ("J","K","Q"):
        card_holdone = 10   
    elif card_one in ("A"):
        card_holdone = 11
    else:
        card_holdone = int(card_one)
    if card_two in ("J","K","Q"):
        card_holdtwo = 10   
    elif card_two in ("A"):
        card_holdtwo = 11
    else:
        card_holdtwo = int(card_two)
    sum = card_holdone + card_holdtwo
    if sum == 21:
        return True
    else:
        return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    if card_one in ("J","K","Q"):
        card_one = 10   
    elif card_one in ("A"):
        card_one = 1
    if card_two in ("J","K","Q"):
        card_two = 10   
    elif card_two in ("A"):
        card_two = 1
    if card_one == card_two:
        return True
    else:
        return False
    



def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    if card_one in ("J","K","Q"):
        card_one = 10   
    elif card_one in ("A"):
        card_one = 1
    else:
        card_one = int(card_one)
    if card_two in ("J","K","Q"):
        card_two = 10   
    elif card_two in ("A"):
        card_two = 1
    else:
        card_two = int(card_two)
    sum = card_one + card_two
    if sum > 8 and sum < 12:
        return True
    else:
        return False
