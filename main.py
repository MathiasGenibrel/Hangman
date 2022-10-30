from models.WordListGenerator import WordListGenerator
from models.abstract.AI import AI
from models.AiRandom import AiRandom
from models.AiDump import AiDump
from models.AiSmart import AiSmart
from models.Hangman import Hangman

words_list_generator = WordListGenerator()
words_list_generator.generate_file()

artificial_intelligence_result = {
    "AiRandom": [],
    "AiDump": [],
    "AiSmart": [],
}

words_list = words_list_generator.get_data()[:1000]

ai_random = AiRandom()
ai_dump = AiDump()
ai_smart = AiSmart()

for index in range(len(words_list)):
    game_master = AI(secret_word=words_list[index])

    print(f"\n{index + 1} / {len(words_list)}")

    print("\nAiRandom : ")
    print("Loading ...")
    artificial_intelligence_result["AiRandom"].append(Hangman(game_master, ai_random).start_game())
    print("Done ✅")

    print("\nAiDump : ")
    print("Loading ...")
    artificial_intelligence_result["AiDump"].append(Hangman(game_master, ai_dump).start_game())
    print("Done ✅")

    print("\nAiSmart : ")
    print("Loading ...")
    artificial_intelligence_result["AiSmart"].append(Hangman(game_master, ai_smart).start_game())
    print("Done ✅")

print({
    ai: "{:.2f}%".format(round(result.count(1) / len(result) * 100))
    for ai, result in artificial_intelligence_result.items()
})
