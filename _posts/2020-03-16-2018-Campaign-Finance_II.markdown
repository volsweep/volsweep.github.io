---
layout: post
title: "Campaign Finance 2018, Part II: A closer look"
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
* *financial profile of opponents in individual contests, and more.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Do you have domain knowledge of campaign finance issues? I don't and would love to discuss. Please email contact@volsweep.com. General comments section at the bottom. More comprehensive/untruncated outputs available code notebooks if you want to comb through. Cheers, thanks for reading!*


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The &#8594;[first post](https://blog.volsweep.com/blog/2019/12/12/2018-Campaign-Finance_I.html)&#8592; in this series was an overview of trends and exceptions in Congressional midterm contests with respect to party affiliation, incumbency status, and relative funding status. (Recap: incumbents usually lead in fundraising and win. There appear to be some patterns in the exceptions.) This post will be a more in-depth look at the full set of data that the FEC publishes.[^1]  As before, all relevant code is in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018)&#8592; GitHub repo.[^2]


### Data Set 1: "House/Senate current campaigns"

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one row per candidate-committee pairing (note that it does not contain committees that are not linked to candidates). You can see the ones linked to at least three candidates, including candidate info, by searching "list starts here" on &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/03a%20-%202018_CommitteeMaster_clean.ipynb)&#8592; page. The following candidates are linked to more than ten committees each: Tammy Baldwin, Sherrod Brown, Joe Donnelly, Heidi Heitkamp, Amy Klobuchar, Claire McCaskill, Bill Nelson, Jacky Rosen, Debbie Stabenow, and Jon Tester.


### Data set 3: "Committee master"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one row per committee. After deduplication of several columns, we found there are some treasurers associated with large numbers of committees, and some addresses associated with large numbers of committees. (A reminder that this is the low end count because committees linked to candidates not appearing on final ballots were removed during cleaning.) Here are some examples (committee counts in parentheses, only treasurers with two or more associated committees shown):

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


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search the phrase, "look here," in &#8594;[this](https://github.com/volsweep/volsweep.github.io/tree/master/projects/FEC/2018/03a%20-%202018_CommitteeMaster_clean.ipynb)&#8592; notebook for full lists of committee names by address and treasurer.


### Data set 4: "Contributions from committees to candidates & independent expenditures"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution/independent expenditure (IE from now on) per row.[^3] The different types of contributions/independent expenditures are:

* "contribution made to nonaffiliated committee,"
* "independent expenditure advocating election of candidate,"
* "independent expenditure opposing election of candidate,"
* "in-kind contribution made to registered filer,"
* "coordinated party expenditure,"
* "election recount disbursement,"
* "communication cost against candidate (only for Form 7 filer)."

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Some observations from the cleaning process: Invenergy PAC made 691 contributions and/or independent expenditures with no date given (only 3 additional had a date). Embraer Aircraft Holding Inc PAC made 154 contributions and/or independent expenditures with no date given. The Democratic Senatorial Campaign Committee (DSCC) received $306,644 total in contributions with no individuals' names given. The National Republican Senatorial Committee (NRSC) received $294,519 total in contributions with no individuals' names given.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The next plot shows one dot per committee (mostly political action committees, or PACs) which made IE(s). The following spent at least $10 million with respect to either Republican-affiliated candidates, Democratic-affiliated candidates, or both (total amount in parentheses):

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


![senate]({{ site.url }}/assets/FECpt2/committees_log.png)  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We see from the plot that most committees make IEs totaling from around $1,000 to $1,000,000. The committees seem to be spending with respect to candidates affiliated with both major parties, although not always on the same order of magnitude. (Note: This plot does not distinguish between IEs advocating vs opposing.) We also see that committees represented by yellower dots made IEs with respect a large number of candidates (100 or more).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Now, let's look at where these IEs are going. Each plot below represents, per recipient (the 'to' in the plot title), IEs advocating and/or opposing candidates. Each plot symbol represents one candidate. It's not immediately apparent, but the plots are sorted in decreasing order of total IE dollars received from upper left corner to lower right corner (we left some out, go to notebook for full list & plots). Discussion below.

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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nebo Media doesn't have a direct online presence, either. It received at least $112.7MM in IEs, the vast majority of it from the Congressional Leadership Fund (over $112MM). Almost 95% of the total IE dollar amount Nebo Media received went toward opposing candidates. Looking at the plot, the IEs _advocated_ Republican-affiliated candidates (mostly incumbents) and _opposed_ mostly Democratic-affiliated challengers.  Interestingly, some Republican-affiliated candidates were opposed; they are Young Kim, Rodney Davis, and Dana Rohrbacher, who were all opposed by the Congressional Leadership Fund.


[**Del Ray Media**](http://delraymediabuying.com/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Del Ray Media has a very minimal online presence (click name above). It received almost $54.4MM in IEs, 98% of which was in opposition to candidates. We see in the plot that there are three Republican-affiliated candidates advocated, whereas almost all the opposed candidates are Democratic-affiliated challengers. The IEs came from NRCC ($49.5MM) and NRSC ($4.8MM).


[**Bully Pulpit Interactive**](https://bpimedia.com/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bully Pulpit Interactive (BPI) has a pretty strong online presence (click name above). It received $41.7MM in IEs, $26.7MM of which came from Priorities USA Action. Other big spenders included Independence USA PAC ($5.9MM), NextGen Climate Action Committee ($3.9MM), Human Rights Campaign Equality Votes ($1.7MM), and LCV Victory Fund ($1.4MM). About 35% of IE dollars BPI received advocated candidates, and the rest opposed. It received large IEs, mostly from Priorities USA Action, for the Florida U.S. Senate contest between incumbent Bill Nelson ($4.5MM total, advocating) and Rick Scott ($5.9MM total, opposing).


[**SKDKnickerbocker**](https://www.skdknick.com/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;SKDKnickerbocker received about $30.5MM in IEs, the overwhelming majority of which came from Independence USA PAC ($25.4MM). Others who made large IEs to SKDKnickerbocker are the Environmental Defense Action Fund ($1.5MM), LCV Victory Fund ($1.4MM), and Everytown for Gun Safety Victory Fund ($724K). Interestingly, Everytown for Gun Safety Victory Fund made a very large number of $851 IEs to SKDKnickerbocker in opposition of candidates. Looking at the plot, the Republican-affiliated incumbent in the middle stands out; this is Randy Hultgren, who had Independence USA PAC spend about $460K opposing him and $19K advocating him. Otherwise the plot is very partisan, with most advocating IEs made with respect to Democratic-affiliated challengers and most opposing IEs made with respect to Republican-affiliated incumbents.


[**Facebook**](https://www.facebook.com/gpa)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Facebook received about $4.4MM in IEs, mostly from MoveOn.org Political Action ($2.7MM). Just over 80% of the total IE dollars to Facebook advocated candidates, while the rest opposed. As you can see from the plot, proportionately more candidates had IEs both advocating and opposing them than in other plots we've just seen (i.e., the center of the plot is crowded).


### Data set 5: "Contributions by individuals"

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This data set has one contribution from an individual per row. We had to do a lot of cleaning in this set in particular. Any names containing "anonymous", "unitemized", and/or anything like "hat pass" we switched to simply "Anonymous." The FEC rules state:

> *"An anonymous contribution of cash is limited to $50. Any amount in excess of $50 must be promptly disposed of and may be used for any lawful purpose unrelated to any federal election, campaign or candidate." [^4][^5]*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This doesn't seem to be the case, as $246,892 total across two contributions to Composition Roofers Local Union #30 PAC and $54,458 total across two contributions to Association for Firefighters PAC. These appear to be above the limits allowed by the FEC.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

**U.S. Senate, Florida**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png">
      <img alt="Florida Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png">
      <img alt="Florida Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_FLsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Indiana**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png">
      <img alt="Indiana Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png">
      <img alt="Indiana Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_INsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Missouri**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MOsenate_committee.png">
      <img alt="Missouri Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_MOsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MOsenate_individual.png">
      <img alt="Missouri Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_MOsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, North Dakota**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NDsenate_committee.png">
      <img alt="North Dakota Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_NDsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NDsenate_individual.png">
      <img alt="North Dakota Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_NDsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, New Jersey**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NJsenate_committee.png">
      <img alt="New Jersey Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_NJsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NJsenate_individual.png">
      <img alt="New Jersey Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_NJsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Nevada**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png">
      <img alt="Nevada Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png">
      <img alt="Nevada Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_NVsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. Senate, Texas**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_TXsenate_committee.png">
      <img alt="Texas Senate committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_TXsenate_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_TXsenate_individual.png">
      <img alt="Texas Senate individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_TXsenate_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, California District 21**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png">
      <img alt="California district 21 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_CA21_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png">
      <img alt="California district 21 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_CA21_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Florida District 26**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png">
      <img alt="Florida district 26 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_FL26_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png">
      <img alt="Florida district 26 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_FL26_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Georgia District 6**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png">
      <img alt="Georgia District 06 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_GA06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png">
      <img alt="Georgia District 06 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_GA06_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Illinois District 6**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png">
      <img alt="Illinois District 06 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_IL06_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png">
      <img alt="Illinois District 06 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_IL06_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Michigan District 9**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MI09_committee.png">
      <img alt="Michigan District 09 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_MI09_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_MI09_individual.png">
      <img alt="Michigan District 09 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_MI09_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Oklahoma District 5**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png">
      <img alt="Oklahoma District 05 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_OK05_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png">
      <img alt="Oklahoma District 05 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_OK05_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Pennsylvania District 8**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_PA08_committee.png">
      <img alt="Pennsylvania District 08 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_PA08_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_PA08_individual.png">
      <img alt="Pennsylvania District 08 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_PA08_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Utah District 4**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png">
      <img alt="Utah District 04 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_UT04_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png">
      <img alt="Utah District 04 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_UT04_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Virginia District 10**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png">
      <img alt="Virginia District 10 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA10_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png">
      <img alt="Virginia District 10 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA10_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Virginia District 11**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA11_committee.png">
      <img alt="Virginia District 11 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA11_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_VA11_individual.png">
      <img alt="Virginia District 11 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_VA11_individual.png" style="width: 100%">
    </a>
  </div>
</div>

**U.S. House, Wisconsin District 1**

<div class="clearfix">
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_WI01_committee.png">
      <img alt="Wisconsin District 01 committee contributions" src="{{ site.url }}/assets/FECpt2/contributions_WI01_committee.png" style="width: 100%">
    </a>
  </div>  
  <div class="img-container2">
    <a href="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png">
      <img alt="Wisconsin District 01 individual contributions" src="{{ site.url }}/assets/FECpt2/contributions_WI01_individual.png" style="width: 100%">
    </a>
  </div>
</div>

_**Footnotes**_

[^1]: Data sets analyzed in this post found here: [https://www.fec.gov/data/browse-data/?tab=bulk-data](https://www.fec.gov/data/browse-data/?tab=bulk-data)
[^2]: Cleaning notes to consider: 1) only data pertaining to candidates appearing on final ballots remain, 2) any candidate not affiliated with one of the two major parties has been categorized as, "Third party," 3) some entries in the state abbreviation column do not match those of U.S. states or territories, but we left them for now as they only constitute ~0.2% of total observations. The reason why the state abbreviation per observation is important is that we want to distinguish between in-state contributions/IEs and out of state ones.
[^3]: Read more about independent expenditures: [https://ballotpedia.org/Independent_expenditure](https://ballotpedia.org/Independent_expenditure)
[^4]: [https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/](https://www.fec.gov/help-candidates-and-committees/candidate-taking-receipts/contribution-limits/)
[^5]: PDF of FEC limits (2017-18): [https://transition.fec.gov/info/contriblimitschart1718.pdf](https://transition.fec.gov/info/contriblimitschart1718.pdf)
