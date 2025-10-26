def create_card(rank:str, suite:str) -> dict:
    value = {"A":14, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "k":13}
    return {"rank":rank, "suite":suite, "value":value[rank]}   

def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    if p1_card["value"] < p2_card["value"]:
        return "p2"
    return "WAR"

def create_deck() -> list[dict]:
    rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "k"]
    suite = ["H", "C", "D", "S"]
    result = []
    for i in rank:
        for j in suite:
            result.append(create_card(i, j))
    return result

    