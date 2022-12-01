from ast import Constant
from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'testapp_1'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1

    ENDOWMENT = cu(10)
    MULT_FACTOR = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        label = "How much do you want to send?",
        min = cu(0),
        max = C.ENDOWMENT
    )
    sent_back_amount = models.CurrencyField()

    pass


class Player(BasePlayer):
    pass

def sent_back_amount_choices(group):
    return currency_range(
        cu(0),
        group.sent_amount * C.MULT_FACTOR,
        cu(1)
    )

# PAGES
class Sent(Page):
    form_model  = "Group"
    form_fields  = ["fields"]

    pass

class SentBack(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
