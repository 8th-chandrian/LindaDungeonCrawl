from constants import MOUSETRAP_ATTACK_NAME
from model.attack import Attack


# Linda attacks will be listed with their opponents
# only Linda attacks need a name attribute

# Static Linda attacks (added when she obtains a new item)
linda_explain_vitamix = Attack(30, 'Linda presented her Vitamix. She explained its various benefits (manifold) and drawbacks (none) to the Enemy. \nShe spoke matter-of-factly. Obviously, the Vitamix was superior.', 'psychic damage, on account of how cool Linda\'s Vitamix was', 'vitamix')
linda_explain_vitamix_l2 = Attack(60, 'Linda presented her Vitamix. She explained its various benefits (manifold) and drawbacks (none) to the Enemy. \nShe spoke matter-of-factly. Obviously, the Vitamix was superior.', 'psychic damage, on account of how cool Linda\'s Vitamix was', 'vitamix')
linda_nyt = Attack(80, 'Linda landed an overhead strike with the Failing New York Times!', 'fake news damage', 'failing nyt')

# jackie attacks (Linda HP 100, Jackie HP 200)
jackie_act_unpleasant = Attack(20, "Jackie acted unpleasant, contributing to a toxic workplace environment.", "damage")
jackie_yell = Attack(120, "Jackie got mad. Oh no, she started YELLING!", "loudness damage")
linda_jackie_try = Attack(20, "Linda did her best to fix what Jackie was upset about.", "damage", "try to appease")

# mega jackie attacks (Linda HP 400, Mega Jackie HP 400)
mega_jackie_yell = Attack(120, "Mega Jackie got really mad! Oh no, she started YELLING!", "loudness damage")
mega_jackie_toxicity = Attack(100, "Mega Jackie continued acting really toxic.\n\n\"AAAAHAHAHAHAHAAAA..... MY TOXICITY HAS ONLY GROWN SINCE LAST WE FOUGHT!!!\"\n\nLinda lost sleep due to stress!", "stress damage")
mega_jackie_guilt = Attack(80, "Mega Jackie tried to guilt Linda into continuing to work with her.", "damage")
linda_mega_jackie_observe = Attack(150, "Jackie yelled at Linda.\n\"Jackie, you're yelling at me,\" Linda said.\n\n...ouch.\n", "observation damage", "observe")
linda_mega_jackie_nyt = Attack(120, 'Mega Jackie DEMANDED to know WHY Linda wouldn\'t work with her.\n\nMega Jackie: "Tell me the real reason!!!"\n\nLuckily, Linda had the Failing New York Times, allowing her to disseminate fake news effectively!', 'fake news damage', "failing nyt")
linda_mega_jackie_hangup = Attack(200, 'Linda hung up. This dealt a DEVESTATING blow to MEGA JACKIE.', 'damage', 'hang up')

# Patrick (Linda HP 125, Patrick HP 150)
patrick_promise = Attack(25, "Patrick promised Linda that she would only have to do another few decades of exceptionally taxing work, and then it would all get better.", "poison damage")
patrick_set_up = Attack(40, "Patrick put Linda in a situation where her clients were going to be upset no matter what she did.", "damage")
patrick_work = Attack(25, "Patrick gave Linda other people's work to do, on top of her own.", "damage")
linda_patrick_recognize = Attack(40, "Linda took a moment just to consciously recognize how the stress of work had built up within her.", "damage", "breathe")
linda_patrick_work = Attack(50, "Linda continued to crush it despite her difficult circumstances.", "damage", "do good work")
linda_patrick_push = Attack(55, "Linda pushed back against some of the things Patrick was saying.", "damage", "push back")


# IRS (Linda HP 250, IRS HP 1000)
IRS_tax = Attack(100, "The IRS demanded that Linda do LLC taxes. Oh no, they're really confusing!", "damage")
linda_accountant = Attack(2000, "Linda hired an accountant. It's super effective!", 'accounting damage', 'accountant')

# mouse (Linda HP 250, mouse HP 5)
mouse_run = Attack(10, "The mouse skittered across the floor.\nLinda shrieked!\n\n\"If only I hadn't defeated Tilly in LINDA SUPER ULTRA MEGA BOSS RUSH 2018...\"\n", "damage")
linda_mousetrap = Attack(1000, "Linda set a mousetrap. \"Great, now Stella will have to clean it up later... ugh...\"", "Stella pulled further ahead on the leaderboard!", MOUSETRAP_ATTACK_NAME)

# store bought chocolate chip cookies (Linda HP 250, cookies HP 5)
cookies_sit_there = Attack(50, "The cookies sat there, looking disgusting.", "grossness damage")
linda_cookies_flex = Attack(10, 'Linda flexed on the cookies.\n"These cookies are far inferior to mine. I could bake a better batch of cookies in my sleep"', "inferiority damage", "flex")

# big john (Linda HP 250, Big John HP 50)
john_ask = Attack(50, "Big John asked Linda to work with him.\n\"Oh brother...\" Linda thought.", "damage")
john_everybody = Attack(10, "Big John said, \"Everybody's doin' it...\"", "indecision damage")
john_feel_good = Attack(10, "Big John said, \"It'll make you feel good...\"", "indecision damage")
john_want_to = Attack(10, "Big John said, \"You know you want to...\"", "indecision damage")
linda_say_no = Attack(100, "Linda politely declined Big John's offer.", "rejection damage", 'say no')

# email inbox (Linda HP 100, inbox HP 50)
inbox_sit_there = Attack(15, "The inbox just sat there.", "damage from the stress of thinking about all those emails")
inbox_grow = Attack(25, "The inbox swelled in size!", "damage from the stress of thinking about all those emails")
linda_delete = Attack(20, "Linda deleted a bunch of emails.", "damage", 'delete')
linda_ignore_email = Attack(20, "Linda ignored a bunch of emails.\nThe inbox is devestated!", "sadness damage :(", 'ignore')

# dissatisfied clients (Linda HP 125, clients HP 75)
d_clients_attention = Attack(20, "The dissatisfied clients demanded attention.\nOh no, there are so many of them all at once!\n(this is a diss on reward gateway)", "stress damage")
d_clients_complain = Attack(30, "The dissatisfied clients decided to complain to Patrick. Ugh, Linda got frustrated...", "frustration damage")
linda_shrug = Attack(40, "Linda shrugged.\n\n\"Whatever.\"\n\nIt's super effective!!", 'damage', 'shrug')
linda_pacify = Attack(35, "Linda did what she could to quell the clients' annoyances.", "pacification damage", 'appease')

# inferior coworkers (Linda HP 125, coworkers HP 100)
coworkers_slack = Attack(20, "Linda's coworkers sent her ten billion slack messages asking for advice.\nLinda got too distracted and could't get any work done.", "overwhelm damage")
coworkers_collaborate = Attack(30, "Linda took pity on her coworkers and helped them out...but they later took credit for her ideas.", "plagiarism damage")
linda_help = Attack(40, "Linda went above and beyond helping her coworkers out.", "pacification damage", "help out")
linda_ignore_coworkers = Attack(50, "Linda ignored the slack messages. Her coworkers will have to fend for themselves for today, she's simply too busy.", "damage", "ignore")

# difficult clients (Linda HP 250, clients HP 200)
# TODO: we need better text for this attack
dif_clients_expectations = Attack(60, "The difficult clients built up unrealistic expectations, and then got upset when Linda couldn't meet them.", 'damage. "Ugh, this goes beyond the scope of the contract..." Linda muttered')
dif_clients_red_tape = Attack(80, 'Linda made a good suggestion, but the difficult clients objected.\n"No, no!" they protested, "we can\'t do that! We don\'t have the budget, and there are 500,000 forms that still need to be filled out!', 'frustration damage')
linda_dif_work_harder = Attack(80, "Linda gritted her teeth and simply worked harder.", "damage. It worked, but this could only go on for so long before someone got smacked with a copy of the Failing New York Times...", 'work harder')
linda_dif_escalate = Attack(150, "Linda met with the bosses of the people trying to resist change, and successfully sheared through some red tape.", "damage", "escalate")