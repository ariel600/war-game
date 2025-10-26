def create_card(rank:str, suite:str) -> dict:
    value = {"A":14, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "k":13}
    return {"rank":rank, "suite":suite, "value":value[rank]}   

def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    if p1_card["value"] < p2_card["value"]:
        return "p2"
    return "WAR"
