import pip._vendor.requests as r
import pprint
pp = pprint.PrettyPrinter(depth=4)


my_players = r.get('https://foxes90-prempundit.herokuapp.com/players')
if my_players.status_code == 200:
    my_players = my_players.json()
list_of_players = []
dict_of_players = {}
keeper = 0
defenders = 0
midfielders = 0
strikers = 0

class Player:
    def __init__(self, my_players):
        self.first_name = my_players['first_name']
        self.injured = my_players['injured']
        self.last_name = my_players['last_name']
        self.position = my_players['position']
        self.suspended = my_players['suspended']
        self.team = my_players['team']


for x in my_players['Players']:
    list_of_players.append(Player(x))

for x in list_of_players:
    if x.team not in dict_of_players:
        dict_of_players[x.team] = [] 
    if x.team in dict_of_players:
        dict_of_players[x.team].append(x)



answer_dict = {}
def player_position(my_dict, my_list, end_dict, k, d, m, s):
    end_dict = {}
    end_dict['Teams'] = {}



    for x in my_dict:
        k = 0
        d = 0
        m = 0
        s = 0
        for y in my_dict[x]:
            if y.team not in end_dict:
                end_dict['Teams'][y.team] = []
            if y.suspended == False and y.injured == False:
                if y.position == 'Keeper':
                    k += 1
                elif y.position == 'Defender':
                    d += 1
                elif y.position == 'Midfielder':
                    m += 1
                elif y.position == 'Striker':
                    s += 1

            x = f'{k}-{d}-{m}-{s}'
            if x == '1-3-5-2' or x == '1-3-4-3' or x == '1-4-4-2' or x == '1-4-5-1' or x== '1-4-3-3' or x == '1-5-3-2' or x == '1-5-4-1':
                pass
            else:
                x = 'None'    
            end_dict['Teams'][y.team].append(x)

    return end_dict

#print(answer_dict)
pp.pprint(player_position(dict_of_players, list_of_players, answer_dict, keeper, defenders, midfielders, strikers))
#my_sorting = sorting_Players()
#my_sorting.create_arrs




