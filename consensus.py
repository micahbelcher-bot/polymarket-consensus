from collections import defaultdict
from api.positions import get_all_positions

positions = get_all_positions()

markets = defaultdict(list)

# Group positions by market
for position in positions:
    title = position.get("title")
    if title:
        markets[title].append(position)

consensus = []

for market, traders in markets.items():

    sides = defaultdict(int)
    money = defaultdict(float)

    for trader in traders:
        side = trader.get("outcome")
        size = float(trader.get("size", 0))

        sides[side] += 1
        money[side] += size

    winning_side = max(sides, key=sides.get)

    consensus.append({
        "market": market,
        "side": winning_side,
        "whales": sides[winning_side],
        "money": money[winning_side]
    })

consensus.sort(
    key=lambda x: (x["whales"], x["money"]),
    reverse=True
)

print("\n🔥 TOP CONSENSUS OPPORTUNITIES 🔥\n")

for c in consensus[:15]:
    print("=" * 60)
    print(c["market"])
    print(f"Side: {c['side']}")
    print(f"Whales Agreeing: {c['whales']}")
    print(f"Money Behind It: ${c['money']:,.0f}")