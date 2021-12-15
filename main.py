from board import Board

myboard = Board()

player1 = 'x'
player2 = 'o'
current_player = player1
while True:
    selected_choice = input('select a grid square to mark: ')
    print(f"It is {current_player}'s turn")
    if selected_choice == 'g1':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g2':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g3':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g4':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g5':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g6':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g7':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g8':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)
    if selected_choice == 'g9':
        myboard.mark_board(chosen_grid=selected_choice, player=current_player)

    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
    if myboard.game_over():
        print("GAME OVER!")
        break
