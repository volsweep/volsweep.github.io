---
layout: post
title: "FEC Campaign Finance, Part 1: A 2018 retrospective"
date: 2019-12-12 16:00:00 -0400
comments: true
categories:
---
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*TL;DR Incumbents ahead in funding almost always win Congressional elections (see 2018 counts &#8594;[here]({{ site.url }}/assets/FECpt1/profile_breakdowns.png)&#8592;; excluding unopposed, 97% won in the House of Representatives (243/250) and 92% won in the Senate (24/26)). Even when there is not an incumbent ahead in funding, there are other patterns between campaign finance filings and election outcomes.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The Federal Election Commission (FEC) publishes U.S. federal election campaign finance data[^1], which we looked at to find potential VolSweep customers. Interesting patterns appeared so far in 2020 filings, so we inspected the 2018 midterm filings to see how well they would have predicted the actual election outcomes[^2]. We are sharing our findings in a series of blog posts since they are of potential public interest.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This post is an overview of trends and exceptions in the 2018 data; the next posts will cover predictive model building and evaluation on 2018 data, and then 2020 predictions using those models. All relevant code is in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018)&#8592; GitHub repository. Let's start with the 2018 Senate plot and develop some hypotheses.


## U.S. Senate
![senate]({{ site.url }}/assets/FECpt1/senate_2018.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As you can see, most winners are incumbents ahead in funding (that is, you see a lot of solid circles to the right of any other symbol on the same horizontal line). Some notes before we hypothesize:

* Open seats: The "+" symbols represent candidates for open[^3] seats. We're going to disregard those contests for now.
* Uncontested seats: While there were no uncontested candidates in the Senate, that did happen in the House of Representatives; clearly, an opponent-less candidate will win. Those cases are trivial so we'll ignore them for predictive purposes.
* Multiple incumbents: Due to redistricting, there were actually two incumbents in PA_17 in 2018[^4]; cases like that are very exceptional and will also be ignored while we build a general model.
* Candidates per party: States like Louisiana and California have rules allowing more than one candidate per party on the ballot. Our models will assume for the most part that a maximum of one candidate per party ends up on the ballot.
* Timing assumption: A big assumption we're making is that it's reasonable to make predictions using Q3 FEC filings. Incumbency status obviously doesn't change per candidate over the course of an election season, but relative funding status very well might. We're not (yet) taking into account changes in funding over time.
* Time machine issue: Finally, the FEC is reporting some candidates' final 2018 filing after the election date. We're assuming that post-election funding changes over part of November and all of December are relatively small compared to the rest of the election season.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This brings us to...

**Hypothesis &#35;1: Any incumbent will win when s/he is ahead in funding.**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This is the same as saying that any challenger who is behind in funding will lose. If this happens, our prediction is correct (otherwise, it failed). Since our hypothesis imposes two relative conditions on a candidate that do not always align &#8212; incumbency status and funding status &#8212; we need a new predictive model whenever an incumbent is behind in funding (same as a challenger ahead in funding). &#8594;[Here]({{ site.url }}/assets/FECpt1/show_odds_senate_2018.png)&#8592; are the raw data and a plot of where Hypothesis &#35;1 breaks down:

![senate_unexpecteds]({{ site.url }}/assets/FECpt1/senate_2018_unexpecteds.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;So what happened?

**Hypothesis &#35;1 was wrong:**
* NJ &#8212; Democratic incumbent raised *less* and won;
* TX &#8212; Republican incumbent raised *less* and won;
* FL &#8212; Republican *challenger* raised more and won;
* NV &#8212; Democratic *challenger* raised more and won;
* IN &#8212; Republican *challenger* raised more and won.

**Hypothesis &#35;1 didn't apply:**
* MO &#8212; Republican *challenger* raised *less* and won;
* ND &#8212; Republican *challenger* raised *less* and won.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The FEC provides a breakdown of funding sources for the campaign finance data it reports. In the next posts we're going to check whether additional funding data can help explain these outcomes; for now, let's move to the 2018 House of Representatives data.


## U.S. House of Representatives
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The full House of Representatives plot is a bit long to display, so head &#8594;[here]({{ site.url }}/assets/FECpt1/house_2018.png)&#8592; to check it out & be prepared to zoom in.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Like we did for the Senate, here is a plot of all House contests where Hypothesis &#35;1 is wrong or doesn't apply. There seems to be some amount of total funding between $3-5MM when Republican incumbents become more likely to lose to Democratic challengers:

![house_unexpecteds]({{ site.url }}/assets/FECpt1/house_2018_unexpecteds.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;And because we're on a plotting roll, here's a plot of all the remaining contests after removing the ones matching that $3-5MM threshold trend (raw data &#8594;[here]({{ site.url }}/assets/FECpt1/oddest_house_2018.png)&#8592;). That is, the following contests were removed:

**Winner funding <$3MM:**
* Republican incumbent raised *less* and won.

**Winner funding >$3MM:**
* Democratic *challenger* raised more and won.

![house_most_unexpecteds]({{ site.url }}/assets/FECpt1/house_2018_most_unexpecteds.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;So what happened in these?

* PA_08 &#8212; Democratic incumbent raised *less* and won;
* MI_09 &#8212; Democratic incumbent raised *less* and won;
* OK_05 &#8212; Democratic *challenger* raised more and won;
* IL_06 &#8212; Democratic *challenger* raised *less* and won;
* VA_10 &#8212; Democratic *challenger* raised *less* and won;
* FL_26 &#8212; Democratic *challenger* raised *less* and won;
* UT_04 &#8212; Democratic *challenger* raised *less* and won;
* CA_21 &#8212; Democratic *challenger* raised *less* and won;
* GA_06 &#8212; Democratic *challenger* raised *less* and won;
* VA_11 &#8212; Republican *challenger* raised *less* and won.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Future posts will discuss whether additional FEC data on funding sources can help improve our predictive capacity beyond Hypothesis &#35;1 (that any incumbent will win when s/he is ahead in funding). It certainly works well as a starting point.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thanks for reading! We'd love to hear what you're thinking&#8212; please leave thoughts and questions in the comments below or email contact@volsweep.com. If you'd like a free plot of a particular state/U.S. territory, send an email as well. &#8212;Rebecca


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

[^1]: https://www.fec.gov/data/browse-data/?tab=bulk-data
[^2]: https://ballotpedia.org/United_States_Congress_elections,_2018
[^3]: "Open" means there was no incumbent on the ballot, which happens due to certain redistricting scenarios, retirement/resignation/death of the sitting elected official, etc. You can see a plot of 2018 open contests with more than one candidate &#8594;[here]({{ site.url }}/assets/FECpt1/open_seats_2018.png)&#8592;.
[^4]: https://ballotpedia.org/Redistricting_in_Pennsylvania
[^5]: https://ballotpedia.org/United_States_Senate_special_election_in_Minnesota,_2018
[^6]: https://ballotpedia.org/North_Carolina%27s_9th_Congressional_District_election,_2018
