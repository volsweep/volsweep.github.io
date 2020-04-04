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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one candidate ID per row. This is the one we used to construct the plots in the first post of this series, showing relative candidate fundraising status by contest. We know from this set the following breakdown of the top three contest "types" for each branch of Congress:

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one row per committee. After deduplicating several columns, we found there are some treasurers associated with large numbers of committees, and some addresses associated with large numbers of committees. (A reminder that this is the low end count because committees linked to candidates not appearing on final ballots were removed during cleaning.) Here are some examples (committee counts in parentheses, only treasurers with two or more associated committees shown):

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig.s 2-7

<div class="clearfix">

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_WaterfrontStrategies.png">
      <img alt="Waterfront Strategies" src="{{ site.url }}/assets/FECpt2/ie_WaterfrontStrategies.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_NeboMedia.png">
      <img alt="Nebo Media" src="{{ site.url }}/assets/FECpt2/ie_NeboMedia.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_DelRay.png">
      <img alt="Del Ray Media Group" src="{{ site.url }}/assets/FECpt2/ie_DelRay.png" style="width: 100%">
    </a>
  </div>

</div>

<div class="clearfix">

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_BullyPulpitInteractive.png">
      <img alt="Bully Pulpit Interactive" src="{{ site.url }}/assets/FECpt2/ie_BullyPulpitInteractive.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/ie_SKDKnickerbocker.png">
      <img alt="SKDK" src="{{ site.url }}/assets/FECpt2/ie_SKDKnickerbocker.png" style="width: 100%">
    </a>
  </div>

  <div class="img-container">
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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The lefthand plots in the next section were constructed using this section's data set but are presented where they are in order to allow side-by-side comparisons.


### Data set 5: "Contributions by individuals"
> (notebook &#8594;[here](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/05a%20-%202018_IndividualContributions_clean1.ipynb)&#8592;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution from an individual per row. We had to do a lot of cleaning in this set in particular. Any names containing "anonymous", "unitemized", and/or anything like "hat pass" we switched to simply "Anonymous." The FEC rules state:

> *"An anonymous contribution of cash is limited to $50. Any amount in excess of $50 must be promptly disposed of and may be used for any lawful purpose unrelated to any federal election, campaign or candidate." [^4][^5]*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This doesn't seem to be the case, as $246,892 total across two contributions to Composition Roofers Local Union #30 PAC and $54,458 total across two contributions to Association for Firefighters PAC. These appear to be above the limits allowed by the FEC.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;With last post in mind, let's go through some contests' committee & individual contributions plots to see what the fundraising landscape was like leading up to election day. We'll keep an eye out for things like who has more opposition money spent against them (usually in the form of attack ads), who has a higher in-state to out-of-state individual contributions ratio, etc. The statistical modeling in a future post will help us quantify the significance of these observations; right now, we're exploring the scene. As a refresher, see the Senate contest fundraising overview plot &#8594;[here]({{ site.url }}/assets/FECpt1/senate_2018.png)&#8592; and the House one (without contests where incumbents ahead in fundraising won) &#8594;[here]({{ site.url }}/assets/FECpt1/house_2018_unexpecteds.png)&#8592;. Remember, we're only looking at contests with an incumbent running (i.e., not open seats). The faint vertical lines that are the same in every plot are FEC filing deadlines and election day.


_**Scenario: incumbent ahead in fundraising who won**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As discussed in the previous FEC post, the most common scenario is when an incumbent leads in fundraising and wins. We'll go over one example of this to start.

**U.S. House, Alabama District 3**

<div class="clearfix">
  <div class="img-container2">
    <span>Fig. 8(a)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_AL03_committee.png">
      <img alt="Alabama district 3 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_AL03_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <span>Fig. 8(b)</span><br/>
    <a href="{{ site.url }}/assets/FECpt2/contributions_AL03_individual.png">
      <img alt="Alabama district 3 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_AL03_individual.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 8(a) shows the incumbent's principal campaign committee, Mike Rogers for Congress, raised money consistently starting in January 2017. The highest contributors &#x2014; giving $10,000 each &#x2014; included PACs for Blue Cross Blue Shield, Northrop Grumman, Raytheon, Bechtel Group, General Atomics, General Dynamics, PeanutPAC, Harris Corp, and others. Everytown For Gun Safety Action Fund made an $851 IE to SKDKnickerbocker opposing Rogers.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Challenger Mallory Hagan's fundraising started over a year later, around March 2018. The campaign had an advocating IE from Vote Me Too PAC to Facebook for $39 and committee contributions (all under the maximum of $10K) from PACs for CWA-COPE, United Transportation Union, IBEW, End Citizens United, Seeking Justice, Brotherhood of Locomotive Engineers and Trainmen, and RWDSU COPE.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now, looking at the individual contributions plot Fig. 8(b), we see that the incumbent got a big boost shortly after the campaign started, and then again after what looks like the challenger's campaign launch. The incumbent's proportion of in-state individual contribution dollars to total individual contribution dollars is very high (i.e., dashed red line closely mirrors solid red line). We can see that the out-of-state individual contributions raised by the incumbent are almost equal to in-state individual contributions raised by the challenger.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;That is a review of a typical contest where an incumbent ahead in fundraising defeated a challenger and not a lot of independent expenditures were made. If something isn't clear, let us know in the comments section at the bottom and we'll clarify. Now, let's look at some of the contests discussed in the previous post that had unexpected outcomes.


_**Scenario: incumbent ahead in fundraising who lost**_

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The only two instances of this scenario in all of 2018's contests are the Missouri Senate contest where incumbent/leading fundraiser Claire McCaskill lost to challenger Joshua Hawley and the North Dakota Senate contest where incumbent/leading fundraiser Heidi Heitkamp lost to challenger Kevin Cramer.

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*NOTE: from these two plots it looks as though the incumbent leads in fundraising; check back &#8594;[here]({{ site.url }}/assets/FECpt1/senate_2018.png)&#8592; to see that the FEC lists the challenger as having almost $40MM (far more than the incumbent & what's shown above). We have one more data set to process which may explain where the rest of that money came from & will update as needed.*


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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This contest looks like we need to check the new data set, as well. Fig. 13(a) shows that incumbent Matt Cartwright dominated in committee contributions to nonaffiliated committees (his being Cartwright for Congress); challenger John Chrin started raising in earnest around June 2018. IEs advocating Cartwright mirrored this with a delay and came mostly from SEIU COPE ($62.3K), and also from For Our Future, MoveOn.org Political Action, Communications Workers of America Working Voices, NEA Advocacy Fund, and Environment America Action Fund. The IEs opposing Cartwright were made by the NRCC ($375.9K to Del Ray Media, $144.7K to FP1 Strategies, and $35.8K to The Strategy Group) and Pennsylvania Pro-Life Federation PAC (<$100 each to Erdman Advertising Marketing and Design and SSS Printing).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 13(b) shows fairly competitive individual contribution fundraising. Cartwright spent no personal money on his campaign, and over 1,200 individuals contributed less than the combined FEC minimum (seven contributed over the minimum, anywhere from $5,450 to $8,100). Chrin contributed $521.8K to his own campaign committee, John Chrin for Congress, with fewer than 300 individuals contributing. We notice the large vertical jumps in John Chrin's solid red line, which suggests perhaps the number of individuals contributing in-state is lower than the number contributing in-state to Cartwright, even though Chrin's in-state dollar amount is larger. Cartwright seems to have gotten more out-of-state attention than Chrin.


_**Scenario: incumbent behind in fundraising who lost**_

**U.S. Senate, Florida**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 14(a)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png">
      <img alt="Florida Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 14(b)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png">
      <img alt="Florida Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 14(c)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_cm2cm.png">
      <img alt="Florida Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fig. 8(L) shows incumbent Bill Nelson's fundraising for his campaign committee, Bill Nelson for U.S. Senate, grew at a pretty constant rate through election day. As soon as Rick Scott's fundraising appears around April 2018, the IEs with respect to Nelson take off. Top advocating expenditures include SMP to Waterfront Strategies ($6.0MM), Priorities USA Action to Bully Pulpit Interactive ($4.1MM), and Win Justice to Hard Knocks Field ($1.2MM). Top opposing expenditures include New Republican PAC to Matson Media ($29.3MM, also $191K to SRCP Media and $70K to Strategic Direction Com) and Americans for Prosperity Action Inc. (AFP Action) to In Pursuit Of ($1.1MM, also $227K to USPS and $130K to Presstige Printing). for US Senate received contributions to nonaffiliated committees at a pretty constant rate from January 2017 through election day 2018. About $40K came from an entity/ies with a null name value; beyond that, $15K each came from M-PAC, Narragansett Bay PAC, American Federation of Teachers/AFL-CIO Committee on Political Education,

**U.S. Senate, Indiana**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 15(a)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png">
      <img alt="Indiana Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 15(b)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png">
      <img alt="Indiana Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 15(c)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_cm2cm.png">
      <img alt="Indiana Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>


**U.S. Senate, Nevada**

<div class="clearfix">
  <div class="img-container">
    <span>Fig. 16(a)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png">
      <img alt="Nevada Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <span>Fig. 16(b)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png">
      <img alt="Nevada Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png" style="width: 100%">
    </a>
  </div>
  <div class="img-container">
    <span>Fig. 16(c)</span>
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_cm2cm.png">
      <img alt="Nevada Senate transfers between committees" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_cm2cm.png" style="width: 100%">
    </a>
  </div>
</div>

---------------------------------------------------------------
**U.S. House, California District 21**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png">
      <img alt="California district 21 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png">
      <img alt="California district 21 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Florida District 26**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png">
      <img alt="Florida district 26 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png">
      <img alt="Florida district 26 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Georgia District 6**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png">
      <img alt="Georgia District 06 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png">
      <img alt="Georgia District 06 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Illinois District 6**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png">
      <img alt="Illinois District 06 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png">
      <img alt="Illinois District 06 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png" style="width: 100%">
    </a>
  </div>
</div>


**U.S. House, Oklahoma District 5**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png">
      <img alt="Oklahoma District 05 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png">
      <img alt="Oklahoma District 05 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png" style="width: 100%">
    </a>
  </div>
</div>


**U.S. House, Utah District 4**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png">
      <img alt="Utah District 04 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png">
      <img alt="Utah District 04 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Virginia District 10**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png">
      <img alt="Virginia District 10 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png">
      <img alt="Virginia District 10 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Wisconsin District 1**

<div class="clearfix">
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_WI01_committee.png">
      <img alt="Wisconsin District 01 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_WI01_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container">
    <a href="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png">
      <img alt="Wisconsin District 01 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png" style="width: 100%">
    </a>
  </div>
</div>

_**Footnotes**_

[^1]: Data sets analyzed in this post found here: [https://www.fec.gov/data/browse-data/?tab=bulk-data](https://www.fec.gov/data/browse-data/?tab=bulk-data)
[^2]: Cleaning notes to consider: 1) only data pertaining to candidates appearing on final ballots remain, 2) any candidate not affiliated with one of the two major parties has been categorized as, "Third party," 3) some entries in the state abbreviation column do not match those of U.S. states or territories, but we left them for now as they only constitute ~0.2% of total observations (the reason why the state abbreviation per observation is important is that we want to distinguish between in-state contributions/IEs and out-of-state ones).
[^3]: Read more about independent expenditures: [https://ballotpedia.org/Independent_expenditure](https://ballotpedia.org/Independent_expenditure)
[^4]: [https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/](https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/)
[^5]: PDF of FEC limits (2017-18): [https://transition.fec.gov/info/contriblimitschart1718.pdf](https://transition.fec.gov/info/contriblimitschart1718.pdf)
