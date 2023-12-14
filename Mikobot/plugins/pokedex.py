# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/O_okarma
# API BY https://www.github.com/SOME-1HING
# PROVIDED BY https://t.me/ProjectCodeX

# <============================================== IMPORTS =========================================================>
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes, CallbackQueryHandler, CommandHandler

from Mikobot import function
from Mikobot.state import state

# <=======================================================================================================>


# <================================================ FUNCTIONS =====================================================>
async def get_pokemon_info(name_or_id):
    try:
        response = await state.get(
            f"https://sugoi-api.vercel.app/pokemon?name={name_or_id}"
        )
        if response.status_code == 200:
            return response.json()

        response = await state.get(
            f"https://sugoi-api.vercel.app/pokemon?id={name_or_id}"
        )
        if response.status_code == 200:
            return response.json()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return None


async def pokedex(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if context.args:
            name_or_id = context.args[0]
            pokemon_info = await get_pokemon_info(name_or_id)

            if pokemon_info:
                reply_message = (
                    f"🐾 𝗡𝗔𝗠𝗘: {pokemon_info['name']}\n"
                    f"•➥ 𝗜𝗗: {pokemon_info['id']}\n"
                    f"•➥ 𝗛𝗘𝗜𝗚𝗛𝗧: {pokemon_info['height']}\n"
                    f"•➥ 𝗪𝗘𝗜𝗚𝗛𝗧: {pokemon_info['weight']}\n"
                )

                abilities = ", ".join(
                    ability["ability"]["name"] for ability in pokemon_info["abilities"]
                )
                reply_message += f"•➥ 𝗔𝗕𝗜𝗟𝗜𝗧𝗜𝗘𝗦: {abilities}\n"

                types = ", ".join(
                    type_info["type"]["name"] for type_info in pokemon_info["types"]
                )
                reply_message += f"•➥ 𝗧𝗬𝗣𝗘𝗦: {types}\n"

                image_url = f"https://img.pokemondb.net/artwork/large/{pokemon_info['name']}.jpg"

                # Create inline buttons
                keyboard = [
                    [
                        InlineKeyboardButton(text="🔖 STATS", callback_data="stats"),
                        InlineKeyboardButton(text="⚜️ MOVES", callback_data="moves"),
                    ]
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)

                await update.message.reply_photo(
                    photo=image_url,
                    caption=reply_message,
                    reply_markup=reply_markup,
                )
            else:
                await update.message.reply_text("Pokemon not found.")
        else:
            await update.message.reply_text("Please provide a Pokemon name or ID.")
    except Exception as e:
        await update.message.reply_text(f"An error occurred: {str(e)}")


async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    try:
        name = query.message.caption.split("\n")[0].split(": ")[1]
        pokemon_info = await get_pokemon_info(name)

        if pokemon_info:
            stats = "\n".join(
                f"{stat['stat']['name'].upper()}: {stat['base_stat']}"
                for stat in pokemon_info["stats"]
            )
            stats_message = f"•➥ STATS:\n{stats}\n"

            moves = ", ".join(
                move_info["move"]["name"] for move_info in pokemon_info["moves"]
            )
            moves_message = f"•➥ MOVES: {moves}"

            if query.data == "stats":
                await query.message.reply_text(stats_message)
            elif query.data == "moves":
                if len(moves_message) > 1000:
                    with open("moves.txt", "w") as file:
                        file.write(moves_message)
                    await query.message.reply_text(
                        "The moves exceed 1000 characters. Sending as a file.",
                        disable_web_page_preview=True,
                    )
                    await query.message.reply_document(document=open("moves.txt", "rb"))
                else:
                    await query.message.reply_text(moves_message)
        else:
            await query.message.reply_text("Pokemon not found.")
    except Exception as e:
        await query.message.reply_text(f"An error occurred: {str(e)}")


# <================================================ HANDLER =======================================================>
# Add the command and callback query handlers to the dispatcher
function(CommandHandler("pokedex", pokedex, block=False))
function(
    CallbackQueryHandler(callback_query_handler, pattern="^(stats|moves)$", block=False)
)

# <================================================ HANDLER =======================================================>
__help__ = """

🍥 *POKEMON SEARCH*

➠ *Commands*:

»  /pokedex < Search > : Gives that pokemon info.
"""

__mod_name__ = "𝗣𝗢𝗞𝗘𝗗𝗘𝗫"
# <================================================ END =======================================================>
