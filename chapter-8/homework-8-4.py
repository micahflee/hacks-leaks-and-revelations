import os
import click


@click.command()
@click.argument("path")
@click.option("--password", prompt="Enter password", help="Password is required")
def main(path, password):
    """Get information about files and folders"""

    # Make sure the password is valid
    if password != "yourefired":
        click.echo("Access Denied")
        return

    # Make sure the path is valid
    if not os.path.exists(path):
        click.echo("Error: Invalid path")
        return
    
    # See if the path is a file
    if os.path.isfile(path):
        # Display information about this file
        file_size = os.path.getsize(path)
        click.echo(f"{path} is a file that is {file_size} bytes.")

    # See if the path is a folder
    else:
        # Display information about this folder
        click.echo(f"{path} is a folder. Here are the files inside it:")
        for filename in os.listdir(path):
            if os.path.isfile(os.path.join(path, filename)):
                file_size = os.path.getsize(os.path.join(path, filename))
                click.echo(f"- FILE: {filename} ({file_size} bytes)")
            else:
                click.echo(f"- FOLDER: {filename}")


if __name__ == "__main__":
    main()
