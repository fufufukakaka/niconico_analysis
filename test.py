# -*- coding: utf-8 -*-

from NiconicoSnapshotAPIWrapper import *

if __name__ == '__main__':
    api = NiconicoSnapshotAPIWrapper('NiconicoSnapshotAPIWrapper')#

    count = collections.Counter()

    data = u"""博麗霊夢
    霧雨魔理沙
    ルーミア
    大妖精
    チルノ
    紅美鈴
    小悪魔
    パチュリー・ノーレッジ
    十六夜咲夜
    レミリア・スカーレット
    フランドール・スカーレット
    レティ・ホワイトロック
    橙
    アリス・マーガトロイド
    リリーホワイト
    ルナサ・プリズムリバー
    メルラン・プリズムリバー
    リリカ・プリズムリバー
    魂魄妖夢
    西行寺幽々子
    八雲藍
    八雲紫
    伊吹萃香
    リグル･ナイトバグ
    ミスティア・ローレライ
    上白沢慧音
    因幡てゐ
    鈴仙・優曇華院・イナバ
    八意永琳
    蓬莱山輝夜
    藤原妹紅
    メディスン・メランコリー
    風見幽香
    小野塚小町
    四季映姫・ヤマザナドゥ
    射命丸文
    秋静葉
    秋穣子
    鍵山雛
    河城にとり
    犬走椛
    東風谷早苗
    八坂神奈子
    洩矢諏訪子
    永江衣玖
    比那名居天子
    キスメ
    黒谷ヤマメ
    水橋パルスィ
    星熊勇儀
    古明地さとり
    火焔猫燐
    霊烏路空
    古明地こいし
    ナズーリン
    多々良小傘
    雲居一輪
    雲山
    村紗水蜜
    寅丸星
    聖白蓮
    封獣ぬえ
    姫海棠はたて
    幽谷響子
    宮古芳香
    霍青娥
    蘇我屠自古
    物部布都
    豊聡耳神子
    二ッ岩マミゾウ
    秦こころ
    わかさぎ姫
    赤蛮奇
    今泉影狼
    九十九弁々
    九十九八橋
    鬼人正邪
    少名針妙丸
    堀川雷鼓
    綿月豊姫
    綿月依姫
    レイセン
    サニーミルク
    ルナチャイルド
    スターサファイア
    茨木華扇
    本居小鈴
    森近霖之助
    稗田阿求
    宇佐見蓮子
    マエリベリー・ハーン""".split()
    for word in data:
        time.sleep(1)
        count[word] = api.query(word, retry = 3, size = 0, filters=[api.makeFilterRange('start_time', '2014-01-01 00:00:00', '2014-12-31 23:59:59')]).total
    
    for word, freq in count.most_common(10):
        print word, freq