#!/usr/bin/env python3
import os
import json
import sqlalchemy
import click
from app import app, db, Server, User, Channel, Message


@click.group()
def main():
    """Discord Analysis admin tools"""


@main.command()
def create_db():
    db_path = app.config["SQLALCHEMY_DATABASE_URI"][10:]  # strip "sqlite://"
    if os.path.isfile(db_path):
        print("Database already exists")
    else:
        with app.app_context():
            db.create_all()


@main.command()
@click.argument("filename", type=click.Path(exists=True))
def import_json(filename):
    print(f"Importing: {filename}")

    # Import JSON file
    with open(filename) as f:
        data = json.load(f)

    with app.app_context():
        # Add the servers
        print("Adding servers: ", end="", flush=True)
        for item in data["meta"]["servers"]:
            name = item["name"]

            try:
                server = Server(name)
                db.session.add(server)
                db.session.commit()
                print("+", end="", flush=True)
            except sqlalchemy.exc.IntegrityError:
                db.session.rollback()
                print(".", end="", flush=True)
        print("")

        # Add the users
        print("Adding users: ", end="", flush=True)
        for user_discord_id in data["meta"]["users"]:
            name = data["meta"]["users"][user_discord_id]["name"]

            try:
                user = User(user_discord_id, name)
                db.session.add(user)
                db.session.commit()
                print("+", end="", flush=True)
            except sqlalchemy.exc.IntegrityError:
                db.session.rollback()
                print(".", end="", flush=True)
        print("")

        # Add the channels
        print("Adding channels: ", end="", flush=True)
        for channel_discord_id in data["meta"]["channels"]:
            name = data["meta"]["channels"][channel_discord_id]["name"]
            server_id = data["meta"]["channels"][channel_discord_id]["server"]
            server = Server.query.filter_by(
                name=data["meta"]["servers"][server_id]["name"]
            ).first()

            try:
                channel = Channel(server, channel_discord_id, name)
                db.session.add(channel)
                db.session.commit()
                print("+", end="", flush=True)
            except sqlalchemy.exc.IntegrityError:
                db.session.rollback()
                print(".", end="", flush=True)
        print("")

        # Loop through each channel in data
        for channel_discord_id in data["data"]:
            # Get the channel
            channel = Channel.query.filter_by(discord_id=channel_discord_id).one()

            # Loop through each message in this channel
            print(
                f"Adding messages from {channel.server.name}, #{channel.name}: ",
                end="",
                flush=True,
            )
            for message_discord_id in data["data"][channel_discord_id]:
                try:
                    timestamp = data["data"][channel_discord_id][message_discord_id][
                        "t"
                    ]
                    message = data["data"][channel_discord_id][message_discord_id]["m"]

                    user_index = data["data"][channel_discord_id][message_discord_id][
                        "u"
                    ]
                    user_discord_id = data["meta"]["userindex"][user_index]

                    user = User.query.filter_by(discord_id=user_discord_id).one()

                    if "a" in data["data"][channel_discord_id][message_discord_id]:
                        attachments_json = json.dumps(
                            data["data"][channel_discord_id][message_discord_id]["a"]
                        )
                    else:
                        attachments_json = None

                    message = Message(
                        channel.server,
                        message_discord_id,
                        timestamp,
                        message,
                        user,
                        channel,
                        attachments_json,
                    )
                    db.session.add(message)
                    db.session.commit()
                    print("+", end="", flush=True)
                except sqlalchemy.exc.IntegrityError:
                    db.session.rollback()
                    print(".", end="", flush=True)
            print("")

    print("Import complete")
    print("")


@main.command()
def user_stats():
    users = User.query.order_by(User.name).all()
    servers = Server.query.order_by(Server.name).all()

    server_users = {}

    for user in users:
        print(f"User: {user.name}")
        for server in servers:
            message_count = (
                Message.query.filter_by(server=server).filter_by(user=user).count()
            )
            if message_count > 0:
                if server.name in server_users:
                    server_users[server.name] += 1
                else:
                    server_users[server.name] = 1

                print(f"- {message_count} messages on server {server.name}")
        print("")

    print("Users per server:")
    print("")
    for server_name in server_users:
        print(f"{server_name}: {server_users[server_name]} users")


if __name__ == "__main__":
    main()
