
from constants import BIG_JOHN_ENEMY_NAME, MEGA_JACKIE_ENEMY_NAME, PATRICK_ENEMY_NAME
from model.enemy import Enemy
from app.init_attacks import *

jackie = Enemy(
    'Jackie',
    [
        'We fade in on a standoff between our hero and an old foe.',
        'Jackie: "Just give up, Linda. I\'ll NEVER be satisfied!!"',
        'Linda (under her breath, but Jackie can hear): "Patrick won\'t let me stop working with her..."',
        'Jackie: "Urgh- FINE." "Come on then!!!"',
        'Jackie and Linda sprang into battle!'
    ],
    200,
    [jackie_act_unpleasant, jackie_yell],
    [linda_jackie_try]
)

patrick = Enemy(
    PATRICK_ENEMY_NAME,
    [
        'Linda found herself at the exit of Reward Gateway.',
        'She stepped forward, ready to be done.',
        'A figure stood there, blocking her path.',
        '\n',
        'Patrick: "Hang on. I need to have a meeting with you, real quick."',
    ],
    150,
    [patrick_work, patrick_set_up, patrick_promise],
    [linda_patrick_recognize, linda_patrick_work, linda_patrick_push]
)

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
    [linda_shrug, linda_pacify],
    is_plural=True
)

inferior_coworkers = Enemy(
    'The inferior coworkers',
    [
        'Linda sat down at her desk, weary from her battle (meeting) with the dissatisfied clients.',
        'The desk was situated in an office full of people who just weren\'t quite as good at what they did as she was.',
        'Sensing an opportunity to defeat her and thus gain her power, Linda\'s inferior coworkers attacked!'
    ],
    100,
    [coworkers_slack, coworkers_collaborate],
    [linda_help, linda_ignore_coworkers],
    is_plural=True
)

IRS = Enemy(
    'The IRS',
    [
        'Linda entered the next room. She found the IRS waiting for her.',
        'The IRS stepped forward, menacingly.'
    ],
    1000,
    [IRS_tax],
    [linda_accountant]
)

mouse = Enemy(
    'The mouse',
    [
        'Linda entered the kitchen.',
        'EEEK, A MOUSE!!!!'
    ],
    5,
    [mouse_run],
    [linda_mousetrap]
)

big_john = Enemy(
    BIG_JOHN_ENEMY_NAME,
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

difficult_clients = Enemy(
    "The difficult clients",
    [
        'Back to business.',
        'Linda walked into the next room, and found herself face to face with all of her most difficult clients.',
        'Time for battle.',
        'Normally Linda would sigh, but now that she runs her own business, she is more fulfilled and feels energized with the thrill of the fight!'
    ],
    200,
    [dif_clients_expectations, dif_clients_red_tape],
    [linda_dif_work_harder, linda_dif_escalate],
    is_plural=True
)

mega_jackie = Enemy(
    MEGA_JACKIE_ENEMY_NAME,
    [
        'Linda walked into her office and closed the door.',
        'She sat down in her beautiful, glorious Aeron.',
        'She opened her laptop.',
        'Who did she see, staring back at her from the glossy screen?',
        'Why, none other than...',
        '...',
        'MEGA JACKIE!!!\n',
        'Mega Jackie: "Muhahahahahaaa... LINDA PIONTEK."',
        '"YOU THOUGHT I WAS GONE, LINDA PIONTEK."',
        '"BUT HERE I AM... I\'VE RETURNED!!!"',
        '"HAVE AT YOU!!!!"',
    ],
    400,
    [mega_jackie_guilt, mega_jackie_toxicity, mega_jackie_yell],
    [linda_mega_jackie_nyt, linda_mega_jackie_observe, linda_mega_jackie_hangup]
)

store_bought_cookies = Enemy(
    'Store-bought chocolate chip cookies',
    [
        'Linda went to Wegmans.',
        'Linda strolled down one of the aisles.',
        'A package of store-bought chocolate chip cookies slithered up.', # Hahaha this is great Stella
        '"Ugh, how disgusting..."',
        'The store-bought chocolate chip cookies attacked!'
    ],
    5,
    [cookies_sit_there],
    [linda_cookies_flex],
    is_plural=True
)