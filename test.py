def check_high_score():
        with open("Day20/snakegame/data.txt") as high_score_file:
            new_high_score = int(high_score_file.read())
            return new_high_score
        

highscore = check_high_score()

print (highscore)