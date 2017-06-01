import random


message_num = input("What do you want to know? ")



if message_num[0:3] == "why":
    messages = ["I don't know",
        'Because you are an idiot',
        'Because the universe wanted it to',
        'Stop patronizing me',
        "I tell fortunes about the future what is this garbage?",
        'Why would you ask me this?',
        'seriously?',
        'Because',
        'Shut up']
    print (messages[random.randint(0, len(messages) - 1)])

elif message_num[0:3] == "how":
    messages = ["The how could not be answered for comment. Probably. I didn't try.",
            'The moon’s weird though, right?',
            'Time itself doesn’t work.',
            'The sky. The Earth. Life. Existence as an unchanging plain with horizons of birth and death in the faint distance.”',
            "In other news, a recent report suggests that things may not be as they seem.",
            "Curse you. Curse your family. Curse your children. And your children's children.",
            'We do not have answers. I am not certain we even have questions.',
            'In terms of tacos, you are doing fine.',
            'It was a fair question, although the problem with fair questions is that they are asked about an unfair world.']
    print (messages[random.randint(0, len(messages) - 1)])

elif message_num[0:3] == "wha":
    messages = ['I am unsure',
            'Of course',
            'Not looking so great',
            'Not at all',
            'Totes Mcgoats',
            'Maybe you should ask an expert',
            'Fortunes say, whatever',
            'I find you unimportant enough to answer',
            'Never bro']
    print (messages[random.randint(0, len(messages) - 1)])
