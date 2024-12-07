from rouge_score import rouge_scorer


scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
scores = scorer.score("Configure environment for DeepMind-style Atari.",
                      "Wrap an environment into a deepmind environment.")

print(scores)



from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


reference = [["Configure", "environment", "for", "DeepMind-style", "Atari"]]
candidate = ["Wrap", "an", "environment", "into", "a", "deepmind", "environment"]

bleu_score = sentence_bleu(reference, candidate, smoothing_function=SmoothingFunction().method1)

print(f"BLEU Score: {bleu_score}")
