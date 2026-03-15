import game

p = game.Question.play(game.Question.load_questions("domande"))
p.update_players("punti", p.sort_by_score(p.load_players("punti")))