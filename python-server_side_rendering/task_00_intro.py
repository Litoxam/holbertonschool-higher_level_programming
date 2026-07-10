#!/usr/bin/env python3
import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # check if template is empty
    if len(template) == 0:
        print("Template is empty, no output files generated.")
        return

    # check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: attendees must be a list of dictionaries.")
        return

    # check if elements of attendees are dicts
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: attendees must be a list of dictionaries.")
            return
    
    # Check if attendees is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    

    for i, attendee in enumerate(attendees, start=1):
        invitation = template

        # Get all the data ine the dict
        name = attendee.get("name") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        # replace the fields in the invitation with the date
        invitation = invitation.replace("{name}", name)
        invitation = invitation.replace("{event_title}", event_title)
        invitation = invitation.replace("{event_date}", event_date)
        invitation = invitation.replace("{event_location}", event_location)

        
        filename = f"output_{i}.txt"
        # if filename exists, remove it
        if os.path.exists(filename):
            os.remove(filename)
        # and write inside again
        with open(filename, "w") as file:
            file.write(invitation)
