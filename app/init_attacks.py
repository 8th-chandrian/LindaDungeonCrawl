from model.attack import Attack

# TODO: adjust damage values
# Linda attacks will be listed with their opponents
# only Linda attacks need a name attribute

# Static Linda attacks (added when she obtains a new item)
# TODO: Stella can you write some better text for this? I'm not sure what to put here
linda_explain_vitamix = Attack(15, 'vitamix', 'Linda presented her Vitamix. She explained its various benefits (manifold) and drawbacks (none) to the Enemy. \nShe spoke matter-of-factly. Obviously, the Vitamix was superior.', 'psychic damage, on account of how cool Linda\'s Vitamix was')
linda_nyt = Attack(30, 'failing nyt', 'Linda landed an overhead strike with the Failing New York Times!', 'fake news damage')

# mega jackie attacks
mega_jackie_yell = Attack(75, "Mega Jackie got really mad! Oh no, she started YELLING!", "loudness damage")
mega_jackie_toxicity = Attack(30, "Mega Jackie continued acting really toxic.\n\n\"MUAHAHAHAHAHAAAA..... MY TOXICITY HAS ONLY GROWN SINCE LAST WE FOUGHT!!!\"\n\nLinda lost sleep due to stress!", "psychic damage")
mega_jackie_guilt = Attack(30, "Mega Jackie tried to guilt Linda into continuing to work with her.", " damage")
linda_jackie_nyt = Attack(50, "failing nyt", 'Jackie DEMANDED to know WHY Linda wouldn\'t work with her.\n\n"Tell me the real reason!!!"\n\nLuckily, Linda had the Failing New York Times, allowing her to disseminate fake news effectively!', 'fake news damage')

# jackie attacks ("yell" is an event, not an attack)
# scoff, or something?

# IRS
IRS_tax = Attack(50, "The IRS demanded that Linda do her taxes. Oh no, they're really confusing!", "damage")
linda_accountant = Attack()

# mouse
mouse_run = Attack(30, "The mouse skittered across the floor.\nLinda shrieked!\n\n\"If only I hadn't defeated Tilly in LINDA SUPER ULTRA MEGA BOSS RUSH 2018...\"\n", "damage")
linda_mousetrap = Attack(10, "mousetrap", "Linda set a mousetrap. Great, now Stella will have to clean it up later... ugh...\nWhatever. She gets another point.", "Stella pulled further ahead on the leaderboard, and the mouse was defeated!")
# TODO: implement linda's mousetrap thing without saying damage value

# problematic clients
p_clients_expectations = Attack(30, "The problematic clients demanded that Linda go beyond the scope of the contract!", "damage")
linda_work_harder = Attack(10, 'work harder', "Linda gritted her teeth and simply worked harder.", "damage. It worked, but this could only go on for so long before someone got smacked with a copy of the Failing New York Times..")

# big john
john_ask = Attack(50, "Big John asked Linda to work with him.\n\n\"Oh brother...\" Linda thinks.\n", "damage")
john_everybody = Attack(20, "Big John said, \"Everybody's doin' it...\"", "damage")
john_feel_good = Attack(20, "Big John said, \"It'll make you feel good...\"", "damage")
john_want_to = Attack(20, "Big John said, \"You know you want to...\"", "damage")
linda_say_no = Attack(10, 'say no', "Linda politely declined Big John's offer.", "damage")

# email inbox
inbox_sit_there = Attack(15, "The inbox just sat there.", "damage from the stress of thinking about all those emails.\n\nThe emails assumed a fighting stance..")
inbox_grow = Attack(25, "The inbox swelled in size!", "damage from the stress of thinking about all those emails.\n\nThe emails assumed a fighting stance..")
linda_delete = Attack(20, 'delete', "Linda deleted a bunch of emails.", "damage")
linda_ignore = Attack(30, 'ignore', "Linda ignored a bunch of emails.\nThe inbox is devestated!", "sadness damage :(")

# dissatisfied clients
d_clients_attention = Attack(25, "The dissatisfied clients demanded attention.\nOh no, there are so many of them all at once!\n(this is a diss on reward gateway)", "stress damage")
d_clients_complain = Attack(30, "The dissatisfied clients decided to complain to Patrick. Ugh, Linda got frustrated...", "damage")
linda_shrug = Attack(50, 'shrug', "Linda shrugged.\n\n\"Whatever.\"\n\nIt's super effective!!", 'damage')
linda_pacify = Attack(30, 'appease', "Linda did what she could to quell the clients' annoyances.", "pacification damage")

# inferior coworkers
coworkers_slack = Attack(40, )