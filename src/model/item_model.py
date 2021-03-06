import re
from util.shelve_tool import item_at_map11


class Item(object):

    def __init__(self, name):
        self.name = name
        self.stats = item_at_map11.get_attr_from_item(name, 'stats')

    def get_item_dict(self):
        return item_at_map11.get_item_with_key(self.name)

    def update_champion(self, champion):
        for stat in self.stats.keys():
            fun = getattr(self, '_{0}'.format(stat), self._doNothing)
            para = self.stats[stat]
            fun(champion, para, stat)

    def _doNothing(self, champion, para, stat):
        print(stat, 'is requiring')

    def _FlatArmorMod(self, champion, para, stat):
        champion.armor += para

    def _FlatPhysicalDamageMod(self, champion, para, stat):
        champion.attackdamage += para

    def _PercentAttackSpeedMod(self, champion, para, stat):
        champion.attackspeed += champion.BAS * para

    def _FlatCritChanceMod(self, champion, para, stat):
        champion.crit += para

    def _FlatCritDamage(self, champion, para, stat):
        champion.critdamage += para

    def _FlatMovementSpeedMod(self, champion, para, stat):
        champion.movespeed += para

    def _FlatHPPoolMod(self, champion, para, stat):
        champion.hp += para

    def _FlatMagicDamageMod(self, champion, para, stat):
        champion.magicdamage += para

    def _FlatSpellBlockMod(self, champion, para, stat):
        champion.spellblock += para

    def _PercentLifeStealMod(self, champion, para, stat):
        champion.lifesteal_p += para

    def _PercentBonusArmorPenetration(self, champion, para, stat):
        champion.pbap += para

    def _FlatArmorPenetration(self, champion, para, stat):
        champion.fap += para
