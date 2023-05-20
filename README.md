# project.py
    #### Mini Adventure Game by Joan Kusuma
    #### Video Demo:  https://youtu.be/mr8mLCL8JNw
    #### Description: You are invited to play different games with different characters in this project.
    You first met a dragon who welcomed you to this place, dragon-land.
    You're required to enter your first and last name, for example: Joan Kusuma
    You will be invited to enter a cottage and once you're inside, you'll meet 3 different characters: Stimpy, Tux, and Cheese.
    You will be invited whom to play the game with, each with different level.
    If you didn't pass this game, you'll be eaten by the dragon! NO!
    If you pass the first game, you'll then move on to the next room.
    In the next room, you'll meet a cat, make sure you greet it with the appropriate greeting!
    it'll give you coins if it likes you enough, you'll then move on to the next door, which opens up to the backyard.
    You'll meet Beavis the wizard in the backyard and he'll need your help.
    Make sure to help him and if you successfully helped him, he'll grant you a wish tonight.

    ### Functions used:
    validate_name(x): used to validate the name enterd at the beginning. Make sure to only use First and Last name
    get_choice(): with this function, you'll get to choose to play a guessing game with three different characters, stimpy, tux, or cheese. It must be either one of them, or the game will not move forward.
    generate_game(): through this function, it will generate the correct answer randomly based on the character that you choose, each with a level of difficulty.
    simulate_round(x): through simulate_round, you'll get three attempts to guess the correct answer that was generated randomly by the previous function, with a hint if you got it wrong.
    value(greeting): If you successfully move to the next section, you'll then be greeted by a cat, in which you'll have to greet it back with an appropriate greeting, you will be rewarded, or not, based on the value of your answer.
    simulate_grimoire(): through this function, it will simulate the guessing game again, but this time, the answer was already predetermined, if you guessed the correct answer. You'll complete this mini game, and be granted a wish from the wizard.
    simulate_answer(grimoire): this final function will have the correct answer in the simulate_grimoire() round.

    ### cowsay library
    I used the different visual characters from the cowsay libraries, starting from the dragon, the three characters (stimpy, tux, and cheese), to the cat, and the final wizard (Beavis)

    ### random library
    I used a function in the random library to simulate different rounds in the game

    ### sys library
    through the sys library, I was able to exit certain while loops