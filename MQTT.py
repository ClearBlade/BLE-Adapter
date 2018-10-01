import sys
from clearblade.ClearBladeCore import System

class MQTT:
	def __init__(self, credentials):
		self.systemKey = credentials['systemKey']
		self.systemSecret = credentials['systemSecret']
		self.system = System(self.systemKey, self.systemSecret)
		self.username = credentials['username']
		self.password = credentials['password']
		self.user = self.system.User(self.username, self.password)
		self.platformURL = credentials['platformURL']

                #Connect to MQTT
                self.messagingClient = self.Connect()

	def Connect(self):
                messagingClient = self.system..Messaging(self.user)
                messagingClient.connect()
		return messagingClient

	def PublishTopic(self, topic, message, callback):
                self.messagingClient.publishMessage(topic, message)

	def SubscribeToTopic(self, topic, callback):
		self.messagingClient.subscribe(topic)
