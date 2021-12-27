#Bot Version
GENERAL_VERSION = "v" + "24" + "12" + "2021"

#updater URL (change this to something else if you want to use the o!update)
DISCORD_URL =  "https://cdn.discordapp.com/attachments/840336835166732290/"
ZIP_FILE = "osr2mp4-bot.zip"

#Bot Tokens
NATSUMI_TOKEN = None
OSR2MP4_ALT_TOKEN  = None
OSR2MP4_TOKEN = None

#Bot Owner ID (change that in order to be able to use owner commands)
OWNER = 0

#commands list
keywords = [
    ["ValueError('range() arg 3 must not be zero')", "MustNotBeZero"],
    ["subprocess.ValueError", "MustNotBeZero"],  
    ["CalledProcessError(1, ['ffmpeg', '-i'", "CalledProcessError"],
    ["CalledProcessError(1, ['ffmpeg', '-safe'", "CalledProcessError"],
    ["subprocess.CalledProcessError:", "CalledProcessError"], 
    ["ZeroDivisionError('division by zero')", "DivisionByZero"],
    ["subprocess.ZeroDivisionError", "DivisionByZero"],
    ["object of type 'NoneType has no len())", "NoneType"],
    ["Source contains parsing errors:", "ParsingError"],
    ["IndexError('list index out of range')", "IndexError"],
    ["Scalar value for argument 'color' is longer than 4)", "TypeError"],
    ["MemoryError()", "MemoryError"],
    ["EOFError()", "EOFError"]
    ]


samekeyvalues = ["-slidertick.ogg", "-hitclap.ogg", "-hitfinish.ogg", "-hitwhistle.ogg", "-sliderslide.ogg"]