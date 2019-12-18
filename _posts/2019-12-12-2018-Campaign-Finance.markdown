---
layout: post
title: "FEC Campaign Finance, Part 1: A 2018 retrospective"
date: 2019-12-12 16:00:00 -0400
comments: true
categories:
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*TL;DR Well-funded incumbents almost always win Congressional elections (see 2018 counts &#8594;[here]({{ site.url }}/assets/FECpt1/profile_breakdowns.png)&#8592;). Even when that is not the case, there are other patterns between campaign finance filings and election outcomes.*


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Peer-to-peer (P2P) text messaging has become increasingly common on political election campaigns over the past few years[^1]. The [Federal Election Commission (FEC)](https://www.fec.gov/)[^2] publishes U.S. federal election campaign finance data, which we looked at to find potential VolSweep customers. While doing so, we found evidence for relationships between FEC campaign finance filings and election outcomes reported on [Ballotpedia](https://ballotpedia.org/United_States_Congress_elections,_2018)[^3]. Since these findings are of potential public interest, we're sharing them in a series of blog posts.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This first post is an overview of trends and exceptions in the 2018 midterm FEC campaign finance filings and election results. The next posts will cover predictive model building & evaluation on 2018 data and then 2020 U.S. Congressional and Presidential election predictions using those models.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For detailed notes on data processing for this post, please scroll to the bottom of this page. The Jupyter notebooks for this campaign finance analysis series are &#8594;[here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018)&#8592;.  And if you'd like a free plot of a particular state/U.S. territory, send us a request at contact@volsweep.com.

## U.S. Senate
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The full Senate plot shows that most winners are incumbents who have higher funding than their challenger(s):

![senate]({{ site.url }}/assets/FECpt1/senate_2018.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Let's use a super simple predictive model that says that for any contest that is not an open seat[^4], the incumbent will win for sure when s/he has the highest funding. Now let's see where that model either doesn't apply (meaning the incumbent was not the highest-funded) or is wrong (meaning a lesser-funded challenger won):

![senate_unexpecteds]({{ site.url }}/assets/FECpt1/senate_2018_unexpecteds.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;See raw data &#8594;[here]({{ site.url }}/assets/FECpt1/show_odds_senate_2018.png)&#8592;. What happened in these contests that makes our super simple predictive model not work?

* FL &#8212; Republican *challenger* raised more and won;
* TX &#8212; Republican incumbent raised *less* and won;
* NV &#8212; Democratic *challenger* raised more and won;
* IN &#8212; Republican *challenger* raised more and won;
* MO &#8212; Republican *challenger* raised *less* and won;
* NJ &#8212; Democratic incumbent raised *less* and won;
* ND &#8212; Republican *challenger* raised *less* and won.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The FEC provides a breakdown of funding sources for the campaign finance data it reports. In the next post we're going to take a look at whether additional funding data can help explain these outcomes that our super simple predictive model can't handle. For now, though, let's move on to the House of Representatives data.


## U.S. House of Representatives
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The full House of Representatives plot is a bit long to display, so head &#8594;[here]({{ site.url }}/assets/FECpt1/house_2018.png)&#8592; to check it out & be prepared to zoom in.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Just like we did above for the Senate, here is a plot of all House of Representatives races that our super simple predictive model can't handle. There seems to be some amount of total funding between $3-5MM when Republican incumbents become more likely to lose to Democratic challengers:

![house_unexpecteds]({{ site.url }}/assets/FECpt1/house_2018_unexpecteds.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;And because we're on a plotting roll, here's a plot of all the remaining contests after removing the ones matching that $3-5MM threshold trend (raw data &#8594;[here]({{ site.url }}/assets/FECpt1/oddest_house_2018.png)&#8592;):

![house_most_unexpecteds]({{ site.url }}/assets/FECpt1/house_2018_most_unexpecteds.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In the next post we'll see whether FEC data on funding sources helps improve on our super simple predictive model. Thank you for reading!  We'd love to hear what you're thinking&#8212; please leave thoughts and questions in the comments below or email contact@volsweep.com. &#8212;Rebecca


Notes on data cleaning:

* The FEC data do not include all candidates per election listed on Ballotpedia (exclusions possibly due to some candidates' not meeting the conditions requiring filing set by the Commission);
* we aggregated candidates who are neither Republican nor Democrat but appeared on the final ballot into a single "Third party" category;
* the FEC data appears to list Danny Tarkanian as a candidate for the Nevada U.S. Senate seat, which we changed to reflect his candidacy for Nevada's 3rd district U.S. House of Representatives seat;
* a contest name containing '00' &#8212; e.g., 'MT_00' &#8212; refers to an *at-large* U.S. House of Representatives seat;
* entries pertaining to the Marshall Islands U.S. House of Representatives election were adjusted to reflect that it is an at-large seat, not a "1st district" seat;
* we removed Liz Matory's entry pertaining to Maryland's 2nd district U.S. House of Representatives seat and kept her entry for Maryland's 8th district U.S. House of Representatives seat;
* Minnesota had one regular and one special U.S. Senate election in 2018 ('MN_senate' and 'MN_senate_special', respectively)[^5];
* David Trone won Maryland's 6th district U.S. House of Representatives seat but the candidates listed in the FEC data appear incorrect so we excluded that election;
* we excluded the 2017 Alabama U.S. Senate special election won by Doug Jones;
* we excluded the 2016 Illinois U.S. Senate election won by Tammy Duckworth;
* North Carolina's 9th district U.S. House of Representatives election results were declared invalid by the state's Board of Elections over concerns of ballot tampering[^6];
* Susan Wild won Pennsylvania's 7th district U.S. House of Representatives election, not Pennsylvania's 15th district election;
* ten candidates' party listings conflicted between FEC and Ballotpedia (we corrected by inspection and found Ballotpedia was correct).


Footnotes

[^1]: https://www.npr.org/2018/11/22/669591667/from-get-out-to-vote-to-text-out-to-vote-the-rise-of-peer-to-peer-texting
[^2]: https://www.fec.gov/data/browse-data/?tab=bulk-data
[^3]: https://ballotpedia.org/United_States_Congress_elections,_2018
[^4]: "Open" means there was no incumbent on the ballot, which happens due to certain redistricting scenarios, retirement/resignation/death of the sitting elected official, etc.  You can see a plot of 2018 open contests &#8594;[here]({{ site.url }}/assets/FECpt1/open_seats_2018.png)&#8592;.
[^5]: https://ballotpedia.org/United_States_Senate_special_election_in_Minnesota,_2018
[^6]: https://ballotpedia.org/North_Carolina%27s_9th_Congressional_District_election,_2018
