import datetime as DT
now = DT.datetime.now()


RUN_NAME = 'SynData_Queue_.9.6.68.87_50runs_2Q_100I' + "_" + str(now.date())+ "_" + str(now.time())[:-7]

ITEM_TYPE = "Hotel"
#We have 5 questions for hotels right now, 10 for restaurants
NUM_QUEST = 10 #used for accuracy testing

INPUT_PATH = 'dynamicfilterapp/simulation_files/hotels/'
OUTPUT_PATH = 'dynamicfilterapp/simulation_files/'
IP_PAIR_DATA_FILE = 'hotel_cleaned_data.csv'

DEBUG_FLAG = True # useful print statements turned on

####################### CONFIGURING CONSENSUS ##############################
NUM_CERTAIN_VOTES = 10
UNCERTAINTY_THRESHOLD = 0.2
FALSE_THRESHOLD = 0.2
DECISION_THRESHOLD = 0.5
CUT_OFF = 21

################ CONFIGURING THE ALGORITHM ##################################
#############################################################################
NUM_WORKERS = 101
EDDY_SYS = 4
# EDDY SYS KEY:
# 1 - queue pending system (uses PENDING_QUEUE_SIZE parameter)
# 2 - random system
# 3 - controlled system (uses CHOSEN_PREDS parameter)

PENDING_QUEUE_SIZE = 1

CHOSEN_PREDS = [3,4] # predicates that will be used when run on real data
# If using EDDY_SYS 3 (controlled system), CHOSEN_PREDS should be a
# list of 2 predicates (for now). They will be passed items in the order
# they appear in the list.

# HOTEL PREDICATE INDEX
# 0 - not selective and not ambiguous
# 1 - selective and not ambiguous
# 2 - not selective and medium ambiguity
# 3 - medium selectivity and ambiguous
# 4 - not selective and not ambiguous

# RESTAURANT PREDICATE INDEX
# 1,4,5 - three most selective
# 4,5,8 - least ambiguous questions
# 0,2,9 - most ambiguous questions
# 2,3,8 - least selective

ITEM_SYS = 0
# ITEM SYS KEY:
# 0 - randomly choose an item
# 1 - item-started system
# 2 - item-almost-false system

SLIDING_WINDOW = False # right now, only works in controlled run mode
LIFETIME = 10

#############################################################################
#############################################################################


###################### CONFIGURING TESTING ##################################
#############################################################################

REAL_DATA = False #if set to false, will use synthetic data (edit in syndata file)

GEN_GRAPHS = False # if true, any tests run will generate their respective graphs automatically

#################### TESTING OPTIONS FOR SYNTHETIC DATA ############################
NUM_QUESTIONS = 2
NUM_ITEMS = 100

# not really selectivity: selectivity is more selectivity_list[i]*cost_prob_list[i]
# this is just the probabiility of leaning towards false
selectivity_list = [0.9, 0.6, 0.9]
# keep probabilities above .5 for this simulation to make sense.
# the closer to 0.5, the more ambiguous the predicate is
cost_prob_list = [0.68, 0.87, 0.9]

#################### TESTING OPTIONS FOR REAL DATA ############################
RUN_DATA_STATS = False

RUN_ABSTRACT_SIM = False
ABSTRACT_VARIABLE = "UNCERTAINTY_THRESHOLD"
ABSTRACT_VALUES = [0.01,0.05,0.1,0.2,0.3,0.4,0.5]

COUNT_TICKETS = False

RUN_AVERAGE_COST = False
COST_SAMPLES = 1000

RUN_SINGLE_PAIR = False
SINGLE_PAIR_RUNS = 1000

RUN_ITEM_ROUTING = False # runs a single test with two predicates, for a 2D graph showing which predicates were priotatized

RUN_MULTI_ROUTING = False # runs NUM_SIM simulations and averges the number of "first items" given to each predicate, can auto gen a bar graph

################### OPTIONS FOR REAL OR SYNTHETIC DATA ########################
NUM_SIM = 50 # how many simulations to run?

TIME_SIMS = False

RUN_TASKS_COUNT = True # actually simulate handing tasks to workers

## WILL ONLY RUN IF RUN_TASKS_COUNT IS TRUE ##

TEST_ACCURACY = False

OUTPUT_SELECTIVITIES = False

OUTPUT_COST = False
