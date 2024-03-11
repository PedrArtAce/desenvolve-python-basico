import emoji
print("Emojis disponiveis: ")
print(emoji.emojize(":red_heart:"), "- :red_heart:")
print(emoji.emojize(":thumbs_up:"), "- :thumbs_up:")
print(emoji.emojize(":thinking_face:"), "- :thinking_face:")

frs = (str(input("insira a frase a ser emojizada: ")))
print (emoji.emojize(frs))