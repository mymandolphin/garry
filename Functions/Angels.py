import json

async def generate_user_info(uid):

    with open("users.json", "r") as f:

        file = json.load(f)

    if not str(uid) in file:

        file[str(uid)] = {

            "xp": 0,
            "level": 0,
            "prestige": 0,
            "pepega_posts": 0,
            "angels": 0

        }

        with open("users.json", "w") as f:

            json.dump(file, f, indent=4)

    return file

async def get_angel_count(ctx):

    file = await generate_user_info(ctx.author.id)

    return file[str(ctx.author.id)]["angels"]

async def increment_angels(ctx, amount):

    with open("global.json", "r") as f:

        file_global = json.load(f)

    file = await generate_user_info(ctx.author.id)

    file[str(ctx.author.id)]["angels"] += amount

    file_global["angels_killed_today"] += amount

    with open("users.json", "w") as f:

        json.dump(file, f, indent=4)

    with open("global.json", "w") as f:

        json.dump(file_global, f, indent=4)
