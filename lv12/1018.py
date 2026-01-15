#행, 열 입력
N, M = map(int, input().split())
board = []
chess = []

for _ in range(N):
  board.append(list(input()))

def checkChessBoard(chessBoard):
  bcounter = 0
  wcounter = 0
  # 첫 칸을 B로 가정
  for N in range(8):
    for M in range(8):
      if (N + M) % 2 == 0 and chessBoard[N][M] == 'W':
        bcounter = bcounter + 1
      if (N + M) % 2 == 1 and chessBoard[N][M] == 'B':
        bcounter = bcounter + 1
    
  # 첫 칸을 W로 가정
  for N in range(8):
    for M in range(8):
      if (N + M) % 2 == 0 and chessBoard[N][M] == 'B':
        wcounter = wcounter + 1
      if (N + M) % 2 == 1 and chessBoard[N][M] == 'W':
        wcounter = wcounter + 1
  print(f'bcounter: {bcounter}, wcounter: {wcounter}')
  return min(bcounter, wcounter)

print(checkChessBoard(board))

