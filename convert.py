import itertools
import re


def convert(string: str) -> str:
    tmp = re.sub("\\(dark\\)", ";<sup>0</sup>;34;{{P|Peasant Zombie|2}}", re.sub("\\(dark_armor1\\)", ";<sup>0</sup>;35;{{P|Conehead Peasant|2}}", re.sub("\\(dark_armor2\\)", ";<sup>0</sup>;36;{{P|Buckethead Peasant|2}}", re.sub("\\(dark_armor3\\)", ";<sup>0</sup>;37;{{P|Knight Zombie|2}}", re.sub("\\(dark_juggler\\)", ";<sup>0</sup>;43;{{P|Jester Zombie|2}}", re.sub("\\(dark_wizard\\)", ";<sup>0</sup>;41;{{P|Wizard Zombie|2}}", re.sub("\\(dark_king\\)", ";<sup>0</sup>;42;{{P|Zombie King|2}}", re.sub("\\(dark_imp_dragon\\)", ";<sup>0</sup>;40;{{P|Imp Dragon Zombie|2}}", re.sub("\\(dark_gargantuar\\)", ";<sup>0</sup>;38;{{P|Dark Ages Gargantuar|2}}", re.sub("\\(dark_imp\\)", ";<sup>0</sup>;39;{{P|Imp Monk Zombie|2}}", re.sub("\\(night_camel\\)", ";<sup>0</sup>;44;{{P|Shadow Zombie|2}}", str(string))))))))))))

    return re.sub("\\(ra\\)", ";<sup>0</sup>;13;{{P|Ra Zombie|2}}", re.sub("\\(mummy\\)", ";<sup>0</sup>;7;{{P|Mummy Zombie|2}}", re.sub("\\(mummy_armor1\\)", ";<sup>0</sup>;8;{{P|Conehead Mummy|2}}", re.sub("\\(mummy_armor2\\)", ";<sup>0</sup>;9;{{P|Buckethead Mummy|2}}", re.sub("\\(camel_onehump\\)", ";<sup>0</sup>;14;{{P|Camel Zombies|2}}", re.sub("\\(explorer\\)", ";<sup>0</sup>;15;{{P|Explorer Zombie|2}}", re.sub("\\(egypt_imp\\)", ";<sup>0</sup>;12;{{P|Imp Mummy|2}}", re.sub("\\(mummy_armor4\\)", ";<sup>0</sup>;10;{{P|Pyramid-Head Zombie|2}}", re.sub("\\(egypt_gargantuar\\)", ";<sup>0</sup>;11;{{P|Mummified Gargantuar|2}}", re.sub("\\(pharaoh\\)", ";<sup>0</sup>;16;{{P|Pharaoh Zombie|2}}", re.sub("\\(tomb_raiser\\)", ";<sup>0</sup>;17;{{P|Tomb Raiser Zombie|2}}", re.sub("\\(explorer_veteran\\)", ";<sup>0</sup>;18;{{P|Torchlight Zombie|2}}", re.sub("\\(cleopatra_zombie\\)", ";<sup>0</sup>;19;{{P|Cleopatra Zombie|2}}", tmp)))))))))))))

if __name__ == '__main__':
    list = [[['apple'], ['pear'], ['apple'], ['banana'], ['pear'], ['apple']]]
    list_set = set(list)
    number = len(list_set)
    print(number)