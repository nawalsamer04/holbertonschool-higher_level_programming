#!/usr/bin/python3
"""Task 0 - Creating a Simple Templating Program"""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendee data."""
    if not isinstance(template, str):
        print("Error: template must be a string")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        print("Error: attendees must be a list of dictionaries")
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for i, attendee in enumerate(attendees, start=1):
        output_text = template

        for key in placeholders:
            value = attendee.get(key, "N/A")
            if value is None:
                value = "N/A"
            output_text = output_text.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(i)

        with open(filename, "w", encoding="utf-8") as file:
            file.write(output_text)
