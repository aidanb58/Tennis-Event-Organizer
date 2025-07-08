# Tennis Event Organizer

A Python script designed to organize **matchplay events** at a tennis club, handling **8 to 12 players** efficiently. The script uses an **object-oriented** approach, where each player is represented as an object with the following attributes:

- `name`
- `skill` (numerical rating)
- `partner` (preferred doubles partner)
- `singles` (willingness to play singles)
- `previous_partners`
- `previous_opponents`

---

## Script Usage & Matchmaking

To begin, the script prompts the user to enter players one by one:

- If a player is **already stored** in the program, enter their **name**.
- If a player is **not stored**, enter `"new"` and follow the prompts to add their information temporarily.
- When all players are entered, type `"stop"` to begin matchmaking.

Once all players are submitted, the script:

- Organizes **3 rounds** of matchplay
- Calculates the most **competitive and fair matchups** based on player skill ratings.
- Ensures:
  - No two players (unless partners) play **together more than once**.
  - No player faces the same **opponents more than once**.
  - Preferred partners are **kept together** all three rounds.
  - Only players willing to play singles are rotated into singles matches.

This matchmaking process guarantees variety, balance, and a fun playing experience for everyone involved.

---

## Player Management

- The program is **scalable** and designed to store a full club roster.
- To store players in the program, follow the instructions in the comments within the code.
- This streamlines event setup by letting you quickly add members by name, reserving the `"new"` option for guest or one-time players.

---

## Coaches and Edge Cases

- A list of **pro/coach** players is built into the class.
- If the number of players is **odd**, the program will:
  - Prefer placing coaches into **singles** matches.
  - If necessary, have a coach play **1 vs 2** to allow all regular players to participate in doubles.

This ensures the event stays smooth and enjoyable for everyone, even with uneven numbers.

---
