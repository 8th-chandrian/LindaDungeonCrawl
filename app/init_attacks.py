from model.attack import Attack

# TODO: I (Stella) need to go over damage values to make sure it makes sense for sequential attacks. I want these battles to go real smooth

# Linda attacks will be listed with their opponents
# only Linda attacks need a name attribute

# TODO: REFACTOR AND PUT NAME LAST

# Static Linda attacks (added when she obtains a new item)
linda_explain_vitamix = Attack(15, 'Linda presented her Vitamix. She explained its various benefits (manifold) and drawbacks (none) to the Enemy. \nShe spoke matter-of-factly. Obviously, the Vitamix was superior.', 'psychic damage, on account of how cool Linda\'s Vitamix was', 'vitamix')
linda_nyt = Attack(30, 'Linda landed an overhead strike with the Failing New York Times!', 'fake news damage', 'failing nyt')

# mega jackie attacks (Linda HP 400, Mega Jackie HP 400)
mega_jackie_yell = Attack(200, "Mega Jackie got really mad! Oh no, she started YELLING!", "loudness damage")
mega_jackie_toxicity = Attack(100, "Mega Jackie continued acting really toxic.\n\n\"MUAHAHAHAHAHAAAA..... MY TOXICITY HAS ONLY GROWN SINCE LAST WE FOUGHT!!!\"\n\nLinda lost sleep due to stress!", "stress damage")
mega_jackie_guilt = Attack(150, "Mega Jackie tried to guilt Linda into continuing to work with her.", "damage")
linda_mega_jackie_nyt = Attack(100, 'Mega Jackie DEMANDED to know WHY Linda wouldn\'t work with her.\n\nMega Jackie: "Tell me the real reason!!!"\n\nLuckily, Linda had the Failing New York Times, allowing her to disseminate fake news effectively!', 'fake news damage', "failing nyt")
linda_mega_jackie_observe = Attack(150, "Jackie yelled at Linda.\n\"Jackie, you're yelling at me,\" Linda said.\n\n...ouch.\n", "observation damage", "observe")
linda_mega_jackie_hangup = Attack(175, 'Linda hung up. This dealt a DEVESTATING blow to MEGA JACKIE.', 'damage', 'hang up')

# jackie attacks ("yell" is an event, not an attack)
# scoff, or something?

# IRS (Linda HP 250, IRS HP 1000)
IRS_tax = Attack(100, "The IRS demanded that Linda do LLC taxes. Oh no, they're really confusing!", "damage")
linda_accountant = Attack(2000, "Linda hired an accountant. It's super effective!", 'accounting damage', 'accountant')

# mouse (Linda HP 250, mouse HP 5)
mouse_run = Attack(50, "The mouse skittered across the floor.\nLinda shrieked!\n\n\"If only I hadn't defeated Tilly in LINDA SUPER ULTRA MEGA BOSS RUSH 2018...\"\n", "damage")
linda_mousetrap = Attack(10, "Linda set a mousetrap. Great, now Stella will have to clean it up later... ugh...", "Stella pulled further ahead on the leaderboard, and the mouse was defeated!", "mousetrap")
# TODO: implement linda's mousetrap thing without saying damage value

# problematic clients
p_clients_expectations = Attack(30, "The problematic clients demanded that Linda go beyond the scope of the contract!", "damage")
linda_work_harder = Attack(10, "Linda gritted her teeth and simply worked harder.", "damage. It worked, but this could only go on for so long before someone got smacked with a copy of the Failing New York Times...", 'work harder')

# big john (Linda HP 250, Big John HP 50)
john_ask = Attack(50, "Big John asked Linda to work with him.\n\n\"Oh brother...\" Linda thought.\n", "damage")
# TODO make it say "Linda is paralyzed with indecision!" between Big John's attacks, maybe? I guess that would require a separate fight function for Big John specifically though
john_everybody = Attack(10, "Big John said, \"Everybody's doin' it...\"", "indecision damage")
john_feel_good = Attack(10, "Big John said, \"It'll make you feel good...\"", "indecision damage")
john_want_to = Attack(10, "Big John said, \"You know you want to...\"", "indecision damage")
linda_say_no = Attack(10, "Linda politely declined Big John's offer.", "rejection damage", 'say no')

# email inbox (Linda HP 100, inbox HP 50)
inbox_sit_there = Attack(20, "The inbox just sat there.", "damage from the stress of thinking about all those emails")
inbox_grow = Attack(30, "The inbox swelled in size!", "damage from the stress of thinking about all those emails")
linda_delete = Attack(20, "Linda deleted a bunch of emails.", "damage", 'delete')
linda_ignore_email = Attack(30, "Linda ignored a bunch of emails.\nThe inbox is devestated!", "sadness damage :(", 'ignore')

# dissatisfied clients (Linda HP 125, clients HP 75)
d_clients_attention = Attack(30, "The dissatisfied clients demanded attention.\nOh no, there are so many of them all at once!\n(this is a diss on reward gateway)", "stress damage")
d_clients_complain = Attack(40, "The dissatisfied clients decided to complain to Patrick. Ugh, Linda got frustrated...", "frustration damage")
linda_shrug = Attack(50, "Linda shrugged.\n\n\"Whatever.\"\n\nIt's super effective!!", 'damage', 'shrug')
linda_pacify = Attack(40, "Linda did what she could to quell the clients' annoyances.", "pacification damage", 'appease')

# inferior coworkers (Linda HP 125, coworkers HP 100)
coworkers_slack = Attack(40, "Linda's coworkers sent her ten billion slack messages asking for advice.\nAaaah, it's too much!!", "overwhelm damage")
linda_help = Attack(50, "Linda went above and beyond helping her coworkers out.", "pacification damage", "help out")
linda_ignore_coworkers = Attack(60, "Linda ignored the slack messages. Her coworkers will have to fend for themselves for today, she's simply too busy.", "damage", "ignore")