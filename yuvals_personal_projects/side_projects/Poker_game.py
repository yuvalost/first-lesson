import random



# Define the card ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♥', '♦', '♣', '♠']

# Cowboy names for other players
cowboy_names = ['Billy the Kid', 'Jesse James', 'Calamity Jane', 'Wild Bill Hickok', 'Annie Oakley', 'Butch Cassidy']


# Function to create a deck of cards
def create_deck():
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Function to deal cards to each player
def deal_cards(deck, num_players):
    hands = [deck[i:i + 2] for i in range(0, 2 * num_players, 2)]
    open_cards = deck[2 * num_players:2 * num_players + 5]
    return hands, open_cards


# Function to print the player's hand
def print_player_hand(player_hand):
    for card in player_hand:
        print("╭───────╮ ", end="")
    print()
    for card in player_hand:
        rank = card['rank']
        suit = card['suit']
        rank_str = f"{rank:<2}" if len(rank) == 1 else f"{rank}"
        print(f"│ {rank_str}    │ ", end="")
    print()
    for card in player_hand:
        print("│       │ ", end="")
    print()
    for card in player_hand:
        print(f"│   {suit}   │ ", end="")
    print()
    for card in player_hand:
        print("│       │ ", end="")
    print()
    for card in player_hand:
        rank_str = f"{card['rank']:>2}" if len(card['rank']) == 1 else f"{card['rank']}"
        print(f"│    {rank_str} │ ", end="")
    print()
    for card in player_hand:
        print("╰───────╯ ", end="")
    print()

# function to print the open cards after flop
def print_open_cards(open_cards):
    for _ in open_cards:
        print("+-------+ ", end="")
    print()

    for card in open_cards:
        suit = card['suit']
        print(f"|   {suit}   | ", end="")
    print()

    for _ in open_cards:
        print("|       | ", end="")
    print()

    for _ in open_cards:
        print("|       | ", end="")
    print()

    for card in open_cards:
        print(f"|   {suit}   | ", end="")
    print()

    for _ in open_cards:
        print("|       | ", end="")
    print()

    for _ in open_cards:
        print("+-------+ ", end="")
    print()

# Function to evaluate a hand and determine its rank (Simplified for High Card)
def evaluate_hand(hand):
    hand_ranks = [card['rank'] for card in hand]
    hand_suits = [card['suit'] for card in hand]


    # Check for pairs, three of a kind, and four of a kind
    rank_counts = {rank: hand_ranks.count(rank) for rank in set(hand_ranks)}
    if 4 in rank_counts.values():
        return "Four of a Kind"
    elif 3 in rank_counts.values() and 2 in rank_counts.values():
        return "Full House"
    elif 3 in rank_counts.values():
        return "Three of a Kind"
    elif list(rank_counts.values()).count(2) == 2:
        return "Two Pair"
    elif 2 in rank_counts.values():
        return "Pair"

    # Check for straight and flush
    sorted_ranks = sorted(hand_ranks, key=lambda x: ranks.index(x))
    if len(set(hand_suits)) == 1 and sorted_ranks[-1] == ranks[ranks.index(sorted_ranks[0]) + 4]:
        return "Straight Flush"
    elif len(set(hand_suits)) == 1:
        return "Flush"
    elif sorted_ranks[-1] == ranks[ranks.index(sorted_ranks[0]) + 4]:
        return "Straight"

    return max(hand_ranks, key=ranks.index)  # Return the highest card rank as a fallback


# Function to determine the winner of the game
# Function to determine the winner of the game
def determine_winner(hands, open_cards):
    best_hand = None
    best_rank = None
    best_player = None

    for player, hand in enumerate(hands):
        full_hand = hand + open_cards
        player_rank = evaluate_hand(full_hand)
        if best_rank is None or ranks.index(player_rank) > ranks.index(best_rank):
            best_hand = hand
            best_rank = player_rank
            best_player = player

    for i in range(len(hands)):
        if i == 0:
            print("\nYour Hand:")
            print_player_hand(hands[i])  # Corrected function call here
        else:
            print(f"\n{cowboy_names[i - 1]}'s Hand:")
            print_player_hand(hands[i])  # Corrected function call here
        print(f"\nHand Rank: {evaluate_hand(hands[i])}")

    print("\nOpen Cards:")
    print_player_hand(open_cards)  # Corrected function call here

    if best_player == 0:
        print(f"\nCongratulations! You win the round with {best_rank}.")
        # Show the opponent's hand only if the player wins
        print(f"\n{cowboy_names[best_player - 1]}'s Hand:")
        print_player_hand(hands[best_player])  # Corrected function call here
        return 1
    else:
        print(f"\n{cowboy_names[best_player - 1]} wins the round with {best_rank}.")
        # Hide the opponent's hand if the player loses
        print(f"\n{cowboy_names[best_player - 1]}'s Hand:")
        print_player_hand(hands[best_player])  # Corrected function call here
        return -1


# Function for bad guy opponents to place a bet
def opponent_bet():
    return random.randint(10, 50)


# Function for the player to place a bet
def player_bet(balance):
    while True:
        bet = input(f"\nYou have ${balance}. Place your bet (minimum 10, maximum {balance}): ")
        if bet.isdigit():
            bet = int(bet)
            if 10 <= bet <= balance:
                return bet
        print("Invalid bet amount. Please try again.")


# Function for the player to call or fold
def call_or_fold(opponent_bet, balance):
    print(f"\nYour current balance: ${balance}")
    print(f"{cowboy_names[0]}'s bet: ${opponent_bet}")
    while True:
        choice = input("Do you want to (c)all or (f)old? ").strip().lower()
        if choice == 'c':
            return 'call'
        elif choice == 'f':
            return 'fold'
        print("Invalid choice. Please enter 'c' to call or 'f' to fold.")


# Short story about the sheriff playing poker to save the town
def cowboy_poker_story():
    story = """
    In the Wild West town of Dusty Gulch, the peaceful days were over as ruthless outlaws led by Black Jack Malone
    laid siege to the town. The Sheriff, known for his legendary poker skills, decided to take matters into his own hands.

    A high-stakes Texas Hold'em poker game was set to determine the fate of the town. As the cards were dealt,
    the Sheriff's steely gaze and poker face revealed his determination to outwit the notorious outlaws.

    With courage and cunning, the Sheriff played each hand, determined to defend Dusty Gulch from the clutches of evil.

    As the final card was revealed, the Sheriff's unmatched skills prevailed, and Black Jack Malone and his gang were defeated.

    The town erupted in cheers as peace returned to Dusty Gulch. The Sheriff had once again proven that sometimes,
    it takes more than just a quick draw to save the day.

    From that day forward, the legend of the Sheriff who fought bad guys in a Texas Hold'em poker game echoed through the Wild West.
    """
    print(story)


# Function to allow the player to switch cards
def switch_cards(player_hand, deck):
    print("\nYour Hand:")
    print_player_hand(player_hand)

    switch_option = input("\nDo you want to switch one card, both cards, or keep your hand? (1, 2, or 0): ").strip()

    if switch_option == '1':
        switch_index = int(input("Choose the index (1 or 2) of the card you want to switch: "))
        if switch_index in [1, 2]:
            player_hand[switch_index - 1] = deck.pop()
    elif switch_option == '2':
        player_hand[0] = deck.pop()
        player_hand[1] = deck.pop()

# function of start game
def pre_flop_betting(balance):
    while True:
        bet = input(f"\nYou have ${balance}. Place your bet (minimum 10, maximum {balance}): ")
        if bet.isdigit():
            bet = int(bet)
            if 10 <= bet <= balance:
                return bet
        print("Invalid bet amount. Please try again.")

def flop():
    return random.sample(deck, 3)


## Main function to run the cowboy poker game
def cowboy_poker_game():
    print("Welcome to the Cowboy Texas Hold'em Poker Game!")

    cowboy_poker_story()

    num_players = 2
    balance = 200

    print("\nGame Rules:")
    print("In Texas Hold'em, each player is dealt two private cards (known as 'hole cards') that belong to them alone.")
    print("Five open cards are dealt face-up, to form the 'board'. All players in the game use these shared")
    print(
        "open cards in conjunction with their own hole cards to each make their best possible five-card poker hand.")

    start_game = input("\nPress 'yay' to start the game or 'nay' to quit: ").strip().lower()

    while start_game == 'yay' and balance > 0:
        # Randomly select a cowboy name for the opponent
        opponent_name = random.choice(cowboy_names)

        print(f"\nYou are playing against {opponent_name}!")

        deck = create_deck()
        hands, open_cards = deal_cards(deck, num_players)

        print(f"\nYour current balance: ${balance}")

        # Display the player's hand separately
        print("\nYour Hand:")
        print_player_hand(hands[1])

        # Display the opponent's hand separately
        print(f"\n{opponent_name}'s Hand:")
        print_player_hand(hands[1])

        switch_cards(hands[0], deck)

        opponent_bet_amount = opponent_bet()
        player_bet_amount = player_bet(balance)

        if opponent_bet_amount > player_bet_amount:
            action = call_or_fold(opponent_bet_amount, balance)
            if action == 'fold':
                print("\nYou folded. You lose the round.")
                balance -= player_bet_amount
                start_game = input(
                    "\nDo you want to play another round? Type 'yay' to continue or 'nay' to quit: ").strip().lower()
                continue

        balance -= player_bet_amount

        print("\nOpen Cards:")
        print_player_hand(open_cards)  # Corrected function call here

        balance += determine_winner(hands, open_cards) * (player_bet_amount + opponent_bet_amount)

        start_game = input(
            "\nDo you want to play another round? Type 'yay' to continue or 'nay' to quit: ").strip().lower()

    print("Thanks for playing! See you next time!")


# Run the cowboy poker game
if __name__ == "__main__":
    cowboy_poker_game()