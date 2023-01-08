
from model.enemy import Enemy
from app.init_attacks import *


full_email_inbox = Enemy(
    'The full email inbox', 
    [
        'Linda came into work on Monday morning and opened her laptop.',
        'A monstrous pile of emails was waiting in her inbox.',
        'Oh no! The emails began to congeal, and formed a huge, person-shaped blob!',
        'The emails assumed a fighting stance...'
    ], 
    50, 
    [inbox_sit_there, inbox_grow], 
    [linda_delete, linda_ignore_email]
)

dissatisfied_clients = Enemy(
    'The dissatisfied clients',
    [
        'Linda advanced into the next room to find many dissatisfied clients of Reward Gateway sitting cross-legged on the floor.',
        'They were playing monopoly.',
        'Upon sighting Linda, they all jumped up and started clamoring for her attention!',
        'Linda braced herself...'
    ],
    75,
    [d_clients_attention, d_clients_complain],
    [linda_shrug, linda_pacify]
)

inferior_coworkers = Enemy(
    'The inferior coworkers',
    [
        'Linda sat down at her desk, weary from her battle (meeting) with the dissatisfied clients.',
        'This desk was situated in an office full of people who just weren\'t quite as good at what they do as she was.',
        'Sensing an opportunity, Linda\'s inferior coworkers attacked!'
    ],
    100,
    [coworkers_slack],
    [linda_help, linda_ignore_coworkers]
)

IRS = Enemy(
    'The IRS',
    [
        'Linda approached the kitchen, but the IRS blocked her path.',
        'The IRS stepped forward, menacingly.'
    ],
    1000,
    [IRS_tax],
    [linda_accountant]
)

mouse = Enemy(
    'The mouse',
    [
        'Linda entered the kitchen. EEEK, A MOUSE!!!!'
    ],
    5,
    [mouse_run],
    [linda_mousetrap]
)
# TODO this is probably not how we want the mouse to work so I'm just doing it like this temporarily

john = Enemy(
    'Big John',
    [
        'Linda ventured forth into the next room.',
        'The smell of a mossy forest slapped her in the face.',
        'A tent was pitched in the middle of the room. Puzzled, Linda approached.',
        'Who did she see, emerging from the tent...?',
        'It was Big John.',
        '"IT\'S ME," he said. "BIG JOHN."'
    ],
    50,
    [john_ask, john_everybody, john_feel_good, john_want_to],
    [linda_say_no]
)

# difficult_clients = Enemy(
#     "The difficult clients",
#     [
#         'Back to business.',
#         'Linda walked into the next room, and found herself face to face with all of her most difficult clients.',
#         'Time for battle.',
#         'Normally Linda would sigh, but now that she runs her own business, she is more fulfilled and feels energized with the thrill of the fight!'
#     ],
#     250,
#     [dif_clients_expectations]
# )
# TODO finish difficult clients

mega_jackie = Enemy(
    'Mega Jackie',
    [
        'Linda walked into her office and closed the door.',
        'She sat down in her beautiful, glorious Aeron.',
        'She opened her laptop.',
        'Who did she see, staring back at her from the glossy screen?',
        'Why, none other than...',
        '...',
        'MEGA JACKIE!!!',
        '\n',
        'Mega Jackie: "Muhahahahahaaa... LINDA PIONTEK."',
        '"YOU THOUGHT YOU DEFEATED ME, LINDA PIONTEK."',
        '"BUT HERE I AM... I\'VE RETURNED!!!"',
        '"HAVE AT YOU!!!!"',
        '\n',
        'Mega Jackie attacked!'
    ],
    400,
    [mega_jackie_guilt, mega_jackie_toxicity, mega_jackie_yell],
    [linda_mega_jackie_nyt, linda_mega_jackie_observe, linda_mega_jackie_hangup]
)

# TODO I gotta do regular Jackie and figure out the intro. Also I should write that star wars crawl at the beginning.
# jackie = Enemy(
#     'Jackie',
#     [
#         'We fade in '
#     ]
# )

store_bought_cookies = Enemy(
    'Store-bought chocolate chip cookies',
    [
        'Linda went to Wegmans.',
        'Linda strolled down one of the aisles.',
        'A package of store-bought chocolate chip cookies slithered up.', # Hahaha this is great Stella
        '"Ugh, how disgusting..."',
        'The cookies attacked!'
    ],
    5,
    [cookies_sit_there],
    [linda_cookies_flex]
)