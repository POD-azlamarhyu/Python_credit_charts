from cmath import polar
import numpy as np
import matplotlib.pyplot as plt
import os
import japanize_matplotlib as jmp
from tqdm import tqdm

def train_travel_card():
    values = [
        [4.0,3.5,3.0,4.5,3.0,4.0,4.5],
        [3.5,3.0,3.0,3.5,3.0,3.0,4.5],
        [4.0,3.0,3.0,2.5,1.0,3.5,3.5],
        [3.5,3.0,3.0,3.5,1.0,4.0,4.5],
        [4.0,3.5,3.0,4.5,3.0,4.0,4.5],
        [4.0,3.5,3.0,4.5,2.0,4.0,4.0],
        [4.5,3.5,3.0,4.0,3.0,3.0,3.5],
    ]

    index = [
        "カード汎用性",
        "還元率",
        "ステータス",
        "電子マネー",
        "ブランド選択肢",
        "ポイントの利用の汎用性",
        "旅行時の利便性"
    ]

    names = [
        "JREカード",
        "J-Westベーシックカード",
        "JQEPOSカード",
        "BIC CAMERA JQ SUGOCA エクスプレス",
        "View Suicaカード",
        "ビックカメラ Suica",
        "イオンSuicaカード"
    ]

    filename=[
        "JRE_card",
        "JWest_card",
        "JQEPOS_card",
        "biccamera_sugoca",
        "View_Suica",
        "Biccamera_Suica_card",
        "Aeon_suica_card"
    ]
    rgrids = [0,1,2,3,4,5]
    if os.path.exists("./img/") is not True:
        os.mkdir("./img/")

    for i in tqdm(range(len(names))):
        val = np.array(values[i])

        radar_val = np.concatenate([val,[val[0]]])
        angles = np.linspace(0, 2*np.pi,len(index)+1,endpoint=True)
        print(angles)

        print(angles)
        fig = plt.figure(facecolor="w",figsize=(16,9))
        ax = fig.add_subplot(1,1,1,polar=True)
        ax.plot(angles,radar_val,"o-")
        ax.fill(angles,radar_val,alpha=0.2)
        ax.set_rgrids([])
        
        # ax.set_rlim([-3.0, 3.0])
        # ax.set_rgrids(np.arange(-3, 3.01, 1),
        #           labels=abc,
        #           fontsize=12,
        #           angle=150) # angle で 表示方向を選択(度数法)

        # theta方向の設定
        ax.set_thetalim([0, 2*np.pi])
        # ラジアンではなく, 度数法で指定するっぽい
        ax.set_thetagrids(np.rad2deg(np.linspace(0, 2*np.pi, 8)[1:]), labels=index,fontsize=12)

        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.spines['polar'].set_visible(False)
        
        ax.set_rlabel_position(-10)        
        for grid_value in range(len(rgrids)):
            grid_values = [grid_value] * (len(index)+1)
            ax.plot(angles, grid_values, color="gray",  linewidth=0.6)
            # print(grid_value)
        
        for j in range(len(rgrids)):
            ax.text(x=0,y=rgrids[j],s=rgrids[j],fontsize=15)
        
        fig.suptitle(names[i], size=42,color="black")
        plt.savefig("./img/鉄道・旅行系/chart_{}.png".format(filename[i]),format="png",dpi=450)

def student_card():
    values = [
        [4.5,3.0,3.5,3.0,4.0,1.0,4.0],# DP
        [3.5,4.0,3.5,3.0,4.0,2.0,4.0],# NL
        [3.0,2.0,3.0,4.0,3.0,1.0,5.0],# Epos
        [5.0,2.0,5.0,2.0,3.0,4.0,3.0],# Rakuten
        [4.0,2.0,4.0,5.0,5.0,1.0,2.0],# lifeme
        [4.0,3.0,3.0,3.0,3.0,1.0,4.0],# jcb
        [3.5,2.0,4.0,3.0,5.0,2.0,3.5],# biccamera
    ]

    index = [
        "還元率",
        "ステータス",
        "ポイントの使いやすさ",
        "ポイント管理",
        "電子マネー",
        "ブランドの選択肢",
        "その他優待",
    ]

    names = [
        "三井住友 デビュープラス",
        "三井住友 NL",
        "Epos カード",
        "Rakuten カード",
        "Lifeme saison",
        "JCB W カード",
        "Biccamera Suica"
    ]

    filename=[
        "sumitomomitsui_dp",
        "sumitomomitsui_nl",
        "epos_card",
        "rakuten",
        "lifeme_saison",
        "jcb_w",
        "biccamera_suica_std"
    ]
    rgrids = [0,1,2,3,4,5]
    # coodi = [0,0,100,0,0,100,0]
    if os.path.exists("./img/") is not True:
        os.mkdir("./img/")

    if os.path.exists("./img/学生向け") is not True:
        os.mkdir("./img/学生向け/")

    for i in tqdm(range(len(names))):
        val = np.array(values[i])

        radar_val = np.concatenate([val,[val[0]]])
        angles = np.linspace(0, 2*np.pi,len(index)+1,endpoint=True)

        fig = plt.figure(facecolor="w",figsize=(16,9))
        ax = fig.add_subplot(1,1,1,polar=True)
        ax.plot(angles,radar_val,"o-")
        ax.fill(angles,radar_val,alpha=0.2)
        ax.set_rgrids([])
        ax.set_thetagrids(angles[:-1] * 180 / np.pi, index,fontsize=16)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.spines['polar'].set_visible(False)
        
        ax.set_rlabel_position(-10)        
        for grid_value in range(len(rgrids)):
            grid_values = [grid_value] * (len(index)+1)
            ax.plot(angles, grid_values, color="gray",  linewidth=0.6)
        for j in range(len(rgrids)):
            ax.text(x=0,y=rgrids[j],s=rgrids[j])
        
        fig.suptitle(names[i], size=42,color="black")
        plt.savefig("./img/学生向け/chart_{}.png".format(filename[i]),format="png",dpi=450)

def rader_chart():
    values = [
        [4.5,3.0,3.5,3.0,4.0,1.0,4.0],# DP
        [3.5,4.0,3.5,3.0,4.0,2.0,4.0],# NL
        [3.0,2.0,3.0,4.0,3.0,1.0,5.0],# Epos
        [5.0,2.0,5.0,2.0,3.0,4.0,3.0],# Rakuten
        [4.0,2.0,4.0,5.0,5.0,1.0,2.0],# lifeme
        [4.0,3.0,3.0,3.0,3.0,1.0,4.0],# jcb
        [3.5,2.0,4.0,3.0,5.0,2.0,3.5],# biccamera
    ]

    index = [
        "還元率",
        "ステータス",
        "ポイントの使いやすさ",
        "ポイント管理",
        "電子マネー",
        "ブランドの選択肢",
        "その他優待",
    ]

    names = [
        "三井住友 デビュープラス",
        "三井住友 NL",
        "Epos カード",
        "Rakuten カード",
        "Lifeme saison",
        "JCB W カード",
        "Biccamera Suica"
    ]

    filename=[
        "sumitomomitsui_dp",
        "sumitomomitsui_nl",
        "epos_card",
        "rakuten",
        "lifeme_saison",
        "jcb_w",
        "biccamera_suica_std"
    ]
    rgrids = [0,1,2,3,4,5]
    # coodi = [0,0,100,0,0,100,0]
    if os.path.exists("./img/") is not True:
        os.mkdir("./img/")

    if os.path.exists("./img/学生向け") is not True:
        os.mkdir("./img/学生向け/")

    for i in tqdm(range(len(names))):
        val = np.array(values[i])

        # radar_val = np.concatenate([val,[val[0]]])
        # angles = np.linspace(0, 2*np.pi,len(index)+1,endpoint=True)

        fig = plt.figure(facecolor="w",figsize=(16,9))
        ax = fig.add_subplot(1,1,1,polar=True)
        
        size = 1000
        x = np.concatenate([val,[val[0]]])
        y = np.linspace(0, 2*np.pi,len(index)+1,endpoint=True)
        
        ax.plot()
        
        fig.suptitle(names[i], size=42,color="black")
        plt.savefig("./img/学生向け/chart_{}.png".format(filename[i]),format="png",dpi=450)

def main():
    train_travel_card()
    # student_card()
if __name__ == "__main__":
    main()  