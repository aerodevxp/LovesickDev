import math
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

#Mostly Constant Vars
series3_total = 77
series4_total = 10
series5_total = 10

credit_to_gold_ratio = 150/120
#Reserves
res_level_up = 12
credits_needed_for_res = 550

res_series3 = 22.25/100
res_series4 = 2.5/100
res_series5 = 0.25/100

res_tkn = 1/4
res_300_credits = 1/10
res_400_credits = 1/20
res_gold = 1/10

#Token Shop
tkn_series3 = 3/5
tkn_series4 = 1/4
tkn_series5 = 12.5/100

#Setup Variables
series3_owned = 55
series4_owned = 3
series5_owned = 1
current_collector_lvl = 2074 #Rounded up to nearest collector's reserve plz

def printProgress():
    print(f"Let's start with Series 3!\nYou currently have {series3_owned} cards out of {series3_total} ({series3_total-series3_owned} left).\nThat's {round(series3_owned/series3_total*100)}% of a complete collection. Keep it up!")
    print(f"Next up, Series 4!\nYou currently have {series4_owned} cards out of {series4_total} ({series4_total-series4_owned} left).\nThat's {round(series4_owned/series4_total*100)}% of a complete collection. Not that bad!")
    print(f"Finally with Series 5!\nYou currently have {series5_owned} cards out of {series5_total} ({series5_total-series5_owned} left).\nThat's {round(series5_owned/series5_total*100)}% of a complete collection. Keep it going!")

print("Simple Marvel Snap Tool\nCopyright ComboDev - 2023\n")

def tknShopOdds():
    print(f"Your chance to get a specific card from Series 3 in the token shop is {round(tkn_series3/(series3_total-series3_owned)*100, 2)}%.")
    print(f"Your chance to get a specific card from Series 4 in the token shop is {round(tkn_series4/(series4_total-series4_owned)*100, 2)}%.")
    print(f"Your chance to get a specific card from Series 5 in the token shop is {round(tkn_series5/(series5_total-series5_owned)*100, 2)}%.")

def resOdds(): #Doing Series 3 only for now
    print(Fore.YELLOW + f"WARNING: The word 'reserve' here is used to define the reserves you need to play to get and work for with daily missions, not the actual reserves opened.")
    print(f"You need {credits_needed_for_res} credits to get a new reserve (including bonus 50 credits).")

    #Series 3 complete
    cards_left = series3_total - series3_owned
    res_needed = cards_left/res_series3
    credits_needed = res_needed * credits_needed_for_res
    days_needed = credits_needed/450

    print(f"""
Since you have {cards_left} cards left for Series 3, you would need {round(res_needed)} reserves to get them all.
That is assuming there is no token shop purchase. This would cost {round(credits_needed)} credits.
{Fore.GREEN}You'd reach it once you are CL {round(current_collector_lvl + res_needed*res_level_up)}.{Fore.WHITE}
By daily missions, you get 450 credits per day. At that rate, you will reach this CL in {round(days_needed)} days.\n""")
    if (days_needed > 10 and days_needed < 37):
        print(f"It will take you around {round(days_needed/7)} weeks.")
    elif(days_needed >= 37):
        print(f"It will take you around {round(days_needed/30)} months.")
    print("\n")

    #Buying cards from the token shop
    print("However, you do get tokens you can spend on the token shop. Let's see how fast it could be if you only spent tokens on Series 3 cards.")
    tknprice = 1000
    reserves_to_get_to_price = (tknprice / 100) / res_tkn
    with_tkn_res_needed = res_needed - 4/40*res_needed
    with_tkn_credits_needed = with_tkn_res_needed * credits_needed_for_res
    with_tkn_days_needed = with_tkn_credits_needed/450
    print(f"This is assuming you come across a Series 3 card within {round(reserves_to_get_to_price * credits_needed_for_res / 450)} days. By odds, you should come across one {round(reserves_to_get_to_price * credits_needed_for_res / 450 * tkn_series3) * 3} times out of those days.\n{Fore.RED}So... You'd be pretty stupid to miss them all smh >:/!\n")
    print(f"To get to the price of a Series 3 card, you would need {round(reserves_to_get_to_price)} reserves.")
    print(f"That means that for every {round(reserves_to_get_to_price)} reserves, you'd remove {round(res_needed/cards_left)}.")
    print(f"With this in mind, your {cards_left} cards would be unlocked with {round(with_tkn_res_needed)} reserves instead of {round(res_needed)}.")
    print(f"This would cost {round(with_tkn_credits_needed)} credits.")
    print(Fore.GREEN +f"You'd reach it once you are CL {round(current_collector_lvl + with_tkn_res_needed*res_level_up)}.")
    print(f"By daily missions, you get 450 credits per day. At that rate, you will reach this CL in {round(with_tkn_days_needed)} days.\n""")
    if (days_needed > 10 and days_needed < 37):
        print(f"It will take you around {round(with_tkn_days_needed/7)} weeks.")
    elif(days_needed >= 37):
        print(f"It will take you around {round(with_tkn_days_needed/30)} months.")
    print(f"The token shop saves you {round(days_needed - with_tkn_days_needed)} days of grinding. Yahoo!")
    print("\n")

    #Credits from reserves
    print(Fore.GREEN +f"There is also a chance to get credits to advance your CL further. These numbers are very rounded.")
    res_300_needed_for_res = credits_needed_for_res/300/res_300_credits
    res_400_needed_for_res = credits_needed_for_res/400/res_400_credits
    res_creds_needed_for_res = res_400_needed_for_res - res_300_needed_for_res
    print(f"You need around {round(res_creds_needed_for_res)} credits reserve to get another essentially free reserve.")
    with_creds_res_needed = with_tkn_res_needed * res_creds_needed_for_res/(res_creds_needed_for_res+1)
    with_creds_days_needed = with_creds_res_needed * credits_needed_for_res / 450
    print(f"Suddenly, you would need {round(with_creds_res_needed)} reserves instead of {round(with_tkn_res_needed)}! It'll take {round(with_tkn_days_needed - with_creds_days_needed)} days off the grind for a total of {round(with_creds_days_needed)} days!")
    print("\n")

    #Gold from reserves
    print(f"You also receive a bit of gold from the reserves. Assuming you only spend your gold on credits or daily missions, this is what you would get.")
    res_gold_needed_for_res = credits_needed_for_res/(credit_to_gold_ratio*200)/res_gold
    print(f"You need {round(res_gold_needed_for_res)} gold reserves to get another free reserve.")
    with_gold_res_needed = with_creds_res_needed * res_gold_needed_for_res/(res_gold_needed_for_res+1)
    with_gold_days_needed = with_gold_res_needed * credits_needed_for_res / 450
    print(f"...and now, you would need {round(with_gold_res_needed)} reserves instead of {round(with_creds_res_needed)}! It'll take {round(with_creds_res_needed - with_gold_res_needed)} days off for a total of {round(with_gold_days_needed)} days.")
    print(Fore.GREEN +f"Right now, we're down at CL {round(current_collector_lvl + with_gold_res_needed*res_level_up)}.")
    print("\n")

    #Season Pass
    print(f"You usually get the Season Pass every month and so let's count those rewards as well.")
    total_season_gold = 900+300
    total_season_credits = 2300+300
    average_season_length = 5*7

    season_gold_to_res = (credit_to_gold_ratio*total_season_gold)/credits_needed_for_res
    season_credits_to_res = total_season_credits/credits_needed_for_res
    seasons_passed = math.floor(with_creds_days_needed/average_season_length)
    total_res_gained_from_seasons = (season_gold_to_res + season_credits_to_res) * seasons_passed

    with_season_res_needed = with_gold_res_needed - total_res_gained_from_seasons

    print(f"From buying the pass every month, you get a lot of time saving.")
    print(f"You would be able to get an additionnal {round(total_res_gained_from_seasons)} in total.")
    print(f"That's approximatively {round(season_gold_to_res + season_credits_to_res)} per season.")
    print(f"You'd need {round(with_season_res_needed)} reserves now instead of {round(with_gold_res_needed)}.")
    with_season_days_needed = with_season_res_needed * credits_needed_for_res / 450
    print(f"That's only {round(with_season_days_needed)} days (Removing {round(with_gold_days_needed-with_season_days_needed)}).")
    print("\n")

    #Daily 50 Credits
    print("You also get 50 credits per day for free.")
    daily_credits_earned_total = with_season_days_needed * 50
    with_dailycredits_res_needed = with_season_res_needed - (daily_credits_earned_total/credits_needed_for_res)
    print(f"It would take it down to {round(with_dailycredits_res_needed)} reserves.")



    


#===============
#Stuff to run

printProgress()
print("====================\n")
resOdds()



#===============

#Command input system if you want to use it for some reason
useCmdSys = False

while useCmdSys:
    cmdToRun = input(">> ")
    try:
        locals()[cmdToRun]()
    except:
        print("Something went wrong. Please try again.")




