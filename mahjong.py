from random import shuffle
from typing import Literal, Self
from collections import Counter
from enum import Enum, unique, auto
import pygame

@unique
class MentsuType(Enum):
    tehai = auto()
    tehai_ron = auto()
    chi = auto()
    pon = auto()
    ankan = auto()
    daiminkan = auto()
    kakan = auto()

    def is_kantsu(self):
        return self in (MentsuType.ankan, MentsuType.daiminkan, MentsuType.kakan)

MPSZtype = Literal["m", "p", "s", "z"]
class HaiWithPosition: ...
class Hai:
    every_hais: list[Self]
    every_hai_quartets: list[Self]

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

    def __eq__(self, other):
        """Normal and aka are the same"""

        if isinstance(other, Hai):
            return (self.number, self.mpsz_type) == (other.number, other.mpsz_type)

    def __lt__(self, other):
        mpsz_order = ("m", "p", "s", "z")
        if isinstance(other, Hai):
            return (mpsz_order.index(self.mpsz_type), self.number, not self.aka) < (mpsz_order.index(other.mpsz_type), other.number, not other.aka)

    def __hash__(self):
        return hash((self.number, self.mpsz_type, self.aka))

    def with_pos(self, pos) -> HaiWithPosition:
        ...

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

@unique
class HaiPosition(Enum):
    tehai = auto()
    tsumo = auto()
    tedashi = auto() # Naki's tedashi
    shimocha = auto()
    toimen = auto()
    kamicha = auto()
    kakan = auto()
    tsumo_kawa = auto()
    tedashi_kawa = auto()

    def __lt__(self, other):
        if isinstance(other, HaiPosition):
            return self.value < other.value

class HaiWithPosition(Hai):
    def __init__(self, number: int, mpsz_type: MPSZtype, pos: HaiPosition, aka: bool = False):
        self.hai = Hai(number, mpsz_type, aka)
        self.pos = pos
        super().__init__(number, mpsz_type, aka)

    def __hash__(self):
        return hash((self.number, self.mpsz_type, self.aka, self.pos))

    def __eq__(self, other):
        """Normal and aka are the same"""

        if isinstance(other, HaiWithPosition):
            return (self.number, self.mpsz_type, self.pos) == (other.number, other.mpsz_type, other.pos)

    def __lt__(self, other):
        mpsz_order = ("m", "p", "s", "z")
        if isinstance(other, HaiWithPosition):
            return (mpsz_order.index(self.mpsz_type), self.number, not self.aka, self.pos) < (mpsz_order.index(other.mpsz_type), other.number, not other.aka, other.pos)

Hai.every_hais = [
            Hai(1, "m"), Hai(2, "m"), Hai(3, "m"), Hai(4, "m"), Hai(5, "m"), Hai(6, "m"), Hai(7, "m"), Hai(8, "m"), Hai(9, "m"),
            Hai(1, "p"), Hai(2, "p"), Hai(3, "p"), Hai(4, "p"), Hai(5, "p"), Hai(6, "p"), Hai(7, "p"), Hai(8, "p"), Hai(9, "p"),
            Hai(1, "s"), Hai(2, "s"), Hai(3, "s"), Hai(4, "s"), Hai(5, "s"), Hai(6, "s"), Hai(7, "s"), Hai(8, "s"), Hai(9, "s"),
            Hai(1, "z"), Hai(2, "z"), Hai(3, "z"), Hai(4, "z"), Hai(5, "z"), Hai(6, "z"), Hai(7, "z"),
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

Hai.with_pos = lambda self, pos: HaiWithPosition(self.number, self.mpsz_type, pos, self.aka)

class Mentsu:
    def __init__(self, mentsu_type: MentsuType, hais_with_pos: list[HaiWithPosition]):
        self.mentsu_type = mentsu_type
        self.hais_with_pos = sorted(hais_with_pos)

        if not (
            self.is_kantsu() and len(hais_with_pos) == 4
            or (self.is_shuntsu() or self.is_koutsu()) and len(hais_with_pos) == 3):

            raise Exception("Invalid Mentsu")

    def __repr__(self):
        return repr(self.hais())

    def __hash__(self):
        return hash((self.mentsu_type, tuple(self.hais_with_pos)))

    def __eq__(self, other):
        if isinstance(other, Mentsu):
            return self.mentsu_type == other.mentsu_type\
                and self.hais_with_pos == other.hais_with_pos

    def __lt__(self, other):
        if isinstance(other, Mentsu):
            return (self.hais_with_pos < other.hais_with_pos)

    def hais(self):
        return [hai_with_pos.hai for hai_with_pos in self.hais_with_pos]

    def is_koutsu_or_kantsu(self):
        return self.is_koutsu() or self.is_kantsu()

    def is_ankou_or_ankan(self):
        return self.is_koutsu() and self.mentsu_type == MentsuType.tehai\
            or self.mentsu_type == MentsuType.ankan

    def is_shuntsu(self):
        numbers = set(hai.number for hai in self.hais())
        least_number = min(numbers)

        return all(hai.is_suupai() for hai in self.hais())\
            and len(set(hai.mpsz_type for hai in self.hais())) == 1\
            and least_number < 8 and numbers == set((least_number, least_number+1, least_number+2))

    def is_koutsu(self):
        return len(set(self.hais())) == 1 and not self.is_kantsu()

    def is_kantsu(self):
        return self.mentsu_type.is_kantsu()

    def is_similar_to(self, other: Self):
        return self.hais() == other.hais()

class Jantou:
    def __init__(self, hais_with_pos: list[HaiWithPosition]):
        self.hais_with_pos = hais_with_pos

    def __repr__(self):
        return repr(self.hais_with_pos)

    def __lt__(self, other):
        if isinstance(other, Jantou):
            return self.hais_with_pos < other.hais_with_pos

    def __eq__(self, other):
        if isinstance(other, Jantou):
            return self.hais_with_pos == other.hais_with_pos

    def hais(self):
        return [hai_with_pos.hai for hai_with_pos in self.hais_with_pos]

class MachiType(Enum):
    ryanmen = auto(), "両面"
    shanpon = auto(), "双碰"
    kanchan = auto(), "間張"
    penchan = auto(), "辺張"
    tanki = auto(), "単騎"

    def __init__(self, value, machi_name):
        self.machi_name = machi_name

    def __repr__(self):
        return self.machi_name

class Configuration:
    # Completed configuration (14 hais)
    def __init__(self, jantou: Jantou | None, non_naki_mentsus: list[Mentsu], nakis: list[Mentsu], last_hai_with_pos: HaiWithPosition, etc_hais_with_pos: list[HaiWithPosition] = [], is_chiitoi: bool = False, is_kokushi: bool = False):
        self.jantou = jantou
        self.non_naki_mentsus = non_naki_mentsus
        self.nakis = nakis
        self.last_hai_with_pos = last_hai_with_pos
        self.etc_hais_with_pos = etc_hais_with_pos
        self.is_chiitoi = is_chiitoi
        self.is_kokushi = is_kokushi

    def __repr__(self):
        return f"{repr(self.jantou)} / {repr(self.non_naki_mentsus)} / {repr(self.nakis)}: {repr(self.machi())}"

    def mentsus(self):
        return self.non_naki_mentsus + self.nakis

    def shuntsus(self):
        return [mentsu for mentsu in self.mentsus() if mentsu.is_shuntsu()]

    def shuntsu_hais(self):
        return [shuntsu.hais()[0] for shuntsu in self.shuntsus()]

    def koutsus(self):
        return [mentsu for mentsu in self.mentsus() if mentsu.is_koutsu()]

    def kantsus(self):
        return [mentsu for mentsu in self.mentsus() if mentsu.is_kantsu()]

    def koutsus_or_kantsus(self):
        return [mentsu for mentsu in self.mentsus() if mentsu.is_koutsu_or_kantsu()]

    def koutsu_or_kantsu_hais(self):
        return [koutsu_or_kantsu.hais()[0] for koutsu_or_kantsu in self.koutsus_or_kantsus()]

    def last_hai(self):
        return self.last_hai_with_pos.hai

    def last_hai_pos(self):
        return self.last_hai_with_pos.pos

    def machi(self):
        if any(hai is self.last_hai() for hai in self.jantou.hais()):
            return MachiType.tanki
        else:
            [last_mentsu] = [mentsu for mentsu in self.mentsus() if any(hai is self.last_hai() for hai in mentsu.hais())]
            if last_mentsu.is_koutsu_or_kantsu():
                return MachiType.shanpon
            else:
                tenpai_shape = {hai.number for hai in last_mentsu.hais() if hai is not self.last_hai()}
                if tenpai_shape in ({1, 2}, {8, 9}):
                    return MachiType.penchan
                elif min(tenpai_shape) + 1 == max(tenpai_shape):
                    return MachiType.ryanmen
                elif min(tenpai_shape) + 2 == max(tenpai_shape):
                    return MachiType.kanchan
                else:
                    raise Exception("Invalid machi type")

    def etc_hais(self):
        return [etc_hai_with_pos.hai for etc_hai_with_pos in self.etc_hais_with_pos]

    def hais(self):
        return self.jantou.hais() + sum([mentsu.hais() for mentsu in self.mentsus()], []) + self.etc_hais()

    def is_menzen(self):
        return self.nakis == []

    def tehai_yaku(self):
        return Yaku.tehai_yaku(self)

def correspond_yaku(yaku):
    def decorater(func):
        func.corresponding_yaku = yaku
        return func

    return decorater

def similar_mentsu_counter(mentsus: list[Mentsu]):
    mentsus_by_hais = [Mentsu(MentsuType.tehai, mentsu.hais_with_pos) for mentsu in mentsus]
    return Counter(mentsus_by_hais)

@unique
class Yaku(Enum):
    riichi = auto(), "立直"
    tanyao = auto(), "断么九"
    menzen_tsumo = auto(), "門前清自摸和"
    yakuhai_jikazehai = auto(), "役牌：自風牌"
    yakuhai_bakazehai = auto(), "役牌：場風牌"
    yakuhai_haku = auto(), "役牌　白"
    yakuhai_hatsu = auto(), "役牌　発"
    yakuhai_chun = auto(), "役牌　中"
    pinfu = auto(), "平和"
    iipeikou = auto(), "一盃口"
    chankan = auto(), "槍槓"
    rinshankaihou = auto(), "嶺上開花"
    haiteiraoyue = auto(), "海底摸月"
    houteiraoyui = auto(), "河底撈魚"
    ippatsu = auto(), "一発"
    dora = auto(), "ドラ"
    akadora = auto(), "赤ドラ"
    uradora = auto(), "抜きドラ"
    daburu_riichi = auto(), "ダブル立直"
    sanshoku_doukou = auto(), "三色同刻"
    sankantsu = auto(), "三槓子"
    toitoihou = auto(), "対々和"
    sanankou = auto(), "三暗刻"
    shousangen = auto(), "小三元"
    honroutou = auto(), "混老頭"
    chiitoitsu = auto(), "七対子"
    chanta = auto(), "混全帯么九"
    ikkitsuukan = auto(), "一気通貫"
    sanshoku_doujun = auto(), "三色同順"
    ryanpeikou = auto(), "二盃口"
    junchan = auto(), "純全帯么九"
    honitsu = auto(), "混一色"
    chinitsu = auto(), "清一色"
    nagashi_mangan = auto(), "流し満貫"

    tenhou = auto(), "天和"
    chiihou = auto(), "地和"
    daisangen = auto(), "大三元"
    suuankou = auto(), "四暗刻"
    tsuuiisou = auto(), "字一色"
    ryuuiisou = auto(), "緑一色"
    chinroutou = auto(), "清老頭"
    kokushimusou = auto(), "国士無双"
    shousuushii = auto(), "小四喜"
    suukantsu = auto(), "四槓子"
    chuurenpoutou = auto(), "九蓮宝燈"
    suuankou_tanki = auto(), "四暗刻単騎"
    kokushi_13men_machi = auto(), "国士無双十三面待ち"
    junsei_chuuren_poutou = auto(), "純正九蓮宝燈"
    daisuushii = auto(), "大四喜"

    def __init__(self, value, yaku_name):
        self.yaku_name = yaku_name

    def __repr__(self):
        return self.yaku_name

    @correspond_yaku(daisangen)
    def is_daisangen(configuration: Configuration):
        return set(Hai.sangenpais()).issubset(set(configuration.koutsu_or_kantsu_hais()))

    @correspond_yaku(suuankou)
    def is_suuankou(configuration: Configuration):
        return configuration.is_menzen()\
            and all(mentsu.is_ankou_or_ankan() for mentsu in configuration.mentsus())\
            and configuration.last_hai() not in configuration.jantou.hais()\
            and not configuration.is_chiitoi and not configuration.is_kokushi

    @correspond_yaku(tsuuiisou)
    def is_tsuuiisou(configuration: Configuration):
        return all(hai.is_jihai() for hai in configuration.hais())

    @correspond_yaku(ryuuiisou)
    def is_ryuuiisou(configuration: Configuration):
        return all(hai.is_green_hai() for hai in configuration.hais())

    @correspond_yaku(chinroutou)
    def is_chinroutou(configuration: Configuration):
        return all(hai.is_routouhai() for hai in configuration.hais())

    @correspond_yaku(kokushimusou)
    def is_kokushimusou(configuration: Configuration):
        return configuration.is_kokushi\
            and configuration.hais().count(configuration.last_hai()) == 1

    @correspond_yaku(shousuushii)
    def is_shousuushii(configuration: Configuration):
        return len(set(Hai.kazehais()).intersection(configuration.koutsu_or_kantsu_hais())) == 3\
            and configuration.jantou.hais()[0].is_kazehai()

    @correspond_yaku(suukantsu)
    def is_suukantsu(configuration: Configuration):
        return len(configuration.kantsus()) == 4

    @correspond_yaku(chuurenpoutou)
    def is_chuurenpoutou(configuration: Configuration):
        mpsz_type = configuration.hais()[0].mpsz_type
        hai_counter = Counter(configuration.hais())
        hai_counter[Hai(1, mpsz_type)] -= 3
        hai_counter[Hai(2, mpsz_type)] -= 1
        hai_counter[Hai(3, mpsz_type)] -= 1
        hai_counter[Hai(4, mpsz_type)] -= 1
        hai_counter[Hai(5, mpsz_type)] -= 1
        hai_counter[Hai(6, mpsz_type)] -= 1
        hai_counter[Hai(7, mpsz_type)] -= 1
        hai_counter[Hai(8, mpsz_type)] -= 1
        hai_counter[Hai(9, mpsz_type)] -= 3

        return configuration.is_menzen()\
            and mpsz_type != "z"\
            and all(hai.mpsz_type == mpsz_type for hai in configuration.hais())\
            and Counter(hai_counter.values()) == Counter([0]*8+[1])\
            and configuration.hais().count(configuration.last_hai()) in (1, 3)

    @correspond_yaku(suuankou_tanki)
    def is_suuankou_tanki(configuration: Configuration):
        return all(mentsu.is_ankou_or_ankan() for mentsu in configuration.mentsus())\
            and configuration.last_hai() in configuration.jantou.hais()\
            and not configuration.is_chiitoi and not configuration.is_kokushi

    @correspond_yaku(kokushi_13men_machi)
    def is_kokushi_13men_machi(configuration: Configuration):
        return configuration.is_kokushi\
            and configuration.hais().count(configuration.last_hai()) == 2

    @correspond_yaku(junsei_chuuren_poutou)
    def is_junsei_chuuren_poutou(configuration: Configuration):
        mpsz_type = configuration.hais()[0].mpsz_type
        hai_counter = Counter(configuration.hais())
        hai_counter[Hai(1, mpsz_type)] -= 3
        hai_counter[Hai(2, mpsz_type)] -= 1
        hai_counter[Hai(3, mpsz_type)] -= 1
        hai_counter[Hai(4, mpsz_type)] -= 1
        hai_counter[Hai(5, mpsz_type)] -= 1
        hai_counter[Hai(6, mpsz_type)] -= 1
        hai_counter[Hai(7, mpsz_type)] -= 1
        hai_counter[Hai(8, mpsz_type)] -= 1
        hai_counter[Hai(9, mpsz_type)] -= 3

        return configuration.is_menzen()\
            and mpsz_type != "z"\
            and all(hai.mpsz_type == mpsz_type for hai in configuration.hais())\
            and Counter(hai_counter.values()) == Counter([0]*8+[1])\
            and configuration.hais().count(configuration.last_hai()) in (2, 4)

    @correspond_yaku(daisuushii)
    def is_daisuushii(configuration: Configuration):
        return set(Hai.kazehais()) == set(configuration.koutsu_or_kantsu_hais())\

    def tehai_yakuman(configuration: Configuration) -> list[Self]:
        """Yakumans that is applied only by the hais and do not rely on the bakyou"""

        yaku_checkers = (
            Yaku.is_daisangen,
            Yaku.is_suuankou,
            Yaku.is_tsuuiisou,
            Yaku.is_ryuuiisou,
            Yaku.is_chinroutou,
            Yaku.is_kokushimusou,
            Yaku.is_shousuushii,
            Yaku.is_suukantsu,
            Yaku.is_chuurenpoutou,
            Yaku.is_suuankou_tanki,
            Yaku.is_kokushi_13men_machi,
            Yaku.is_junsei_chuuren_poutou,
            Yaku.is_daisuushii,
        )

        return [Yaku(yaku_checker.corresponding_yaku) for yaku_checker in yaku_checkers if yaku_checker(configuration)]

    def is_tehai_yakuman(configuration: Configuration):
        return any(Yaku.tehai_yakuman(configuration))

    @correspond_yaku(tanyao)
    def is_tanyao(configuration: Configuration):
        return all(not hai.is_yaochuuhai() for hai in configuration.hais())

    @correspond_yaku(menzen_tsumo)
    def is_menzen_tsumo(configuration: Configuration):
        return configuration.is_menzen()\
            and configuration.last_hai_pos() == HaiPosition.tsumo

    @correspond_yaku(yakuhai_haku)
    def is_yakuhai_haku(configuration: Configuration):
        return Hai(5, "z") in configuration.koutsu_or_kantsu_hais()

    @correspond_yaku(yakuhai_hatsu)
    def is_yakuhai_hatsu(configuration: Configuration):
        return Hai(6, "z") in configuration.koutsu_or_kantsu_hais()

    @correspond_yaku(yakuhai_chun)
    def is_yakuhai_chun(configuration: Configuration):
        return Hai(7, "z") in configuration.koutsu_or_kantsu_hais()

    @correspond_yaku(iipeikou)
    def is_iipeikou(configuration: Configuration):
        shuntsu_counter = list(similar_mentsu_counter(configuration.shuntsus()).values())
        return configuration.is_menzen()\
            and (shuntsu_counter.count(2) == 1\
                or shuntsu_counter.count(3) == 1
                )

    @correspond_yaku(chankan)
    def is_chankan(configuration: Configuration):
        return configuration.last_hai_pos() == HaiPosition.kakan

    @correspond_yaku(akadora)
    def is_akadora(configuration: Configuration):
        return any(hai.aka for hai in configuration.hais())

    @correspond_yaku(akadora)
    def count_akadora(configuration: Configuration):
        return len([True for hai in configuration.hais() if hai.aka])

    @correspond_yaku(sanshoku_doukou)
    def is_sanshoku_doukou(configuration: Configuration):
        return list(Counter(hai.number for hai in configuration.koutsu_or_kantsu_hais() if hai.is_suupai()).values()).count(3) == 1

    @correspond_yaku(sankantsu)
    def is_sankantsu(configuration: Configuration):
        return len(configuration.kantsus()) == 3

    @correspond_yaku(toitoihou)
    def is_toitoihou(configuration: Configuration):
        return all(mentsu.is_koutsu_or_kantsu() for mentsu in configuration.mentsus())

    @correspond_yaku(sanankou)
    def is_sanankou(configuration: Configuration):
        return len([koutsu_or_kantsu for koutsu_or_kantsu in configuration.koutsus_or_kantsus() if koutsu_or_kantsu.is_ankou_or_ankan()]) == 3

    @correspond_yaku(shousangen)
    def is_shousangen(configuration: Configuration):
        return len(set(Hai.sangenpais()).intersection(configuration.koutsu_or_kantsu_hais())) == 2\
            and configuration.jantou.hais()[0].is_sangenpai()

    @correspond_yaku(honroutou)
    def is_honroutou(configuration: Configuration):
        return all(hai.is_routouhai() or hai.is_jihai() for hai in configuration.hais())

    @correspond_yaku(chiitoitsu)
    def is_chiitoitsu(configuration: Configuration):
        return configuration.is_chiitoi

    @correspond_yaku(chanta)
    def is_chanta(configuration: Configuration):
        return all(set(Hai.yaochuuhais()).intersection(mentsu.hais()) != set() for mentsu in configuration.mentsus())\
            and configuration.shuntsus() != []

    @correspond_yaku(ikkitsuukan)
    def is_ikkitsuukan(configuration: Configuration):
        mentsu_color_counter = Counter([mentsu.hais()[0].mpsz_type for mentsu in configuration.mentsus()])
        main_color, count = mentsu_color_counter.most_common(1)[0]
        ikkitsuukan_shuntsus = {
            Mentsu(MentsuType.tehai, [HaiWithPosition(1, main_color, HaiPosition.tehai), HaiWithPosition(2, main_color, HaiPosition.tehai), HaiWithPosition(3, main_color, HaiPosition.tehai)]),
            Mentsu(MentsuType.tehai, [HaiWithPosition(1, main_color, HaiPosition.tehai), HaiWithPosition(2, main_color, HaiPosition.tehai), HaiWithPosition(3, main_color, HaiPosition.tehai)]),
            Mentsu(MentsuType.tehai, [HaiWithPosition(1, main_color, HaiPosition.tehai), HaiWithPosition(2, main_color, HaiPosition.tehai), HaiWithPosition(3, main_color, HaiPosition.tehai)]),
            }

        return main_color != "z"\
            and all([any(mentsu.is_similar_to(ikkitsuukan_shuntsu) for mentsu in configuration.shuntsus())
                 for ikkitsuukan_shuntsu in ikkitsuukan_shuntsus])

    @correspond_yaku(sanshoku_doujun)
    def is_sanshoku_doujun(configuration: Configuration):
        return list(Counter(hai.number for hai in configuration.shuntsu_hais() if hai.is_suupai()).values()).count(3) == 1

    @correspond_yaku(ryanpeikou)
    def is_ryanpeikou(configuration: Configuration):
        shuntsu_counter = list(similar_mentsu_counter(configuration.shuntsus()).values())
        return configuration.is_menzen()\
            and shuntsu_counter.count(2) == 2

    @correspond_yaku(junchan)
    def is_junchan(configuration: Configuration):
        return all(set(Hai.routouhais()).intersection(mentsu.hais()) != set() for mentsu in configuration.mentsus())\
            and configuration.shuntsus() != []

    @correspond_yaku(honitsu)
    def is_honitsu(configuration: Configuration):
        colors = {hai.mpsz_type for hai in configuration.hais()}
        return len(colors) == 2 and "z" in colors

    @correspond_yaku(chinitsu)
    def is_chinitsu(configuration: Configuration):
        colors = {hai.mpsz_type for hai in configuration.hais()}
        return len(colors) == 1 and "z" not in colors

    def tehai_non_yakuman(configuration: Configuration) -> list[Self]:
        """Non-yakumans that is applied only by the hais and do not rely on the bakyou"""

        yaku_checkers = [
            Yaku.is_tanyao,
            Yaku.is_menzen_tsumo,
            Yaku.is_yakuhai_haku,
            Yaku.is_yakuhai_hatsu,
            Yaku.is_yakuhai_chun,
            Yaku.is_iipeikou,
            Yaku.is_chankan,
            Yaku.is_sanshoku_doukou,
            Yaku.is_sankantsu,
            Yaku.is_toitoihou,
            Yaku.is_sanankou,
            Yaku.is_shousangen,
            Yaku.is_honroutou,
            Yaku.is_chiitoitsu,
            Yaku.is_chanta,
            Yaku.is_ikkitsuukan,
            Yaku.is_sanshoku_doujun,
            Yaku.is_ryanpeikou,
            Yaku.is_junchan,
            Yaku.is_honitsu,
            Yaku.is_chinitsu,
        ]

        dora_checkers_with_counters = [
            (Yaku.is_akadora, Yaku.count_akadora),
        ]

        return [Yaku(yaku_checker.corresponding_yaku) for yaku_checker in yaku_checkers if yaku_checker(configuration)]\
            + sum([[Yaku(dora_checker.corresponding_yaku)] * dora_counter(configuration) for dora_checker, dora_counter in dora_checkers_with_counters if dora_checker(configuration)], [])

    def tehai_yaku(configuration: Configuration):
        """Yakus that is applied only by the hais and do not rely on the bakyou"""

        if Yaku.is_tehai_yakuman(configuration):
            return Yaku.tehai_yakuman(configuration)
        else:
            return Yaku.tehai_non_yakuman(configuration)

class Tehai:
    def __init__(self, non_naki_hais_with_pos: list[HaiWithPosition], nakis: list[Mentsu] = []):
        if len(non_naki_hais_with_pos) + 3*len(nakis) != 13:
            raise Exception("Invalid tehai")

        self.non_naki_hais_with_pos = non_naki_hais_with_pos
        self.nakis = nakis
        self.tsumo_hai_with_pos: HaiWithPosition | None = None

    def non_naki_hais(self):
        return [non_naki_hai_with_pos.hai for non_naki_hai_with_pos in self.non_naki_hais_with_pos]

    def every_hais(self):
        return self.non_naki_hais() + sum([naki.hais() for naki in self.nakis], [])

    def is_menzen(self):
        return self.nakis == []

    def is_tenpai(self):
        return self.agari_hais()

    def agari_hais(self):
        agari_hais = set()

        for hai in Hai.every_hais:
            if self.is_completed(hai.with_pos(HaiPosition.tehai)):
                if self.every_hais().count(hai) != 4:
                    agari_hais.add(hai)

        return agari_hais

    def is_completed(self, last_hai_with_pos: HaiWithPosition):
        return self.is_normal_completed(last_hai_with_pos) or self.is_chiitoi_completed(last_hai_with_pos) or self.is_kokushi_completed(last_hai_with_pos)

    def is_kokushi_completed(self, last_hai_with_pos: HaiWithPosition):
        entire_hais = self.every_hais() + [last_hai_with_pos.hai]
        return all(hai in Hai.yaochuuhais() for hai in entire_hais) and len(set(entire_hais)) == 13

    def is_chiitoi_completed(self, last_hai_with_pos: HaiWithPosition):
        entire_hais = self.every_hais() + [last_hai_with_pos.hai]
        return self.is_menzen() and all(entire_hais.count(hai) == 2 for hai in entire_hais)

    def is_normal_completed(self, last_hai_with_pos: HaiWithPosition):
        non_fixed_hais = self.non_naki_hais_with_pos + [last_hai_with_pos]
        return bool(filter_valid_normal_configurations(get_possible_jantou_and_mentsu_configurations(None, non_fixed_hais, last_hai_with_pos)))

    def possible_configurations(self, last_hai_with_pos: HaiWithPosition) -> list[Configuration]:
        non_fixed_hais_with_pos = self.non_naki_hais_with_pos + [last_hai_with_pos]

        if self.is_normal_completed(last_hai_with_pos):
            possible_jantou_and_mentsu_configurations = sorted(remove_duplicate_from([(jantou, sorted(mentsus)) for jantou, mentsus
                                                               in filter_valid_normal_configurations(get_possible_jantou_and_mentsu_configurations(None, non_fixed_hais_with_pos, last_hai_with_pos))]))

            return [Configuration(jantou, non_naki_mentsus, self.nakis, last_hai_with_pos) for jantou, non_naki_mentsus in possible_jantou_and_mentsu_configurations]
        elif self.is_chiitoi_completed():
            return [Configuration(None, [], [], last_hai_with_pos, non_fixed_hais_with_pos, True, False)]
        elif self.is_kokushi_completed():
            return [Configuration(None, [], [], last_hai_with_pos, non_fixed_hais_with_pos, False, True)]
        else:
            return []

    def tehai_yaku(self, last_hai_with_pos: HaiWithPosition):
        for possible_configuration in self.possible_configurations(last_hai_with_pos):
            return possible_configuration.tehai_yaku()

def filter_valid_normal_configurations(configurations: list[tuple[Jantou, list[Mentsu]]]):
    return [(jantou, mentsus) for jantou, mentsus in configurations
            if jantou and len(mentsus) == 4 and max(Counter(every_hais := jantou.hais() + sum([mentsu.hais() for mentsu in mentsus], [])).values()) <= 4]

def get_possible_jantou_and_mentsu_configurations(jantou: Jantou | None, non_fixed_hais_with_pos: list[HaiWithPosition], target_hai_with_pos: HaiWithPosition | None = None) -> list[tuple[Jantou, list[Mentsu]]]:
    if len(non_fixed_hais_with_pos) == 0:
        return []
    elif not jantou and len(non_fixed_hais_with_pos) == 2 and len(set(non_fixed_hais_with_pos)) == 1:
        return [(Jantou(non_fixed_hais_with_pos), [])]
    elif len(non_fixed_hais_with_pos) == 3:
        try:
            return [(jantou, [Mentsu(MentsuType.tehai, non_fixed_hais_with_pos)])]
        except:
            return []
    elif not (
        jantou and len(non_fixed_hais_with_pos) % 3 == 0
        or not jantou and len(non_fixed_hais_with_pos) % 3 == 2):
        raise Exception("Invalid non-fixed hais")

    non_fixed_hais_with_pos.sort()
    if not target_hai_with_pos:
        target_hai_with_pos = non_fixed_hais_with_pos[0]
    possible_jantou_and_mentsu_configurations = []
    if non_fixed_hais_with_pos.count(target_hai_with_pos) >= 3: # Check koutsu
        potential_mentsu_hais_with_pos = [
            strictly_extract(target_hai_with_pos, non_fixed_hais_with_pos),
            extract_similar_hai(target_hai_with_pos.hai, non_fixed_hais_with_pos),
            extract_similar_hai(target_hai_with_pos.hai, non_fixed_hais_with_pos),
            ]

        potential_fixed_mentsu = Mentsu(MentsuType.tehai, potential_mentsu_hais_with_pos)
        if (possible_remainder_mentsu_configurations := get_possible_jantou_and_mentsu_configurations(jantou, non_fixed_hais_with_pos[:])):
            possible_jantou_and_mentsu_configurations += [(jantou, [potential_fixed_mentsu] + mentsus) for jantou, mentsus in possible_remainder_mentsu_configurations]

        non_fixed_hais_with_pos += potential_mentsu_hais_with_pos # Undo

    if target_hai_with_pos.hai in Hai.suupais(): # Check shuntsu
        if 3 <= target_hai_with_pos.number <= 9 and check_similar_hai(Hai(target_hai_with_pos.number-2, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos) and check_similar_hai(Hai(target_hai_with_pos.number-1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos): # -2, -1, 0
            potential_mentsu_hais_with_pos = [
                strictly_extract(target_hai_with_pos, non_fixed_hais_with_pos),
                extract_similar_hai(Hai(target_hai_with_pos.number-2, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos),
                extract_similar_hai(Hai(target_hai_with_pos.number-1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos),
                ]

            potential_fixed_mentsu = Mentsu(MentsuType.tehai, potential_mentsu_hais_with_pos)

            if (possible_remainder_mentsu_configurations := get_possible_jantou_and_mentsu_configurations(jantou, non_fixed_hais_with_pos[:])):
                possible_jantou_and_mentsu_configurations += [(jantou, [potential_fixed_mentsu] + mentsus) for jantou, mentsus in possible_remainder_mentsu_configurations]

            non_fixed_hais_with_pos += potential_mentsu_hais_with_pos # Undo

        if 2 <= target_hai_with_pos.number <= 8 and check_similar_hai(Hai(target_hai_with_pos.number-1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos) and check_similar_hai(Hai(target_hai_with_pos.number+1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos): # -1, 0, +1
            potential_mentsu_hais_with_pos = [
                strictly_extract(target_hai_with_pos, non_fixed_hais_with_pos),
                extract_similar_hai(Hai(target_hai_with_pos.number-1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos),
                extract_similar_hai(Hai(target_hai_with_pos.number+1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos),
            ]

            potential_fixed_mentsu = Mentsu(MentsuType.tehai, potential_mentsu_hais_with_pos)

            if (possible_remainder_mentsu_configurations := get_possible_jantou_and_mentsu_configurations(jantou, non_fixed_hais_with_pos[:])):
                possible_jantou_and_mentsu_configurations += [(jantou, [potential_fixed_mentsu] + mentsus) for jantou, mentsus in possible_remainder_mentsu_configurations]

            non_fixed_hais_with_pos += potential_mentsu_hais_with_pos # Undo

        if 1 <= target_hai_with_pos.number <= 7 and check_similar_hai(Hai(target_hai_with_pos.number+1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos) and check_similar_hai(Hai(target_hai_with_pos.number+2, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos): # 0, +1, +2
            potential_mentsu_hais_with_pos = [
                strictly_extract(target_hai_with_pos, non_fixed_hais_with_pos),
                extract_similar_hai(Hai(target_hai_with_pos.number+1, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos),
                extract_similar_hai(Hai(target_hai_with_pos.number+2, target_hai_with_pos.mpsz_type), non_fixed_hais_with_pos),
            ]

            potential_fixed_mentsu = Mentsu(MentsuType.tehai, potential_mentsu_hais_with_pos)

            if (possible_remainder_mentsu_configurations := get_possible_jantou_and_mentsu_configurations(jantou, non_fixed_hais_with_pos[:])):
                possible_jantou_and_mentsu_configurations += [(jantou, [potential_fixed_mentsu] + mentsus) for jantou, mentsus in possible_remainder_mentsu_configurations]

            non_fixed_hais_with_pos += potential_mentsu_hais_with_pos # Undo

    if not jantou and non_fixed_hais_with_pos.count(target_hai_with_pos) >= 2: # Check jantou
        fixed_jantou = Jantou([
            non_strictly_extract(target_hai_with_pos, non_fixed_hais_with_pos),
            non_strictly_extract(target_hai_with_pos, non_fixed_hais_with_pos),
        ])
        possible_jantou_and_mentsu_configurations += get_possible_jantou_and_mentsu_configurations(fixed_jantou, non_fixed_hais_with_pos[:])


    return possible_jantou_and_mentsu_configurations

class Haiyama:
    def __init__(self, hais: list[Hai]):
        self.toncha_hais: list[Hai] = []
        self.nancha_hais: list[Hai] = []
        self.shaacha_hais: list[Hai] = []
        self.peicha_hais: list[Hai] = []

        for _ in range(3):
            self.toncha_hais += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]
            self.nancha_hais += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]
            self.shaacha_hais += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]
            self.peicha_hais += [hais.pop(0), hais.pop(0), hais.pop(0), hais.pop(0),]

        self.toncha_hais += [hais.pop(0), hais.pop(3)]
        self.nancha_hais += [hais.pop(0)]
        self.shaacha_hais += [hais.pop(0)]
        self.peicha_hais += [hais.pop(0)]

        self.rinshanpai = [hais.pop(), hais.pop(), hais.pop(), hais.pop()]
        self.dorahyoujihai = [hais[-2], hais[-4], hais[-6], hais[-8], hais[-10]]
        self.uradorahyoujihai = [hais[-1], hais[-3], hais[-7], hais[-9], hais[-11]]
        del hais[-11:-1]

        self.piipai = hais[:]

    def __repr__(self):
        return repr([self.toncha_hais, self.nancha_hais, self.shaacha_hais, self.peicha_hais, self.rinshanpai, self.dorahyoujihai, self.dorahyoujihai, self.uradorahyoujihai])

    def tsumo(self):
        return self.piipai.pop(0).with_pos(HaiPosition.tsumo)

    def random():
        hais = Hai.every_hai_quartets
        shuffle(hais)

        return Haiyama(hais)

def remove_duplicate_from(list: list):
    copy = []
    for element in list:
        if element not in copy:
            copy.append(element)

    return copy

def non_strictly_extract(target, list: list):
    return list.pop(list.index(target))

def strictly_extract(target, list: list):
    for i, element in enumerate(list):
        if element is target:
            return list.pop(i)

def extract_similar_hai(target_hai: Hai, hai_with_pos_list: list[HaiWithPosition]):
    for i, hai_with_pos in enumerate(hai_with_pos_list):
        if hai_with_pos.hai == target_hai:
            return hai_with_pos_list.pop(i)

def check_similar_hai(target_hai: Hai, hai_with_pos_list: list[HaiWithPosition]):
    for hai_with_pos in hai_with_pos_list:
        if hai_with_pos.hai == target_hai:
            return True

    return False






if __name__ == "__main__":
    pygame.init()

    class HashableRect:
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

        def __hash__(self):
            return hash((self.x, self.y, self.width, self.height))

        def collide_point(self, pos):
            return self.convert_to_rect().collidepoint(pos)

        def convert_to_rect(self):
            return pygame.Rect(self.x, self.y, self.width, self.height)





    image_for = {}
    for hai in set(Hai.every_hai_quartets):
        image_for[hai] = pygame.transform.scale(
            pygame.image.load(f"./images/{repr(hai)}.png")
            , (60, 90))

    haiyama = Haiyama.random()
    is_riichi = False
    first = True
    while True:
        if not first:
            if haiyama.piipai:
                tsumo_hai_with_pos = haiyama.tsumo()
            else:
                if my_tehai.is_tenpai():
                    print("ニャンパイ")
                else:
                    print("ノーテンにゃ")

                break
        else:
            my_tehai = Tehai([hai.with_pos(HaiPosition.tehai) for hai in haiyama.toncha_hais[:-1]])
            tsumo_hai_with_pos = haiyama.toncha_hais[-1].with_pos(HaiPosition.tsumo)

        my_tehai.tsumo_hai_with_pos = tsumo_hai_with_pos
        my_tehai.non_naki_hais_with_pos.sort()

        screen = pygame.display.set_mode((800,700))
        hai_with_pos_for_hashable_rect: dict[HashableRect, HaiPosition] = {}
        for i, hai_with_pos in enumerate(my_tehai.non_naki_hais_with_pos):
            (x, y) = (i*50, 0)
            rect = HashableRect(x, y, 60, 90)
            screen.blit(image_for[hai_with_pos.hai], (x, y))
            hai_with_pos_for_hashable_rect[rect] = hai_with_pos
        (x, y) = (i*50 + 70, 0)
        rect = HashableRect(x, y, 60, 90)
        screen.blit(image_for[tsumo_hai_with_pos.hai], (x, y))
        hai_with_pos_for_hashable_rect[rect] = tsumo_hai_with_pos
        pygame.display.update()

        if my_tehai.is_completed(tsumo_hai_with_pos):
            print("ツモにゃー！！！")
            last_hai_with_pos = tsumo_hai_with_pos

            for configuration in my_tehai.possible_configurations(last_hai_with_pos):
                print(configuration)
                print(configuration.tehai_yaku())
                print()
            break

        my_tehai.non_naki_hais_with_pos.append(tsumo_hai_with_pos)

        if is_riichi:
            kiru_hai_with_pos = strictly_extract(tsumo_hai_with_pos, my_tehai.non_naki_hais_with_pos)
        else:
            while True:
                kiru_yotei_no_hai_with_pos = None

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()

                    # https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
                    # handle MOUSEBUTTONUP
                    elif event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()

                        # get a list of all sprites that are under the mouse cursor
                        clicked_hais_with_pos = [
                            hai_with_pos for hashable_rect, hai_with_pos in hai_with_pos_for_hashable_rect.items()
                            if hashable_rect.collide_point(pos)]

                        # do something with the clicked sprites...
                        if len(clicked_hais_with_pos) == 1:
                            kiru_yotei_no_hai_with_pos = clicked_hais_with_pos[0]
                            break
                        else:
                            kiru_yotei_no_hai_with_pos = None

                    if kiru_yotei_no_hai_with_pos == None:
                        continue
                else:
                    continue

                kiru_hai_with_pos = strictly_extract(kiru_yotei_no_hai_with_pos, my_tehai.non_naki_hais_with_pos)
                break

        if my_tehai.is_tenpai() and not is_riichi:
            print("ダブルリーチにゃ！" if first else "リーチにゃ！")
            is_riichi = True
            print(sorted(list(my_tehai.agari_hais())))

        if first:
            first = False


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

# TODO
# 1. 손패 역 구현
# 2. 4인 구현
# 3. 울기 구현
# 4. 상황 역 구현
# 5. 통신 구현


