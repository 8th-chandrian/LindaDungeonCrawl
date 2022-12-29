
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