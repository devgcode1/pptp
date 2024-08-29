import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text("😃你好!欢迎使用maiT全国个户机器人\n———————————————\n获得帮助请点击 /help \n———————————————\n限时特价78块钱解锁🔓永久查询功能（客服联系）\n👮‍♂️人工查询请联系： @userasuse（不在联系客服）\n🧑‍💻客服联系： @Tiam_like")
    await update.message.reply_text("❗️频道链接🔗：https://t.me/Tiam_ovo")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("❗️指令列表：\n/start -- 开始\n/help -- 使用方法\n/plc -- 全国社保头（姓名｜身份证）\n/search -- 综合查询（手机号、身份证、姓名、地址）\n———————————————\n💡全国大头查询格式：/plc 姓名 身份证\n💡综合查询格式：/search 姓名/身份证/手机号/地址/QQ号/原始wxid")


async def plc_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("❗️无使用权限\n💡请联系人工客服充值 @Tiam_like")


async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("❗️无使用权限\n💡请联系人工客服充值 @Tiam_like")


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7363590479:AAFqX5K9NMIKDdtMGVBc8daQpkd7p8S4FeM").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("plc", plc_command))
    application.add_handler(CommandHandler("search", search_command))

    # on non command i.e message - echo the message on 

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
