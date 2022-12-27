
from model.enemy import Enemy
from app.init_attacks import *


full_email_inbox = Enemy(
    'The full email inbox', 
    [
        'Linda came into work on Monday morning and opened her laptop',
        'A monstrous pile of emails was waiting in her inbox',
        'Oh no! The emails began to congeal, and formed a huge, person-shaped blob!',
        'The emails assumed a fighting stance...'
    ], 
    50, 
    [inbox_sit_there, inbox_grow], 
    [linda_delete, linda_ignore]
)