p ="""Several years ago, Channel 4, together with Jo Frost (perhaps better known as Supernanny) conducted an experiment. Forty children, aged six, were invited to a party and divided into two halves. One half was given typical sugary party foods. The other half ate sugar-free foods. The parents were unaware as to which group their child was in. No artificial colourings or flavourings commonly found in sweets were present. Artificial colourings and flavourings have already been linked to hyperactivity. Many parents believe that sugar consumption causes hyperactivity in their children. ‘Sugar highs’ are often blamed for rowdiness or excitability, but is sugar guilty of causing hyperactivity or is it simply a case of ‘normal’ childhood behaviour? As the children ran about and enjoyed the party, the parents were asked whether they believed their own child had been given sugar. The majority believed they had. As the children sat down to watch a magic show, many parents changed their minds. They could not accept that their child was capable of sitting still after consuming sugary foods. The experiment suggested that there was no link between hyperactivity and sugar intake. The children were naturally excited because they were at a party."""
pl= p.split()
dic = {}

for word in pl:
    count = 0
    for string_word in pl:
        if word == string_word:
            count = count + 1
    dic[word]= count

most_repeated = None
max_count = 0

for word in pl:
    count = dic.get(word)
    if max_count < count:
        max_count=count
        most_repeated=word

print(f"The {most_repeated} is repeaded most upto {max_count}")
