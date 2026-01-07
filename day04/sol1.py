rolls = 0
res = []

# 1. Zuerst das gesamte Gitter einlesen
with open('input.txt') as f:
    # Alle Zeilen lesen und Whitespace/Zeilenumbrüche entfernen
    grid = [line.strip() for line in f if line.strip()]
    rows = len(grid)
    cols = len(grid[0])

    # 2. Jetzt das gesamte Gitter verarbeiten
    for r in range(rows):
        current_line = ""
        for c in range(cols):
            if grid[r][c] == '@':
                nb = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                nb += 1
                if nb < 4:
                    rolls += 1
                    current_line += 'x'
                else:
                    current_line += '@'
            else:
                current_line += '.'
        res.append(current_line)

print(f'Rolls: {rolls}')