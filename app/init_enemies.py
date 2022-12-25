
from model.enemy import Enemy
from app.init_attacks import *


full_email_inbox = Enemy(
    'The full email inbox', 
    'TODO intro text here', 
    50, 
    [inbox_sit_there, inbox_grow], 
    [linda_delete, linda_ignore]
)