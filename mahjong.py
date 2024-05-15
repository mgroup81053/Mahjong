from random import shuffle

class Naki_type:
    none = 0
    chi = 1
    pon = 2
    ankan = 3.0
    daiminkan = 3.1
    kakan = 3.2

class Hai:
    def __init__(self, number, mpsz_type, aka = False):
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

    def every_hais(): # No akas
        return [
            Hai(1, "m"), Hai(2, "m"), Hai(3, "m"), Hai(4, "m"), Hai(5, "m"), Hai(6, "m"), Hai(7, "m"), Hai(8, "m"), Hai(9, "m"),
            Hai(1, "p"), Hai(2, "p"), Hai(3, "p"), Hai(4, "p"), Hai(5, "p"), Hai(6, "p"), Hai(7, "p"), Hai(8, "p"), Hai(9, "p"),
            Hai(1, "s"), Hai(2, "s"), Hai(3, "s"), Hai(4, "s"), Hai(5, "s"), Hai(6, "s"), Hai(7, "s"), Hai(8, "s"), Hai(9, "s"),
            Hai(1, "z"), Hai(2, "z"), Hai(3, "z"), Hai(4, "z"), Hai(5, "z"), Hai(6, "z"), Hai(7, "z"), Hai(8, "z"), Hai(9, "z"),
        ]


    def every_hai_quartets():
        return [
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

    def is_yaochuuhai(self):
        return self.number == 1 or self.number == 9 or self.mpsz_type == "z"
    
    def is_chunchanpai(self):
        return self.number in range(2, 8+1) and self.mpsz_type != "z"
    
    def is_suupai(self):
        return self.mpsz_type != "z"
    
    def is_jihai(self):
        return self.mpsz_type == "z"
    
    def __eq__(self, other): # Normal and aka are the same
        if isinstance(other, Hai):
            return (self.number, self.mpsz_type) == (other.number, other.mpsz_type)
        
class Naki_hai_info:
    none = 0
    tedashi = 1
    shimocha = 2
    toimen = 3
    kamicha = 4
    kakan = 5

class Mentsu:
    def __init__(self, naki_type: Naki_type, hais_with_info: list[tuple[Hai, Naki_hai_info]]):
        self.naki_type = naki_type
        self.hais_with_info = hais_with_info

    def __repr__(self):
        return repr([hai for hai, info in self.hais_with_info])

class Naki_hai_type:
    def __init__(self, naki_type: Naki_type, is_tedashi):
        self.naki_type = naki_type
        self.is_tedashi = is_tedashi

class Tehai:
    # 13mai
    def __init__(self, non_naki_hais: list[Hai], nakis: list[Mentsu] = []):
        self.non_naki_hais = non_naki_hais
        self.nakis = nakis

    def is_tenpai(self):
        for hai in set(Hai.every_hais()):
            if self.is_completed(hai):
                entire_hais = self.non_naki_hais + sum([[hai for hai, info in naki.hais_with_info] for naki in self.nakis], [])
                return entire_hais.count(hai) != 4
            
        return False
    
    def is_completed(self, last_hai: Hai):
        return self.is_normal_completed(last_hai) or self.is_chitoi_completed(last_hai) or self.is_kokushi_completed(last_hai)
    
    def is_kokushi_completed(self, last_hai):
        entire_hais = self.non_naki_hais+[last_hai]
        return all(hai.is_yaochuuhai() for hai in entire_hais) and len(set(entire_hais)) == 13

    def is_chitoi_completed(self, last_hai):
        entire_hais = self.non_naki_hais+[last_hai]
        return self.nakis == [] and all(entire_hais.count(hai) == 2 for hai in entire_hais)
    
    def _is_normal_completed(self, non_fixed_hais: list[Hai], fixed_mentsus: list[Mentsu], fixed_toitsu: list[Hai]):
        if len(non_fixed_hais) == 0:
            return True

        hai = non_fixed_hais[0]
        if non_fixed_hais.count(hai) >= 3: # Check koutsu
            new_mentsu_hais = []
            for _ in range(3):
                new_mentsu_hais.append(non_fixed_hais.pop(non_fixed_hais.index(hai)))

            new_fixed_mentsu = Mentsu(Naki_type.none, [(new_mentsu_hai, Naki_hai_info.none) for new_mentsu_hai in new_mentsu_hais])
            if self._is_normal_completed(non_fixed_hais, fixed_mentsus + [new_fixed_mentsu], fixed_toitsu):
                return True
            else:
                non_fixed_hais += new_mentsu_hais
            
        if hai.is_suupai(): # Check shuntsu
            if Hai(hai.number-2, hai.mpsz_type) in non_fixed_hais and Hai(hai.number-1, hai.mpsz_type) in non_fixed_hais: # -2, -1, 0
                new_mentsu_hais = [
                    non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number-2, hai.mpsz_type))),
                    non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number-1, hai.mpsz_type))),
                    non_fixed_hais.pop(non_fixed_hais.index(hai)),
                ]

                new_fixed_mentsu = Mentsu(Naki_type.none, [(new_mentsu_hai, Naki_hai_info.none) for new_mentsu_hai in new_mentsu_hais])
                if self._is_normal_completed(non_fixed_hais, fixed_mentsus + [new_fixed_mentsu], fixed_toitsu):
                    return True
                else:
                    non_fixed_hais += new_mentsu_hais

            if Hai(hai.number-1, hai.mpsz_type) in non_fixed_hais and Hai(hai.number+1, hai.mpsz_type) in non_fixed_hais: # -1, 0, +1
                new_mentsu_hais = [
                    non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number-1, hai.mpsz_type))),
                    non_fixed_hais.pop(non_fixed_hais.index(hai)),
                    non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number+1, hai.mpsz_type))),
                ]

                new_fixed_mentsu = Mentsu(Naki_type.none, [(new_mentsu_hai, Naki_hai_info.none) for new_mentsu_hai in new_mentsu_hais])
                if self._is_normal_completed(non_fixed_hais, fixed_mentsus + [new_fixed_mentsu], fixed_toitsu):
                    return True
                else:
                    non_fixed_hais += new_mentsu_hais
                
            if Hai(hai.number+1, hai.mpsz_type) in non_fixed_hais and Hai(hai.number+2, hai.mpsz_type) in non_fixed_hais: # 0, +1, +2
                new_mentsu_hais = [
                    non_fixed_hais.pop(non_fixed_hais.index(hai)),
                    non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number+1, hai.mpsz_type))),
                    non_fixed_hais.pop(non_fixed_hais.index(Hai(hai.number+2, hai.mpsz_type))),
                ]

                new_fixed_mentsu = Mentsu(Naki_type.none, [(new_mentsu_hai, Naki_hai_info.none) for new_mentsu_hai in new_mentsu_hais])
                if self._is_normal_completed(non_fixed_hais, fixed_mentsus + [new_fixed_mentsu], fixed_toitsu):
                    return True
                else:
                    non_fixed_hais += new_mentsu_hais

        if fixed_toitsu:
            return False
        else:
            if non_fixed_hais.count(hai) >= 2:
                fixed_toitsu = [
                    non_fixed_hais.pop(non_fixed_hais.index(hai)),
                    non_fixed_hais.pop(non_fixed_hais.index(hai)),
                ]
                return self._is_normal_completed(non_fixed_hais, fixed_mentsus, fixed_toitsu)
    
    def is_normal_completed(self, last_hai, fixed_mentsus: list[Mentsu] = [], fixed_toitsu: list[Hai] = []):
        non_fixed_hais = self.non_naki_hais+[last_hai]
        return self._is_normal_completed(non_fixed_hais, self.nakis, [])



class Haiyama:
    def __init__(self, hais: list[Hai]):
        self.toncha_hai = []
        self.nancha_hai = []
        self.shaacha_hai = []
        self.peicha_hai = []

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
        hais = Hai.every_hai_quartets()
        shuffle(hais)

        return Haiyama(hais)



haiyama = Haiyama.random()
my_hai = sorted(haiyama.toncha_hai)[:-1]
mpsz = {
    "m": "m",
    "p": "p",
    "s": "s",
    "z": "z",
}
import sys
sys.setrecursionlimit(300)
is_riichi = False
while True:
    tsumo_hai = haiyama.tsumo()

    print(my_hai, tsumo_hai)
    if Tehai(my_hai).is_completed(tsumo_hai):
        print("ツモにゃー！！！")
        quit()
    my_hai.append(tsumo_hai)

    if is_riichi:
        kiru_hai = tsumo_hai
    else:
        while True:
            try:
                _kiru_hai = input()
                if _kiru_hai[0] == "0":
                    kiru_hai = Hai(5, mpsz[_kiru_hai[1]], aka = True)
                else:
                    kiru_hai = Hai(int(_kiru_hai[0]), mpsz[_kiru_hai[1]])

                if kiru_hai in my_hai:
                    break
            except KeyError:
                pass

    if kiru_hai.number == 5 and kiru_hai.mpsz_type != "z":
        for i, hai in enumerate(my_hai):
            if hai == kiru_hai and hai.aka == kiru_hai.aka:
                del my_hai[i]
    else:
        my_hai.remove(kiru_hai)
    my_hai.sort()
    if Tehai(my_hai).is_tenpai() and not is_riichi:
        print("リーチにゃ！")
        is_riichi = True


# Todo
# 1. 손패 역 구현
# 2. 4인 구현
# 3. 울기 구현
# 4. 상황 역 구현
# 5. 통신 구현

