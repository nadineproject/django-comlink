from django.core.mail import EmailMultiAlternatives


class MailingListMessage(EmailMultiAlternatives):
	"""
	Unlike the default EmailMessage, this does *not* include the 'To' address
	in the list of recipients. We don't send the mailing list a copy
	of its own mail.
	"""
	def recipients(self):
		return self.bcc


# Copyright 2012 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
