import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

from copy import deepcopy
from datetime import datetime as dt
from matplotlib import font_manager as fm, rcParams
from matplotlib.lines import Line2D
from matplotlib.offsetbox import (
    AnnotationBbox,
    OffsetImage, 
)

# plotting function
def show_lineups(
    dataframe, 
    position, 
    count=1000, 
    uncontested=True,
    figsize=(9, 3), 
    title='2018 U.S. Congressional Elections',
    incl_incumb=True,
    yticks=[],
    ylabel='State_district',
    sort_by=['ttl_receipts'],
    ascending=[False],
    
):
    # plot settings per party
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

    if type(position) == str:
        this_dataframe = dataframe[dataframe['position'] == position]
    else:
        this_dataframe = pd.DataFrame()
        for which in position:
            new_df = dataframe[dataframe['position'] == which]
            this_dataframe = pd.concat([this_dataframe, new_df], axis = 0, sort = True)
        this_dataframe.drop_duplicates(keep = 'first', inplace = True)
        this_dataframe.reset_index(drop = True, inplace = True)

    this_dataframe.sort_values(sort_by, ascending = ascending, inplace = True)

    this_dataframe['ttl_receipts'] = this_dataframe['ttl_receipts']/1.0E6
    
    if not uncontested:
        solos = list(this_dataframe['contest'].value_counts()\
                     [this_dataframe['contest'].value_counts() == 1].index)
        for which in solos:
            this_dataframe = this_dataframe[this_dataframe['contest'] != which]
            
    allcontests = this_dataframe.drop_duplicates(['contest'], keep = 'first')['contest'].values
    
    try:
        contests = allcontests[:count][::-1]
    except:
        contests = allcontests[::-1]

    vol_light = '#f8fbfc'
    vol_dark = '#263C4D'
    
    fig = plt.figure(figsize = figsize)
    
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
    
    for party in ['Third party', 'Democrat', 'Republican']:

        lil_dataframe = this_dataframe[this_dataframe['cand_pty_affiliation'] == party]
        
        data = [lil_dataframe.loc[lil_dataframe['contest'] == contest, 
                                  'ttl_receipts'].values for contest in contests]
        
        incumbents = [lil_dataframe.loc[lil_dataframe['contest'] == contest, 
                                    'cand_ici'].values for contest in contests]
        
        winners = [lil_dataframe.loc[lil_dataframe['contest'] == contest, 
                                    'winner_flag'].values for contest in contests]

        for i in range(len(data)):
            x = data[i]
            y = [i*2.0+0.4*party_dict[party]['mult']]*len(data[i])
            for j in range(len(data[i])):
                if incumbents[i][j] == 'I':
                    marker = 'o'
                    if winners[i][j] == 1:
                        facecolors = party_dict[party]['hex']
                    else:
                        facecolors = 'none'
                    plt.scatter(
                        x[j], 
                        y[j], 
                        color=party_dict[party]['hex'],
                        marker=marker,
                        facecolors=facecolors,
                        s=50,
                        alpha=0.85,

                    ) 
                elif incumbents[i][j] == 'C':
                    marker = 'D'
                    if winners[i][j] == 1:
                        facecolors = party_dict[party]['hex']
                    else:
                        facecolors = 'none'
                    plt.scatter(
                        x[j], 
                        y[j], 
                        color=party_dict[party]['hex'],
                        marker=marker,
                        facecolors=facecolors,
                        s=50,
                        alpha=0.85,

                    )
                else:
                    marker = '+'
                    if winners[i][j] == 1:
                        lw = 3
                    else:
                        lw = None
                    plt.scatter(
                        x[j], 
                        y[j], 
                        color=party_dict[party]['hex'],
                        marker=marker,
                        lw=lw,
                        s=50,
                        alpha=0.85,

                    )

    if yticks == True:
        if incl_incumb == True:
            to_add = []
            for contest in contests:
                lil_df = dataframe.loc[(dataframe['contest'] == contest) & (dataframe['cand_ici'] == 'I'), 
                                'cand_pty_affiliation'].values
                if len(lil_df) == 0:
                    to_add.append('open')
                else:
                    to_add.append(lil_df[0][0])
        finalcontests = [contests[i] for i in range(len(contests))]
        if ylabel == 'State':
            finalcontests = [x.replace('_senate', '') for x in finalcontests]

        plt.yticks(
            range(0, len(contests) * 2, 2), 
            finalcontests, 
            fontsize = 12, 
            fontname = 'DM Sans Medium'
        )
    else:
        plt.yticks(
            range(0, len(contests) * 2, 2), 
            yticks, 
            fontsize = 12, 
            fontname = 'DM Sans Medium'
        )
        
    legend_elements = [
        mpatches.Patch(
            [0], 
            [0], 
            color=party_dict['Republican']['hex'], 
            label='Republican'
        ), 
        mpatches.Patch(
            [0], 
            [0], 
            color=party_dict['Democrat']['hex'], 
            label='Democrat', 
        ), 
        mpatches.Patch(
            [0], 
            [0], 
            color=party_dict['Third party']['hex'], 
            label='Third party', 
        ),
        Line2D(
            [0], 
            [0], 
            marker='o', 
            color=vol_light, 
            label='Incumbent', 
            markerfacecolor='#446d8c', 
            markersize=9,
        ),
        Line2D(
            [0], 
            [0], 
            marker='D', 
            color=vol_light, 
            label='Challenger', 
            markerfacecolor='#446d8c', 
            markersize=9,
        ),        
        Line2D(
            [0], 
            [0], 
            marker='P', 
            color=vol_light, 
            label='Open seat', 
            markerfacecolor='#446d8c', 
            markersize=9,
        ), 
        Line2D(
            [0], 
            [0], 
            color=vol_light, 
            label='(winners bolded/\nfilled in)', 
        ),
    ]
    legend = plt.legend(
        loc='lower right', 
        fontsize=12, 
        facecolor='#f8fbfc', 
        handles=legend_elements,
    )
    plt.title(title, fontsize = 16, fontname = 'DM Sans Medium', color='#263C4D')
    plt.ylim(-2, len(contests)*2)
    plt.ylabel(ylabel, fontsize = 16, fontname = 'DM Sans Medium')
#     if len(this_dataframe) > 10:
#         x_factor = 1.1
#     else:
#         x_factor = 1.5
    x_factor = 1.5
    plt.xlim(
        [
            -0.1*this_dataframe['ttl_receipts'].max(), 
            x_factor*this_dataframe['ttl_receipts'].max(),
        ]
    )
    plt.xlabel('Total funds received ($MM)', fontsize = 16, fontname = 'DM Sans Medium')

    # source citation
    x = ax.annotate('Sources: Ballotpedia, FEC.gov', 
                    xy=(0.0, 0.0), 
                    xytext=(69.0, -28.0), 
                    ha='center', 
                    va='bottom', 
                    textcoords='axes pixels', 
                    xycoords='axes pixels',
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
    
    plt.axvline(0, lw=1, color=vol_dark, alpha=0.2)
    if len(contests) > 1:
        for i in np.arange(-1, 2 * len(data) + 1, 2):
            plt.axhline(i, lw=1.5, ls=':', color=vol_dark, alpha=0.2)
            
    switch = False
    poss_vert = [10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01, 0.005, 0.0025, 0.001, 0.0005]
    while switch == False:
        for i in poss_vert:
            v_count = int(x_factor*this_dataframe['ttl_receipts'].max()/i)
            if v_count < 5:
                continue
            else:
                for j in range(1, v_count + 1):
                    plt.axvline(j*i, lw=1, ls='--', color=vol_dark, alpha=0.1)
                plt.xticks(np.arange(0, i*(v_count + 1), i), fontsize = 12, fontname = 'DM Sans Medium')
                switch = True
                break
    
    plt.show();
    
    return
