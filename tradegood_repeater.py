def print_out_good(tradegood):
	loc = """DEMAND_consumer_{tradegood} = {{ # Consumer demand for {tradegood}; the amount bought locally
	value = DEMAND_total_food_need_governorship
	divide = DEMAND_{tradegood}_price_diff_to_food_avg
	divide = DEMAND_{tradegood}_price_diff_to_food_avg
	max = DEMAND_total_food_need_governorship_doubled # Should this be the amount available to buy?
	divide = DEMAND_num_food_tradegoods
	if = {{
		limit = {{
			NOT = {{ DEMAND_{tradegood}_price_div_per_capita_wealth = 0 }}
		}}
		divide = DEMAND_{tradegood}_price_div_per_capita_wealth
	}}
}}

DEMAND_{tradegood}_price_div_per_capita_wealth = {{ # Price of {tradegood} divided by per capita wealth, used to multiply consumer demand - consumers turn away from food goods that cost too much compared to the wealth they have.
	if = {{
		limit = {{ has_variable = PRICE_{tradegood} }}
		value = var:PRICE_{tradegood}
	}}
	if = {{
		limit = {{ has_variable = var_WEALTH_governorship_per_capita }}
		divide = var:var_WEALTH_governorship_per_capita
	}}	
}}
""".format(tradegood=tradegood)
	print(loc)

#all_goods = ["grain","fur","industrial_fibres","textile_fibres","wool","silk","wood","stone","sulphur","whales","gems","peat","tin","inorganic_compounds","copper","iron","gold","silver","lead","coal","oil","tea","coffee","opium","tobacco","sugar","hardwood","rubber","dye","spices","temperate_fruit","tropical_fruit","mediterranean_fruit","chocolate","livestock","salt","fish","clothing","luxury_clothing","furniture","luxury_furniture","alcohol","glass","chemicals","rare_alloys","construction_materials","early_munitions","late_munitions","naval_supplies","steel_ships","wooden_ships","steel","bronze","machine_parts","early_artillery","late_artillery","electronics","pharmaceuticals","motors","processed_foods","petrochemicals"]
all_categories = ["essential_goods","luxury_goods","business_goods","military_goods"]

all_spenders = ["upper_strata","middle_strata","lower_strata","proletariat","tribesmen","indentured","slaves","the_state"]

all_goods = {
	"grain":"food",
	"fish":"food",
	"livestock":"food",
        "vegetables":"food",
	"tropical_fruit":"food",
	"mediterranean_fruit":"food",
	"temperate_fruit":"food",
	"processed_foods":"food",
	"clothing":"essential_goods",
	"furniture":"essential_goods",
	"pharmaceuticals":"essential_goods",
	"coal":"essential_goods",
	"whales":"essential_goods",
	"alcohol":"luxury_goods",
	"gems":"luxury_goods",
	"opium":"luxury_goods",
	"tobacco":"luxury_goods",
	"chocolate":"luxury_goods",
	"coffee":"luxury_goods",
	"tea":"luxury_goods",
	"spices":"luxury_goods",
	"sugar":"luxury_goods",
	"luxury_clothing":"luxury_goods",
	"luxury_furniture":"luxury_goods",
	"glass":"luxury_goods",
	"motors":"luxury_goods",
	"fur":"business_goods",
	"industrial_fibres":"business_goods",
	"textile_fibres":"business_goods",
	"wool":"business_goods",
	"silk":"business_goods",
	"wood":"business_goods",
	"stone":"business_goods",
	"sulphur":"business_goods",
	"peat":"business_goods",
	"tin":"business_goods",
	"inorganic_compounds":"business_goods",
	"copper":"business_goods",
	"iron":"business_goods",
	"gold":"business_goods",
	"silver":"business_goods",
	"dye":"business_goods",
	"lead":"business_goods",
	"oil":"business_goods",
	"hardwood":"business_goods",
	"rubber":"business_goods",
	"salt":"business_goods",
	"electronics":"business_goods",
	"construction_materials":"business_goods",
	"steel":"business_goods",
	"bronze":"business_goods",
	"machine_parts":"business_goods",
	"chemicals":"business_goods",
	"naval_supplies":"business_goods",
	"steel_ships":"business_goods",
	"wooden_ships":"business_goods",
	"petrochemicals":"business_goods",
	"early_munitions":"military",
	"late_munitions":"military",
	"early_artillery":"military",
	"late_artillery":"military"
        }

for tradegood, category in all_goods.items():
        if category == "food":
                print_out_good(tradegood)
