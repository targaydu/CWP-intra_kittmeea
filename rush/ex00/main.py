from checkmate import checkmate

def main():
    board = """
.....
Q....
.K...
.....
.....
"""
    checkmate(board)

if __name__ == "__main__":
    main()
   
#เบี้ย / Pawn (P):** เดินเฉียงไปข้างหน้า 1 ช่อง'
#บิชอป / Bishop (B):** เดินแนวทแยงได้ทุกทิศทาง'
#เรือ / Rook (R):** เดินแนวตั้งและแนวนอน'
#ควีน / Queen (Q):** เดินได้ทั้งแนวทแยง แนวตั้ง และแนวนอน'
    