---
layout: post
title: "Campaign Finance 2018, Part II: A closer look"
date: 2020-03-016 16:00:00 -0400
comments: true
category: blog
tags: ["FEC", "campaign finance", "2018 elections", "data science", "EDA"]
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*TL;DR*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The &#8594;[first post](https://blog.volsweep.com/blog/2019/12/12/2018-Campaign-Finance_I.html)&#8592; in this series on 2018 campaign finance filings with the Federal Election Commission (FEC) was an overview of trends and exceptions with respect to party affiliation, incumbency status, and relative funding status. To recap: incumbents are usually ahead in fundraising and win. For contests where the incumbent is not ahead in fundraising (excludes open seat contests), there is a threshold between $3-5MM above which challengers are more likely to win. In 2018's case, these were mostly Democratic-affiliated challengers; it remains to be seen how this pattern generalizes across midterm vs. general elections, for example.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This post will be more of an in-depth examination of the &#8594;[full set of data](https://www.fec.gov/data/browse-data/?tab=bulk-data)&#8592; that the FEC makes available.  As before, all relevant code is in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018)&#8592; GitHub repo.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Some cleaning notes to consider: 1) only data pertaining to candidates appearing on final ballots remain, and 2) any candidate not affiliated with one of the two major parties has been categorized as, "third party." Now we'll go through the FEC data sets one by one in the order we processed them.


### House/Senate current campaigns

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one candidate ID per row. This is the one we used to construct the plots in the first post of this series, showing relative candidate fundraising status by contest. We know from this set the following breakdown of the top three contest "types" for each branch of Congress:

*2018 U.S. Senate contests*
* 58.8% had a Democratic incumbent ahead in fundraising,
* 8.8% had a Republican incumbent ahead in fundraising,
* 8.8% had a Republican challenger ahead in fundraising.

*2018 U.S. House of Representatives contests*
* 30.8% had a Republican incumbent ahead in fundraising,
* 24.0% had a Democratic incumbent ahead in fundraising,
* 14.6% had a Democratic incumbent running unopposed.


### Candidate-committee linkages

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one line per committee-candidate pairing (NB it does not contain committees that are not linked to candidates). You can see the ones linked to at least three candidates, including candidate info, by searching "list starts here" on [this page]. The following candidates are linked to more than ten committees in this data set: Tammy Baldwin, Sherrod Brown, Joe Donnelly, Heidi Heitkamp, Amy Klobuchar, Claire McCaskill, Bill Nelson, Jacky Rosen, Debbie Stabenow, and Jon Tester.


### Committee master

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one line per committee. After deduplication of several columns, we found there are some treasurers associated with large numbers of committees, and some addresses associated with large numbers of committees. For example:


_Treasurers pertaining to over 50 committees_

* *Paul Kilgore*, 144 committees (27 linked to candidates)
* *Christopher Marston*, 122 committees (11 linked to candidates)
* *Judith Zamore*, 109 committees (53 linked to candidates)
* *Lisa Lisker*, 88 committees (14 linked to candidates)
* *Jennifer May*, 62 committees (15 linked to candidates)
* *Benjamin Ottenhoff*, 56 committees (4 linked to candidates)
* *Jay Patterson*, 56 committees (20 linked to candidates)


_Addresses pertaining to over 100 committees, treasurers listed_

* *228 S Washington St, Alexandria, VA 22314*, 156 committees
  * David Satterfield
  * Francis Kirley
  * Greg Laughlin
  * John Dwyer
  * Keith Davis
  * Larry Steinberg
  * Lisa Lisker
  * Taylor Moose
&nbsp;
* *918 Pennsylvania Ave AE, Washington, D.C. 20003*, 112 committees
  * Aaron Watson
  * Amy Eckert
  * Ellen Tauscher
  * Halle Mayes
  * Judith Zamore
  * Karen Mascott
  * Kristin Solander
  * Megan Mielnik
  * Melissa Nissen
  * Michael Schrum
&nbsp;
* *824 S Milledge Ave, Athens, GA 30605*, 101 committees
  * Greg Mosing
  * Megan Brown
  * Michael Goode
  * Paul Kilgore


### Contributions from committees to candidates & independent expenditures

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution/independent expenditure per row. The different types are:

* "contribution made to nonaffiliated committee,"
* "independent expenditure advocating election of candidate,"
* "independent expenditure opposing election of candidate,"
* "in-kind contribution made to registered filer,"
* "coordinated party expenditure,"
* "election recount disbursement,"
* "communication cost against candidate (only for Form 7 filer)."

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;During the cleaning process before plotting, we made some observations. First of all, Invenergy PAC made 691 contributions and/or independent expenditures with no date given (only 3 additional had a date). Embraer Aircraft Holding Inc PAC made 154 contributions and/or independent expenditures with no date given. The Democratic Senatorial Campaign Committee (DSCC) received $306,644 total in contributions with no individuals' names given. The National Republican Senatorial Committee (NRSC) received $294,519 in contributions with no individuals' names given.

<img width="400" alt="Club For Growth" src="{{ site.url }}/assets/FECpt2/contributions_committee_ClubForGrowth.png">

<img width="400" alt="Connection Strategy" src="{{ site.url }}/assets/FECpt2/contributions_committee_ConnectionStrategy.png">

<img width="400" alt="Facebook" src="{{ site.url }}/assets/FECpt2/contributions_committee_Facebook.png">

<img width="400" alt="Google" src="{{ site.url }}/assets/FECpt2/contributions_committee_Google.png">

<img width="400" alt="I360" src="{{ site.url }}/assets/FECpt2/contributions_committee_I360.png">

<img width="400" alt="Nebo Media" src="{{ site.url }}/assets/FECpt2/contributions_committee_NeboMedia.png">

<img width="400" alt="Planned Parenthood" src="{{ site.url }}/assets/FECpt2/contributions_committee_PlannedParenthood.png">

<img width="400" alt="Prolist" src="{{ site.url }}/assets/FECpt2/contributions_committee_Prolist.png">

<img width="400" alt="SKDKnickerbocker" src="{{ site.url }}/assets/FECpt2/contributions_committee_SKDKnickerbocker.png">

<img width="400" alt="USPS" src="{{ site.url }}/assets/FECpt2/contributions_committee_USPS.png">


### Contributions by individuals

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Any names containing "anonymous", "unitemized", and/or anything like "hat pass" we switched to simply "Anonymous". The FEC rules state: "An anonymous contribution of cash is limited to $50. Any amount in excess of $50 must be promptly disposed of and may be used for any lawful purpose unrelated to any federal election, campaign or candidate." This doesn't seem to be the case, as $246,892 total across two contributions to Composition Roofers Local Union #30 PAC and $54,458 total across two contributions to Association for Firefighters PAC. These appear to be above the limits allowed by the FEC.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In cleaning the state abbreviations column, we found some that do not match those of U.S. states or territories: AE, AP, FM, ZZ, MH, AA, PW, and null. A lot of the FM ones appear to be Florida cities; a lot of the ZZ ones appear to be cities in foreign countries; most of the null ones are U.S. cities and the state abbreviation is just missing. We left these as-is for now as they only constitute ~0.2% of total observations. The reason why the state abbreviation per observation is important is that we want to distinguish between in-state contributions/independent expenditures and out of state ones.
