n = int(input())

def r(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

total = 9395
male_old = 1703
female_old = 3714
male_young = 2058
female_young = 1920
new_male = male_young // 3 * 2
new_female = female_young // 3 * 2
male_young -= new_male
female_young -= new_female
year = 1994

print("         HERD     ADULT     ADULT     MALE     FEMALE     MALE     FEMALE")
print("YEAR     SIZE     MALES    FEMALES    FAWNS     FAWNS    NEWBORN   NEWBORN")
print("----   -------   -------   -------   -------   -------   -------   -------")

for _ in range(n):
    print(f"{year:<4}   {total:>7}   {male_old:>7}   {female_old:>7}   "
          f"{male_young + new_male:>7}   {female_young + new_female:>7}   "
          f"{new_male:>7}   {new_female:>7}")

    year += 1
    new_born = (female_old * 1.5)
    delete_old_male = male_old * 0.75
    male_old = male_old * 0.9
    male_old -= delete_old_male
    female_old = (female_old * 0.9)
    male_old = (male_old + 0.6 * male_young)
    female_old = (female_old + 0.6 * female_young)
    male_young = (new_male * 0.55)
    female_young = (new_female * 0.55)
    new_male = (new_born * 0.52)
    new_female = new_born * 0.48

    male_old = r(male_old)
    female_old = r(female_old)
    male_young = r(male_young)
    female_young = r(female_young)
    new_male = r(new_male)
    new_female = r(new_female)

    total = male_old + female_old + male_young + female_young + new_male + new_female