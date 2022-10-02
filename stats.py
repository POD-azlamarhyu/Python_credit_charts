from cmath import polar
import numpy as np
import matplotlib.pyplot as plt
import os
import japanize_matplotlib as jmp

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

if os.path.exists("./img/") is not True:
    os.mkdir("./img/")

for i in range(len(names)):
    val = np.array(values[i])
    
    radar_val = np.concatenate([val,[val[0]]])
    angles = np.linspace(0, 2*np.pi,len(index)+1,endpoint=True)
    
    fig = plt.figure(facecolor="w",figsize=(12,8))
    fig.suptitle(names[i], size=25,color="black")
    ax = fig.add_subplot(1,1,1,polar=True)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_rlim([0.0,5.0])
    ax.plot(angles,radar_val,"o-")
    ax.fill(angles,radar_val,alpha=0.2)
    ax.set_thetagrids(angles[:-1]*180/np.pi,index)
    
    plt.savefig("./img/chart_{}.png".format(filename[i]),format="png",dpi=450)
    
    
    