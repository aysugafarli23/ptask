# 1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]


# print("Zehmet olmasa 5 eded daxil edin: ")
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# list=[a,b,c,d,e]
# print(f"{list} >> {sorted(list)}")
    


# 2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 


# sentence = input("Cümlə daxil edin: ")
# words = sentence.split()
# result = []

# for word in words:
#     unique_chars = sorted(set(word))
#     result.append("".join(unique_chars))

# output = " ".join(result)
# print(output)



# 3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13

# tebrikler . 4 cehdde 13 reqemeni tapdiz



# target_number = 13
# guess = -1
# attempts = 0
# inputs = []

# while guess != target_number:
#     guess = int(input(f"Attempt #{attempts+1}: Təxmin etdiyiniz ədədi qeyd edin: "))
#     inputs.append(guess)
#     attempts += 1

# print(f"Təbrikləəər! Siz #{attempts} cehdde {target_number} tapdiniz. ")
# print(f"Sizin cəhdləriniz də aşağıda qeydə alınmışdır:\n{', '.join([f'#{i+1} input == {previous_guess}' for i, previous_guess in enumerate(inputs)])}")


#P.S.I know that we haven't done with >>> enumerate <<< yet, but trying new ways seems interesting dear mentor,isn't it?)) Regards, Aysu)


# 4). 1 ile 100 arasinda sade ededleri print edin. (for loops)


# min = 1
# max = 100

# for i in range(min , max + 1):
#     count = 0
#     for j in range(1, i + 1 ):
#         if (i % j) == 0:
#             count = count + 1
#     if (count == 2):
#             print(i , end = ' ')

