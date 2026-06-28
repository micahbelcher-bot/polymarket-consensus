import requests

wallets = [
    "0x132f78734e5fecba945c24d5c49cd84d8c0f453b",
    "0xc8075693f48668a264b9fa313b47f52712fcc12b",
    "0x924379a79c64b77ad5816ad362122a5f6228658e",
    "0x7c1ee865a785de4c00ee90ed86a38489fb8bbab3",
    "0xce5bec63b40392845a9a504915f607c8e03a047a",
    "0x076daa87c4fe1a85402a9b6b8e0a866224388d4c",
    "0x709e8dcb133555794decc598e07f2c923b8366f5",
    "0x5e9458202b5817a72cf81105ec8a30e6f3705ba1",
    "0x204f72f35326db932158cba6adff0b9a1da95e14",
    "0xf0318c32136c2db7fec88b84869aee6a1106c80c"
]

url = "https://gamma-api.polymarket.com/public-profile"

for i, wallet in enumerate(wallets, start=1):
    print(f"\nChecking Wallet {i}...")

    response = requests.get(url, params={"address": wallet})

    if response.status_code == 200:
        data = response.json()
        print("Name:", data.get("name", "Unknown"))
        print("Wallet:", wallet)
    else:
        print("Failed:", response.status_code)