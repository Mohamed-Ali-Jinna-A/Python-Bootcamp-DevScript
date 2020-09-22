print("\t\t Welcome !!!")
repeat = "yes"
while repeat == "yes":
  print("\n\tKnow about your day !!!")
  print('''
  \t  1. ARIES
  \t  2. TAURUS
  \t  3. GEMINI
  \t  4. CANCER
  \t  5. LEO
  \t  6. VIGRO
  \t  7. LIBRA
  \t  8. SCORPIO
  \t  9. SAGITTARIUS
  \t 10. CAPRICORN
  \t 11. AQUARIUS
  \t 12. PISCES
  ''')
  user_choice = int(input("Pick your horoscope:\n"))
  if user_choice == 1:
    print("\nToday, you may receive some kind of material support from family. It is probably for a wise cause, so be sure to use it accordingly, says Ganesha. You may spend the evening with those very loved ones who have supported you.")
  elif user_choice == 2:
    print("\nThere is a strong prospect that you will work extremely hard to prove yourself at your workplace today, predicts Ganesha. At times, the returns may not be in proportion to your efforts. You will unwind at the end of the day with a happy and content feeling, expects Ganesha.")
  elif user_choice == 3:
    print("\nToday is an important phase in your life. You will be making a few crucial decisions.\nAt work, you will come up with several fresh ideas, which, along with your will power, form the winning concoction for your company. In the evening, you may spend a few extra bucks on comforts and entertainment, says Ganesha.")
  elif user_choice == 4:
    print("\nYou plan a slow but steady strategy to achieve your goals. Your business rivals can come nowhere you in efficiency or expertise. You will win all-out praise for this from all quarters. And, Ganesha is highly delighted")
  elif user_choice == 5:
    print("\nYou may want to carry some aspirin with you today, suggests Ganesha. For, there are strong indications that you may encounter a plenty of stress and roadblocks at work. This headache-inducing factor aside, you'll be blessed with the uncanny knack of beating your opponents at their own game. This will superimpose your position of awe and respect at the workplace, as people realise the stuff you are made of. Go get 'em Lion!!")
  elif user_choice == 6:
    print("\nWork like a thrall to have your contribution noticed, says Ganesha. However, do not expect appreciation in the same degree. Unwind at the end of a long day with the solace of putting in your best.")
  elif user_choice == 7:
    print("\nWork is always unrelenting and today, it manages to catch up with you in a big way. Expect to be under some pressure to meet deadlines, says Ganesha. But all it takes is to remain level-headed and shrewd in your ways, and you can turn things around to make it a prosperous and flourishing day.")
  elif user_choice == 8:
    print("\nLife's not too slow nor too fast: you are going steady and strong, feels Ganesha. On the career front, simply grin and bear it all. Workplace efficiency will improve today. At home, you will be happy and content and more importantly – at peace, says Ganesha.")
  elif user_choice == 9:
    print("\nYou are on a high today, professionally and personally. You have a good convincing power and you will be using it to the optimum level. Seek advice of experienced and seniors for better implementation of ideas on professional front, says Ganesha.")
  elif user_choice == 10:
    print("\nA couple of fascinating developments on the family front will fill the air with excitement, and will keep you pleasantly occupied throughout the day, says Ganesha. Your outstanding efforts at work will be rewarded adequately, but you will need to be extra careful while executing plans as you may commit mistakes that will do irreparable damage.")
  elif user_choice == 11:
    print("\nA couple of fascinating developments on the family front will fill the air with excitement, and will keep you pleasantly occupied throughout the day, says Ganesha. Your outstanding efforts at work will be rewarded adequately, but you will need to be extra careful while executing plans as you may commit mistakes that will do irreparable damage.")
  elif user_choice == 12:
    print("\nRemaining dispassionate and being cold and clinical is the way to achieve success for you today, says Ganesha. Do not let your sentiments interfere in matters of business, lest you regret it later. The evening may see you feel blue. Find something to do to cheer you up!")
  else:
    print("\nIncorrect horoscope. Try once more.")
  repeat=input("\nDo you want to know again ? (yes/no)\n")
