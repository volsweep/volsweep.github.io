import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from copy import deepcopy
from matplotlib import font_manager as fm, rcParams
from matplotlib.lines import Line2D
from matplotlib.offsetbox import (
    AnnotationBbox,
    OffsetImage,
)

party_dict = {
    'Republican' : {
        'hex' : '#FF6661', 
        'mult' : 0,#0.3, 
        'party' : 'Republican',
    },
    'Democrat' : {
        'hex' : '#5494F7', 
        'mult' : 0,#-0.3, 
        'party' : 'Democrat',
    },
    'Third party' : {
        'hex' : '#15DCDC',
        'mult' : 0,
        'party' : 'Third party',
    }
}

vol_light = '#f8fbfc'
vol_dark = '#263C4D'

def scatterparty(plotdf_orig, title='plot'):
    plotdf = deepcopy(plotdf_orig)
    fig = plt.figure(figsize = (8, 8))

    # face/axis colors
    fig.patch.set_facecolor(vol_light)
    ax = fig.add_subplot(111)
    ax.patch.set_facecolor(vol_light)

    vol_dark_rcparams = [
        'patch.edgecolor',
        'grid.color',
        'text.color',
        'axes.labelcolor',
        'xtick.color',
        'ytick.color',
        'axes.edgecolor'
    ]

    for which in vol_dark_rcparams:
        plt.rcParams[which] = vol_dark

    font_dirs = ['../../css/fonts/for_matplotlib/', ]
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    font_list = fm.createFontList(font_files)
    fm.fontManager.ttflist.extend(font_list)

    plt.rcParams['font.family'] = 'DM Sans Medium'
    contests = list(set(plotdf.loc[plotdf['position'] == 'H', 'contest']))
    max_funding = plotdf.loc[plotdf['position'] == 'H', 'ttl_receipts'].max()/1.0E6
    for contest in contests:
        this_contest = plotdf[plotdf['contest'] == contest]
        winner = list(this_contest.loc[this_contest['winner_flag'] == 1, 'cand_pty_affiliation'].values)[0]
        winner_ici = list(this_contest.loc[this_contest['winner_flag'] == 1, 'cand_ici'].values)[0]
        if winner_ici == 'I':
            marker = 'o'
        else:
            marker = 'D'
        color = party_dict[winner]['hex']
        plt.scatter(
            list(this_contest.loc[this_contest['cand_pty_affiliation'] == 'Republican', 'ttl_receipts'].values)[0]/1.0E6,
            list(this_contest.loc[this_contest['cand_pty_affiliation'] == 'Democrat', 'ttl_receipts'].values)[0]/1.0E6,
            color = color,
            marker = marker,
            alpha = 0.65,
            s = 150,
        )
        plt.xlabel('Republican candidate\ntotal funds received ($MM)', fontsize = 16)
        plt.ylabel('Democratic candidate\ntotal funds received ($MM)', fontsize = 16)
        plt.xticks(fontsize = 12)
        plt.yticks(fontsize = 12)
        plt.xlim()
        plt.plot([0, max_funding], [0, max_funding], ls = '--', lw = 0.25, color = 'grey', alpha = 0.2)
        plt.title(
            title, 
            fontsize = 16, 
        )
        legend_elements = [
            mpatches.Patch(
                [0], 
                [0], 
                color=party_dict['Republican']['hex'], 
                label='Republican won',
                alpha = 0.85,
            ), 
            mpatches.Patch(
                [0], 
                [0], 
                color=party_dict['Democrat']['hex'], 
                label='Democrat won', 
                alpha = 0.85,
            ), 
            Line2D(
                [0], 
                [0], 
                marker='o', 
                color=vol_light, 
                label='Incumbent won', 
                markerfacecolor='#446d8c', 
                markersize=12,
                alpha = 0.85,
            ),
            Line2D(
                [0], 
                [0], 
                marker='D', 
                color=vol_light, 
                label='Challenger won', 
                markerfacecolor='#446d8c', 
                markersize=12,
                alpha = 0.85,
            ),   
            Line2D(
                [0], 
                [0], 
                color='grey', 
                label='Equal funds', 
                alpha = 0.85
            ),
        ]
        legend = plt.legend(
            loc='lower right', 
            fontsize=14, 
            facecolor='#f8fbfc', 
            handles=legend_elements,
        )
            # source citation
        x = ax.annotate('Sources: Ballotpedia, FEC.gov', 
                        xy=(0.0, 0.0), 
                        xytext=(69.0, -28.0), 
                        ha='center', 
                        va='bottom', 
                        textcoords='axes pixels', 
                        xycoords='axes pixels',
                        alpha = 0.85,
                       )
        # logo
        arr_img = plt.imread('../../assets/VOL_Logo_Color_Light_Green.png')
        imagebox = OffsetImage(arr_img, zoom=0.07)
        imagebox.image.axes = ax
        xy = (0.0, -45.0)
        ab = AnnotationBbox(imagebox, 
                            xy,
                            xybox=(xy[0], xy[1]),
                            xycoords='axes pixels',
                            boxcoords=('axes pixels'),
                            box_alignment=(0., 0.),
                            frameon=False,
                           )
        ax.add_artist(ab)
        plt.tight_layout()
    plt.show();
    return
