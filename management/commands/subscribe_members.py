import os
import sys
import time
import urllib
import logging
import datetime

logger = logging.getLogger()

from django.core.management.base import BaseCommand, CommandError

from staff.models import Member
from interlink.models import MailingList

class Command(BaseCommand):
	help = "Subscribes every user with an active membership to a mailing list."
	requires_model_validation = True

	def print_usage(self):
		print './manage.py subscribe_members <mailing-list-id>'

	def handle(self, *labels, **options):
		if len(labels) != 1:
			self.print_usage()
			return
		ml_id = labels[0]
		if not MailingList.objects.filter(pk=ml_id).exists():
			logger.error('Did not find find mailing list with id %s' % mk_id)
			return
		mailing_list = MailingList.objects.get(pk=ml_id)
		
		for member in Member.objects.active_members(): mailing_list.subscribers.add(member.user)
		
# Copyright 2011 Office Nomads LLC (http://officenomads.name/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
