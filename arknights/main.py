import json

from slugify import slugify

professionMap = {"TANK": "defender", "PIONEER": "vanguard", "WARRIOR": "guard"}


def map_data(it):
    key = it[0]
    data = it[1]
    return {
        "profession": professionMap.get(data["profession"], data["profession"]).lower(),
        "rarity": data["rarity"],
        "name": data["name"],
        "slug": slugify(data["name"]),
    }


def main():
    with open("data/aceship/json/gamedata/en/excel/character_table.json") as f:
        data = json.load(f)
    mapped = list(map(map_data, data.items()))
    print(len(mapped))


if __name__ == "__main__":
    main()
