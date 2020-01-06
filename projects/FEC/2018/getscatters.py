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

def getscatters(orig_cand, committee, party = None):
    df_new = deepcopy(orig_cand)
    # no third party
    df_new = df_new[df_new['cand_pty_affiliation'] != 'Third party']
    # print(len(df_new))
    # subset that received from this committee
    all_ = list(set(df_new.loc[df_new[committee] > 0, 'contest']))
    df_new = df_new[df_new['contest'].apply(lambda x: x in all_)]
    # print(len(df_new))
    #
    keeps = []
    for contest in list(set(df_new['contest'])):
        lil_df = df_new[df_new['contest'] == contest]
        # print(len(lil_df))
        # there must be two candidates competing
        if (len(lil_df) == 2) & (len(lil_df['cand_pty_affiliation'].value_counts()) == 2):
            lil_cand = lil_df[lil_df[committee] > 0]
            # print(len(lil_cand))
            ptys = list(lil_cand['cand_pty_affiliation'].values)
            if not party:
                if ('Democrat' in ptys) & ('Republican' in ptys):
                    keeps.append(contest)
            elif party == 'rep':
                if ('Democrat' not in ptys) & ('Republican' in ptys):
                    keeps.append(contest)
            else:
                if ('Democrat' in ptys) & ('Republican' not in ptys):
                    keeps.append(contest)
    df_newest = df_new[df_new['contest'].apply(lambda x: x in keeps)]
    return df_newest
