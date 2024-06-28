from random import shuffle
from typing import Literal, Self

class MentsuType:
    tehai = 0
    tehai_ron = 1
    chi = 2
    pon = 3
    ankan = 4.0
    daiminkan = 4.1
    kakan = 4.2

MPSZtype = Literal["m", "p", "s", "z"]
class Hai:
    every_hais = list[Self]
    every_hai_quartets = list[Self]

    def __init__(self, number: int, mpsz_type: MPSZtype, aka = False):
        if not (
            mpsz_type == "z" and number in range(1, 7+1)
            or mpsz_type in ("m", "p", "s") and number in range(1, 9+1)):
            
            raise Exception("Invalid Hai")

        self.number = number
        self.mpsz_type = mpsz_type
        self.aka = aka

    def __repr__(self):
        repr_number = str(self.number)
        repr_mpsz_type = str(self.mpsz_type)
        if self.aka:
            repr_number = "0"

        return repr_number + repr_mpsz_type
    
    def __lt__(self, other):
        mpsz_order = ("m", "p", "s", "z")
        if isinstance(other, Hai):
            return (mpsz_order.index(self.mpsz_type), self.number, not self.aka) < (mpsz_order.index(other.mpsz_type), other.number, not other.aka)

    def __hash__(self):
        return hash((self.number, self.mpsz_type, self.aka))
    
    def routouhais():
        return [hai for hai in Hai.every_hais if hai.number in (1, 9)]

    def yaochuuhais():
        return [hai for hai in Hai.every_hais if hai.number in (1, 9) or hai.mpsz_type == "z"]
    
    def chunchanpais():
        return [hai for hai in Hai.every_hais if hai.number in range(2, 8+1) and hai.mpsz_type != "z"]
    
    def suupais():
        return [hai for hai in Hai.every_hais if hai.mpsz_type != "z"]
    
    def jihais():
        return [hai for hai in Hai.every_hais if hai.mpsz_type == "z"]
    
    def green_hais():
        return [hai for hai in Hai.every_hais if hai in (Hai(2, "s"), Hai(3, "s"), Hai(4, "s"), Hai(6, "s"), Hai(8, "s"), Hai(6, "z"))]
    
    def sangenpais():
        return [hai for hai in Hai.every_hais if hai in (Hai(5, "z"), Hai(6, "z"), Hai(7, "z"))]

    def kazehais():
        return [hai for hai in Hai.every_hais if hai in (Hai(1, "z"), Hai(2, "z"), Hai(3, "z"), Hai(4, "z"))]

    def is_routouhai(self):
        return self in Hai.routouhais()

    def is_yaochuuhai(self):
        return self in Hai.yaochuuhais()

    def is_chunchanpai(self):
        return self in Hai.chunchanpais()

    def is_suupai(self):
        return self in Hai.suupais()

    def is_jihai(self):
        return self in Hai.jihais()

    def is_green_hai(self):
        return self in Hai.green_hais()

    def is_sangenpai(self):
        return self in Hai.sangenpais()

    def is_kazehai(self):
        return self in Hai.kazehais()

    def __eq__(self, other):
        """Normal and aka are the same"""
        
        if isinstance(other, Hai):
            return (self.number, self.mpsz_type) == (other.number, other.mpsz_type)

Hai.every_hais = [
            Hai(1, "m"), Hai(2, "m"), Hai(3, "m"), Hai(4, "m"), Hai(5, "m"), Hai(5, "m", aka=True), Hai(6, "m"), Hai(7, "m"), Hai(8, "m"), Hai(9, "m"),
            Hai(1, "p"), Hai(2, "p"), Hai(3, "p"), Hai(4, "p"), Hai(5, "p"), Hai(5, "p", aka=True), Hai(6, "p"), Hai(7, "p"), Hai(8, "p"), Hai(9, "p"),
            Hai(1, "s"), Hai(2, "s"), Hai(3, "s"), Hai(4, "s"), Hai(5, "s"), Hai(5, "s", aka=True), Hai(6, "s"), Hai(7, "s"), Hai(8, "s"), Hai(9, "s"),
            Hai(1, "z"), Hai(2, "z"), Hai(3, "z"), Hai(4, "z"), Hai(5, "z"), Hai(5, "z", aka=True), Hai(6, "z"), Hai(7, "z"),
    ]

Hai.every_hai_quartets = [
        Hai(1, "m"), Hai(1, "m"), Hai(1, "m"), Hai(1, "m"),
        Hai(2, "m"), Hai(2, "m"), Hai(2, "m"), Hai(2, "m"),
        Hai(3, "m"), Hai(3, "m"), Hai(3, "m"), Hai(3, "m"),
        Hai(4, "m"), Hai(4, "m"), Hai(4, "m"), Hai(4, "m"),
        Hai(5, "m"), Hai(5, "m"), Hai(5, "m"), Hai(5, "m", aka=True),
        Hai(6, "m"), Hai(6, "m"), Hai(6, "m"), Hai(6, "m"),
        Hai(7, "m"), Hai(7, "m"), Hai(7, "m"), Hai(7, "m"),
        Hai(8, "m"), Hai(8, "m"), Hai(8, "m"), Hai(8, "m"),
        Hai(9, "m"), Hai(9, "m"), Hai(9, "m"), Hai(9, "m"),

        Hai(1, "p"), Hai(1, "p"), Hai(1, "p"), Hai(1, "p"),
        Hai(2, "p"), Hai(2, "p"), Hai(2, "p"), Hai(2, "p"),
        Hai(3, "p"), Hai(3, "p"), Hai(3, "p"), Hai(3, "p"),
        Hai(4, "p"), Hai(4, "p"), Hai(4, "p"), Hai(4, "p"),
        Hai(5, "p"), Hai(5, "p"), Hai(5, "p"), Hai(5, "p", aka=True),
        Hai(6, "p"), Hai(6, "p"), Hai(6, "p"), Hai(6, "p"),
        Hai(7, "p"), Hai(7, "p"), Hai(7, "p"), Hai(7, "p"),
        Hai(8, "p"), Hai(8, "p"), Hai(8, "p"), Hai(8, "p"),
        Hai(9, "p"), Hai(9, "p"), Hai(9, "p"), Hai(9, "p"),

        Hai(1, "s"), Hai(1, "s"), Hai(1, "s"), Hai(1, "s"),
        Hai(2, "s"), Hai(2, "s"), Hai(2, "s"), Hai(2, "s"),
        Hai(3, "s"), Hai(3, "s"), Hai(3, "s"), Hai(3, "s"),
        Hai(4, "s"), Hai(4, "s"), Hai(4, "s"), Hai(4, "s"),
        Hai(5, "s"), Hai(5, "s"), Hai(5, "s"), Hai(5, "s", aka=True),
        Hai(6, "s"), Hai(6, "s"), Hai(6, "s"), Hai(6, "s"),
        Hai(7, "s"), Hai(7, "s"), Hai(7, "s"), Hai(7, "s"),
        Hai(8, "s"), Hai(8, "s"), Hai(8, "s"), Hai(8, "s"),
        Hai(9, "s"), Hai(9, "s"), Hai(9, "s"), Hai(9, "s"),

        Hai(1, "z"), Hai(1, "z"), Hai(1, "z"), Hai(1, "z"),
        Hai(2, "z"), Hai(2, "z"), Hai(2, "z"), Hai(2, "z"),
        Hai(3, "z"), Hai(3, "z"), Hai(3, "z"), Hai(3, "z"),
        Hai(4, "z"), Hai(4, "z"), Hai(4, "z"), Hai(4, "z"),
        Hai(5, "z"), Hai(5, "z"), Hai(5, "z"), Hai(5, "z"),
        Hai(6, "z"), Hai(6, "z"), Hai(6, "z"), Hai(6, "z"),
        Hai(7, "z"), Hai(7, "z"), Hai(7, "z"), Hai(7, "z"),
    ]

class HaiPosition:
    tehai = 0
    tsumo = 1
    tedashi = 2 # Naki's tedashi
    shimocha = 3
    toimen = 4
    kamicha = 5
    kakan = 6
    kawa = 7

class Mentsu:
    def __init__(self, mentsu_type: MentsuType, hais_with_pos: list[tuple[Hai, HaiPosition]]):
        self.mentsu_type = mentsu_type
        self.hais_with_pos = hais_with_pos

        if not (
            self.is_kantsu() and len(hais_with_pos) == 4
            or (self.is_shuntsu() or self.is_koutsu()) and len(hais_with_pos) == 3):

            raise Exception("Invalid Mentsu")

    def hais(self):
        return [hai for hai, pos in self.hais_with_pos]
    
    def is_koutsu_or_kantsu(self):
        return self.is_koutsu() or self.is_kantsu()
    
    def is_ankou_or_ankan(self):
        return (
            self.is_koutsu() and self.mentsu_type == MentsuType.tehai
            or self.mentsu_type == MentsuType.ankan
            )

    def is_shuntsu(self):
        numbers = set(hai.number for hai in self.hais())
        least_number = min(numbers)

        return all(hai.is_suupai() for hai in self.hais())\
            and len(set(hai.mpsz_type for hai in self.hais())) == 1\
            and least_number < 8 and numbers == set((least_number, least_number+1, least_number+2))

    def is_koutsu(self):
        return len(set(self.hais())) == 1 and not self.is_kantsu()
    
    def is_kantsu(self):
        return self.mentsu_type in (MentsuType.daiminkan, MentsuType.kakan, MentsuType.ankan)

    def __repr__(self):
        return repr(self.hais())
    
    def __eq__(self, other):
        if isinstance(other, Mentsu):
            return (
                self.mentsu_type == other.mentsu_type
                and all(self_hai == other_hai and self_pos == other_pos
                    for (self_hai, self_pos), (other_hai, other_pos) in zip(self.hais_with_pos, other.hais_with_pos))
                )
    
class Jantou:
    def __init__(self, hais: list[Hai]):
        self.hais = hais

class Configuration:
    # Completed configuration (14 hais)
    def __init__(self, jantou: Jantou | None, non_naki_mentsus: list[Mentsu], nakis: list[Mentsu], last_hai_with_pos: tuple[Hai, HaiPosition], etc_hais: list[Hai] = [], is_chitoi: bool = False, is_kokushi: bool = False):
        self.jantou = jantou
        self.non_naki_mentsus = non_naki_mentsus
        self.nakis = nakis
        self.mentsus = non_naki_mentsus + nakis
        self.shuntsus = [mentsu for mentsu in self.mentsus if mentsu.is_shuntsu()]
        self.koutsus = [mentsu for mentsu in self.mentsus if mentsu.is_koutsu()]
        self.kantsus = [mentsu for mentsu in self.mentsus if mentsu.is_kantsu()]
        self.koutsus_or_kantsus = [mentsu for mentsu in self.mentsus if mentsu.is_koutsu() or mentsu.is_kantsu()]
        self.hais = jantou.hais + sum([mentsu.hais() for mentsu in self.mentsus], []) + etc_hais
        self.last_hai = last_hai_with_pos[0]
        self.last_hai_with_pos = last_hai_with_pos
        self.is_chitoi = is_chitoi
        self.is_kokushi = is_kokushi

    def is_menzen(self):
        return self.nakis == []

    def is_daisangen(self):
        koutsu_or_kantsu_hais = []
        for mentsu in self.mentsus:
            if mentsu.is_koutsu_or_kantsu():
                koutsu_or_kantsu_hais.append(mentsu.hais()[0])

        return set(Hai.sangenpais()) == set(koutsu_or_kantsu_hais)

    def is_suuankou(self):
        return all(mentsu.is_ankou_or_ankan() for mentsu in self.mentsus)\
                and self.last_hai not in Jantou.hais\
                and not self.is_chitoi and not self.is_kokushi

    def is_tsuuiisou(self):
        return all(hai.is_jihai() for hai in self.hais)
    
    def is_ryuuiisou(self):
        return all(hai.green_hais() for hai in self.hais)
    
    def is_chinroutou(self):
        return all(hai.routouhais() for hai in self.hais)
    
    def is_kokushimusou(self):
        return self.is_kokushi

    def is_shousuushi(self):
        koutsu_or_kantsu_hais = []
        for mentsu in self.mentsus:
            if mentsu.is_koutsu_or_kantsu():
                koutsu_or_kantsu_hais.append(mentsu.hais()[0])

        return set(Hai.kazehais()).intersection(koutsu_or_kantsu_hais) == 3\
                and self.jantou.hais[0].is_kazehai()
    
    def is_suukantsu(self):
        return all(naki.mentsu_type in (MentsuType.daiminkan, MentsuType.kakan, MentsuType.ankan) for naki in self.nakis) and len(self.nakis) == 4

    def is_chuurenpoutou(self):
        # TODO
        ...

    def tehai_yakuman(self):
        # TODO
        """Yakumans that is applied only by the pais and do not rely on the bakyou"""

        return (
            self.is_daisangen()
            or self.is_suuankou(self.last_hai)
            or self.is_tsuuiisou()
            or self.is_ryuuiisou()
            or self.is_chinroutou()
            or self.is_kokushimusou()
            or self.is_shousuushi()
            or self.is_suukantsu()
            or self.is_chuurenpoutou(self.last_hai)
        )

    def tehai_yaku(self):
        # TODO
        """Yakus that is applied only by the pais and do not rely on the bakyou"""

        entire_hais = self.hais + [self.last_hai]
        if self.is_tehai_yakuman():
            ...
        else:
            ...

"""
구련보등
스안커 단기
국사무쌍 13면 대기
순정구련보등
대사희
"""

class Tehai:
    def __init__(self, non_naki_hais: list[Hai], nakis: list[Mentsu] = []):
        if len(non_naki_hais) + 3*len(nakis) != 13:
            raise Exception("Invalid tehai")

        self.non_naki_hais = non_naki_hais
        self.nakis = nakis

    def every_hais(self):
        return self.non_naki_hais + [sum(naki.hais(), []) for naki in self.nakis]

    def is_menzen(self):
        return self.nakis == []
    
    def is_tenpai(self):
        return self.agari_hais()

    def agari_hais(self):
        agari_hais = set()

        for hai in Hai.every_hais:
            if self.is_completed(hai):
                entire_hais = self.non_naki_hais + sum([[hai for hai, pos in naki.hais_with_pos] for naki in self.nakis], [])
                if entire_hais.count(hai) != 4:
                    agari_hais.add(hai)
            
        return agari_hais
    
    def is_completed(self, last_hai: Hai):
        return self.is_normal_completed(last_hai) or self.is_chitoi_completed(last_hai) or self.is_kokushi_completed(last_hai)
    
    def is_kokushi_completed(self, last_hai):
        entire_hais = self.every_hais() + [last_hai]
        return all(hai in Hai.yaochuuhais() for hai in entire_hais) and len(set(entire_hais)) == 13

    def is_chitoi_completed(self, last_hai):
        entire_hais = self.every_hais() + [last_hai]
        return self.is_menzen() and all(entire_hais.count(hai) == 2 for hai in entire_hais)

    def is_normal_completed(self, last_hai):
        non_fixed_hais = self.non_naki_hais + [last_hai]
        return possible_jantou_and_mentsu_configurations(None, non_fixed_hais)

    def posible_configurations(self, last_hai_with_pos: tuple[Hai, HaiPosition]) -> list[Configuration]:
        last_hai = last_hai_with_pos[0]
        non_fixed_hais = self.non_naki_hais + [last_hai]

        if self.is_normal_completed(last_hai):
            possible_jantou_and_mentsu_configuration = possible_jantou_and_mentsu_configurations(None, non_fixed_hais)

            return [Configuration(jantou, non_naki_mentsus, self.nakis, last_hai_with_pos) for jantou, non_naki_mentsus in possible_jantou_and_mentsu_configuration]
        elif self.is_chitoi_completed():
            return [Configuration(None, [], [], last_hai_with_pos, non_fixed_hais, True, False)]
        elif self.is_kokushi_completed():
            return [Configuration(None, [], [], last_hai_with_pos, non_fixed_hais, False, True)]
        else:
            return []

def possible_jantou_and_mentsu_configurations(jantou: Jantou | None, non_fixed_hais: list[Hai]) -> list[tuple[Jantou, list[Mentsu]]]:
    if len(non_fixed_hais) == 0:
        return []
    elif not jantou and len(non_fixed_hais) == 2 and len(set(non_fixed_hais)) == 1:
        return [(Jantou(non_fixed_hais), [])]
    elif len(non_fixed_hais) == 3:
        try:
            return [(jantou, [Mentsu(MentsuType.tehai, [(hai, HaiPosition.tehai) for hai in non_fixed_hais])])]
        except:
            return []
    elif not (
        jantou and len(non_fixed_hais) % 3 == 0
        or not jantou and len(non_fixed_hais) % 3 == 2):
        raise Exception("Invalid non-fixed hais")

    non_fixed_hais.sort()
    hai = non_fixed_hais[0]
    if non_fixed_hais.count(hai) >= 3: # Check koutsu
        potential_mentsu_hais = []
        for _ in range(3):
            potential_mentsu_hais.append(non_fixed_hais.pop(non_fixed_hais.index(hai)))

        potential_fixed_mentsu = Mentsu(MentsuType.tehai, [(potential_mentsu_hai, HaiPosition.tehai) for potential_mentsu_hai in potential_mentsu_hais])
        if (left_possible_mentsu_configurations := possible_jantou_and_mentsu_configurations(jantou, non_fixed_hais[:])):
            return [(jantou, [potential_fixed_mentsu] + mentsus) for jantou, mentsus in left_possible_mentsu_configurations]
        else:
            non_fixed_hais += potential_mentsu_hais # Undo

    if hai in Hai.suupais(): # Check shuntsu 
        if hai.number < 8 and Hai(hai.number+1, hai.mpsz_type) in non_fixed_hais and Hai(hai.number+2, hai.mpsz_type) in non_fixed_hais: # 0, +1, +2
            potential_mentsu_hais = [
                non_fixed_hais.pop(non_fixed_hais.index(hai)),
                non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number+1, hai.mpsz_type))),
                non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number+2, hai.mpsz_type))),
            ]

            potential_fixed_mentsu = Mentsu(MentsuType.tehai, [(potential_mentsu_hai, HaiPosition.tehai) for potential_mentsu_hai in potential_mentsu_hais])

            if (left_possible_mentsu_configurations := possible_jantou_and_mentsu_configurations(jantou, non_fixed_hais[:])):
                return [(jantou, [potential_fixed_mentsu] + mentsus) for jantou, mentsus in left_possible_mentsu_configurations]
            else:
                non_fixed_hais += potential_mentsu_hais # Undo

    if jantou:
        return []
    else:
        if non_fixed_hais.count(hai) >= 2:
            fixed_jantou = Jantou([
                non_fixed_hais.pop(non_fixed_hais.index(hai)),
                non_fixed_hais.pop(non_fixed_hais.index(hai)),
            ])
            return possible_jantou_and_mentsu_configurations(fixed_jantou, non_fixed_hais[:])
        else:
            return []

class Haiyama:
    def __init__(self, hais: list[Hai]):
        self.toncha_hai: list[Hai] = []
        self.nancha_hai: list[Hai] = []
        self.shaacha_hai: list[Hai] = []
        self.peicha_hai: list[Hai] = []

        for _ in range(3):
            self.toncha_hai += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]
            self.nancha_hai += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]
            self.shaacha_hai += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]
            self.peicha_hai += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]

        self.toncha_hai += [hais.pop(0), hais.pop(3)]
        self.nancha_hai += [hais.pop(0)]
        self.shaacha_hai += [hais.pop(0)]
        self.peicha_hai += [hais.pop(0)]

        self.rinshanpai = [hais.pop(), hais.pop(), hais.pop(), hais.pop()]
        self.dorahyoujihai = [hais[-2], hais[-4], hais[-6], hais[-8], hais[-10]]
        self.uradorahyoujihai = [hais[-1], hais[-3], hais[-7], hais[-9], hais[-11]]
        del hais[-11:-1]

        self.piipai = hais[:]

    def __repr__(self):
        return repr([self.toncha_hai, self.nancha_hai, self.shaacha_hai, self.peicha_hai, self.rinshanpai, self.dorahyoujihai, self.dorahyoujihai, self.uradorahyoujihai])

    def tsumo(self):
        return self.piipai.pop(0)

    def random():
        hais = Hai.every_hai_quartets
        shuffle(hais)

        return Haiyama(hais)



if __name__ == "__main__":
    haiyama = Haiyama.random()
    my_hai = haiyama.toncha_hai
    my_hai = [
        Hai(1, "m"),
        Hai(1, "m"),
        Hai(2, "m"),
        Hai(2, "m"),
        Hai(3, "m"),
        Hai(3, "m"),
        Hai(4, "m"),
        Hai(4, "m"),
        Hai(5, "p"),
        Hai(6, "p"),
        Hai(7, "p"),
        Hai(1, "s"),
        Hai(2, "s"),
        Hai(1, "z")
    ]
    is_riichi = False
    first = True
    while True:
        if not first:
            if haiyama.piipai:
                tsumo_hai = haiyama.tsumo()
            else:
                if Tehai(my_hai).is_tenpai():
                    print("ニャンパイ")
                    quit()
                else:
                    print("ノーテンにゃ")
                    quit()
        else:
            tsumo_hai = my_hai[-1]
            my_hai = my_hai[:-1]

        my_hai.sort()
        print(my_hai, tsumo_hai)
        if Tehai(my_hai).is_completed(tsumo_hai):
            print("ツモにゃー！！！")
            tehai_yaku = Tehai(my_hai).tehai_yaku(tsumo_hai)
            quit()
        my_hai.append(tsumo_hai)

        if is_riichi:
            kiru_hai = tsumo_hai
        else:
            while True:
                try:
                    _kiru_hai = input()
                    number, mpsz_type = _kiru_hai
                    if _kiru_hai[0] == "0":
                        kiru_hai = Hai(5, mpsz_type, aka = True)
                    else:
                        kiru_hai = Hai(int(number), mpsz_type)

                    if kiru_hai in my_hai:
                        break
                except (KeyError, ValueError):
                    pass

        if kiru_hai.number == 5 and kiru_hai.mpsz_type != "z":
            for i, hai in enumerate(my_hai):
                if hai == kiru_hai and hai.aka == kiru_hai.aka:
                    del my_hai[i]
                    break
        else:
            my_hai.remove(kiru_hai)

        if Tehai(my_hai).is_tenpai() and not is_riichi:
            print("ダブルリーチにゃ！" if first else "リーチにゃ！")
            is_riichi = True

        if first:
            first = False


# TODO
# 1. 손패 역 구현
# 2. 4인 구현
# 3. 울기 구현
# 4. 상황 역 구현
# 5. 통신 구현


