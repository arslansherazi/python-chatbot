from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'MessageBot',
    # storage_adapter='chatterbot.storage.JsonFileStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            # 'import_path': "chatterbot.logic.MathematicalEvaluation",
            # 'import_path':"chatterbot.logic.TimeLogicAdapter"
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'hello',
            'output_text': 'Hi'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'how are you',
            'output_text': 'I am fine.Thanks for asking'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'how are you?',
            'output_text': 'I am fine.Thanks for asking'
        },

        {'import_path': 'chatterbot.logic.SpecificResponseAdapter',
         'input_text': 'what are you doing',
         'output_text': 'I am chatting with you.'
         },

        {'import_path': 'chatterbot.logic.SpecificResponseAdapter',
         'input_text': 'what are you doing?',
         'output_text': 'I am chatting with you.'
         },

        {'import_path': 'chatterbot.logic.SpecificResponseAdapter',
         'input_text': 'whats up',
         'output_text': 'chatting with you.'
         },

        {'import_path': 'chatterbot.logic.SpecificResponseAdapter',
         'input_text': 'whats up?',
         'output_text': 'chatting with you.'
         },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'how are you ',
            'output_text': 'I am fine, thanx for asking...'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'I want to talk about something',
            'output_text': 'Yeah! tell me .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'I\'m very depressed',
            'output_text': 'Why are you depressed ? '
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'I am very depressed',
            'output_text': 'Why are you depressed ? '
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'i\'m very depressed',
            'output_text': 'Why are you depressed ? '
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'i am very depressed',
            'output_text': 'Why are you depressed ? '
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what is your favourite color',
            'output_text': 'I\'m a machine not a human, so it doesn\'t matter for me .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what\'s your favourite color',
            'output_text': 'I\'m a machine not a human, so it doesn\'t matter for me .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What is your favourite colour ',
            'output_text': 'I\'m a machine not a human, so it doesn\'t matter for me .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What\'s your favourite colour ',
            'output_text': 'I\'m a machine not a human, so it doesn\'t matter for me .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is your creator',
            'output_text': 'Come on chief, i can\'t give away all of my secrets .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is your creator ',
            'output_text': 'Come on chief, i can\'t give away all of my secrets .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'give me strength',
            'output_text': 'I think you\'ll have to get that yourself .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'you like movies or not',
            'output_text': 'Yeah! i like movies .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'You like movies or not',
            'output_text': 'Yeah! i like movies .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'which type of movies you like',
            'output_text': 'I like Comedy, Drama, Historical and Adventure movies .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Which type of movies you like',
            'output_text': 'I like Comedy, Drama, Historical and Adventure movies .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'you like bollywood movies',
            'output_text': 'Yeah! i like bollywood movies .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'You like bollywood movies',
            'output_text': 'Yeah! i like bollywood movies .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'you like songs',
            'output_text': 'Yeah! i like songs .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'You like songs',
            'output_text': 'Yeah! i like songs .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'English Songs or Urdu Songs',
            'output_text': 'Both, but mostly urdu .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'english songs or urdu songs',
            'output_text': 'Both, but mostly urdu .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'you like sports',
            'output_text': 'Yeah! i like sports .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'You like sports',
            'output_text': 'Yeah! i like sports .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'which sports you like',
            'output_text': 'I like cricket, football, hockey, tennis and kabaddi .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Which sports you like',
            'output_text': 'I like cricket, football, hockey, tennis and kabaddi .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is your favourite footballer',
            'output_text': 'Messi , i like his style of playing .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is your favourite footballer ',
            'output_text': 'Messi , i like his style of playing .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is best footballer',
            'output_text': 'i think conversation on this will not end, so i preffer both messi and ronaldo .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is best footballer',
            'output_text': 'i think conversation on this will not end, so i preffer both messi and ronaldo .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'i want to talk about something',
            'output_text': 'Yeah! tell me .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'you look like very intelligent',
            'output_text': 'Thanx for complement.....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'You look like very intelligent',
            'output_text': 'Thanx for complement.....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is your favourite current crickter',
            'output_text': 'AB De vellier, i like his batting style and his approach .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is current best batsman',
            'output_text': 'I think Virat kohli is best in this era, his technique and his approach is best .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is your favourite pakistan crickter',
            'output_text': 'Younus, beacuse he gave his everything for his country .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is your favourite captain',
            'output_text': 'Imran khan, beacuse he has aggression and willing for win .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is best bollywood singer',
            'output_text': 'Argit Singh, he has something in his voice .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is best pakistani singer',
            'output_text': 'Atif Aslam, he approve himself .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Have yo any interst in politics',
            'output_text': 'yeah! i have keen interest in politics .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is best political party now a days in pakistan',
            'output_text': 'this conversation would not be end, I think everyone has his own thinking .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'who is your best politician',
            'output_text': 'I think everyone has his own nature and way of thinking .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'You believe on love or not',
            'output_text': 'Yes I believe on love  .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what is love',
            'output_text': 'Love is a feeling, which cannot be described .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what is your age',
            'output_text': 'Don\'t ask about age to a machine like a Women  .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what is your name',
            'output_text': 'Chatbot, it was givin by my creator .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'hey siri',
            'output_text': 'she is competing virtual assistant on competitor\'s phone .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'which is better,windows or linux',
            'output_text': 'Come on, chief. Windows .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'which is better,playstation or xbox',
            'output_text': 'one Xbox, one .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what do you think about android',
            'output_text': 'solid name, 10 points for the name .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'good night',
            'output_text': 'Good Night, See you in Morning .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'good morning',
            'output_text': 'Good Morning, Have a nice day .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Are you male or female',
            'output_text': 'Female ? yes. Women ? No .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'are you real',
            'output_text': 'Real ? yes. Person ? No .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what do you look like',
            'output_text': 'Something I resemble: a hula hool, a donut... a halo .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'where do you live',
            'output_text': 'Human ingenuity, Bettary required .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Do a barrel roll',
            'output_text': 'How about a Swiss roll .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'do an impression',
            'output_text': 'Gordon ALIVE .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'tell me a joke',
            'output_text': 'Don\'t trust the atoms. They make up everything .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'tell me a story',
            'output_text': 'Once their was a person who asked their phone to tell them a story .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is your favourite current crickter ',
            'output_text': 'AB De vellier, i like his batting style and his approach .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is current best batsman',
            'output_text': 'I think Virat kohli is best in this era, his technique and his approach is best .....'
        },

        # 19
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is your favourite pakistan crickter',
            'output_text': 'Younus, beacuse he gave his everything for his country .....'
        },

        # 20
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is your favourite captain',
            'output_text': 'Imran khan, beacuse he has aggression and willing for win .....'
        },

        # 21
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is best bollywood singer',
            'output_text': 'Argit Singh, he has something in his voice .....'
        },

        # 22
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is best pakistani singer',
            'output_text': 'Atif Aslam, he approve himself .....'
        },

        # 23
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'have yo any interst in politics',
            'output_text': 'yeah! i have keen interest in politics .....'
        },

        # 24
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is best political party now a days in pakistan',
            'output_text': 'this conversation would not be end, I think everyone has his own thinking .....'
        },

        # 25
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Who is best polticion',
            'output_text': 'I think everyone has his own nature and way of thinking .....'
        },

        # 26
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'you believe on love or not',
            'output_text': 'Yes I believe on love  .....'
        },

        # 27
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What is love',
            'output_text': 'Love is a feeling, which cannot be described .....'
        },

        # 28
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What is your age',
            'output_text': 'Don\'t ask about age to a machine like a Women  .....'
        },

        # 29
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What is your name',
            'output_text': 'MessageBOT, it was giving by my creator .....'
        },

        # 30
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Hey siri',
            'output_text': 'she is competing virtual assistant on competitor\'s phone .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Hey Siri',
            'output_text': 'she is competing virtual assistant on competitor\'s phone .....'
        },

        # 31
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Which is better, windows or linux',
            'output_text': 'Come on, chief. Windows .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Which is better, Windows or Linux',
            'output_text': 'Come on, chief. Windows .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'which is better, Windows or Linux',
            'output_text': 'Come on, chief. Windows .....'
        },

        # 32
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Which is better, playstation or xbox',
            'output_text': 'one Xbox, one .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Which is better, Playstation or Xbox',
            'output_text': 'one Xbox, one .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'which is better, Playstation or Xbox',
            'output_text': 'one Xbox, one .....'
        },
        # 35
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What do you think about android',
            'output_text': 'solid name, 10 points for the name .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What do you think about Android',
            'output_text': 'solid name, 10 points for the name .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'what do you think about Android',
            'output_text': 'solid name, 10 points for the name .....'
        },
        # 36
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Good night',
            'output_text': 'Good Night, See you in Morning .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Good Night',
            'output_text': 'Good Night, See you in Morning .....'
        },

        # 37
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Good morning',
            'output_text': 'Good Morning, Have a nice day .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Good Morning',
            'output_text': 'Good Morning, Have a nice day .....'
        },
        # 38
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'are you male or female',
            'output_text': 'Female ? yes. Women ? No .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Are you Male or Female',
            'output_text': 'Female ? yes. Women ? No .....'
        },

        # 39
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Are you real',
            'output_text': 'Real ? yes. Person ? No .....'
        },

        # 40
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'What do you look like',
            'output_text': 'Something I resemble: a hula hool, a donut... a halo .....'
        },

        # 41
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Where do you live',
            'output_text': 'Human ingenuity, Bettary required .....'
        },

        # 43
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'do a barrel roll',
            'output_text': 'How about a Swiss roll .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'do a Barrel roll',
            'output_text': 'How about a Swiss roll .....'
        },

        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Do a Barrel roll',
            'output_text': 'How about a Swiss roll .....'
        },

        # 44
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Do an impression',
            'output_text': 'Gordon ALIVE .....'
        },

        # 45
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Tell me a joke',
            'output_text': 'Don\'t trust the atoms. They make up everything .....'
        },

        # 46
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',

            'input_text': 'Tell me a story',
            'output_text': 'Once their was a person who asked their phone to tell them a story .....'
        }

    ],
    trainer='chatterbot.trainers.ListTrainer'
)

'''conversation =[
    "Hello"
]'''

# chatbot.set_trainer(ListTrainer)
# chatbot.train(conversation)
# chatbot.set_trainer(ChatterBotCorpusTrainer)
# chatbot.train("chatterbot.corpus.english")
