def checkmate(board):

    if not board:
        return
    
    rows = [line for line in board.strip().split('\n') if line]
    if not rows:
        return
    
    size = len(rows)
    king_pos = None
    king_count = 0

    for r in range(size):
        if len(rows[r]) != size:
            return  # ตารางต้องเป็นสี่เหลี่ยมจัตุรัส
        for c in range(size):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    # ต้องมี King เพียง 1 ตัวเท่านั้น
    if king_count != 1 or king_pos is None:
        return

    kr, kc = king_pos

    chess_pieces = ('P', 'B', 'R', 'Q', 'K')

    pawn_moves = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for pr, pc in pawn_moves:
        if 0 <= pr < size and 0 <= pc < size:
            if rows[pr][pc] == 'P':
                print("Success")
                return

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
 
            if piece in chess_pieces:
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break  
            
            r += dr
            c += dc

    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]

            if piece in chess_pieces:
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break  
            
            r += dr
            c += dc
    print("Fail")