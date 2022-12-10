import httpx
import click


@click.command()
@click.argument("gab_username")
def main(gab_username):
    """Download a user's posts from Gab"""

    # Get information about the user
    r = httpx.get(f"https://gab.com/api/v1/account_by_username/{gab_username}")
    user_info = r.json()
    if "error" in user_info:
        print(user_info["error"])
        return

    # Display some user info
    click.echo(f"Display name: {user_info['display_name']}")
    click.echo(
        f"{user_info['followers_count']:,} followers, {user_info['following_count']:,} following, {user_info['statuses_count']:,} posts"
    )
    print()

    # Get this user's posts
    r = httpx.get(f"https://gab.com/api/v1/accounts/{user_info['id']}/statuses")
    posts = r.json()
    for post in posts:
        if post["reblog"]:
            print(
                f"repost @{post['reblog']['account']['username']}: {post['reblog']['created_at']}: {post['reblog']['content']}"
            )
        else:
            print(f"{post['created_at']}: {post['content']}")


if __name__ == "__main__":
    main()
