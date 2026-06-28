import requests

wallets = [
    "0x132f78734e5fecba945c24d5c49cd84d8c0f453b",
    "0xc8075693f48668a264b9fa313b47f52712fcc12b",
    "0x924379a79c64b77ad5816ad362122a5f6228658e",
    "0x7c1ee865a785de4c000ee90ed86a38489fb8bbab3",
    "0xce5bec63b40392845a9a504915f607c8e03a047a",
    "0x076daa87c4fe1a85402a9b6b8e0a866224388d4c",
    "0x709e8dcb133555794decc598e07f2c923b8366f5",
    "0x5e9458202b5817a72cf81105ec8a30e6f3705ba1",
    "0x204f72f353260f932158cba6adff0b9a1da95e14",
    "0xf0318c32136c2db7fec88b84869aeee6a1106c80c"
]

def get_all_positions():
    all_positions = []

    for wallet in wallets:
        url = f"https://data-api.polymarket.com/positions?user={wallet}"
        response = requests.get(url)

        if response.status_code != 200:
            continue

        for position in response.json():
            position["wallet"] = wallet
            all_positions.append(position)

    return all_positions


if __name__ == "__main__":
    positions = get_all_positions()
    print(f"Loaded {len(positions)} positions")