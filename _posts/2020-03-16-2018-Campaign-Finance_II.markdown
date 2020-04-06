---
layout: post
title: "2018 Campaign Finance, Part II: A closer look"
date: 2020-03-16 16:00:00 -0400
comments: true
category: blog
tags: ["FEC", "campaign finance", "2018 elections", "data science", "EDA"]
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*TL;DR We continue our investigation of FEC campaign finance data. Observations & analyses in this post include:*

* *candidates linked to more committees than average,*
* *treasurers associated with very large numbers of committees,*
* *committees making highest total independent expenditures,*
* *who's receiving the independent expenditures and for what,*
* *visual representation of finances for opposing candidates, and more.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Do you have domain knowledge of campaign finance regulations? I don't and would love to discuss. Please email contact@volsweep.com. General comments section at the bottom. See notebook links for full outputs too long to include here. Cheers, thanks for reading! &#8212;Rebecca*


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The &#8594;[first post](https://blog.volsweep.com/blog/2019/12/12/2018-Campaign-Finance_I.html)&#8592; in this series was an overview of trends and exceptions in Congressional midterm contests with respect to party affiliation, incumbency status, and relative funding status. (Recap: incumbents usually lead in fundraising and win. There appear to be some patterns in the exceptions.) This post will be a more in-depth look at the full set of data that the FEC publishes.[^1] As before, all relevant code is in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018)&#8592; GitHub repo.[^2]


### Data Set 1: "House/Senate current campaigns"
> (notebook &#8594;[here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/01b%20-%202018_HouseSenateCurrentCampaigns_withwinners.ipynb)&#8592;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one candidate ID per row. We used this data set to construct the plots in the first post of this series, where we showed candidate fundraising status by contest and compared opponents. We know from this set the following breakdown of the top three contest "types" for each branch of Congress (compared close to election day):

*Senate contests*
* 58.8% had a Democratic incumbent ahead in fundraising,
* 8.8% had a Republican incumbent ahead in fundraising,
* 8.8% had a Republican challenger ahead in fundraising.

*House contests*
* 30.8% had a Republican incumbent ahead in fundraising,
* 24.0% had a Democratic incumbent ahead in fundraising,
* 14.6% had a Democratic incumbent running unopposed.


### Data set 2: "Candidate-committee linkages"
> (notebook &#8594;[here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/02a%20-%202018_CandidateCommitteeLinkages_clean.ipynb)&#8592;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one row per candidate-committee pairing (note that it does not contain committees that are not linked to candidates). You can see the ones linked to at least three candidates, including candidate info, by searching "list starts here" on &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/03a%20-%202018_CommitteeMaster_clean.ipynb)&#8592; page. The following candidates are linked to more than ten committees each: Tammy Baldwin, Sherrod Brown, Joe Donnelly, Heidi Heitkamp, Amy Klobuchar, Claire McCaskill, Bill Nelson, Jacky Rosen, Debbie Stabenow, and Jon Tester.


### Data set 3: "Committee master"
> (notebook &#8594;[here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/03a%20-%202018_CommitteeMaster_clean.ipynb)&#8592;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one row per committee. After deduplicating several columns, we found there are some treasurers associated with large numbers of committees, and some addresses associated with large numbers of committees. (A reminder that this is the low end count because committees linked to candidates not appearing on final ballots were removed during cleaning.) Here are some examples (committee counts in parentheses; only treasurers with two or more associated committees shown):

_Example #1_<br/>
**Address:** 228 S Washington St, Alexandria, VA 22314 (156)<br/>
**Treasurers:** Lisa Lisker (74), Keith Davis (37), and David Satterfield (36)<br/>

_Example #2_<br/>
**Address:** 918 Pennsylvania Ave SE, Washington, DC 20003 (112)<br/>
**Treasurers:** Judith Zamore (97), Kristin Solander (3), Ellen Tauscher (2), Megan Mielnik (2)<br/>

_Example #3_<br/>
**Address:** 824 S Milledge Ave, Athens, GA 30605 (101)<br/>
**Treasurers:** Paul Kilgore (96), Michael Goode (2), Megan Brown (2)<br/>

_Example #4_<br/>
**Address:** PO Box 26141, Alexandria, VA 22313 (95)<br/>
**Treasurers:** Christopher Marston (85), Brenda Hankins (4), (no treasurer listed) (2)<br/>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search the phrase, "look here," in the &#8594;[notebook](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/03a%20-%202018_CommitteeMaster_clean.ipynb)&#8592; for full lists of committee names by address and treasurer.


### Data set 4: "Contributions from committees to candidates & independent expenditures"
> (lot of notebooks for this one! click on any: &#8594;[here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/04ai%20-%202018_CommitteeContributions_clean_withwinner.ipynb), [here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/04aii%20-%202018_CommitteeContributions_clean_withwinner.ipynb), [here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/04bi%20-%202018_CommitteeContributions_EDA1.ipynb), [here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/04bii%20-%202018_CommitteeContributions_EDA1.ipynb), and [here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/04bii%20-%202018_CommitteeContributions_EDA2.ipynb)&#8592;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution/independent expenditure (IE from now on) per row.[^3] The different types of contributions/independent expenditures are:

* "contribution made to nonaffiliated committee,"
* "independent expenditure advocating election of candidate,"
* "independent expenditure opposing election of candidate,"
* "in-kind contribution made to registered filer,"
* "coordinated party expenditure,"
* "election recount disbursement,"
* "communication cost against candidate (only for Form 7 filer)."

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Some observations from the cleaning process: Invenergy PAC made 691 contributions and/or independent expenditures with no date given (only 3 additional had a date). Embraer Aircraft Holding Inc PAC made 154 contributions and/or independent expenditures with no date given. The Democratic Senatorial Campaign Committee (DSCC) received $306,644 total in contributions with no individuals' names given. The National Republican Senatorial Committee (NRSC) received $294,519 total in contributions with no individuals' names given.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 1 shows one dot per committee (mostly political action committees, or PACs) which made IE(s). The following spent at least $10 million with respect to either Republican-affiliated candidates, Democratic-affiliated candidates, or both (total amount in parentheses):

* Congressional Leadership Fund ($125MM),
* SMP ($108MM),
* Senate Leadership Fund ($86MM),
* DCCC ($79MM)
* NRCC ($69MM),
* House Majority PAC ($59MM),
* NRSC ($42MM),
* Majority Forward ($40MM),
* DSCC ($40MM),
* Independence USA PAC ($38MM),
* New Republican PAC ($31MM),
* Priorities USA Action ($27MM),
* America First Action, Inc. ($26MM),
* Women Vote! ($24MM),
* DefendArizona ($16MM),
* LCV Victory Fund ($14MM),
* End Citizens United ($11MM).


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 1

![PAC independent expenditures Republican vs Democrat]({{ site.url }}/assets/FECpt2/committees_log.png)  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We see from the plot that most committees make IEs totaling from around $1,000 to $1,000,000. The committees seem to be spending with respect to candidates affiliated with both major parties, although not always on the same order of magnitude. (Note: This plot does not distinguish between IEs advocating vs opposing.) We also see that committees represented by yellower dots made IEs with respect a large number of candidates (100 or more).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now, let's look at where these IEs are going. Each plot below represents, per recipient (i.e., the 'to' in each plot title), IEs advocating and/or opposing candidates. Each plot symbol represents one candidate. It's not immediately apparent, but the plots are sorted in decreasing order of total IE dollars received, from upper left corner to lower right corner (we left some out, go to notebook for full list & plots). Discussion below.

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 2: Waterfront Strategies</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/ie_WaterfrontStrategies.png">
      <img alt="Waterfront Strategies" src="{{ site.url }}/assets/FECpt2/ie_WaterfrontStrategies.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 3: Nebo Media</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/ie_NeboMedia.png">
      <img alt="Nebo Media" src="{{ site.url }}/assets/FECpt2/ie_NeboMedia.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 4: Del Ray Media</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/ie_DelRay.png">
      <img alt="Del Ray Media Group" src="{{ site.url }}/assets/FECpt2/ie_DelRay.png" style="width: 100%">
    </a>
  </div>
</div>

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 5: Bully Pulpit Interactive</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/ie_BullyPulpitInteractive.png">
      <img alt="Bully Pulpit Interactive" src="{{ site.url }}/assets/FECpt2/ie_BullyPulpitInteractive.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 6: SKDKnickerbocker</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/ie_SKDKnickerbocker.png">
      <img alt="SKDK" src="{{ site.url }}/assets/FECpt2/ie_SKDKnickerbocker.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 7: Facebook</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/ie_Facebook.png">
      <img alt="Facebook" src="{{ site.url }}/assets/FECpt2/ie_Facebook.png" style="width: 100%">
    </a>
  </div>
</div>


**Waterfront Strategies**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Waterfront Strategies has no direct online presence. It received at least $246MM in IEs. As you can see in the plot, the advocating vs opposing split is highly partisan, with about 10% of IEs advocating Democratic-affiliated candidates (many of whom were challengers) and about 90% of IEs opposing Republican-affiliated candidates. Those three Democratic-affiliated incumbents standing out on the right (blue circles) are Bill Nelson ($7.1MM), Joe Manchin III ($4.6MM), and Joe Donnelly ($2.7MM). The largest total IEs to Waterfront Strategies came from SMP ($96.9MM), House Majority PAC ($49.7MM), Majority Forward ($39.5MM), and Women Vote! ($18.8MM).


**Nebo Media**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nebo Media doesn't have a direct online presence, either. It received at least $112.7MM in IEs, the vast majority of it from the Congressional Leadership Fund (over $112MM). Almost 95% of the total IE dollar amount Nebo Media received went toward opposing candidates. Looking at the plot, the IEs _advocated_ Republican-affiliated candidates (mostly incumbents) and _opposed_ mostly Democratic-affiliated challengers. Interestingly, some Republican-affiliated candidates were opposed; they are Young Kim, Rodney Davis, and Dana Rohrabacher, who were all opposed by the Congressional Leadership Fund.


[**Del Ray Media**](http://delraymediabuying.com/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Del Ray Media has a very minimal &#8594;[online presence](http://delraymediabuying.com/)&#8592;. It received almost $54.4MM in IEs, 98% of which was in opposition to candidates. We see in the plot that there are three Republican-affiliated candidates advocated, whereas almost all the opposed candidates are Democratic-affiliated challengers. The IEs came from NRCC ($49.5MM) and NRSC ($4.8MM).


[**Bully Pulpit Interactive**](https://bpimedia.com/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bully Pulpit Interactive (BPI) has a pretty strong &#8594;[online presence](https://bpimedia.com/)&#8592;. It received $41.7MM in IEs, $26.7MM of which came from Priorities USA Action. Other big spenders included Independence USA PAC ($5.9MM), NextGen Climate Action Committee ($3.9MM), Human Rights Campaign Equality Votes ($1.7MM), and LCV Victory Fund ($1.4MM). About 35% of IE dollars to BPI advocated candidates, and about 65% opposed. The U.S. Senate Florida contest saw a lot of IEs flowing to BPI, mostly from Priorities USA Action, with $4.5MM advocating incumbent Bill Nelson and $5.9MM opposing Rick Scott.


[**SKDKnickerbocker**](https://www.skdknick.com/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8594;[SKDKnickerbocker](https://www.skdknick.com/)&#8592; received about $30.5MM in IEs, the overwhelming majority of which came from Independence USA PAC ($25.4MM). Others who made large IEs to SKDKnickerbocker are the Environmental Defense Action Fund ($1.5MM), LCV Victory Fund ($1.4MM), and Everytown for Gun Safety Victory Fund ($724K). Interestingly, Everytown for Gun Safety Victory Fund made a very large number of $851 IEs to SKDKnickerbocker in opposition of candidates. Looking at the plot, the Republican-affiliated incumbent in the middle stands out; this is Randy Hultgren, who had Independence USA PAC spend about $460K opposing him and $19K advocating him. Otherwise the plot is very partisan, with most advocating IEs made with respect to Democratic-affiliated challengers and most opposing IEs made with respect to Republican-affiliated incumbents.


[**Facebook**](https://www.facebook.com/gpa)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#8594;[Facebook, Inc.](https://www.facebook.com/gpa)&#8592;, received about $4.4MM in IEs, mostly from MoveOn.org Political Action ($2.7MM). Just over 80% of the total IE dollars to Facebook advocated candidates and the rest opposed. As you can see from the plot, proportionately more candidates had IEs both advocating and opposing them than in other plots we've just seen (i.e., the center of the plot is crowded).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The lefthand plots two sections down were constructed using this section's data set but are presented where they are in order to allow side-by-side comparisons.


### Data set 5: "Any transaction from one committee to another"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We took the subset of this data set containing any transfer to a principal campaign committees. The righthand plots in the next section were constructed using this data set.


### Data set 6: "Contributions by individuals"
> (notebook &#8594;[here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/05a%20-%202018_IndividualContributions_clean1.ipynb)&#8592;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution from an individual per row. We had to do a lot of cleaning in this set in particular. Any names containing "anonymous", "unitemized", and/or anything like "hat pass" we switched to simply "Anonymous." The FEC rules state:

> *"An anonymous contribution of cash is limited to $50. Any amount in excess of $50 must be promptly disposed of and may be used for any lawful purpose unrelated to any federal election, campaign or candidate." [^4][^5]*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This doesn't seem to be the case, as $246,892 total across two contributions to Composition Roofers Local Union #30 PAC and $54,458 total across two contributions to Association for Firefighters PAC. These appear to be above the limits allowed by the FEC.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Some individual contributors make many small contributions and others make a few extremely large ones. Here are the 40 donors with the highest contribution totals (in parentheses) and any summed amounts over $1MM shown itemized:

* Michael R Bloomberg ($85.9MM)
  * Independence USA PAC &#8212; $54.3MM
  * SMP &#8212; $20MM
  * LCV Victory Fund &#8212; $5MM
  * Women Vote! &#8212; $1.96MM
  * VoteVets &#8212; $1.5MM
  * Planned Parenthood Votes &#8212; $1.5MM

<br/>
* Thomas F Steyer ($65.7MM)
  * NextGen Climate Action Committee &#8212; $52.4MM
  * Need to Impeach &#8212; $12.1MM

<br/>
* Sheldon G Adelson ($61.9MM)
  * Congressional Leadership Fund &#8212; $27.5MM
  * Senate Leadership Fund &#8212; $25MM
  * America First Action, Inc. &#8212; $5MM
  * New Republican PAC &#8212; $2.5MM
  * ESAFund &#8212; $1MM

<br/>
* Miriam O Adelson ($61.7MM)
  * Congressional Leadership Fund &#8212; $27.5MM
  * Senate Leadership Fund &#8212; $25MM
  * America First Action, Inc. &#8212; $5MM
  * New Republican PAC &#8212; $2.5MM
  * ESAFund &#8212; $1MM  

<br/>
* Richard Uihlein ($34.8MM)
  * Restoration PAC &#8212; $8.20MM
  * Americas PAC &#8212; $5.4MM
  * Solutions for Wisconsin &#8212; $4.4MM
  * Club for Growth Action &#8212; $3.2MM
  * CFG Action Wisconsin &#8212; $2.5MM
  * Tea Party Patriots Citizens Fund &#8212; $2MM
  * CFG Action Missouri &#8212; $2MM

<br/>
* Selwyn Donald Sussman ($24.5MM)
  * Priorities USA Action &#8212; $6.45MM
  * SMP &#8212; $5.25MM
  * House Majority PAC &#8212; $4.75MM
  * Women Vote! &#8212; $2.8MM
  * Democratic Grassroots Victory Fund &#8212; $1.6MM
  * Win Justice &#8212; $1.1MM

<br/>
* Kenneth C Griffin ($19.4MM)
  * New Republican PAC &#8212; $10MM
  * Congressional Leadership Fund &#8212; $4.5MM
  * DefendArizona &#8212; $2MM
  * Future45 &#8212; $1MM

<br/>
* James Harris Simons ($19.4MM)
  * House Majority PAC &#8212; $10MM
  * SMP &#8212; $6.8MM

<br/>
* George Soros ($17.4MM)
  * Priorities USA Action &#8212; $5MM
  * Win Justice &#8212; $5MM
  * SMP &#8212; $3.4MM

<br/>
* Stephen A Schwarzman ($12.7MM)
  * Senate Leadership Fund &#8212; $8MM
  * Congressional Leadership Fund &#8212; $3.8MM

<br/>
* Fred J Eychaner ($11.4MM)
  * SMP &#8212; $6MM
  * House Majority PAC &#8212; $4MM

<br/>
* Jeffrey P Bezos ($10.2MM)
  * With Honor Fund, Inc &#8212; $10.1MM

<br/>
* Timothy Mellon ($10.1MM)
  * Congressional Leadership Fund &#8212; $10MM

<br/>
* George M Marcus ($9.7MM)
  * House Majority PAC &#8212; $5MM
  * SMP &#8212; $3MM

<br/>
* Reid G Hoffman ($8.5MM)
  * House Majority PAC &#8212; $3.1MM
  * SMP &#8212; $2MM
  * Forward Majority Action &#8212; $1MM

<br/>
* Charles R Schwab ($8.1MM)
  * Congressional Leadership Fund &#8212; $3.25MM
  * Senate Leadership Fund &#8212; $2MM
  * Future45 &#8212; $1MM

<br/>
* Karla T Jurvetson ($7.8MM)
  * Women Vote! &#8212; $5.4MM
  * SMP &#8212; $1.1MM

<br/>
* Jeffrey S Yass ($7.6MM)
  * Club for Growth Action &#8212; $3.8MM
  * Protect Freedom Political Action Committee Inc &#8212; $1.8MM

<br/>
* Bernard Marcus ($7.2MM)
  * Senate Leadership Fund &#8212; $4MM

<br/>
* Seth A Klarman ($6.9MM)
  * House Majority PAC &#8212; $2.5MM
  * SMP &#8212; $1.5MM

<br/>
* Helen O Schwab ($6.8MM)
  * Congressional Leadership Fund &#8212; $3MM
  * Senate Leadership Fund &#8212; $2MM
  * Future45 &#8212; $1MM

<br/>
* Joshua Bekenstein ($6.6MM)
  * House Majority PAC &#8212; $1.55MM
  * LCV Victory Fund &#8212; $1.5MM
  * SMP &#8212; $1.5MM

<br/>
* Ronald Cameron ($6.4MM)
  * Americans for Prosperity Action Inc (AFP Action) &#8212; $3MM
  * Senate Leadership Fund &#8212; $1MM
  * Congressional Leadership Fund &#8212; $1MM

<br/>
* Dustin A Moskovitz ($5.7MM)
  * MoveOn.org Political Action &#8212; $3MM
  * SMP &#8212; $2MM

<br/>
* Shiva Ayyadurai ($4.8MM)
  * Shiva 4 Senate &#8212; $4.8MM

<br/>
* Herbert Sandler ($4.8MM)
  * SMP &#8212; $2.25MM
  * PowerPACPlus &#8212; $1.85MM

<br/>
* Charles B Johnson ($4.6MM)
  * Congressional Leadership Fund &#8212; $2.15MM
  * Senate Leadership Fund &#8212; $1.3MM

<br/>
* Geoffrey H Palmer ($4.6MM)
  * America First Action, Inc. &#8212; $4MM

<br/>
* Marlene M Ricketts ($4.1MM)
  * ESAFund &#8212; $1.8MM
  * Future45 &#8212; $1.2MM

<br/>
* Dianne Feinstein ($3.5MM)
  * Feinstein for Senate 2024 &#8212; $3.5MM

<br/>
* Cynthia Simon-Skjodt ($3.5MM)
  * SMP &#8212; $2.5MM
  * House Majority PAC &#8212; $1MM

<br/>
* Marilyn Hawrys Simons ($3.2MM)
  * SMP &#8212; $1.35MM

<br/>
* Alexander G Soros ($2.9MM)
  * SMP &#8212; $2MM

<br/>
* Abigail S Wexner ($2.7MM)
  * With Honor Fund Inc. &#8212; $2.5MM

<br/>
* Henry B Laufer ($2.7MM)
  * SMP &#8212; $2MM

<br/>
* Seth W MacFarlane ($2.7MM)
  * SMP &#8212; $2.25MM

<br/>
* Mary A Bergan ($2.1MM)
  * Freedom Partners Action Fund, Inc &#8212; $2MM

<br/>
* Ronald S Lauder ($2.0MM)
  * National Horizon &#8212; $1.65MM

<br/>
* Susan Z Mandel ($1.9MM)
  * Planned Parenthood Votes &#8212; $1.3MM

<br/>
* David Craig Humphreys ($1.2MM)
  * Missouri Rising Action &#8212; $1.2MM.
<br/>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With the previous FEC blog post in mind, let's go through some contests' cumulative financial plots to see what the fundraising landscape was like leading up to election day. We'll keep an eye out for things like who has more opposition money spent against them (usually in the form of attack ads), who has a higher in-state to out-of-state individual contributions ratio, etc. The statistical modeling in a future post will help us quantify the significance of these observations; right now, we're exploring the scene. As a refresher, see the Senate contest fundraising overview plot &#8594;[here]({{ site.url }}/assets/FECpt1/senate_2018.png)&#8592; and the House one (without contests where incumbents ahead in fundraising won) &#8594;[here]({{ site.url }}/assets/FECpt1/house_2018_unexpecteds.png)&#8592;. Remember, we're only looking at contests with an incumbent running (i.e., not open seats). The faint vertical lines that are the same in every plot are FEC filing deadlines and election day.


_**Scenario: incumbent ahead in fundraising who won**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As discussed in the previous FEC post, the most common scenario is when an incumbent leads in fundraising and wins. We'll go over one example of this to start.

**U.S. House, Alabama District 3**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 8(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_AL03_committee.png">
      <img alt="Alabama district 3 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_AL03_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 8(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_AL03_individual.png">
      <img alt="Alabama district 3 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_AL03_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 8(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_AL03_cm2cm.png">
      <img alt="Alabama district 3 transfer between committees" src="{{ site.url }}/assets/FECpt2/contributions_AL03_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 8(a) shows the incumbent's principal campaign committee, Mike Rogers for Congress, raised money consistently starting in January 2017. The highest contributors &#x2014; giving $10,000 each &#x2014; included PACs for Blue Cross Blue Shield, Northrop Grumman, Raytheon, Bechtel Group, General Atomics, General Dynamics, PeanutPAC, Harris Corp, and others. Everytown For Gun Safety Action Fund made an $851 IE to SKDKnickerbocker opposing Rogers.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Challenger Mallory Hagan's fundraising started over a year later, around March 2018. The campaign had an advocating IE from Vote Me Too PAC to Facebook for $39 and committee contributions (all under the maximum of $10K) from PACs for CWA-COPE, United Transportation Union, IBEW, End Citizens United, Seeking Justice, Brotherhood of Locomotive Engineers and Trainmen, and RWDSU COPE.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now, looking at the individual contributions plot Fig. 8(b), we see that the incumbent got a big boost shortly after the campaign started, and then again after what looks like the challenger's campaign launch. The incumbent's proportion of in-state individual contribution dollars to total individual contribution dollars is very high (i.e., dashed red line closely mirrors solid red line). We can see that the out-of-state individual contributions raised by the incumbent are almost equal to in-state individual contributions raised by the challenger.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 8(c) shows a $150K infusion from the National Republican Congressional Committee to Mike Rogers for Congress pretty close to election day.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;So! That is a review of a typical contest where an incumbent ahead in fundraising defeated a challenger and not a lot of independent expenditures were made. If something isn't clear, let us know in the comments section at the bottom and we'll clarify. Now, let's look at some of the contests discussed in the previous post that had unexpected outcomes.


_**Scenario: incumbent ahead in fundraising who lost**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The two instances of this scenario in Senate contests are the Missouri Senate contest where incumbent/leading fundraiser Claire McCaskill lost to challenger Joshua Hawley and the North Dakota Senate contest where incumbent/leading fundraiser Heidi Heitkamp lost to challenger Kevin Cramer. There are six instances of this scenario in House contests (all with Republican incumbents) and we will review them in the final section in a plot-reading exercise.

**U.S. Senate, Missouri**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 9(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_MOsenate_committee.png">
      <img alt="Missouri Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_MOsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 9(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_MOsenate_individual.png">
      <img alt="Missouri Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_MOsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 9(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_MOsenate_cm2cm.png">
      <img alt="Missouri Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_MOsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The first thing we notice looking at the committee contributions in Fig. 9(a) is that there were a _lot_ of IEs made to oppose candidates. IEs opposing challenger Joshua Hawley picked up pace around February 2018, while IEs opposing incumbent Claire McCaskill came in fast and strong around July 2018 and never let up. The largest IEs opposing Hawley were: SMP to Waterfront Strategies ($15.8MM), Women Vote! to Waterfront Strategies ($4.3MM), Priorities USA Action to Bully Pulpit Interactive ($3.7MM), and Majority Forward to Waterfront Strategies ($2.8MM). The largest IEs opposing McCaskill were: Senate Leadership Fund to Main Street Media Group ($16.1MM), NRSC to National Media Research Planning & Placement ($4.0MM), Americans for Prosperity to In Pursuit Of ($3.9MM), Senate Leadership Fund to Arena Online ($3.5MM), CFG Action Missouri (Club for Growth) to Ax Media ($2.9MM), America First Action, Inc. to Red Eagle Media Group ($2.2MM), NRSC to Cavalry ($1.1MM), and Missouri Rising Action to Strategic Media Services ($1.1MM).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Looking at the individual contributions in Fig. 9(b), we see that incumbent Claire McCaskill dominated overall; however, notice that her campaign has far more out-of-state dollars than in-state, and that Hawley's total individual contributions almost equal McCaskill's in-state contributions. Since the vast majority of out-of-state contributors won't participate in an election for a Congressperson in the end, one wonders whether in-state contributions are a better proxy for support at the polls than overall contributions.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;McCaskill as a candidate contributed $41K. As an individual she contributed $134K. About 28K individuals contributed under the FEC combined limit of $5,400 ($2,700 (primary) + $2,700 (general) = $5,400). More than a few others contributed over the FEC limit; see some of them &#8594;[here]({{ site.url }}/assets/FECpt2/bigdonors/mccaskill_bigdonors.png)&#8592;. (Note that many contributed $21,600, which in the code you can see is the sum of eight one-time contributions, and that $2,700 x 8 = $21,600.)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hawley contributed no money to his own principal campaign committee while ~6,000 individuals did amounts totaling under the combined FEC limit. Individuals contributing total amounts over the limit include:

* Larry Potterfield, Columbia MO, Midway USA CEO, $10,800
* Paul Atkins, Arlington VA, Patomak Global Partners LLC consultant, $10,800
* William H Darr, Springfield MO, ADF exec VP, $10,800
* Harry M Cornell, Carthage MO, retired, $10,400
* Sharon J Herschend, Branson MO, Herschend Family Entertainment CEO, $10,000.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The main committee transfers to McCaskill for Missouri in Fig. 9(c) were $1.7MM total from McCaskill Victory Fund, $900K total from Missouri Democratic State Committee, $176K total from McCaskill 2018 Victory, $167K total from Justice 2018, and $116K total from Senate 2018 Impact. The main committee transfers to Josh Hawley for Senate were $805K total from Hawley Victory Committee, $181K total from Hawley Win Fund, $72K total from Indiana/Missouri Victory Committee, $49K total from Protecting the Majority Committee, and $46K total from Strengthen the Senate Majority 2018.


**U.S. Senate, North Dakota**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 10(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NDsenate_committee.png">
      <img alt="North Dakota Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_NDsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 10(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NDsenate_individual.png">
      <img alt="North Dakota Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_NDsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 10(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NDsenate_cm2cm.png">
      <img alt="North Dakota Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_NDsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 10(a) shows that IEs opposing each candidate picked up around early summer 2018 and dwarfed any IEs advocating the candidates. Big spenders opposing incumbent Heidi Heitkamp were the Senate Leadership Fund to Main Street Media Group ($2.3MM) and NRSC to National Media Research Planning & Placement ($2.1MM). Big spenders opposing challenger Kevin Cramer were SMP to Waterfront Strategies ($2.7MM), DSCC to Great American Media ($2.0MM), and Majority Forward to Waterfront Strategies ($1.1MM).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Neither opponent spent personal money on the campaigns. Heitkamp's principal campaign committee, Heidi for Senate, had around 19K individuals contributing below the combined $5,400 FEC limit. Individuals exceeding that limit include, but are not limited to those listed &#8594;[here]({{ site.url }}/assets/FECpt2/bigdonors/heitkamp_bigdonors.png)&#8592;. Cramer's principal campaign committee, Cramer for Senate, had about 2.5K individuals contributing under the combined $5,400 FEC limit. Individuals contributing over the limit include, but are not limited to those listed &#8594;[here]({{ site.url }}/assets/FECpt2/bigdonors/cramer_bigdonors.png)&#8592;.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 10(b) shows that the opponents had about the same amount of in-state individual contribution dollars, and that out-of-state individual contributions made up a very high proportion of each (particularly for Heitkamp).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 10(c) shows committee transfers totals including North Dakota Democratic NLP Party's $3.2MM across 20 instances to Heidi for Senate; also included in that curve are Minnesota Democratic-Farmer-Labor Party ($500K), Heidi Victory Fund ($381K), Missouri Democratic State Committee ($200K), Indiana Democratic Congressional Victory Committee ($200K), and others. Cramer for Senate received $397K from Cramer Victory Fund, $118K from Keep the Senate Red 2018, and others <$100K each.


_**Scenario: incumbent behind in fundraising who won**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The two instances of this scenario in the Senate contests are Texas incumbent Ted Cruz's win over challenger/leading fundraiser Beto O'Rourke and New Jersey incumbent Bob Menendez's win over challenger/leading fundraiser Bob Hugin. The House contest satisfying this scenario is Pennsylvania District 8, where incumbent Matt Cartwright beat challenger/leading fundraiser John Chrin.

**U.S. Senate, Texas**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 11(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_TXsenate_committee.png">
      <img alt="Texas Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_TXsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 11(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_TXsenate_individual.png">
      <img alt="Texas Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_TXsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 11(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_TXsenate_cm2cm.png">
      <img alt="Texas Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_TXsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 11(a) shows that IEs opposing challenger Beto O'Rourke began earlier than and also dwarf those opposing incumbent Ted Cruz. Big spenders opposing O'Rourke were: Texans Are to Main Street Media Group ($4.7MM, also $250K to Cross Screen Media and $26K to Prime Media Partners), ESAFund to Del Cielo Media ($1.4MM, also $150K to CD, $102K to Wilson Research Strategies, and $35K to McCarthy Hennings Whalen), Club for Growth Action to Target Enterprises ($1.1MM, also $29K to Prime Media Partners). The biggest spender opposing Cruz was Texas Forever, which paid $2.3MM to Waterfront Strategies.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Neither opponent personally contributed to the respective principal campaign committee. O'Rourke's, Beto for Texas, received contributions from about 70K individuals under the combined $5,400 FEC limit. Cruz's, Ted Cruz for Senate, received contributions from close to 40K individuals under the FEC limit.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 11(c) shows committee transfer totals to Beto for Texas including $4.6MM from the Texas Democratic Party, $36.9K from 2018 Senate Impact, and $16.8K from O'Rourke Washington Democratic Victory Fund. Transfers to Ted Cruz for Senate include $3.9MM from Ted Cruz Victory Committee, $260K from Cruz himself, $200K from Republican Party of Texas, $129K from 2018 Senators Classic Committee, and $124K from Cruz for President.


**U.S. Senate, New Jersey**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 12(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NJsenate_committee.png">
      <img alt="New Jersey Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_NJsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 12(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NJsenate_individual.png">
      <img alt="New Jersey Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_NJsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 12(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NJsenate_cm2cm.png">
      <img alt="New Jersey Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_NJsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 12(a) shows that incumbent Mendendez raised contributions to nonaffiliated committees consistently across his term, while challenger Hugin started around February 2018. The IEs opposing Hugin took off in July 2018 and were from SMP to Waterfront Strategies ($7.6MM, also $50K to SCN Strategies), Patients for Affordable Drugs Action to Pier 91 Media ($2.4MM, also $853K to Trilogy Interactive and smaller amounts to Patients for Affordable Drugs Now, Politico, Sea of Reeds, and Insider NJ), Leadership Alliance to Ethica Media ($1.2MM), and Committee to Build the Economy to Switchboard Communications ($25K, also $2K to MMA Consultants). IEs opposing Menendez began later and came mostly from Integrity NJ ($5.7MM to Pinpoint Media, $370K to Advictory, $268K to Mottola Consulting, $156K to US Postmaster, and $100K to Red Maverick Media); also included are $158K from Americas PAC to Statenet, and smaller amounts from Citizens for a Stronger New Jersey to Majority Strategies and Tar Heel Targeting.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Menendez's principal campaign committee, Menendez for Senate, received contributions from approximately 5,000 individuals giving less than the combined FEC maximum of $5,400. Of those who exceeded, the ones contributing a total above $10,000 include:

* Lenard Liberman, Burbank CA, Liberman Broadcasting Inc. president, $29,700
* Maria Monzon, Norwood NJ, AM Real Estate Management manager, $29,200
* Joseph Daibes, Edgewater NJ, Daibes Enterprises project manager, $17,759
* Robert Galvin, Camden NJ, Holtec International CFO, $13,500
* Lawrence B Rasky, Jamaica Plain MA, Rasky Baerlein Strategic Comm Inc. CEO, $10,800
* John D Ek, San Pedro CA, self-employed consultant, $10,800.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hugin personally contributed $73,477 to his own principal campaign committee, Bob Hugin for Senate Inc. In addition, at least 1,500 individuals contributed less than the combined FEC maximum. Those exceeding $10,000 are &#8594;[here]({{ site.url }}/assets/FECpt2/bigdonors/mccaskill_bigdonors.png)&#8592;.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Fig. 12(c) we see why Hugin appears so far ahead in fundraising from the plot in the previous blog post; he transferred $44MM across 24 instances to Bob Hugin for Senate Inc. New Jersey Republican State Committee also transferred $375K, and the Founders Committee transferred $26K. Menendez for Senate received $2.2MM from the Mendendez Victory Fund, and $38K from Blue Senate 2018.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All in all, Fig.s 12(a) & 12(b) resemble plots where the blue line is the incumbent and wins. Whatever financial edge Hugin shows in Fig. 12(c) was not utilized to sufficient effect.


**U.S. House, Pennsylvania District 8**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 13(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_PA08_committee.png">
      <img alt="Pennsylvania District 08 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_PA08_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 13(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_PA08_individual.png">
      <img alt="Pennsylvania District 08 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_PA08_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 13(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_PA08_cm2cm.png">
      <img alt="Pennsylvania District 08 transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_PA08_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 13(a) shows that incumbent Matt Cartwright dominated in committee contributions to nonaffiliated committees (the solid line); challenger John Chrin started raising in earnest around June 2018. IEs advocating Cartwright mirrored this with a delay and came mostly from SEIU COPE ($62.3K), and also from For Our Future, MoveOn.org Political Action, Communications Workers of America Working Voices, NEA Advocacy Fund, and Environment America Action Fund. The IEs opposing Cartwright were made by the NRCC ($375.9K to Del Ray Media, $144.7K to FP1 Strategies, and $35.8K to The Strategy Group) and Pennsylvania Pro-Life Federation PAC (<$100 each to Erdman Advertising Marketing and Design and SSS Printing).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 13(b) shows fairly competitive individual contribution fundraising. Cartwright spent no personal money on his campaign, and over 1,200 individuals contributed less than the combined FEC minimum (seven contributed over the minimum, anywhere from $5,450 to $8,100). Chrin contributed $521.8K to his own campaign committee, John Chrin for Congress, with fewer than 300 individuals contributing. We notice the large vertical jumps in John Chrin's solid red line, which suggests perhaps the number of individuals contributing in-state is lower than the number contributing in-state to Cartwright, even though Chrin's in-state dollar amount is larger. Cartwright seems to have gotten more out-of-state attention than Chrin.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Similarly to the Senate contest in New Jersey, Chrin as challenger made a relatively large transfer to his principal campaign committee ($1.87MM across 18 instances). The Republican Federal Committee of Pennsylvania also transferred $100K. In comparison, Cartwright transferred $140K to Cartwright for Congress. Again, this large transfer does not appear to have helped Chrin.


_**Scenario: incumbent behind in fundraising who lost**_

**U.S. Senate, Florida**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 14(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png">
      <img alt="Florida Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 14(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png">
      <img alt="Florida Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 14(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_cm2cm.png">
      <img alt="Florida Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;First of all, it's important to note that Rick Scott was Governor of Florida for the duration of this contest. Unlike many challengers, he did not have to overcome the hurdle of name recognition.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 14(a) shows incumbent Bill Nelson's fundraising for his campaign committee, Bill Nelson for U.S. Senate, grew at a pretty constant rate through election day. As soon as Rick Scott's fundraising appears around April 2018, the IEs with respect to Nelson take off. Top advocating expenditures include SMP to Waterfront Strategies ($6.0MM), Priorities USA Action to Bully Pulpit Interactive ($4.1MM), and Win Justice to Hard Knocks Field ($1.2MM). Top opposing expenditures include New Republican PAC to Matson Media ($29.3MM, also $191K to SRCP Media and $70K to Strategic Direction Com) and Americans for Prosperity Action Inc. (AFP Action) to In Pursuit Of ($1.1MM, also $227K to USPS and $130K to Presstige Printing). Nelson received contributions to nonaffiliated committees at a pretty constant rate from January 2017 through election day 2018. About $40K came from an entity/ies with a null name value; beyond that, $15K each came from M-PAC, Narragansett Bay PAC, American Federation of Teachers/AFL-CIO Committee on Political Education, Fearless for the People PAC, America Works Federal PAC, Impact, Forward Together PAC, MurphPAC, End Citizens United, and Narragansett Bay PAC.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The largest IEs opposing Scott were: SMP to Waterfront Strategies ($15.2MM), Priorities USA Action to Bully Pulpit Interactive ($5.4MM), Majority Forward to Waterfront Strategies ($4.5MM), VoteVets to Waterfront Strategies ($3.8MM), LCV Victory Fund to Waterfront Strategies ($1.8MM, also $500K to Bully Pulpit Interactive), Environmental Defense Action Fund to Waterfront Strategies ($757K), Giffords PAC to Deliver Strategies ($527K), Progressive Turnout Project to Deliver Strategies ($488K), and For Our Future to Deliver Strategies ($369K, also $324K to For Our Future Action Fund).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In Fig. 14(b) we see that 1) Bill Nelson's fundraising from individuals was very smooth over the course of his term, 2) he raised about equally in-state vs out-of-state, 3) Scott raised fiercely starting around April 2018, and 4) most of his funds came from in-state (because, as we're about to see, they were mostly from himself). Scott contributed $27.1MM as an individual and $42.9MM as a candidate to his principal campaign committee. Over 11,500 individuals contributed under the FEC maximum to his principal campaign committee, compared to approximately 22,000 under the maximum who contributed to Bill Nelson's.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 14(c) shows the following largest transfers to Bill Nelson for US Senate: $394K from Florida Senate 2018, $390K from Democratic Executive Committee of Florida, $148K from Florida Senate 2018 (Unitemized) (note: not clear what this distinction means), $99K from 2018 Senate Impact, and $91K from Senate 2018 Impact. Not clear without digging further whether "2018 Senate Impact" and "Senate 2018 Impact" are actually the same committee, but it seems likely. The largest transfers to Rick Scott for Florida were: $968K from Rick Scott Victory Fund, $16K from the Founders Committee, and $10K from Murray Energy PAC.


**U.S. Senate, Indiana**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 15(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png">
      <img alt="Indiana Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 15(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png">
      <img alt="Indiana Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 15(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_cm2cm.png">
      <img alt="Indiana Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 15(a) shows a similar story to the senate contest in Florida, but here the IEs opposing incumbent Joe Donnelly started later. The largest of those were: Senate Leadership Fund to Main Street Media Group ($11.2MM, also $2.8MM to Cross Screen Media and $834K to Majority Strategies), NRSC to Del Ray Media ($2.9MM, also $1.3MM to Targeted Victory), America First Action Inc. to Red Eagle Media Group ($2.1MM), and National Rifle Association of America Political Victory Fund to Starboard Strategic ($1MM). The largest IEs advocating Donnelly were: SMP to Waterfront Strategies ($2.7MM, also $215K to Bully Pulpit Interactive and $105K to Shorr Johnson Magnus), Black Progressive Action Coalition to Revolution Field Strategies ($942K, also $233K to Resonance Campaigns), and Vote for Hoosier Values to JVA Campaigns ($723K).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The largest IEs opposing challenger Mike Braun were: SMP to Waterfront Strategies ($13.7MM, also $270K to Shorr Johnson Magnus), DSCC to Great American Media ($6.8MM), Majority Forward to Waterfront Strategies ($4.5MM), Priorities USA Action to Bully Pulpit Interactive ($3.5MM). The largest IEs advocating Braun were: Senate Leadership Fund to Main Street Media Group ($1.3MM, also $662K to Connection Strategy and $321K to Cross Screen Media), and NRSC to Del Ray Media ($191K).  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In terms of individual contributions, Joe Donnelly contributed $15K to Donnelly for Indiana. Approximately 9,000 individuals contributed less than the combined FEC maximum; of those who contributed over the maximum, none contributed over $10K. Mike Braun for Indiana received contributions from approximately 4K individuals under the combined FEC maximum. While Donnelly raised more individually contributed dollars than Braun, we notice that Braun raised more in-state dollars than Donnelly. It follows that Braun's ratio of in-state to out-of-state was higher than Donnelly's.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 15(c) shows Braun way ahead of Donnelly in terms of transfers between committees. The largest transfers to Donnelly for Indiana were from Senate Impact 2018 ($492K), Donnelly Victory Fund ($342K), and Democrats for Opportunity Fund ($96K). The largest transfers to Mike Braun for Indiana were from Mike Braun ($15.1MM), Indiana Republican State Committee ($342K), Braun Victory Committee ($202K), Team Braun Committee ($130K), Keep the Senate Red 2018 ($126K), and Missouri for GOP Senate Majority ($111K).


**U.S. Senate, Nevada**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 16(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png">
      <img alt="Nevada Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 16(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png">
      <img alt="Nevada Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 16(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_cm2cm.png">
      <img alt="Nevada Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 16(a) shows that incumbent Dean Heller's fundraising was consistent throughout his term. Interestingly, unlike in other contests we've looked at, it appears that challenger Jacky Rosen started fundraising at the beginning of the incumbent's term. IEs opposing Heller began in earnest around June 2018 and continued strongly through the election. The largest of these were: SMP to Waterfront Strategies ($11.1MM, also $3MM to Blueprint Interactive), DSCC to Great American Media ($7.8MM), Majority Forward to Waterfront Strategies ($2.7MM), American Federation of State County and Municipal Employees PEOPLE to Waterfront Strategies ($1.5MM), and Women Vote! to Waterfront Strategies ($1.5MM). The largest IEs opposing Rosen were: Senate Leadership Fund to Main Street Media Group ($13.2MM, also $1.5MM to Arena Online, $852K to Arena Communications, $217K to DMM Media, $57K to Connection Strategy, and $33K to Richard Sales Media), NRSC to Flexpoint Media ($4.7MM, also $217K to OnMessage and $2,317 to i360).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In terms of Rosen's campaign, Fig. 16(b) shows Rosen for Nevada received contributions from at least 19K individuals below the combined FEC maximum. Those contributing over the limit include, but are not limited to the ones shown &#8594;[here]({{ site.url }}/assets/FECpt2/bigdonors/rosen_bigdonors.png)&#8592;. Heller for Senate received contributions from at least 5,600 individuals below the combined FEC maximum. Those contributing over the limit to Heller for Senate include, but are not limited to, those shown &#8594;[here]({{ site.url }}/assets/FECpt2/bigdonors/heller_bigdonors.png)&#8592;. Both opponents received more out-of-state dollars than in-state dollars from individual contributors.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 16(c) shows that Heller's campaign had transfers from other committees relatively consistently throughout his term, and Rosen's campaign had transfers starting around October 2017 that came in at a much higher rate. The largest ones to Rosen for Nevada were: $1MM from Rosen Victory Fund (also $34.5K from "Rosen Victory Fund (Unitemized)," not clear the distinction), $256K from Arizona Nevada Victory Fund, $185K from 2018 Senate Impact, and $94K from Nevada State Democratic Party. The largest transfers to Heller for Senate were: $153K from Heller Victory Committee, $101K from 2017 Senators Classic Committee, and $63K from 2018 Senators Classic Committee.


_**Back to the first scenario, this time House contests: incumbent ahead in fundraising who lost**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For now, we're going to comment on each contest in this section based on the plots and what we've seen above, instead of _a priori_ knowledge from the code notebooks. This kind of thinking will be useful, for example, when looking at the contests currently taking place for 2020.


**U.S. House, California District 21**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 17(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png">
      <img alt="California district 21 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 17(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png">
      <img alt="California district 21 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 17(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_cm2cm.png">
      <img alt="California district 21 transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_CA21_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;From the shape of the solid curves in Fig. 17(a) we could guess that the Republican is incumbent (since fundraising started at the beginning of the term). A large amount of opposing IE money was spent against the incumbent, and relatively little against the challenger. Fig. 17(b) shows that each opponent raised mostly from in-state individual contributors, and that the challenger had a nice rally starting around April 2018 through the election. Fig. 17(c) shows that no committees made transfers to the incumbent and that the challenger's principal campaign committee received about $800K.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-expert diagnosis: The incumbent was outspent in opposing IEs and no committees transferred in for assistance.

**U.S. House, Florida District 26**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 18(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png">
      <img alt="Florida district 26 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 18(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png">
      <img alt="Florida district 26 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 18(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_cm2cm.png">
      <img alt="Florida district 26 transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_FL26_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;From the shapes of the solid curves in Fig. 18(a), we would guess that the Republican is the incumbent. A lot of IEs opposing each candidate were made in this contest, with a larger dollar amount opposing the Democratic challenger. However, IEs advocating the challenger were almost as large and those advocating the incumbent were nowhere even close.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 18(b) shows that total individual contribution dollar amount was almost the same. It's interesting to note that around July 2018, the challenger's out-of-state individual contribution dollars overtook the in-state ones; the out-of-state dollars ended up almost matching the incumbent's in-state dollars. This is a fairly wide margin between opponents' in-state individual contribution dollars, which makes us wonder whether the incumbent's average in-state contribution total per individual is higher than the challenger's.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 18(c) shows some committee transfer kicking in to the incumbent's principal campaign committee at regular FEC deadline intervals. Transfers to the challenger's principal campaign committee began earnestlly around April 2018 and were relatively close to the incumbent's for how wide the starting margin was.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-expert diagnosis: Aggressive spending on IEs advocating the challenger look like they must have helped; individual contributions in total look comparable but it's a bit surprising how wide the in-state dollar margin is. Uptick in interest from out-of-state starting around September 2018. Committee transfers comparable. Seems like there must be something else going on in this contest to explain the upset.

**U.S. House, Georgia District 6**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 19(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png">
      <img alt="Georgia District 06 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 19(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png">
      <img alt="Georgia District 06 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 19(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_cm2cm.png">
      <img alt="Georgia District 06 transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_GA06_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is the first contest we've looked at in this post where IEs started so early. Someone made some _very_ large, early IEs opposing the incumbent around April 2017. IEs advocating the incumbent seem to have picked up to compensate for the negative attention. IEs advocating the challenger started around May 2018 and spiked immediately prior to the election. Surprisingly small amount of opposing IE spending with respect to the challenger. Individual contributions nowhere close. About $100K transferred into the challenger's campaign close to election day.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-expert diagnosis: Looks like some negative something going on around the incumbent unrelated to the challenger early on, with a nice infusion of IEs advocating the challenger near election day.

**U.S. House, Illinois District 6**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 20(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png">
      <img alt="Illinois District 06 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 20(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png">
      <img alt="Illinois District 06 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 20(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_cm2cm.png">
      <img alt="Illinois District 06 transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_IL06_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-expert diagnosis: Lot of IEs opposing the incumbent; individual contributions really started taking off for the challenger around August 2018, with in-state dollars below that of incumbent but good out-of-state attention; much larger transfers from committees for the challenger than the incumbent.

**U.S. House, Oklahoma District 5**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 21(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png">
      <img alt="Oklahoma District 05 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 21(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png">
      <img alt="Oklahoma District 05 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 21(c) is missing here because all amounts were zero.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-expert diagnosis: Pretty clear here that a little bit of IEs advocating the challenger plus a runaway advantage in individual contributions starting June 2018 (especially in-state) helped the challenger.

**U.S. House, Utah District 4**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 22(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png">
      <img alt="Utah District 04 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 22(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png">
      <img alt="Utah District 04 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 22(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_cm2cm.png">
      <img alt="Utah District 04 transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_UT04_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The IEs advocating the incumbent here are curious... haven't seen other contests where either type of IE was made over such an extended period of time. Seems like some kind of damage control. IEs opposing each candidate were about the same, which is interesting again in light of apparent damage control. In terms of individual contributions, these candidates are night and day. First of all, the challenger outraised overall in individual contributions, and secondly the challenger had almost as many in-state contribution dollars as the incumbent had overall dollars! Fig. 22(c) could've been expected to be a bit higher given what trouble the incumbent seemed to be in. The challenger didn't need any transfers based on how Fig. 22(b) was developing.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-expert diagnosis: Fig. 22(b) shows you who will win. Plain as day.

**U.S. House, Virginia District 10**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 23(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png">
      <img alt="Virginia District 10 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 23(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png">
      <img alt="Virginia District 10 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 23(c)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_cm2cm.png">
      <img alt="Virginia District 10 transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_VA10_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 23(a) is an opposing IE battle to the end. Note that all if not most IEs advocating the incumbent were made around May 2018, whereas the ones advocating the challenger were made much close to election day. Fig. 23(b) is a very strong look for the challenger, who overtook the incumbent in July 2018 in overall individual contribution dollars and, perhaps more importantly, in in-state individual contributions. Fig. 23(c), like the previous contest we just reviewed, seems a little low for how strongly the challenger was performing in individual contributions received.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Non-expert diagnosis: Every candidate should want a strong in-state individual contributions surge like the challenger got in this contest.


### Conclusion

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This post was long and varied. Thanks for sticking with us! We need to take the info from here and add it to the models we've started building to predict election outcome. There will also be a post, possibly sooner than the prediction one, on the current state of finances in 2020 contests. If you have any thoughts or insight about what's here, please let us know either in the comments below or at contact@volsweep.com. Thanks again for reading. &#8212;_Team VolSweep_


_**Footnotes**_

[^1]: Data sets analyzed in this post found here: [https://www.fec.gov/data/browse-data/?tab=bulk-data](https://www.fec.gov/data/browse-data/?tab=bulk-data)
[^2]: Cleaning notes to consider: 1) all figures are rounded, please check the code notebooks for more precise values, 2) only data pertaining to candidates appearing on final ballots remain, 3) any candidate not affiliated with one of the two major parties has been categorized as, "Third party," 4) some entries in the state abbreviation column do not match those of U.S. states or territories, but we left them for now as they only constitute ~0.2% of total observations (the reason why the state abbreviation per observation is important is that we want to distinguish between in-state contributions/IEs and out-of-state ones), 5) employers and occupations have not been deduped yet.
[^3]: Read more about independent expenditures: [https://ballotpedia.org/Independent_expenditure](https://ballotpedia.org/Independent_expenditure)
[^4]: [https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/](https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/)
[^5]: PDF of FEC limits (2017-18): [https://transition.fec.gov/info/contriblimitschart1718.pdf](https://transition.fec.gov/info/contriblimitschart1718.pdf)
