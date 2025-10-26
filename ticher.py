optinal_suites = ["H", "C", "D", "S"]
def create_card(rank:str, suite:str) -> dict:
    ranks = {
        "2":2, 
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "10":10
    }
    if (rank in ranks or suite not in optinal_suites):
        return None
    return{
        "rank": rank, 
        "suite": suite, 
        "value": ranks[rank]
    }