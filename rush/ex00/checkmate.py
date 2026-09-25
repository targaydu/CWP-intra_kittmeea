def checkmate(board):
    #แปลง String กระดานให้อยู่ในรูปแบบ List ของแต่ละบรรทัด
    if not board:
        return
    
    rows = [line for line in board.strip().split('\n') if line] #ตัดช่องว่างส่วนเกินหน้า-หลังด้วย .strip() และตัดแบ่งแต่ละบรรทัดด้วย .split('\n') เพื่อแปลงเป็น List ของสตริง
    if not rows:
        return
    
    size = len(rows)#นับจำนวนแถวเพื่อหาขนาดกระดาน
    king_pos = None
    king_count = 0

    #ตรวจสอบเงื่อนไขกระดาน และหาตำแหน่งของ King (K)
    for r in range(size):
        if len(rows[r]) != size:  # ตรวจสอบว่าเป็นสี่เหลี่ยมจัตุรัสหรือไม่
            return
        for c in range(size):
            if rows[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    # ต้องมี King เพียง 1 ตัวเท่านั้น
    if king_count != 1 or king_pos is None:
        return

    kr, kc = king_pos

    # เช็กการถูกรุกจาก Pawn (P)
    # Pawn กินเฉียงไปข้างหน้า (ทิศทางล่าง-ซ้าย และ ล่าง-ขวา บนกระดานตาราง)
    pawn_moves = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for pr, pc in pawn_moves:
        if 0 <= pr < size and 0 <= pc < size:
            if rows[pr][pc] == 'P':
                print("Success")
                return

    #เช็กการถูกรุกจากแนวตรง (Rook & Queen) - 4 ทิศทาง (ขึ้น, ลง, ซ้าย, ขวา)
    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break  # มีตัวหมากอื่นบังอยู่ ไม่สามารถกินขุนได้
            r += dr
            c += dc

    #เช็กการถูกรุกจากแนวเฉียง (Bishop & Queen) - 4 ทิศทางเฉียง
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = rows[r][c]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break  # มีตัวหมากอื่นบังอยู่
            r += dr
            c += dc

    # หากเช็กทุกทิศทางแล้วไม่โดนรุก
    print("Fail")