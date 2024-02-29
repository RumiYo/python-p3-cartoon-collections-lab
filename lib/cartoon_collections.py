def roll_call_dwarves(names):
    indexed_names = [f"{index+1}. {name}" for index, name in enumerate(names)]
    names_together = "\n".join(indexed_names)
    print(names_together)

def summon_captain_planet(calls):
    updated_calls = [f"{call.capitalize()}!" for call in calls]
    return updated_calls 

def long_planeteer_calls(calls):
    long_calls = list()
    for i in calls:
        if len(i) > 4:
           long_calls.append(i)
    return len(long_calls) > 0


def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    for i in items:
        if i in cheeses:
            return i
