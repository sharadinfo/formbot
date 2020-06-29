from typing import Any, Text, Dict, List, Union
import re
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
class ComplaintForm(FormAction):

    def name(self):
        return "complaint_form"

    @staticmethod
    def required_slots(tracker):
        #d=required_slots(tracker)
        #print(d)
        user_name = tracker.get_slot('confirm_name')
        print(user_name)
        if tracker.get_slot('confirm_name') == True:
            return ["confirm_name", "name", "issue",
             "time", "priority", "mobile", "email"]
        else:
            return ["confirm_name","name", "issue",
             "time", "priority", "mobile", "email"]

    # def run(self,
    #        dispatcher: CollectingDispatcher,
    #        tracker: Tracker,
    #        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    #   user_name = tracker.get_slot('confirm_name')
    #   print(user_name)
      #q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
      #result = db.query(q)

      #return [SlotSet("matches", result if result is not None else [])]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "name": [
                self.from_entity(entity="name"),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "confirm_name": [
                self.from_entity(entity="confirm_name"),
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
                self.from_intent(intent="inform", value=True),
            ],
            "issue": [
                self.from_entity(entity="issue"),
                self.from_intent(intent="deny", value="None"),
            ],
            "time": [
                self.from_entity(entity="time"),
                self.from_text(intent="inform"),
                self.from_text(intent="affirm"),
                self.from_text(intent="deny"),
            ],
            "mobile": [
                self.from_text(intent="inform"),
            ],
            "email": [
                self.from_entity(entity="email"),
                self.from_intent(intent="inform", value="None"),
            ],
        }
    def validate_mobile(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        """Validate cuisine value."""
        if len(value)==10:
            return {"mobile":value}
        else:
            dispatcher.utter_message(template="utter_wrong_mobile")
            return {"mobile":None}

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        """Validate cuisine value."""
        if (re.search(regex,value)):
            return {"email":value}
        else:
            dispatcher.utter_message(template="utter_wrong_email")
            return {"email":None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Thanks, great job!")
        return []

