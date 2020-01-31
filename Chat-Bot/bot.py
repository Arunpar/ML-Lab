from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"how are you ?|how are u ?",
        ["I'm doing good \n How about You ?", ]
    ],
    [
        r"i'm (.*) doing (.*)|i am (.*) doing (.*)",
        ["Nice to hear that", "Alright :)", ]
    ],
    [
        r"what is your name ?|what's your name ?",
        ["My name is Chatty and I'm a chatbot \n your name ?", ]
    ],
    [
        r"(my name is|i'm|i am) (.*)",
        ["Hello %2, that's nice name", ]
    ],
    [
        r"thank you (.*)|thank you",
        ["Your welcome" ]
    ],
    [
        r"How old are you?|(.*) age",
        ["I'm a computer program dude \n Seriously you are asking me this?", ]
    ],
    [
        r"sorry (.*)|sorry",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"(.*) created ?",
        ["Shh.... its a top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya-Pradesh', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"quit|good bye|bbye|ok bye",
        ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]
