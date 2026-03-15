import Game

player = Game.Question.play(Game.Question.load_questions("domande"))
player.update_players("punti", player.sort_by_score(player.load_players("punti")))