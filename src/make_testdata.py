#!/usr/bin/env python
import os
import sys
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pretix.settings")

import django

django.setup()

from pretix.base.models import *  # NOQA
from django.utils.timezone import now

if Organizer.objects.exists():
    print("There already is data in your DB!")
    sys.exit(0)
user = User.objects.get_or_create(
    email='admin@localhost',
)[0]
user.set_password('admin')
user.save()
organizer = Organizer.objects.create(
    name='BigEvents LLC', slug='bigevents'
)
OrganizerPermission.objects.get_or_create(
    organizer=organizer, user=user
)
year = now().year + 1
event = Event.objects.create(
    organizer=organizer, name='Demo Conference {}'.format(year),
    slug=year, currency='EUR', live=True,
    date_from=datetime(year, 9, 4, 17, 0, 0),
    date_to=datetime(year, 9, 6, 17, 0, 0),
)
EventPermission.objects.get_or_create(
    event=event, user=user
)
cat_tickets = ItemCategory.objects.create(
    event=event, name='Tickets'
)
cat_merch = ItemCategory.objects.create(
    event=event, name='Merchandise'
)
question = Question.objects.create(
    event=event, question='Age',
    type=Question.TYPE_NUMBER, required=False
)
item_ticket = Item.objects.create(
    event=event, category=cat_tickets, name='Ticket',
    default_price=23, tax_rate=19, admission=True
)
item_ticket.questions.add(question)
item_shirt = Item.objects.create(
    event=event, category=cat_merch, name='T-Shirt',
    default_price=15, tax_rate=19
)
var_s = ItemVariation.objects.create(item=item_shirt, value='S')
var_m = ItemVariation.objects.create(item=item_shirt, value='M')
var_l = ItemVariation.objects.create(item=item_shirt, value='L')
ticket_quota = Quota.objects.create(
    event=event, name='Ticket quota', size=400,
)
ticket_quota.items.add(item_ticket)
ticket_shirts = Quota.objects.create(
    event=event, name='Shirt quota', size=200,
)
ticket_quota.items.add(item_shirt)
ticket_quota.variations.add(var_s, var_m, var_l)
