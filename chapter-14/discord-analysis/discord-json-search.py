#!/usr/bin/python3
import sys
import json
import click
from datetime import datetime


def highlight(message, query):
    new_message = ""
    index = 0
    while True:
        new_index = message.lower().find(query.lower(), index)
        if new_index > 0:
            # Found
            new_message += message[index:new_index]
            new_message += click.style(
                message[new_index : new_index + len(query)], underline=True
            )
            index = new_index + len(query)
        else:
            # Not found
            new_message += message[index:]
            break

    return new_message


def display(channel_name, server_name, user_name, timestamp, message, query):
    click.echo(
        "{} {}".format(
            click.style("#{}".format(channel_name), fg="bright_magenta"),
            click.style("[server: {}]".format(server_name), fg="bright_black"),
        )
    )
    click.echo(
        "{} {}".format(
            click.style(user_name, bold=True),
            click.style(timestamp.strftime("%c"), fg="bright_black"),
        )
    )
    click.echo(highlight(message, query))
    click.echo("")


def search(data, query):
    # Loop through each channel
    for channel_id in data["data"]:
        # Get the channel name and server name
        channel_name = data["meta"]["channels"][channel_id]["name"]
        server_name = data["meta"]["servers"][
            data["meta"]["channels"][channel_id]["server"]
        ]["name"]

        for message_id in data["data"][channel_id]:
            # Pull the user data, timestamp, and message body from the message
            user_index = data["data"][channel_id][message_id]["u"]
            user_id = data["meta"]["userindex"][user_index]
            user_name = data["meta"]["users"][user_id]["name"]
            timestamp = datetime.fromtimestamp(
                data["data"][channel_id][message_id]["t"] / 1000
            )
            message = data["data"][channel_id][message_id]["m"]

            # Is the query in the message?
            if query.lower() in message.lower():
                display(channel_name, server_name, user_name, timestamp, message, query)


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.argument("query")
def main(filename, query):
    # Load the JSON file
    try:
        with open(filename) as f:
            data = json.loads(f.read())
    except:
        print("Failed to load JSON file")
        sys.exit()

    # Search
    search(data, query)


if __name__ == "__main__":
    main()
